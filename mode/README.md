---
title: "Ark Mode"
canonical_path: "mode/README.md"
route_alignment:
  date: "2026-09-22"
  base_commit: "945f789a845350455a8b56162a1fc8cd58576eff"
  scope: "D08: mode inventory, shared-skill route and existing filename exception; no activation or rename"
  change_record: "control-center/changes/STR-001-navigation-and-ownership.md"
---

# Ark Mode

`mode/` は、Ark Projectで一定期間維持されるAI Runtime Modeを置くFolderである。

## 1. Modeとは

Modeは一回の提案Skillではない。

ActivationからExitまで複数Turnにわたり、AIのInteraction State・応答姿勢・進行Flowを導くRuntimeである。

```text
Activation
↓
State Transition
↓
Multi-turn Runtime
↓
Exit
```

## 2. Skillとの違い

```text
skills/README.md
= Shared Skill Source / Distribution Hub

mode/
= 起動後しばらく維持されるRuntime Mode Layer
```

[Skills入口](../skills/README.md)は共有原本・配布の案内を所有する。共有原本の存在は、この環境への導入済みを意味しない。

SkillはModeを助けることがある。
しかし、ModeをSkill Inventoryへ混ぜない。

## 3. Current Modes

### [AI Journaling Mode](ai-journaling_mode.md)

Human Realityを起点にJournalingを開始・継続・切替・終了するMode。

```text
Evidence-First Reversible Reflection
+
One Open Slot
```

本文の記載は `v001` / `experimental / human-editable`。自己パスを実在する `mode/ai-journaling_mode.md` に合わせた。実利用・有効性をこの索引で認定しない。

### [AI Field Test Mode](ai-field-test-mode.md)

Runtimeを持つAI Artifactの挙動・Evidenceを観察し、Human Reviewへ返す検証Mode候補。

本文の記載は `v001.1-draft` / `static-reviewed` / `not runtime-field-tested` / `not final-sealed`。2026-09-22に存在と保存本文を確認した。記録外の実行状況はUnknownであり、掲載自体を起動・試験・採用の承認にしない。

## 4. Core Rule

- ModeはHumanの明示Intentまたは明確なMeaningで起動する
- Modeを全回答へ自動適用しない
- Humanはいつでも修正・中断・終了できる
- Current requestとHuman AuthorityをModeより上位に置く
- ModeはRootやHumanの識別を置換しない
- 必要なModeだけを読み、全Modeをdefaultで起動しない

## 5. Filename Rule

`/prompts/` 内のAI-Promptは、Folder ContextによってPromptであることを識別できる。

`/prompts/` 外へ置くAI-Promptは、Future AIがfilename単体でもRoleを識別できるよう、末尾にunderscoreから始まるRole suffixを付ける。

Mode Fileの基本形：

```text
<semantic-name>_mode.md
```

Good：

```text
mode/ai-journaling_mode.md
```

Avoid：

```text
mode/ai-journaling.md
mode/ai-journaling-mode.md
```

`_mode` は重複ではなく、`/prompts/` 外のAI-PromptであることとRuntime Roleを一目で伝えるRepository Contractである。

既存の `ai-field-test-mode.md` は、この推奨形と異なる名前で存在する。今回の索引整合では元パスを保持し、明示した既存例外として案内する。将来改名する場合は参照元・固定Binding・互換性を確認する独立した変更として扱い、命名差だけで退役や誤ファイルと判定しない。[今回の判断 STR-001](../control-center/changes/STR-001-navigation-and-ownership.md#d08)を参照する。

## 6. KISS / DRY / YAGNI / Lean

- KISS: Deep structure, light next action.
- DRY: Modeの正式説明は対象Mode fileへ置く
- YAGNI: Realityが要求していないModeやRouterを増やさない
- Lean: 実際の詰まりを見て、小さくPatchする

## 7. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

Mode、Skill、AI、GitHub、Markdown、Prompt、WorkflowはFruit / Keliであり、Rootではない。

## 8. Final Compression

```text
Skill lights a capability.
Mode sustains a runtime.
Human starts, corrects, and stops.
```

Stable Coreを守り、Future AIが働ける余白を残す。
