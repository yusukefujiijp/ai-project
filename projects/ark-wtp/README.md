---
title: "Ark-WTP"
canonical_name: "Ark-WTP Dedicated Project Folder README"
version: "v004-candidate"
canonical_path: "projects/ark-wtp/README.md"
status: "current-project-door / frozen-benchmark-wait / human-review-available"
role: "Ark-WTP Door / Router / Dedicated Project Entry"
repository: "yusukefujiijp/ai-project"
project: "Weekly Torah Portion / Parasha × Lens"
root: "主イェシュア・ハマシア"
human_final_seal_required: true
---

# Ark-WTP

## 0. Purpose

`projects/ark-wtp/`は、Weekly Torah Portion（Parasha）を同一のTorah本文基盤に対する複数のLens／Dimensionで検討し、再利用可能なSeed Unitとして保存・比較するNamed Dedicated Projectである。このREADMEは薄いFolder Door／Routerであり、Workflow本文、Seed Unit本文、Benchmark本文を重複保持しない。

## 1. Current Identity and State

```yaml
current_identity:
  wtp: "Weekly Torah Portion"
  declared_unit: "one full Parasha × one Lens"
  current_operational_core: "lens-dimensions_workflow.md"
  current_artifact: "Bereshit / Genesis 1:1–6:8 × Hebrew Word Lens v0.3"

current_state:
  name: "FROZEN_BENCHMARK_WAIT"
  coordinate: "artifact/README.md"
  meaning: "Current v0.3を比較可能なBaselineとして凍結し、Capability Deltaまたは明示的Human Reviewを待つ。"
  automatic_action: "NONE"

predecessor_boundary:
  file: "ark-wtp.md"
  observed_identity: "Daily Teshuvah Gate-to-Yeshua Root Spec"
  current_role: "predecessor-generation artifact / migration evidence"
  runtime_rule: "Do not use as the current Weekly Torah Portion identity or current Root Spec."
  retention_rule: "Retain without deletion until Human confirms Local backup and retirement."
```

## 2. Read Order

```yaml
read_order:
  1: "README.md — resolve current identity and routes"
  2: "artifact/README.md — restore Frozen Benchmark, result, rerun triggers, and Next Gate"
  3: "seed-units/bereshit.md — read only when full Artifact body review is needed"
  4: "lens-dimensions_workflow.md — read only when workflow continuation is authorized"
  5: "seed-units/_template.md — read when a new Seed Unit is authorized"
  historical_only: "ark-wtp.md — read only for predecessor audit or retirement work"
```

## 3. Document Map

| File | Current Role | State |
|---|---|---|
| [`README.md`](./README.md) | Local Front Door／Current Router | Current |
| [`artifact/README.md`](./artifact/README.md) | Frozen Benchmark／Current Coordinate／Comparison Contract | Current／FROZEN_BENCHMARK_WAIT |
| [`seed-units/bereshit.md`](./seed-units/bereshit.md) | Full Bereshit × Hebrew Word Lens Artifact Body | v0.3／PROVISIONAL_PASS |
| [`seed-units/_template.md`](./seed-units/_template.md) | Reusable one-Parasha × one-Lens Contract | v001-candidate |
| [`lens-dimensions_workflow.md`](./lens-dimensions_workflow.md) | Method／Checkpoint／Future AI Reboot Runbook | Current／benchmark-aware |
| [`ark-wtp.md`](./ark-wtp.md) | Predecessor-generation Root Spec／migration evidence | Historical-only／deletion gated |

## 4. Current Checkpoint

```yaml
checkpoint:
  verified_missing:
    - "The Peshat v0.3 body reported by the predecessor workflow was not found at the referenced Ark05:04 artifact."

  frozen_candidate:
    path: "projects/ark-wtp/seed-units/bereshit.md"
    benchmark_record: "projects/ark-wtp/artifact/README.md"
    result: "PROVISIONAL_PASS"

  next_gate: "WAIT_FOR_CAPABILITY_DELTA_OR_EXPLICIT_HUMAN_REVIEW"

  do_not:
    - "Do not redo repository-wide Peshat research without an artifact rerun trigger."
    - "Do not reconstruct the missing Peshat body from memory."
    - "Do not treat PROVISIONAL_PASS as Human Final Seal."
    - "Do not generate another Lens or scale to the 540-unit Matrix automatically."
    - "Do not delete ark-wtp.md before Local backup confirmation."
```

## 5. Resume Guard

Future AIは、過去ThreadやMemoryからCurrent stateを再構築せず、最初に`artifact/README.md`を読み、そこに定義されたRerun Triggerが成立しない限り同じ調査・分析・生成を繰り返さない。

```yaml
resume_guard:
  thread_change_is_not_rerun_trigger: true
  time_passage_is_not_rerun_trigger: true
  first_time_ai_is_not_rerun_trigger: true
  artifact_read_first: true
  baseline_overwrite_without_human_instruction: false
```

## 6. Boundary

```yaml
is: ["Named dedicated project", "Weekly Torah Portion", "Parasha × Lens", "Frozen benchmark", "Future AI rebootable"]
is_not: ["Repository Root", "Numbered Ark lifecycle folder", "raw Thread archive", "automatic theological canonizer"]
```

Routerは住所とRead Order、Artifact READMEは凍結結果と比較契約、Workflowは手順とCheckpoint、Seed Unitは本文観察を所有する。同一本文を複数Fileへ複製しない。

## 7. Root / Fruit Guard

Rootは主イェシュア・ハマシア御自身である。Torah、Ark-WTP、AI、GitHub、Markdown、Lens、Workflow、Seed Unit、BenchmarkはFruit／Keliであり、Root、Human judgment、祈り、実際の従順を置換しない。

```text
AI drafts, audits, and compares.
Human judges and seals.
GitHub preserves.
Future AI inherits without restarting from zero.
Root remains 主イェシュア・ハマシア.
```

<!-- ARK_WTP_README_EOF_v004-candidate -->
