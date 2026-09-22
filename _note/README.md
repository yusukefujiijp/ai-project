---
title: "_note"
canonical_path: "_note/README.md"
status: "living_index"
role: "Living Notes Directory Guide"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
version_model: "git history"
route_alignment:
  date: "2026-09-22"
  base_commit: "945f789a845350455a8b56162a1fc8cd58576eff"
  scope: "D01: purpose-specific handoff and harvest storage routes; note identity and authority rules retained"
  change_record: "control-center/changes/STR-001-navigation-and-ownership.md"
---

# _note

## 0. Purpose

`_note/` is the place for living notes that support Ark Project work.

```text
Record useful insight.
Preserve working knowledge.
Do not turn notes into automatic authority.
```

Notes are support material.  
Notes are not automatic authorization.

```yaml
_note_is:
  - "living note storage"
  - "AI collaboration memory support"
  - "experiment note area"
  - "review note area"
  - "future-AI navigation aid"

_note_is_not:
  - "Root README replacement"
  - "automatic execution permission"
  - "final SSOT by default"
  - "GitHub operation authorization"
  - "Human Seal replacement"
```

---

## 1. What Belongs Here

Use `_note/` for notes that are valuable enough to preserve, but not yet promoted to root-level protocol.

```yaml
belongs_here:
  - "AI collaboration notes"
  - "review capability notes"
  - "workflow observations"
  - "experimental operating notes"
  - "Future AI misread warnings"
  - "minimal patch / guard lessons"
```

A note may later influence README, protocol, or workflow files, but it does not automatically override them.

---

## 2. What Does Not Belong Here

`_note/`は、未整理の大規模Transcript、一時Scratch、既に専用の所有先があるThread Handoff・Harvestの代替保存先ではない。

保存先は、Current Human Requestと選ばれた契約の役割から決める。

| Node | Edge | 保存判断 |
|---|---|---|
| 現行ArkのThread継続・章移行・補助線再接続 | [共通移行契約](../prompts/ai-next-thread-handoff.md) → 明示Handoff／対象Runtime | 対象単位・役割・Exact Pathsを解決する。通常のThread三ファイルはREADMEが安定Runtime、handoffが初期化、stateが可変状態を所有する |
| 保存されているThread-End方式を明示利用 | [Thread-End入口](../thread-end/README.md) → [Artifact入口](../thread-end/ark/README.md) | その方式のBinding・命名・保存先に従う。既存の平置き履歴は保持する |
| Thread固有のHarvest | Current Runtime／該当Projectの所有資料 | その成果の意味に合う既存保存先へ接続する。すべてをHandoffやNoteへまとめない |
| 方法の補助となるLiving Note | このREADME → `_note/` | 専用の所有資料へ昇格していない支援知識を保持する |

例えば、Thread単位のフォルダ内にある `handoff.md` は役割が明確な正規名になり得る。旧方式の平置き用ファイル名を、すべてのThread構成へ一律適用しない。新しい補助線再接続から、不要な章・Thread三ファイルを自動作成しない。

旧 `_thread-end/ark/` は現行の保存先ではない。当時の履歴内の旧パスは歴史資料として扱う。案内を読むことは保存や移動の承認を追加しない。修復理由は[STR-001](../control-center/changes/STR-001-navigation-and-ownership.md#d01)を参照する。

---

## 3. Current Notes

```yaml
current_notes:
  - path: "_note/fable5-review_note.md"
    role: "Ark Project Fable5 Review Operating Note"
    status: "living_note"
    summary:
      - "Fable5 detects risk"
      - "ChatGPT performs Living Review"
      - "Human gives Seal"
      - "GitHub receives only accepted minimal patches"
      - "Fable5 is reviewer, not Root"
```

---

## 4. How Future AI Should Use Notes

Future AI may read `_note/` files to understand context, experiments, and operating patterns.

```yaml
future_ai_use:
  allowed:
    - "read notes for context"
    - "use notes to improve judgment"
    - "cite notes as supporting material"
    - "propose next steps based on notes"

  forbidden:
    - "treat notes as automatic execution permission"
    - "promote notes to SSOT without Human Seal"
    - "overwrite workflow based only on a note"
    - "perform GitHub operations from note content alone"
```

Notes can inform judgment.  
Notes do not replace judgment.

---

## 5. Human Seal / GitHub Guard

Repository operations require explicit authorization.

```yaml
human_seal_ok:
  means:
    - "content / direction / path candidate approved"

  does_not_mean:
    - "repository operation may run automatically"

execute_github_ok:
  means:
    - "explicit permission to perform the repository operation"

  required_for:
    - "create_file"
    - "update_file"
    - "delete_file"
```

Safe rule:

```text
Human Seal OK approves the artifact.
Execute GitHub OK approves the repository operation.
```

---

## 6. Note Promotion Guard

A note can become a stronger project document only after review.

```yaml
promotion_guard:
  possible_future_paths:
    - "README patch"
    - "protocol patch"
    - "workflow note"
    - "thread-end artifact"
    - "mission card / seed card material"

  requires:
    - "ChatGPT Living Review"
    - "Human Seal"
    - "exact target path"
    - "minimal accepted patch"
```

Do not promote a note automatically.

---

## 7. Root / Fruit Guard

`_note/` is Fruit.

```yaml
fruit:
  - "_note/"
  - "living notes"
  - "Markdown"
  - "GitHub"
  - "AI"
  - "Fable5"
  - "Living Review"
  - "Full Rail / Next Gate"

root:
  - "主イェシュア・ハマシア"
```

Final guard:

```text
Notes are Fruit, not Root.
AI is Fruit, not Root.
GitHub is Fruit, not Root.

Root remains 主イェシュア・ハマシア.
```

