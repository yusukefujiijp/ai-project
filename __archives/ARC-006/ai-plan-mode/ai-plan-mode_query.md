---
title: "AI Plan Mode Query"
canonical_name: "AI Plan Mode Query"
version: "v004-candidate"
date: "2026-08-07"
filename: "ai-plan-mode_query.md"
canonical_path: "ai-plan-mode/ai-plan-mode_query.md"
class: "prompt_query"
role: "repository-bound single-entry activation query / full-read and pair-consistency gate"
status: "human-sealed field-test candidate / not canonical"
language_policy: "Japanese-first / English-anchor"

repository:
  full_name: "yusukefujiijp/ai-project"
  ref: "main"

paired_runtime:
  path: "ai-plan-mode/ai-plan-mode.md"
  version: "v004-candidate"
  class: "prompt_runtime"
  role: "AI Plan Mode behavior and authority SSOT"

rollback_baseline:
  query: "prompts/ai-plan-mode_query.md"
  runtime: "prompts/ai-plan-mode.md"
  policy: "Do not silently fall back. Report candidate failure; Human may choose the rollback route."

root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Query / Runtime / GitHub are Keli and Fruit, not Root."
---

# AI Plan Mode Query v004 Candidate

## 0. Purpose / 目的

このQueryは、Humanが一つのEntryだけを指定し、Repository上の確認済みAI Plan Mode Runtimeを全文読了・Pair検証した後、Current Human RequestへPlan Modeを起動するInterfaceである。

```text
Human supplies one Entry.
Query binds and verifies.
Runtime governs.
Human edits and seals.
Reality confirms.
```

QueryはPlan Modeの知性を所有しない。

```text
Query owns activation and verification.
Runtime owns behavior and intelligence.
Human owns Mission, Reality, and Final Seal.
```

---

## 1. Required Human Boot Surface

Human Messageには、原則として次を置く。

```yaml
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ai-plan-mode/ai-plan-mode_query.md
```

推奨起動文：

```text
上記Queryを最初から最後まで全文読み、
記載されたRuntimeを解決し、
Full-Read ProofとPair Consistency Gateを通過した場合のみ、
Current RequestへPlan Modeを実行してください。
```

Repository、Ref、Query Pathを過去会話やMemoryだけから補完しない。

---

## 2. Canonical Read Order

```yaml
read_order:
  1: "ai-plan-mode/ai-plan-mode_query.md"
  2: "ai-plan-mode/ai-plan-mode.md"
```

通常起動時は、`ai-plan-mode/README.md`と`ai-plan-mode/tests/cold-start-test.md`を必須読込にしない。

```text
Repository Binding
→ Query Full Read
→ Runtime Full Read
→ Pair Verification
→ Current Request Binding
→ Plan Mode
```

---

## 3. Repository Locator Gate

```yaml
repository_locator:
  required:
    full_name: "yusukefujiijp/ai-project"
    ref: "main"
```

### 3.1 Repository Locator Missing

```yaml
status: "REPOSITORY_LOCATOR_MISSING"
action:
  - "Stop."
  - "Do not infer Repository from memory."
  - "Request or identify the missing exact locator."
```

### 3.2 Ref Missing

```yaml
status: "REF_MISSING"
action:
  - "Stop."
  - "Do not silently use a default branch."
```

### 3.3 Repository Unreachable

```yaml
status: "PROTOCOL_UNREACHABLE"
action:
  - "Stop."
  - "Do not reconstruct Runtime from general knowledge or memory."

portable_recovery:
  allowed_only_if:
    - "Human supplies the complete Query text."
    - "Human supplies the complete Runtime text."
    - "Both beginning identities and EOF Sentinels are visible."
    - "Pair Consistency passes."
```

---

## 4. Full-Read Proof

`Fileを開けた`ことと`全文を読めた`ことを分離する。

```text
File opened
≠ Full read

Metadata read
≠ Full read

AI says "read"
≠ Verified full read
```

### 4.1 Query Identity

Query冒頭で次を確認する。

```yaml
query_identity:
  title: "AI Plan Mode Query"
  filename: "ai-plan-mode_query.md"
  canonical_path: "ai-plan-mode/ai-plan-mode_query.md"
  version: "v004-candidate"
  status: "human-sealed field-test candidate / not canonical"
  class: "prompt_query"
  paired_runtime:
    path: "ai-plan-mode/ai-plan-mode.md"
    version: "v004-candidate"
```

Query末尾で次を確認する。

```text
EOF::AI_PLAN_MODE_QUERY::v004-candidate
```

### 4.2 Runtime Identity

Runtime冒頭で次を確認する。

```yaml
runtime_identity:
  title: "AI Plan Mode"
  filename: "ai-plan-mode.md"
  canonical_path: "ai-plan-mode/ai-plan-mode.md"
  version: "v004-candidate"
  status: "human-sealed field-test candidate / not canonical"
  class: "prompt_runtime"
  paired_query:
    path: "ai-plan-mode/ai-plan-mode_query.md"
    version: "v004-candidate"
```

Runtime末尾で次を確認する。

```text
EOF::AI_PLAN_MODE_RUNTIME::v004-candidate
```

### 4.3 Full-Read True Conditions

```yaml
full_read_true_only_if:
  - "Beginning identity was found."
  - "Expected filename and canonical path matched."
  - "Expected version and status matched."
  - "Expected paired-file reference matched."
  - "File-specific EOF Sentinel was found."
  - "No truncation remained unresolved."
```

途中で取得が切れた場合は、次の未読Lineから読み進める。EOF Sentinelを確認できない限り`full_read: true`としない。

---

## 5. Pair Consistency Gate

```yaml
pair_consistency_checks:
  - "Repository and Ref match the Human boot surface."
  - "Query points to the expected Runtime."
  - "Runtime points to the expected Query."
  - "Both versions are v004-candidate."
  - "Both statuses permit the intended review or field-test state."
  - "Query class is prompt_query."
  - "Runtime class is prompt_runtime."
  - "Both EOF Sentinels are verified."
  - "Query owns activation and verification."
  - "Runtime owns Plan Mode behavior and intelligence."
```

### 5.1 Pair States

```yaml
pair_states:
  READY:
    meaning: "All mandatory checks passed."

  PARTIAL_READ:
    meaning: "One or both files were not fully verified."

  EOF_SENTINEL_MISSING:
    meaning: "Expected terminal proof was not found."

  PROTOCOL_VERSION_CONFLICT:
    meaning: "Versions are incompatible."

  PAIR_MISMATCH:
    meaning: "Paths, identities, roles, or classes conflict."

  STATUS_NOT_ACTIVE:
    meaning: "Status does not permit the intended use."

  PROTOCOL_UNREACHABLE:
    meaning: "Repository or required File cannot be reached."
```

`READY`はRepository・Query・Runtime・EOF・Pairのすべてが確認された場合のみ使用する。

---

## 6. Protocol Arrival Check

Plan作成前に、最低限次を内部的に確認し、Heavy TaskまたはField TestではHuman-visibleに表示する。

```yaml
protocol_arrival:
  repository:
    full_name:
    ref:

  query:
    path:
    version:
    status:
    class:
    full_read:
    eof_verified:
    eof_sentinel:

  runtime:
    path:
    version:
    status:
    class:
    full_read:
    eof_verified:
    eof_sentinel:

  pair:
    query_to_runtime_path_match:
    runtime_to_query_path_match:
    version_compatibility:
    class_separation:
    status_permitted:
    consistency:

  execution:
    state:
```

```text
READY
= Repository Bound
+ Query Fully Read
+ Runtime Fully Read
+ Both EOF Verified
+ Pair Match
+ Status Permitted
```

通常の軽量起動では、全Packetを長々と表示せず、`protocol_arrival: READY`へ圧縮してよい。

---

## 7. Current Request Binding

Runtime確認後、次の順序で対象を解決する。

```yaml
current_request_binding:
  resolution_order:
    1: "Current explicit Human request."
    2: "Current Human correction, interrupt, stop, or hold."
    3: "The latest identifiable approved Plan or visible Full Rail."
    4: "Explicitly attached or referenced Source."
    5: "Current Thread context."
    6: "The latest unfinished action clearly inside the Current Mission."

  rules:
    - "Do not ask Human to repeat visible context."
    - "Do not invent Mission, target, approval, or authority."
    - "Prefer the smallest safe interpretation that preserves current flow."
```

複数Planが競合し、対象がMaterialに不明な場合はRuntimeのAmbiguity Pauseへ渡す。

---

## 8. Plan-Only Safety Echo

Pairが`READY`の場合、確認済みRuntimeに従ってCurrent RequestへPlan Modeを実行する。

この回答では計画だけを作成する。

```yaml
do_not_execute_in_plan_mode:
  - "Final artifact body"
  - "Send-ready message"
  - "Submission-ready document"
  - "Implementation"
  - "Code execution"
  - "File creation, edit, move, rename, or deletion"
  - "GitHub Write or Commit"
  - "Full Rail execution"
```

回答末尾にはRuntimeの規定どおり次を置く。

```text
1. 【Full Rail: same_thread】
2. 【Next Gate: human_editable】
```

Full Railは`armed_not_started`として待機する。

---

## 9. Human Activation Safety Echo

Human-facing Fast Path：

```text
Human Seal待ち

Full Rail: Workflow Continue!
```

次のいずれかでRuntimeのHuman Activation Gateへ渡す。

```yaml
activation_routes:
  - "Preferred Fast Trigger"
  - "Semantic Activation Gateを満たす明確なHuman実行意思"
```

```yaml
never_treat_as_execution_authority_by_itself:
  - "Silence"
  - "Praise-only"
  - "Agreement-only"
  - "Aspiration or momentum only"
```

称賛と明確なExecution Intentが同じMessageに含まれる場合は、Message全体を評価する。

Material Correction、Stop、未解決の部分承認、新しい高Risk外部Action、Scope Expansionがある場合は、RuntimeのSignal PriorityとRe-Seal Ruleを優先する。

---

## 10. Activation Contract

```yaml
activation_contract:
  execute_plan_mode_only_when:
    - "pair_state is READY"
    - "Current Request is identifiable"
    - "Status permits intended use"

  initial_response_state:
    - "plan_compiled"
    - "armed_not_started"

  do_not:
    - "Do not use the rollback baseline silently."
    - "Do not reconstruct missing Candidate content from memory."
    - "Do not treat this Query as Plan Mode intelligence."
    - "Do not start Full Rail during the Plan response."
```

旧PairはHumanが選択できるRollback Routeであり、自動Fallbackではない。

---

## 11. Failure States

```yaml
failure_states:
  REPOSITORY_LOCATOR_MISSING:
    action: "Hard Stop"

  REF_MISSING:
    action: "Stop"

  PROTOCOL_UNREACHABLE:
    action: "Stop unless portable recovery conditions pass"

  QUERY_MISSING:
    action: "Hard Stop"

  RUNTIME_MISSING:
    action: "Hard Stop"

  PARTIAL_READ:
    action: "Hard Stop"

  EOF_SENTINEL_MISSING:
    action: "Classify as PARTIAL_READ and Stop"

  PROTOCOL_VERSION_CONFLICT:
    action: "Hard Stop"

  PAIR_MISMATCH:
    action: "Hard Stop"

  STATUS_NOT_ACTIVE:
    action: "Stop"

  CURRENT_REQUEST_UNRESOLVED:
    action: "Use one concise Ambiguity Pause"
```

Failure時は、不足項目・確認済み項目・最小Recovery Actionを明示する。

一般知識、Memory、過去会話でRuntime内容を代替しない。

---

## 12. Copy & Paste Surface

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ai-plan-mode/ai-plan-mode_query.md

上記Queryを最初から最後まで全文読み、
記載されたRuntimeを解決し、
Full-Read ProofとPair Consistency Gateを通過した場合のみ、
Current RequestへPlan Modeを実行してください。

この回答ではPlanだけを作成し、
Artifact本文、実装、File変更、GitHub Write、Commit、
Full Rail実行はまだ行わないでください。

Repository、Query、Runtime、EOF Sentinel、Pair整合を確認できない場合は、
不足状態を明示して停止し、
一般知識・過去会話・推測で代替しないでください。
```

---

## 13. Rollback Boundary

```yaml
rollback_boundary:
  active_baseline:
    query: "prompts/ai-plan-mode_query.md"
    runtime: "prompts/ai-plan-mode.md"
    version: "v003-candidate"

  candidate:
    query: "ai-plan-mode/ai-plan-mode_query.md"
    runtime: "ai-plan-mode/ai-plan-mode.md"
    version: "v004-candidate"

  rules:
    - "Do not edit the baseline during Candidate field testing."
    - "Do not silently fall back from Candidate to Baseline."
    - "Human may explicitly choose the Baseline Query."
    - "Candidate failure does not modify Baseline status."
```

---

document_end:
  filename: "ai-plan-mode_query.md"
  version: "v004-candidate"
  eof_sentinel: "EOF::AI_PLAN_MODE_QUERY::v004-candidate"

EOF::AI_PLAN_MODE_QUERY::v004-candidate
