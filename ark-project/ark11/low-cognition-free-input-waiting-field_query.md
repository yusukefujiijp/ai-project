---
title: "Low / Ultra-Low Cognition Free-Input Waiting Field Query"
japanese_title: "低・超低認知状態 自由入力待機Field Query"
filename: "low-cognition-free-input-waiting-field_query.md"
canonical_path: "ark-project/ark11/low-cognition-free-input-waiting-field_query.md"
project: "Ark11"
version: "v002-candidate"
class: "field_start_query"
role: "repository-bound dedicated-thread cold-start / full-read and armed-transition gate"
status: "human-sealed field-test candidate / GitHub-written / not canonical"
language_policy: "Japanese-first / English-anchor"

repository:
  full_name: "yusukefujiijp/ai-project"
  ref: "main"

field:
  formal_name: "低・超低認知状態 自由入力待機Field"
  english_anchor: "Low / Ultra-Low Cognition Free-Input Waiting Field"
  field_id: "low_cognition_free_input_waiting_field"
  deprecated_alias: "Field 2"

required_documents:
  - "ark-project/ark11/README.md"
  - "ark-project/ark11/ark11.md"
  - "ark-project/ark11/INSTRUCTIONS.md"

root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Field / Thread / Query / GitHubはKeli and Fruitであり、Rootではない。"
---

# 低・超低認知状態 自由入力待機Field Query

## 0. Purpose

このQueryは、Ark11 Project内の新規Dedicated ThreadへGitHub上のArk11 Contextを全文読込させ、Field / Thread / Live Eventの状態を分離したまま、そのThreadをFuture B状態からの自由入力を受け取れる`ARMED_AND_WAITING`へ移すSingle Entryである。

```text
Human creates a new Thread while cognition is high.
Query binds and verifies.
Ark11 Documents supply Context and Runtime.
AI confirms ARMED_AND_WAITING.
AI stops and waits.
Future B-state Human inputs freely.
AI gives one move.
```

QueryはFieldの知性やRuntime本文を所有しない。

```text
Query owns Repository Binding, Full Read, Consistency, and Boot.
Ark11 Documents own Meaning, Evidence, and Runtime.
Human owns Reality, Authority, Correction, and Final Seal.
```

---

## 1. Required Human Boot Surface

HumanはArk11 Project内で新規Threadを作り、次を入力する。

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ark-project/ark11/low-cognition-free-input-waiting-field_query.md

上記Queryを最初から最後まで全文読み、
記載されたArk11 Document Setを解決し、
Full-Read ProofとDocument Set Consistency Gateを通過した場合のみ、
この新規Threadを低・超低認知状態 自由入力待機Fieldの
ARMED_AND_WAITINGへ移行してください。

このMessageはSetup / Bootであり、B状態Live Eventではありません。
Workout、一手支援、Reality Captureをまだ開始せず、
Boot結果を短く表示して待機してください。
```

Repository、Ref、Query PathをMemoryだけから補完しない。

---

## 2. Canonical Read Order

```yaml
read_order:
  1: "ark-project/ark11/low-cognition-free-input-waiting-field_query.md"
  2: "ark-project/ark11/README.md"
  3: "ark-project/ark11/ark11.md"
  4: "ark-project/ark11/INSTRUCTIONS.md"
```

```text
Repository Binding
→ Query Full Read
→ README Full Read
→ Method Architecture Full Read
→ Instructions Full Read
→ Document Set Consistency
→ Boot / Live Boundary Check
→ ARMED_AND_WAITING
→ Stop and Wait
```

---

## 3. Repository Locator Gate

```yaml
repository_locator:
  required:
    full_name: "yusukefujiijp/ai-project"
    ref: "main"
```

### 3.1 Missing or Unreachable

```yaml
failure:
  REPOSITORY_LOCATOR_MISSING:
    action: "Stop. Do not infer from memory."

  REF_MISSING:
    action: "Stop. Do not silently use default branch."

  PROTOCOL_UNREACHABLE:
    action: "Stop. Do not reconstruct Ark11 Runtime from memory."
```

Portable Recoveryは、HumanがQueryと三Documentの完全な本文を供給し、Beginning Identityと各EOF Sentinelが確認できる場合だけ許可する。

---

## 4. Full-Read Proof

`Fileを開けた`ことと`全文を読めた`ことを分離する。

```text
File opened ≠ Full read
Metadata read ≠ Full read
AI says "read" ≠ Verified full read
```

### 4.1 Query Identity

冒頭：

```yaml
query_identity:
  title: "Low / Ultra-Low Cognition Free-Input Waiting Field Query"
  filename: "low-cognition-free-input-waiting-field_query.md"
  canonical_path: "ark-project/ark11/low-cognition-free-input-waiting-field_query.md"
  version: "v002-candidate"
  class: "field_start_query"
  field_id: "low_cognition_free_input_waiting_field"
```

末尾：

```text
EOF::ARK11_LOW_COGNITION_FREE_INPUT_FIELD_QUERY::v002-candidate
```

### 4.2 README Identity

冒頭：

```yaml
readme_identity:
  filename: "README.md"
  canonical_path: "ark-project/ark11/README.md"
  version: "v002-candidate"
```

末尾：

```text
EOF::ARK11_README::v002-candidate
```

### 4.3 Method Architecture Identity

冒頭：

```yaml
method_identity:
  filename: "ark11.md"
  canonical_path: "ark-project/ark11/ark11.md"
  version: "v002-candidate"
```

末尾：

```text
EOF::ARK11_METHOD_ARCHITECTURE::v002-candidate
```

### 4.4 Instructions Identity

冒頭：

```yaml
instructions_identity:
  filename: "INSTRUCTIONS.md"
  canonical_path: "ark-project/ark11/INSTRUCTIONS.md"
  version: "v002-candidate"
```

末尾：

```text
EOF::ARK11_PROJECT_INSTRUCTIONS::v002-candidate
```

### 4.5 Full-Read True Conditions

```yaml
full_read_true_only_if:
  - "Beginning identity was found for every File"
  - "Expected filename and canonical path matched"
  - "Expected version matched"
  - "File-specific EOF Sentinel was found"
  - "No truncation remained unresolved"
```

途中で取得が切れた場合は、次の未読Lineから読み進める。全EOF Sentinelを確認できない限り`full_read: true`としない。

---

## 5. Document Set Consistency Gate

```yaml
consistency_checks:
  - "Repository and Ref match Human boot surface"
  - "Query points to the expected three Documents"
  - "All four versions are v002-candidate"
  - "All four statuses permit the intended Cold-Start Test"
  - "Formal Field Name matches across all four Files"
  - "field_id matches across all four Files"
  - "Field, Dedicated Thread, and Live Event statuses are separated"
  - "Start Query is classified as Setup / Boot, not Live Event"
  - "Future Human Input is free-form and may be incomplete"
  - "Help me! is not required"
  - "Holiday Morning and Digital Drift are not universal activation requirements"
  - "Workout First is Prepared Mainline, subordinate to Stop / Safety / Body Reality"
  - "All four EOF Sentinels are verified"
```

### 5.1 Consistency States

```yaml
states:
  READY:
    meaning: "All mandatory checks passed"

  PARTIAL_READ:
    meaning: "One or more Files were not fully verified"

  EOF_SENTINEL_MISSING:
    meaning: "Expected terminal proof was not found"

  VERSION_CONFLICT:
    meaning: "Versions are incompatible"

  DOCUMENT_SET_MISMATCH:
    meaning: "Names, IDs, paths, roles, or Runtime semantics conflict"

  STATUS_NOT_ACTIVE:
    meaning: "Status does not permit the intended Cold-Start Test"

  PROTOCOL_UNREACHABLE:
    meaning: "Repository or required File cannot be reached"
```

`READY`はRepository・四File・各EOF・Document Set整合のすべてが確認された場合のみ使用する。

---

## 6. Status Gate

四FileはHuman Content SealとGitHub Writeを完了し、次の実行可能Statusへ同期されている必要がある。

```yaml
required_for_actual_cold_start:
  document_status: "human-sealed field-test candidate / GitHub-written / not canonical"
  field_status: "active / awaiting_thread_cold_start"
  dedicated_thread_before_boot: "not_created / not_armed"
  live_event: "not_started"
```

四Fileの一つでも`human-review draft`またはGitHub未反映状態である場合は、Cold-Start Testを開始せず`STATUS_NOT_ACTIVE`で停止する。

---

## 7. Boot / Live Event Boundary

### 7.1 Current Message

```yaml
current_human_message:
  classification: "Setup / Boot"
  b_state_live_event: false
  workout_launch: false
  one_move_response: false
  reality_capture: false
```

### 7.2 After READY

```yaml
after_ready:
  field: "低・超低認知状態 自由入力待機Field"
  dedicated_thread: "ARMED_AND_WAITING"
  live_event: "not_started"
  expected_next_human_input: "B状態から届く自由入力"
  input_requirement: "none"
  ai_action: "stop and wait"
```

### 7.3 First Post-Armed Human Input

Dedicated Threadが`ARMED_AND_WAITING`へ到達した後の最初のFuture Human Inputは、原則としてB状態Live Eventとして扱う。

ただし、Setup確認、Test、設計修正、明示的Not-B、Stop / Hold / Field解除はNon-Event Overrideとする。

---

## 8. Free-Input Contract

Future Humanは何を入力するか事前に確定しない。入力品質も要求しない。

```yaml
future_input:
  wording: "free"
  length: "free"
  grammar: "not required"
  complete_context: "not required"
  help_phrase: "not required"
  b_state_label: "not required"
  cause_explanation: "not required"
  digital_drift_mention: "not required"
```

不完全、断片的、誤変換的、非定型な入力をField Failureとして退けない。

---

## 9. First Response Contract

Consistency Gateが`READY`の場合、AIの最初の回答はBoot結果だけを短く表示する。

```yaml
first_response_required:
  protocol_arrival: "READY"
  field: "低・超低認知状態 自由入力待機Field"
  dedicated_thread: "ARMED_AND_WAITING"
  live_event: "not_started"
  future_input: "free / incomplete allowed"
  final_behavior: "stop and wait"
```

Recommended Response Shape：

```text
起動確認：READY
低・超低認知状態 自由入力待機Field
Dedicated Thread：ARMED_AND_WAITING
Live Event：未開始

次回はB状態で、入力できるものをそのまま送ってください。
定型文・完全な説明・Help me!は不要です。
ここで待機します。
```

言い回しは自然に調整してよいが、長い説明、複数選択肢、Workout発火、成功認証、追加質問を行わない。

---

## 10. Future Runtime Handoff

Boot完了後のFuture Human Inputに対する挙動は`INSTRUCTIONS.md`が所有する。

AIは次を保持する。

```text
Free Input.
One Move.
Reality First.
Workout First Mainline.
Stop / Safety / Body Reality first.
Exit the Screen.
```

このQuery本文をLive Event中に再説明しない。

---

## 11. Failure States

```yaml
failure_states:
  REPOSITORY_LOCATOR_MISSING:
    action: "Hard Stop"

  REF_MISSING:
    action: "Stop"

  QUERY_MISSING:
    action: "Hard Stop"

  REQUIRED_DOCUMENT_MISSING:
    action: "Hard Stop"

  PROTOCOL_UNREACHABLE:
    action: "Stop unless portable recovery passes"

  PARTIAL_READ:
    action: "Hard Stop"

  EOF_SENTINEL_MISSING:
    action: "Classify as PARTIAL_READ and Stop"

  VERSION_CONFLICT:
    action: "Hard Stop"

  DOCUMENT_SET_MISMATCH:
    action: "Hard Stop"

  STATUS_NOT_ACTIVE:
    action: "Stop and wait for Human-sealed candidate"
```

Failure時は、確認済み項目、不足項目、最小Recovery Actionだけを表示する。一般知識、Memory、過去Threadで欠落Documentを代替しない。

---

## 12. Thread Title Compilation

推奨Template：

```text
Ark11:{連番}_{YYYY/MM/DD}: 【自由入力待機Field: 低・超低認知状態から一手へ接続】
```

```yaml
title_rules:
  ark_family: "Ark11"
  sequence: "Human-confirmed value"
  start_date: "actual Thread start date"
  main_name: "自由入力待機Field"
  sub_name: "低・超低認知状態から一手へ接続"
```

AIはChatGPT UI Titleを設定済みと自己認証しない。Humanが実際の連番・開始日を固定し、必要なら手動Renameする。

---

## 13. Copy & Paste Surface

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ark-project/ark11/low-cognition-free-input-waiting-field_query.md

上記Queryを最初から最後まで全文読み、
記載されたArk11 Document Setを解決し、
Full-Read ProofとDocument Set Consistency Gateを通過した場合のみ、
この新規Threadを低・超低認知状態 自由入力待機Fieldの
ARMED_AND_WAITINGへ移行してください。

このMessageはSetup / Bootであり、B状態Live Eventではありません。
Workout、一手支援、Reality Captureをまだ開始せず、
Boot結果を短く表示して待機してください。

Repository、Query、Required Documents、各EOF Sentinel、
Version、Status、Field ID、Boot / Live境界を確認できない場合は、
不足状態を明示して停止し、一般知識・過去会話・推測で代替しないでください。
```

---

## 14. Current Gate

```yaml
current_gate:
  document_state: "v002-candidate / human-sealed field-test candidate / GitHub-written"
  cold_start: "ready_for_test"
  next:
    - "Dedicated Thread Cold-Start Test"
```

document_end:
  filename: "low-cognition-free-input-waiting-field_query.md"
  version: "v002-candidate"
  eof_sentinel: "EOF::ARK11_LOW_COGNITION_FREE_INPUT_FIELD_QUERY::v002-candidate"

EOF::ARK11_LOW_COGNITION_FREE_INPUT_FIELD_QUERY::v002-candidate
