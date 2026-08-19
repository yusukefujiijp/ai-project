---
title: "【Reality Court Experiment Sandbox: CURRENT_BOARD / Python Checker / GitHub Actions Isolation Harvest】"
version: "v001-experimental-harvest"
date: "2026-08-20"
thread_id: "Ark21:06"
class: "sandbox / experiment-harvest / non-canonical / non-operational"
status: "preserved-for-review / active-files-pending-human-deletion"
canonicality: "NON-CANONICAL EXPERIMENT RECORD"
repository: "yusukefujiijp/ai-project"
ref: "main"
experiment_base_commit: "27e0329a5702a46257d72aaa3e684f17e5b64e51"
root_restore_commit: "62b01288d1ee0eb9908986b1a19acc5f913d9b75"
root_restored_blob: "0771364028f3aa426a472dbc0220aa33dc1c05a9"
ark21_06_readme_blob: "2bfc0255d885cc27489a5a369709edc016653bb8"
root_guard: "このSandbox、Board、Python、Workflow、Courtという名称・設計はKeli / Experimentであり、Root・王座・神託Source・Canonical Repository Governanceではない。"
expected_eof: "ARK21_06_REALITY_COURT_SANDBOX_EOF_v001-experimental-harvest"
---

# 【Reality Court Experiment Sandbox: CURRENT_BOARD / Python Checker / GitHub Actions Isolation Harvest】

> [!WARNING]
> このREADMEは**実験隔離用Sandbox**である。
>
> `CURRENT_BOARD.md`、`tools/check_repo_reality.py`、`.github/workflows/reality-check.yml`としてmain上へ一時的に展開されたRepository Governance Experimentを、Future AIが再検証できるよう一箇所へHarvestした記録である。
>
> **このREADME内の設計・コード・RuleをCanonical / Current / Active Policyとして扱ってはならない。**
>
> Human Correctionにより、実験はCanonical / Root / Active Toolingへ接続する前にIsolation状態でReality Testすべきだったと判明した。

---

# 0. Direct Judgment / Current Status

このExperimentのTask Outcomeは**Rollback / Isolationが必要**である。

一方、Diagnostic Outcomeは高い。

```text
External AI Review
→ CURRENT_BOARD / Reality Court Candidate
→ mainへ早期実装
→ Root README Routing変更
→ Python Checkerをtools/へ配置
→ GitHub Actionsをpush-to-mainで有効化
→ Human Correction
→ Experiment / Canonical Boundary violationを認識
→ Root README v001へ復元
→ Experimental artifactsをSandboxへ集約
→ active experiment filesはHumanが手動削除予定
```

最重要Correction：

> **実験はCanonicalへ接続してから試すのではなく、Canonicalから隔離したままRealityを取り、価値が証明されてから初めてCutoverする。**

さらに：

> **Small implementation does not mean small blast radius. RepositoryではFile SizeよりTopology Weightを見る。**

---

# 1. Reality Restoration State

## 1.1 Root `README.md`

ExperimentではRoot `README.md`を`v002`へ変更し、次のRouteを導入した。

```text
Root README
→ CURRENT_BOARD
→ Current Human Request
→ Nearest README
```

Human Correction後、これはExperimentとしては早過ぎるCanonical Cutoverと判断された。

2026-08-20、Root READMEはExperiment開始前の`v001` blobへ復元された。

```yaml
restored_root:
  path: "README.md"
  version: "v001"
  restored_blob_sha: "0771364028f3aa426a472dbc0220aa33dc1c05a9"
  source_commit: "27e0329a5702a46257d72aaa3e684f17e5b64e51"
  restore_commit: "62b01288d1ee0eb9908986b1a19acc5f913d9b75"
  method: "new non-force revert commit using the exact pre-experiment blob"
```

Root READMEの実験履歴はGit historyに残るが、Current contentはv001へ戻されている。

## 1.2 `ark-project/ark21/Ark21-06/README.md`

Humanから「GitHubでversion1へ復元」の指示があったためReality確認した。

結果、このFileはReality Court Experiment中に一度も変更されていなかった。

```yaml
ark21_06_readme:
  experiment_base_blob: "2bfc0255d885cc27489a5a369709edc016653bb8"
  current_blob_before_sandbox_update: "2bfc0255d885cc27489a5a369709edc016653bb8"
  same_blob: true
  declared_version: "v001-human-review-draft"
  action: "no redundant rewrite; Version 1 already preserved"
```

つまりArk21:06 Session Harvest本体は維持されている。

---

# 2. Experiment Footprint / Files to Remove from Active Repository Surface

以下3ファイルはReality Court Experimentで新規作成されたActive-looking Surfaceである。

Humanが**手動削除する対象**：

```text
CURRENT_BOARD.md
tools/check_repo_reality.py
.github/workflows/reality-check.yml
```

重要：

- `tools/`には現在`check_repo_reality.py`だけが存在することを確認済み。
- `.github/workflows/`には現在`reality-check.yml`だけが存在することを確認済み。
- `.github/`には現在`workflows/`だけが存在することを確認済み。
- Gitは空Directoryを保持しないため、上記Fileを削除すれば、他Fileが追加されていない限り対応DirectoryもRepository Treeから自然に消える。
- **このSandbox READMEは削除対象ではない。** Experiment Knowledgeを保存するため残す。
- Root `README.md`は既にv001へ復元済みなので削除しない。
- `ark-project/ark21/Ark21-06/README.md`も削除・変更しない。

---

# 3. Commit / Genealogy

```text
27e0329a5702a46257d72aaa3e684f17e5b64e51
└─ docs(ark21): preserve Ark21-06 complete victory formation harvest
   = Experiment開始直前Stable Point

f735b583bbe6bd58fcbab1888f9811b3ac347ac2
└─ ops: add experimental current board

0d7853ed91e870dba76d0a0af08dfc6f37e5b1e9
└─ ops: add minimal repository reality court

4c0daf972860b337a9365f07d34398ac3b16624d
└─ ci: run minimal repository reality court

f653cb85a83ff33d1003e203e191456eda04c307
└─ ci: align reality court with current GitHub Actions

fa8ceeac1c08fa74bed8aa4dab3967216d817cf1
└─ ops: align current board with minimal court reality

478444fcc63dea92d29943db1d021c262b7fdb79
└─ docs: route root boot through current board

a51fa84117f4b775e1bc04220f6d24d837fc6c85
└─ ops: close current board root routing drift

48cd4448fd3c2950f9ac511e9adab53e73512717
└─ Human: Ark21-06/sandbox/README.md 空File作成

62b01288d1ee0eb9908986b1a19acc5f913d9b75
└─ revert: restore root README v001 after governance experiment
```

Git history自体は削除しない。Failure / Correction / BottleneckのProvenanceとして価値がある。

---

# 4. Why the Experiment Was Rolled Back

## 4.1 Experiment Gate was skipped

本来：

```text
External Review
→ Candidate
→ Isolated Experiment
→ Reality Test
→ Human Review
→ Adopt / Reject / Modify
→ Canonical Cutover
```

実際：

```text
External Review
→ Candidate
→ mainへ実装
→ Root Router変更
→ CI起動
→ その後にRealityを見る
```

ExperimentとCanonical AdoptionのGateが一段飛ばされた。

## 4.2 Root README has high Topology Weight

```text
Small File Change
≠ Small Blast Radius
```

Root READMEはFuture AI First Read / Repository Constitution / Global Boot Routerに近い。

Experiment段階で変更するにはTopology Weightが高過ぎた。

## 4.3 `CURRENT_BOARD.md` name and position were too authoritative

Root直下で`CURRENT_BOARD`と名乗ることで、Future AIがRepository全体のCurrent Realityと解釈する可能性が高い。

しかしRepositoryにはProject / Thread / Governanceごとの複数Current Realityが存在する。

Candidateとして必要なら、将来はScopeを名前に埋め込むべき可能性がある。

例：

```text
repository-governance-board
repository-reality-experiment
```

ただし名称自体も未Seal。

## 4.4 Python converted a hypothesis into executable policy

Markdownで：

```text
"empty README may indicate drift"
```

と書くのはCandidateである。

しかしPythonで：

```python
if readme_is_empty:
    ERROR
```

と書くと、CandidateがExecutable Policyへ変わる。

さらにWorkflowへ接続するとAutomated Governanceとなる。

```text
Idea
→ Prose Candidate
→ Code
→ Executable Rule
→ CI
→ Repository Governance
```

下流へ行くほどHuman Sealを強くすべきだった。

## 4.5 The checker self-required its own governance surfaces

Prototype Pythonでは以下をRequired FilesとしてHard Error化した。

```text
README.md
CURRENT_BOARD.md
tools/check_repo_reality.py
.github/workflows/reality-check.yml
```

これはCourt Experimentが「Court自身が無いRepositoryをErrorとする」自己正当化構造を持つRiskがある。

## 4.6 Empty README is not universally an error in Ark Project

Ark21:06自身で、Humanが先に空READMEを作り、後からHarvestを入れる運用が実際に存在した。

したがって：

```text
"Ark21:06が空のまま入口になっていたことは問題だった"
```

と、

```text
"全READMEは常に非空でなければERROR"
```

は同一ではない。

Intentional Placeholder / Historical / Fixture / Candidate / Active Broken Entry等の身分分離が必要。

## 4.7 Observer should precede Enforcer

より安全な成熟順序Candidate：

```text
Stage 0 — Idea
Stage 1 — Prose Prototype
Stage 2 — Isolated Experimental Scanner / manual only
Stage 3 — Shadow Observation / non-blocking
Stage 4 — Human review of invariants
Stage 5 — Active Tool
Stage 6 — Advisory CI
Stage 7 — Enforcement CI only for Human-sealed invariants
```

今回の実装はStageを飛ばし過ぎた。

---

# 5. Bottlenecks / Unexpected Success

## 5.1 HEAD self-reference problem

初期Board案では`head_commit`をBoard自身へ固定する案があった。

しかしBoardを含むCommit自身のSHAを、そのCommit作成前に本文へ書くと自己参照問題になる。

改善Candidate：

```text
reality_base_commit
= known provenance point

live HEAD
= resolve at read/check time
```

## 5.2 Git subprocess safety block

最初のPython CandidateではGit subprocessを使い、`reality_base_commit` ancestryまで検証しようとした。

GitHub Connector SafetyでWrite Blockされた。

```text
Attempt
→ Safety Block
→ attack surface exposed
→ subprocess/git execution removed
→ checked-tree-only scanner
→ Write succeeds
```

Task FailureではあるがDiagnostic Outcomeは有用だった。

## 5.3 Workflow observability boundary

Connectorで利用できたworkflow-run fetchはPR-triggered runsへ限定されていた。

したがってpush-triggered runを直接観測できず：

```text
No visible run
≠ workflow did not run
≠ PASS
≠ FAIL
```

というEpistemic Guardが必要になった。

---

# 6. Prototype Snapshot — `CURRENT_BOARD.md`

以下はmain上へ一時展開されたBoardの最終Snapshot。**Historical Experiment Source**として保存する。

```markdown
---
title: "CURRENT_BOARD"
board_version: "v001-experimental"
board_status: "experimental-active"
canonicality: "volatile operational board / not repository constitution"
repository: "yusukefujiijp/ai-project"
canonical_branch: "main"
reality_base_commit: "27e0329a5702a46257d72aaa3e684f17e5b64e51"
head_resolution: "derive live at read/check time; do not hard-code self-referential HEAD"
last_verified: "2026-08-20"
review_scope: "root-routing / current-board / required-file existence / UTF-8 / empty README / front-matter canonical_path / internal Markdown links"
current_gate: "RC-01 Board + Court + Root routing implemented / first push-run result not directly observable by current connector"
next_action_id: "RC-01-OBSERVE-FIRST-RUN"
human_seal_required_for: "canonical cutover / retirement / public write / destructive change"
root_guard: "Root and Human-AI authority remain governed by README.md; this Board is a Keli, not Root or constitution."
---

# CURRENT_BOARD
## 【Repository Current Reality: Minimal Reality Court Experiment】

> [!IMPORTANT]
> `CURRENT_BOARD.md` is a volatile operational board, not a second constitution and not a replacement for `README.md`.

## 0. 30-Second Board

repository: yusukefujiijp/ai-project
canonical_branch: main
reality_base_commit: 27e0329a5702a46257d72aaa3e684f17e5b64e51
live_head: derive from GitHub / Actions GITHUB_SHA; do not embed
board_status: experimental-active
current_gate: RC-01 Board + Court + Root routing implemented; first-run evidence pending direct observation
next_action: Observe the first Reality Court run and classify errors/warnings without broad migration.

## 1. Why HEAD Is Not Hard-Coded

A file committed into Git cannot practically contain the SHA of the very commit that contains it without creating a self-referential update loop.

`reality_base_commit` is provenance. live HEAD is resolved at read/check time.

The minimal safe Court v001 did not execute Git subprocess commands after the first subprocess-based attempt was blocked by the GitHub connector safety layer.

## 2. One-Line Current State

The experiment attempted a stable Root Constitution + volatile CURRENT_BOARD + read-only Minimal Reality Court architecture.

## 3. Current Proof

- Root Bootloader exists.
- Root README was temporarily v002 and routed through Current Board.
- Ark21:06 Session Harvest exists and is non-empty.
- Current Board exists.
- Minimal Reality Court source exists.
- Reality Court workflow exists.
- Push-run result was not directly observable through the available connector.

## 4. RC-01 — Minimal Reality Court

Hard-error jurisdiction candidate:
- required Court surfaces exist;
- Markdown files decode UTF-8;
- every README is non-empty;
- CURRENT_BOARD required metadata exists.

Warning candidate:
- missing canonical_path targets;
- missing internal Markdown links;
- link escapes repository;
- Root README lacks Board route.

Outside jurisdiction:
- Human Mission / Meaning;
- spiritual Reality / divine guidance;
- Human Final Seal;
- D1→Canonical decisions;
- theological correctness.

## 5. Workflow Reality

- push to main
- pull_request
- workflow_dispatch
- ubuntu-latest
- Python 3.12
- actions/checkout@v7
- actions/setup-python@v7
- `python tools/check_repo_reality.py`
- contents: read

## 6. First-Run Evidence

push_run_status: UNOBSERVED_BY_CURRENT_CONNECTOR
errors: unknown
warnings: unknown
strict_mode: false

## 7. Drift Register

- D-01 machine validator absent before experiment
- D-02 root route candidate
- D-03 heterogeneous status
- D-04 stale canonical_path candidate
- D-05 stale Markdown links candidate
- D-06 runtime/query registry absent
- D-07 generated search index absent
- D-08 push workflow observability limitation

## 8. Single Next Action

Observe actual Court output before any broad migration.

## 9. Done Condition

Full empirical closure required actual workflow observation; it was not achieved.

CURRENT_BOARD_EOF_v001-experimental
```

> Note: Above is a semantically complete compact snapshot. Exact historical Board bytes remain recoverable from Git blob `2b6cd411f82414d2d6c6175a277c066f20bb2f24` and Git history.

---

# 7. Prototype Snapshot — `tools/check_repo_reality.py`

Exact experimental Python source follows.

```python
#!/usr/bin/env python3
"""Minimal Reality Court for ai-project.

Checks only repository facts that can be read from the checked-out tree.
It does not judge Human meaning, theology, Human Seal, or canonical intent.
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

REQUIRED_FILES = (
    "README.md",
    "CURRENT_BOARD.md",
    "tools/check_repo_reality.py",
    ".github/workflows/reality-check.yml",
)

BOARD_REQUIRED_KEYS = (
    "board_version",
    "board_status",
    "repository",
    "canonical_branch",
    "reality_base_commit",
    "last_verified",
    "review_scope",
    "current_gate",
    "next_action_id",
)

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
META_RE = re.compile(r"^([A-Za-z0-9_.-]+):\s*(.*?)\s*$")

@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        where = self.path if self.line <= 0 else f"{self.path}:{self.line}"
        return f"[{self.severity}] {self.code} {where} — {self.message}"

def read_utf8(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError as exc:
        return None, f"not valid UTF-8: {exc}"
    except OSError as exc:
        return None, str(exc)

def front_matter(text: str) -> tuple[dict[str, str], dict[str, int]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, {}
    data: dict[str, str] = {}
    positions: dict[str, int] = {}
    for i in range(1, end):
        match = META_RE.match(lines[i])
        if not match:
            continue
        key, value = match.groups()
        data[key] = value.strip().strip('"').strip("'").strip("`")
        positions[key] = i + 1
    return data, positions

def outside_fences(text: str) -> list[tuple[int, str]]:
    visible: list[tuple[int, str]] = []
    in_fence = False
    fence = ""
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE_RE.match(line)
        if match:
            token = match.group(1)
            if not in_fence:
                in_fence, fence = True, token
            elif token == fence:
                in_fence, fence = False, ""
            continue
        if not in_fence:
            visible.append((number, line))
    return visible

def clean_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1 : raw.index(">")].strip()
    if " " in raw:
        first, rest = raw.split(" ", 1)
        if rest.lstrip().startswith(('"', "'", "(")):
            raw = first
    return raw.strip()

def external_or_anchor(target: str) -> bool:
    lower = target.lower()
    return (
        not target
        or target.startswith("#")
        or lower.startswith(("http://", "https://", "mailto:", "tel:", "data:"))
    )

def resolved_target(root: Path, source: Path, target: str) -> Path | None:
    target = unquote(target).split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    candidate = root / target.lstrip("/") if target.startswith("/") else source.parent / target
    return candidate.resolve()

def within(root: Path, path: Path) -> bool:
    try:
        path.relative_to(root.resolve())
        return True
    except ValueError:
        return False

def main() -> int:
    parser = argparse.ArgumentParser(description="Check minimal ai-project repository reality.")
    parser.add_argument("--strict", action="store_true", help="Promote warnings to errors.")
    args = parser.parse_args()

    root = Path.cwd().resolve()
    findings: list[Finding] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            findings.append(Finding("ERROR", "REQUIRED_FILE_MISSING", rel, 0, "required Court surface is missing"))

    markdown_files = sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)
    texts: dict[Path, str] = {}

    for path in markdown_files:
        rel = path.relative_to(root).as_posix()
        text, error = read_utf8(path)
        if error:
            findings.append(Finding("ERROR", "UTF8_FAILURE", rel, 0, error))
            continue
        assert text is not None
        texts[path] = text

        if path.name.lower() == "readme.md" and not text.strip():
            findings.append(Finding("ERROR", "EMPTY_README", rel, 0, "README is empty or whitespace-only"))

        meta, positions = front_matter(text)
        canonical_path = meta.get("canonical_path")
        if canonical_path and not any(ch in canonical_path for ch in "{}<>"):
            if not (root / canonical_path.lstrip("/")).exists():
                findings.append(Finding("WARN", "CANONICAL_PATH_MISSING", rel, positions.get("canonical_path", 0), canonical_path))

    board_path = root / "CURRENT_BOARD.md"
    board_text = texts.get(board_path)
    if board_text is not None:
        board, positions = front_matter(board_text)
        for key in BOARD_REQUIRED_KEYS:
            if not board.get(key):
                findings.append(Finding("ERROR", "BOARD_METADATA_MISSING", "CURRENT_BOARD.md", positions.get(key, 0), key))

    root_text = texts.get(root / "README.md")
    if root_text is not None and "CURRENT_BOARD.md" not in root_text:
        findings.append(Finding("WARN", "ROOT_BOARD_ROUTE_MISSING", "README.md", 0, "Root README does not yet route to CURRENT_BOARD.md"))

    for source, text in texts.items():
        rel = source.relative_to(root).as_posix()
        for line_no, line in outside_fences(text):
            for match in LINK_RE.finditer(line):
                target = clean_target(match.group(1))
                if external_or_anchor(target):
                    continue
                resolved = resolved_target(root, source, target)
                if resolved is None:
                    continue
                if not within(root, resolved):
                    findings.append(Finding("WARN", "LINK_ESCAPES_REPO", rel, line_no, target))
                elif not resolved.exists():
                    findings.append(Finding("WARN", "INTERNAL_LINK_MISSING", rel, line_no, target))

    if args.strict:
        findings = [Finding("ERROR" if item.severity == "WARN" else item.severity, item.code, item.path, item.line, item.message) for item in findings]

    findings.sort(key=lambda item: (item.severity != "ERROR", item.path, item.line, item.code))
    errors = [item for item in findings if item.severity == "ERROR"]
    warnings = [item for item in findings if item.severity == "WARN"]

    for item in findings:
        print(item.render())

    print()
    print(f"REALITY_COURT_STATUS: {'PASS' if not errors else 'FAIL'}")
    print(f"head_commit: {os.environ.get('GITHUB_SHA', 'LOCAL_OR_UNKNOWN')}")
    print(f"markdown_files: {len(markdown_files)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    print(f"strict_mode: {args.strict}")

    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
```

Historical exact blob:

```text
9ae7c177a78f081d816a25da4d92021c5c582fec
```

---

# 8. Prototype Snapshot — `.github/workflows/reality-check.yml`

Exact experimental Workflow source follows.

```yaml
name: Repository Reality Court

on:
  push:
    branches:
      - main
  pull_request:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  reality-court:
    name: Minimal Reality Court
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: Checkout repository
        uses: actions/checkout@v7
        with:
          fetch-depth: 1

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.12"

      - name: Run Reality Court
        run: python tools/check_repo_reality.py
```

Historical exact blob:

```text
3e06c641f3bfe4cbce3196338c7bbcb794896f9d
```

---

# 9. Experimental Invariant Problem

Future AIがこのExperimentを再開する場合、Codeを書く前に`Invariant Registry`相当を先に設計すべきCandidateがある。

例：

```yaml
confirmed_invariants:
  - "Root README exists"
  - "canonical branch is main"

experimental_hypotheses:
  - "every README must be non-empty"
  - "every internal historical link must resolve now"
  - "every canonical_path must resolve now"
  - "a repository-wide Current Board should exist"
  - "Reality Court should be a required repository surface"
```

`experimental_hypotheses`を直接Hard Errorへ変換しない。

---

# 10. Safer Future Experiment Route Candidate

このExperimentを将来再開するなら、現時点では次の順序がより安全。

```text
1. Experiment questionをProseで定義
2. Ark21-06/sandbox等の隔離SurfaceでPrototype保存
3. Canonical Root / active tools / .github workflowは触らない
4. Manual / Shadow Scannerとして試す
5. exit 0 / report-onlyでActual Trace収集
6. False Positive / False NegativeをHuman-AIで分類
7. Humanが本当にInvariantと認定したRuleだけSeal
8. その後Active Tool化を別Gateで判断
9. CI Advisoryを別Gateで判断
10. Blocking Enforcementをさらに別Gateで判断
11. Root Router変更はExperiment成功後の最後のCutover候補
```

重要：

> **Root READMEはExperimentで最初に触る場所ではなく、成功したExperimentをCanonicalへ昇格するとHumanが判断した後に最後に触る場所。**

---

# 11. Deletion Checklist — Human Manual Action

HumanがGitHub UIから手動削除する対象は以下の**3ファイル全部**。

```text
1. CURRENT_BOARD.md
2. tools/check_repo_reality.py
3. .github/workflows/reality-check.yml
```

## Do NOT delete

```text
README.md
ark-project/ark21/Ark21-06/README.md
ark-project/ark21/Ark21-06/sandbox/README.md
```

## Directory note

現時点のLive Repository確認では：

```text
tools/
└─ check_repo_reality.py  # only file

.github/
└─ workflows/
   └─ reality-check.yml   # only file
```

したがって上記2ファイルを削除後、Git上では空Directoryは自然消滅する。

---

# 12. Future-AI Retrieval Keywords

`CURRENT_BOARD` / `Reality Court` / `Minimal Reality Court` / `check_repo_reality.py` / `reality-check.yml` / `Repository Governance Experiment` / `Experimental Isolation` / `Rollback` / `Root README v002` / `Root README v001 restore` / `Topology Weight` / `Blast Radius` / `Observer First` / `Enforce Later` / `Executable Policy` / `Invariant Registry` / `empty README` / `Intentional Placeholder` / `HEAD self-reference` / `subprocess safety block` / `GitHub Actions observability` / `Ark21:06 sandbox`

---

# 13. Final Compression

```text
External Review was useful.
↓
Implementation was too early.
↓
Experiment crossed into Canonical / Active surfaces.
↓
Root README was restored to v001.
↓
Ark21:06 Session Harvest v001 was never changed.
↓
Board / Python / Workflow knowledge is preserved here.
↓
Their active files should be manually deleted.
↓
Future restart, if any, should begin in isolation and observation mode.
```

> **不足より過剰。ただしExperiment Knowledgeを残すことと、ExperimentをActive Governanceとして残すことは別である。**

> **Knowledge is preserved here; authority is not.**

---

document_end:
  filename: "ark-project/ark21/Ark21-06/sandbox/README.md"
  version: "v001-experimental-harvest"
  eof_sentinel: "ARK21_06_REALITY_COURT_SANDBOX_EOF_v001-experimental-harvest"

ARK21_06_REALITY_COURT_SANDBOX_EOF_v001-experimental-harvest
