#!/usr/bin/env python3
"""End-to-end regression checks; requires Python 3 and Pandoc, no network."""
import base64
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name('render.py')


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements, self.text = [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)

    def attributes(self, tag, key):
        return [attrs[key] for name, attrs in self.elements if name == tag and key in attrs]


@unittest.skipUnless(shutil.which('pandoc'), 'Pandoc is required for conversion checks')
class RenderTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.source = self.root / 'source.md'
        self.source.write_text('# Document\n\nOriginal source.\n', encoding='utf-8')
        self.output = self.root / 'view.html'

    def tearDown(self):
        self.temporary.cleanup()

    def render(self, *options, output=None):
        return subprocess.run([sys.executable, str(SCRIPT), str(self.source), '-o',
                               str(output or self.output), *map(str, options)],
                              capture_output=True, text=True)

    def assert_rejected_without_writes(self, options=(), output=None, extra=()):
        watched = [self.source, *extra]
        before = {p: p.read_bytes() for p in watched}
        result = self.render(*options, output=output)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        for path, content in before.items():
            self.assertEqual(path.read_bytes(), content, str(path))
        if output is None:
            self.assertFalse(self.output.exists())

    def test_report_cannot_overwrite_source(self):
        self.assert_rejected_without_writes(('--report', self.source))

    def test_report_cannot_overwrite_html(self):
        self.assert_rejected_without_writes(('--report', self.output))

    def test_default_report_cannot_overwrite_source(self):
        self.source = self.root / 'view.report.json'
        self.source.write_text('# Still Markdown content\n', encoding='utf-8')
        self.assert_rejected_without_writes()

    def test_source_cannot_be_html_output(self):
        self.assert_rejected_without_writes(output=self.source)

    def test_symlink_and_hardlink_aliases_are_rejected(self):
        for kind in ('symlink', 'hardlink'):
            alias = self.root / (kind + '.json')
            if kind == 'symlink':
                alias.symlink_to(self.source)
            else:
                os.link(self.source, alias)
            self.assert_rejected_without_writes(('--report', alias), extra=(alias,))
        alias_output = self.root / 'hardlink.html'
        os.link(self.source, alias_output)
        self.assert_rejected_without_writes(output=alias_output, extra=(alias_output,))

    def test_report_and_html_hardlink_aliases_are_rejected(self):
        self.output.write_text('Previous HTML', encoding='utf-8')
        report = self.root / 'alias.json'
        os.link(self.output, report)
        self.assert_rejected_without_writes(('--report', report), output=self.output,
                                            extra=(self.output, report))

    def test_trusted_stylesheet_cannot_be_overwritten(self):
        css = self.root / 'custom.css'
        css.write_text('body { color: black; }', encoding='utf-8')
        self.assert_rejected_without_writes(('--extra-css', css, '--report', css), extra=(css,))

    def test_embedded_image_cannot_be_overwritten(self):
        image = self.root / 'pixel.png'
        image.write_bytes(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a2aYAAAAASUVORK5CYII='))
        self.source.write_text('# Image\n\n![Pixel](pixel.png)\n', encoding='utf-8')
        self.assert_rejected_without_writes(('--report', image), extra=(image,))

    def test_forward_fragments_and_heading_collisions(self):
        self.source.write_text('''# Document

[First](#mdhtml-example) [Second](#source-mdhtml-example)
[Unicode](#%E6%97%A5%E6%9C%AC%E8%AA%9E)

## mdhtml-example

First destination.

## source-mdhtml-example

Second destination.

## 日本語

Third destination.
''', encoding='utf-8')
        self.assertEqual(self.render().returncode, 0)
        doc = Document(self.output.read_text())
        ids = [a['id'] for _, a in doc.elements if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        fragments = [h[1:] for h in doc.attributes('a', 'href') if h.startswith('#')]
        self.assertTrue(all(fragment in ids for fragment in fragments))
        self.assertIn('source-mdhtml-example', fragments)
        self.assertIn('source-mdhtml-example-2', fragments)
        self.assertIn('日本語', fragments)

    def test_unrendered_local_asset_cannot_be_overwritten(self):
        image = self.root / 'drawing.svg'
        image.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding='utf-8')
        self.source.write_text('# Image\n\n![Drawing](drawing.svg)\n', encoding='utf-8')
        self.assert_rejected_without_writes(('--report', image), extra=(image,))

    def test_content_notes_math_and_unicode_survive(self):
        text = '''---
title: "Reading test"
---
# Reading test

Original **evidence** and uncertainty: perhaps, 12.5%. [Source](https://example.org/evidence)

## Table

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| one | two | three | four | five | six |

First[^same], again[^same].

[^same]: Definition with **emphasis** and a [link](https://example.org/note).

## Scripts

שְׁמַ֖ע יִשְׂרָאֵ֑ל

日本語と שָׁלוֹם and English stay mixed.

$x^2 + y^2 = z^2$

```python
print("<tag>")
```

<script>window.UNTRUSTED = true;</script>

[Unsafe](javascript:alert(1))
'''
        self.source.write_text(text, encoding='utf-8')
        before = self.source.read_bytes()
        self.assertEqual(self.render().returncode, 0)
        self.assertEqual(self.source.read_bytes(), before)
        html = self.output.read_text()
        doc = Document(html)
        displayed = ''.join(doc.text)
        for fragment in ['perhaps, 12.5%', 'שְׁמַ֖ע יִשְׂרָאֵ֑ל', '日本語と שָׁלוֹם and English', 'print("<tag>")']:
            self.assertIn(fragment, displayed)
        self.assertEqual(len([1 for tag, _ in doc.elements if tag == 'td']), 6)
        self.assertIn('math', [tag for tag, _ in doc.elements])
        self.assertIn('rtl', doc.attributes('div', 'dir'))
        self.assertIn('https://example.org/evidence', doc.attributes('a', 'href'))
        self.assertFalse(any(h.startswith('javascript:') for h in doc.attributes('a', 'href')))
        self.assertNotIn('<script>window.UNTRUSTED', html)
        self.assertIn('SIL OPEN FONT LICENSE Version 1.1', html)
        report = json.loads(self.output.with_suffix('.report.json').read_text())
        self.assertEqual(report['unique_notes'], 1)
        self.assertEqual(report['note_references'], 2)
        self.assertFalse(report['browser_verified'])
        self.assertIn('#mdhtml-ref-1-1', doc.attributes('a', 'href'))
        self.assertIn('#mdhtml-ref-1-2', doc.attributes('a', 'href'))

    def test_links_assets_and_unrendered_diagram_are_reported(self):
        self.source.write_text('''# Resources

[Related](related.md) ![Missing](missing.png)
![Remote](https://example.org/picture.png)

```mermaid
flowchart TD
  A --> B
```
''', encoding='utf-8')
        result = self.render('--source-url', 'https://github.com/example/project/blob/main/docs/source.md')
        self.assertEqual(result.returncode, 0, result.stderr)
        doc = Document(self.output.read_text())
        self.assertIn('https://github.com/example/project/blob/main/docs/related.md', doc.attributes('a', 'href'))
        self.assertIn('A --> B', ''.join(doc.text))
        report = json.loads(self.output.with_suffix('.report.json').read_text())
        self.assertEqual(report['network_images'], ['https://example.org/picture.png'])
        self.assertEqual(report['mermaid_count'], 1)
        self.assertTrue(any('no rendering bundle' in w for w in report['warnings']))
        self.assertTrue(any('Unresolved local image' in w for w in report['warnings']))

    def test_report_in_separate_directory(self):
        report = self.root / 'diagnostics' / 'result.json'
        result = self.render('--report', report)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(report.exists())
        self.assertTrue(self.output.read_text().startswith('<!doctype html>'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
