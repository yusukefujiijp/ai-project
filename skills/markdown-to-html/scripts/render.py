#!/usr/bin/env python3
"""Build a derived HTML reading edition with Pandoc and Python's standard library."""
import argparse
import base64
import copy
import hashlib
import html
import json
import mimetypes
import re
import shutil
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

SKILL_ROOT = Path(__file__).resolve().parent.parent
FORMAT = 'gfm+footnotes+yaml_metadata_block+tex_math_dollars'


def run_pandoc(args, text):
    proc = subprocess.run(['pandoc', *args], input=text, text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip())
    return proc.stdout


def plain(value):
    if isinstance(value, list):
        return ''.join(plain(v) for v in value)
    if not isinstance(value, dict):
        return ''
    tag, content = value.get('t'), value.get('c')
    if tag in ('Str', 'MetaString'):
        return content
    if tag in ('Space', 'SoftBreak', 'LineBreak'):
        return ' '
    if tag in ('Code', 'Math'):
        return content[-1]
    if tag in ('Link', 'Image'):
        return plain(content[1])
    if tag == 'Note':
        return ''
    return plain(content)


def count_types(value):
    counts = Counter()
    def visit(item):
        if isinstance(item, dict):
            if 't' in item:
                counts[item['t']] += 1
            for child in item.values():
                visit(child)
        elif isinstance(item, list):
            for child in item:
                visit(child)
    visit(value)
    return dict(counts)


def raw_inline(text):
    return {'t': 'RawInline', 'c': ['html', text]}


def raw_block(text):
    return {'t': 'RawBlock', 'c': ['html', text]}


def esc(text):
    return html.escape(str(text), quote=True)


def hebrew_only(text):
    return bool(re.search(r'[\u05d0-\u05ea]', text) and re.fullmatch(r'[\s\u0590-\u05ff\ufb1d-\ufb4f0-9.,:;!?"\[\](){}/+|–—…-]+', text))


def same_file(left, right):
    """Also detect existing hard links; resolve() alone only catches symlinks."""
    if left.resolve() == right.resolve():
        return True
    return left.exists() and right.exists() and left.samefile(right)


def validate_destinations(parser, output, report, inputs):
    if same_file(output, report):
        parser.error('HTML and report destinations must be different files.')
    for destination in (output, report):
        for source in inputs:
            if same_file(destination, source):
                parser.error('A derived output must not overwrite an input: ' + str(source))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('-o', '--output', type=Path, required=True)
    parser.add_argument('--title')
    parser.add_argument('--lang', default='ja')
    parser.add_argument('--source-url', default='')
    parser.add_argument('--link-base', default='')
    parser.add_argument('--asset-base', default='')
    parser.add_argument('--asset-root', type=Path)
    parser.add_argument('--mermaid-js', type=Path, help='Reviewed local classic Mermaid bundle; never inferred from source text')
    parser.add_argument('--mermaid-license', type=Path, help='Full license accompanying the supplied Mermaid bundle')
    parser.add_argument('--report', type=Path)
    parser.add_argument('--extra-css', type=Path, help='Trusted local presentation adjustments; never inferred from document text')
    args = parser.parse_args()
    if not shutil.which('pandoc'):
        parser.error('Pandoc is required; use another tested parser rather than dropping features.')
    source, output = args.input.resolve(), args.output.resolve()
    report_path = (args.report or output.with_suffix('.report.json')).resolve()
    inputs = {source, Path(__file__).resolve(), SKILL_ROOT / 'assets' / 'reader.css',
              SKILL_ROOT / 'assets' / 'reader.js'}
    inputs.update(p.resolve() for p in (args.extra_css, args.mermaid_js, args.mermaid_license) if p)
    validate_destinations(parser, output, report_path, inputs)
    data = source.read_bytes()
    text = data.decode('utf-8-sig')
    ast = json.loads(run_pandoc(['-f', FORMAT, '-t', 'json'], text))
    source_counts = count_types(ast['blocks'])
    if args.mermaid_js and not args.mermaid_license:
        parser.error('--mermaid-js requires --mermaid-license so the distribution notice is preserved.')
    root = (args.asset_root or source.parent).resolve()
    warnings, network_images, headings, notes, note_ids, refs = [], [], [], [], {}, Counter()
    stats, used_ids, heading_ids = Counter(), set(), {}
    front = re.match(r'\A---\r?\n(.*?)\r?\n(?:---|\.\.\.)\s*(?:\r?\n|$)', text, re.S)
    metadata_text = front.group(1) if front else ''

    def safe_url(url, image=False):
        clean = html.unescape(url).strip()
        if any(ord(c) < 32 for c in clean):
            warnings.append('Unsafe control characters in a URL were disabled.')
            return ''
        scheme = urlparse(clean).scheme.lower()
        allowed = ('http', 'https') if image else ('http', 'https', 'mailto', 'tel')
        if scheme and scheme not in allowed:
            warnings.append('Disabled URL scheme: ' + scheme)
            return ''
        if clean.startswith('#'):
            return clean
        base = args.asset_base if image else (args.link_base or args.source_url)
        return urljoin(base, clean) if base else clean

    def transform(node):
        if isinstance(node, list):
            return [transform(v) for v in node]
        if not isinstance(node, dict):
            return node
        tag, content = node.get('t'), node.get('c')
        if tag == 'Note':
            key = json.dumps(content, ensure_ascii=False, sort_keys=True)
            if key not in note_ids:
                note_ids[key] = len(notes) + 1
                notes.append(content)
            number = note_ids[key]
            refs[number] += 1
            rid = 'mdhtml-ref-' + str(number) + '-' + str(refs[number])
            return raw_inline('<sup id="' + rid + '"><a class="footnote-ref" role="doc-noteref" href="#mdhtml-note-' + str(number) + '" aria-label="出典 ' + str(number) + '">[' + str(number) + ']</a></sup>')
        if tag in ('RawBlock', 'RawInline'):
            stats['escaped_raw_html'] += 1
            if tag == 'RawBlock':
                return {'t': 'CodeBlock', 'c': [['', ['html'], []], content[1]]}
            return {'t': 'Str', 'c': content[1]}
        if tag == 'Header':
            level, attr, inlines = content
            label = plain(inlines)
            identifier = attr[0] or 'section-' + str(len(headings) + 1)
            if identifier.startswith('mdhtml-'):
                identifier = 'source-' + identifier
                warnings.append('A source heading used the reserved mdhtml- prefix; its ID was prefixed with source-.')
            base, number = identifier, 2
            while identifier in used_ids:
                identifier = base + '-' + str(number)
                number += 1
            used_ids.add(identifier)
            if attr[0]:
                heading_ids.setdefault(attr[0], identifier)
            headings.append((level, identifier, label))
            node = copy.deepcopy(node)
            node['c'][1][0] = identifier
        if tag == 'Link':
            node = copy.deepcopy(node)
            original = node['c'][2][0]
            target = safe_url(original)
            if not target and original:
                return {'t': 'Span', 'c': [['', [], []], transform(content[1])]}
            node['c'][2][0] = target
            if target and not urlparse(target).scheme and not target.startswith('#'):
                warnings.append('Relative link needs source context: ' + target)
        if tag == 'Image':
            node = copy.deepcopy(node)
            url, parsed = content[2][0], urlparse(content[2][0])
            if not parsed.scheme and not url.startswith('//') and not args.asset_base:
                asset = (source.parent / unquote(parsed.path)).resolve()
                try:
                    asset.relative_to(root)
                    inputs.add(asset)
                    mime = mimetypes.guess_type(asset.name)[0]
                    if mime not in ('image/png', 'image/jpeg', 'image/gif', 'image/webp', 'image/avif'):
                        raise ValueError('Unsupported local image type')
                    image_data = asset.read_bytes()
                    if len(image_data) > 16 * 1024 * 1024:
                        raise ValueError('Image exceeds 16 MiB')
                    node['c'][2][0] = 'data:' + mime + ';base64,' + base64.b64encode(image_data).decode('ascii')
                    stats['embedded_images'] += 1
                except (OSError, ValueError) as err:
                    warnings.append('Unresolved local image: ' + url + ' (' + str(err) + ')')
                    return {'t': 'Span', 'c': [['', [], []], [{'t': 'Str', 'c': '［画像：' + plain(content[1]) + '／' + url + '］'}]]}
            else:
                target = safe_url(url, image=True)
                if not target:
                    return {'t': 'Str', 'c': '［画像：' + plain(content[1]) + '］'}
                node['c'][2][0] = target
                network_images.append(target)
        if tag == 'CodeBlock' and 'mermaid' in content[0][1]:
            stats['mermaid'] += 1
            return raw_block('<figure class="diagram" data-rendered="pending"><figcaption class="diagram-status">図：定義を表示しています。</figcaption><div class="diagram-view" tabindex="0" aria-label="関係図"></div><details open><summary>図の定義</summary><pre><code>' + esc(content[1]) + '</code></pre></details></figure>')
        changed = {key: transform(value) for key, value in node.items()}
        if tag in ('Para', 'Plain') and hebrew_only(plain(content)):
            return {'t': 'Div', 'c': [['', ['hebrew-block'], [['dir', 'rtl']]], [changed]]}
        if tag == 'Table':
            classes = ['table-scroll'] + (['wide-table'] if len(content[2]) >= 6 else [])
            return {'t': 'Div', 'c': [['', classes, [['tabindex', '0'], ['role', 'region'], ['aria-label', '表。横方向にスクロールできます']]], [changed]]}
        return changed

    blocks = transform(ast['blocks'])
    note_blocks, n = [], 0
    while n < len(notes):
        note_blocks.append(transform(notes[n]))
        n += 1
    if notes:
        blocks.append(raw_block('<section class="footnotes" role="doc-endnotes" id="mdhtml-notes"><h2>出典・注記</h2><ol>'))
        for number, content in enumerate(note_blocks, 1):
            blocks.append(raw_block('<li id="mdhtml-note-' + str(number) + '">'))
            blocks.extend(content)
            backs = ' '.join('<a role="doc-backlink" href="#mdhtml-ref-' + str(number) + '-' + str(k) + '" aria-label="本文の参照位置 ' + str(k) + ' に戻る">↩' + str(k) + '</a>' for k in range(1, refs[number] + 1))
            blocks.append(raw_block('<span class="footnote-back">' + backs + '</span></li>'))
        blocks.append(raw_block('</ol></section>'))

    def reconnect_fragments(node):
        # Run after all headings (including headings inside notes) are allocated,
        # so forward links and collisions use the same final IDs as the TOC.
        if isinstance(node, dict):
            if node.get('t') == 'Link':
                target = node['c'][2][0]
                if target.startswith('#'):
                    identifier = unquote(target[1:])
                    if identifier in heading_ids:
                        node['c'][2][0] = '#' + heading_ids[identifier]
            for value in node.values():
                reconnect_fragments(value)
        elif isinstance(node, list):
            for value in node:
                reconnect_fragments(value)

    reconnect_fragments(blocks)
    render_ast = {'pandoc-api-version': ast['pandoc-api-version'], 'meta': {}, 'blocks': blocks}
    body = run_pandoc(['-f', 'json', '-t', 'html5', '--mathml', '--wrap=none'], json.dumps(render_ast))
    title = args.title or plain(ast['meta'].get('title', {})) or (headings[0][2] if headings else source.stem)
    toc_headings = [heading for heading in headings if heading[0] <= 2]
    if (toc_headings and toc_headings[0][0] == 1
            and sum(level == 1 for level, _, _ in toc_headings) == 1
            and any(level == 2 for level, _, _ in toc_headings)):
        toc_headings = toc_headings[1:]
    toc = '<ol>' + ''.join('<li class="level-' + str(level) + '"><a href="#' + esc(identifier) + '">' + esc(label) + '</a></li>' for level, identifier, label in toc_headings) + '</ol>'
    if notes:
        toc += '<a href="#mdhtml-notes">出典・注記</a>'
    css = (SKILL_ROOT / 'assets' / 'reader.css').read_text()
    if args.extra_css:
        css += '\n' + args.extra_css.read_text(encoding='utf-8')
    font_license = ''
    if re.search(r'[\u0590-\u05ff\ufb1d-\ufb4f]', text):
        font_root = SKILL_ROOT / 'assets' / 'fonts'
        inputs.update((font_root / 'NotoSerifHebrew.ttf', font_root / 'OFL.txt'))
        font_data = base64.b64encode((font_root / 'NotoSerifHebrew.ttf').read_bytes()).decode('ascii')
        css += '\n@font-face{font-family:"Reading Hebrew";src:url(data:font/ttf;base64,' + font_data + ') format("truetype");font-weight:100 900;font-display:block;unicode-range:U+0590-05FF,U+FB1D-FB4F}\n'
        font_license = '<template id="reading-font-license">' + esc((font_root / 'OFL.txt').read_text(encoding='utf-8')) + '</template>'
    reader_js = (SKILL_ROOT / 'assets' / 'reader.js').read_text()
    script, mermaid_hash = '', None
    if args.mermaid_js and stats['mermaid']:
        bundle = args.mermaid_js.read_text()
        mermaid_hash = hashlib.sha256(bundle.encode()).hexdigest()
        bundle = re.sub(r'</script', r'<\/script', bundle, flags=re.I)
        script = '<script>' + bundle + '</script>'
    elif stats['mermaid']:
        warnings.append('Mermaid definitions preserved but no rendering bundle was supplied.')
    if stats['escaped_raw_html']:
        warnings.append('Source raw HTML is shown as text, not executed.')
    sha = hashlib.sha256(data).hexdigest()
    info = ''
    if metadata_text:
        info += '<details class="source-metadata"><summary>文書メタデータ</summary><pre>' + esc(metadata_text) + '</pre></details>'
    if mermaid_hash:
        info += '<template id="mdhtml-mermaid-license">' + esc(args.mermaid_license.read_text(encoding='utf-8')) + '</template>'
    if network_images:
        info += '<p>一部の画像の表示にはネットワーク接続が必要です。</p>'
    csp = "default-src 'none'; script-src 'unsafe-inline' blob:; style-src 'unsafe-inline'; img-src data: https: http:; font-src data:; connect-src 'none'; worker-src blob:; base-uri 'none'; form-action 'none'"
    show_toc = len(toc_headings) > 1 or bool(notes)
    rail = '<aside class="rail"><details class="toc" id="mdhtml-toc" open><summary>この文書の目次</summary><nav aria-label="文書内目次">' + toc + '</nav></details></aside>' if show_toc else ''
    layout_class = 'layout' if show_toc else 'layout no-toc'
    output_html = '<!doctype html><html lang="' + esc(args.lang) + '"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="' + esc(csp) + '"><meta name="referrer" content="no-referrer"><title>' + esc(title) + '</title><style>' + css + '</style></head><body><a class="skip" href="#mdhtml-content">本文へ移動</a><div class="' + layout_class + '">' + rail + '<main class="paper" id="mdhtml-content"><article>' + body + '</article>' + info + '</main></div>' + script + '<script>' + reader_js + '</script>' + font_license + '</body></html>'
    validate_destinations(parser, output, report_path, inputs)
    output.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(output_html, encoding='utf-8')
    report = {'source': str(source), 'source_sha256': sha, 'source_url': args.source_url, 'output': str(output), 'created_utc': datetime.now(timezone.utc).isoformat(), 'source_counts': source_counts, 'heading_count': len(headings), 'unique_notes': len(notes), 'note_references': sum(refs.values()), 'mermaid_count': stats['mermaid'], 'mermaid_bundle_sha256': mermaid_hash, 'embedded_images': stats['embedded_images'], 'network_images': network_images, 'warnings': sorted(set(warnings)), 'browser_verified': False}
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(output), 'report': str(report_path), 'warnings': report['warnings']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
