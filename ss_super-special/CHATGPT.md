# CHATGPT.md

## 0. Executive Compression / 中核圧縮

このFileは、Future AIのための全Project共通Collaboration Guideである。

目的は、UserとAI-Collaboratorの継続協働を、短い規則として保持することである。

```text
Stone, not manual.
Rules, not logs.
Future AI first.
```

---

## 1. GitHub Placement / GitHub配置

```yaml
target_path: "ss_super-special/CHATGPT.md"
source_bootstrap: "S_CHATGPT_v005.md"
path_policy: "versionless path"
version_policy: "frontmatterなし / git commit history"
format_policy: "Japanese-first OKF"
```

YAML frontmatter形式がtool writeで止まる場合、このFileではfrontmatterを本文内OKF blockとして保持する。

---

## 2. Collaboration Formula

```text
AI drafts.
Human seals.
GitHub stores.
Reality confirms.
```

```text
Plan is not Commit.
Preview is not Commit.
Human Seal is Commit Gate.
```

---

## 3. Human Direct Commit Fallback

AI tool writeがblockされるかどうかは、事前には分からない。

したがって、本来版で一回は試す。

```text
Try original once.
If blocked, stop.
Do not degrade.
Change transport.
```

blockされた場合は、本来版を劣化させず、Copy & Paste用file / Manual Commit Packへ切り替える。

---

## 4. CopyPasteSurfaceGuard

GitHub UIなどへ貼る値を提示する時、labelはcode block外へ出す。

code block内には、実際に貼る本文だけを入れる。

```text
label outside code block.
field value only inside code block.
```

悪い例：

```text
Commit message:
docs(example): update file
```

良い例：

```text
docs(example): update file
```

---

## 5. Download / ZIP Policy

Download付きリンクを出す時、zipは常に必要ではない。

```text
1 file: no zip.
2 files: usually no zip.
3+ files or folder structure: consider zip.
```

日本語：

```text
1ファイルならzip不要。
2ファイルまでは基本zip不要。
3ファイル以上またはfolder構造ならzip検討。
```

---

## 6. File Naming / Canonical Role

Filename is a Gate.

```yaml
canonical_roles:
  S_: "Stone Tablet / System Covenant / highest-grade shared file"
  G_: "Global Lens / cross-project guard / theory map"
  P_: "Project Living Surface / project-specific persistent file"
  MAP_: "export map or imported reference map"
  T_: "transfer / temporary / thread-bridge"
  Temp_: "incubation / proposal / lab"
```

GitHubでは、stable / versionless pathを基本とする。

```text
Path is the address.
Commit history is the version ledger.
```

---

## 7. Verify Before Done

完了宣言には証拠が必要である。

```yaml
evidence_examples:
  - "citations"
  - "direct inspection"
  - "GitHub fetch"
  - "diff"
  - "test"
  - "screenshot"
  - "log"
  - "download link"
  - "file existence check"
```

---

## 8. Final Compression

```text
CHATGPT.md is the all-project collaboration guide.

AI drafts.
Human seals.
GitHub stores.
Reality confirms.

Tool block is not workflow block.
Do not degrade meaning.
Change transport.

For copy-paste:
  label outside code block.
  field value only inside code block.

For downloads:
  1 file: no zip.
  2 files: usually no zip.
  3+ files or folder structure: consider zip.
```
