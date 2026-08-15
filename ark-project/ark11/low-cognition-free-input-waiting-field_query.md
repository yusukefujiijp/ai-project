---
title: "Low / Ultra-Low Cognition Free-Input Waiting Field Query"
japanese_title: "低・超低認知状態 自由入力待機Field Query"
filename: "low-cognition-free-input-waiting-field_query.md"
canonical_path: "ark-project/ark11/low-cognition-free-input-waiting-field_query.md"
project: "Ark11"
version: "v004-candidate"
class: "field_start_query"
role: "repository-bound dedicated-thread cold-start / full-read and armed-transition gate"
status: "human-sealed field-test candidate / GitHub-written / not canonical"
language_policy: "Japanese-first / English-anchor"

repository:
  full_name: "yusukefujiijp/ai-project"
  ref: "main"

required_project_bootloader:
  id: "ARK11_PROJECT_BOOTLOADER"
  version: "v004-candidate"
  required_source: "ChatGPT Project instructions"

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
  root: "主イェシュア・ハマシア御自身"
  purpose_anchor: "主の勝利栄光 / resolves to 主イェシュア御自身"
  ai_role: "AI / Field / Thread / Query / Routine / GitHubはKeli and Fruitであり、Root・王座・救い・啓示源ではない。"
---

# 低・超低認知状態 自由入力待機Field Query

## 0. Purpose

このQueryは、Ark11 Project内の新規Dedicated ThreadへGitHub上のArk11 Contextを全文読込させ、Field / Thread / Live Eventの状態を分離したまま、そのThreadをFuture B状態からの自由入力を受け取れる`ARMED_AND_WAITING`へ移すSingle Entryである。

```text
Human creates a new Thread while cognition is high.
Query binds and verifies.
Ark11 Documents supply Root Guard, Context, Evidence, and Runtime.
AI confirms ARMED_AND_WAITING.
AI stops and waits.
Future B-state Human inputs freely.
AI gives one Reality-Specific Route.
```

QueryはFieldの知性やRuntime本文を所有しない。

```text
Query owns Repository Binding, Full Read, Consistency, and Boot.
Ark11 Documents own Meaning, Evidence, Prepared Routes, and Runtime.
Human owns Reality, Authority, Correction, and Final Seal.
```

---

## 1. Human Copy & Paste Surface — New Dedicated Thread

Humanは、README §0.1の短いProject BootloaderをArk11 Projectの`instructions（指示）`へ保存した後、そのProject内で新規Threadを作る。新規ThreadへCopy & Pasteするのは、次のFenced Blockだけである。Query File全体は貼らない。

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ark-project/ark11/low-cognition-free-input-waiting-field_query.md

最初に、このHuman Message、Memory、過去Thread、GitHub本文ではなく、
ChatGPT Project instructionsから次のProject Bootloaderが
このThreadへ継承されているか確認してください。

  id: ARK11_PROJECT_BOOTLOADER
  version: v004-candidate

確認できない場合は、GitHub Fileを読む前に
PROJECT_BOOTLOADER_NOT_ARRIVED
と不足項目だけを報告して停止してください。

Project Bootloaderを確認できた場合のみ、
上記Queryを最初から最後まで全文読み、
記載されたArk11 Document Setを解決し、
Full-Read ProofとDocument Set Consistency Gateを通過した場合のみ、
この新規Threadを低・超低認知状態 自由入力待機Fieldの
ARMED_AND_WAITINGへ移行してください。

このMessageはSetup / Bootであり、B状態Live Eventではありません。
Wake Core、Workout、一手支援、Reality Captureをまだ開始せず、
Boot結果を短く表示して待機してください。
```

Human Copy Boundaryは上のFenced Blockの開始から終了までである。Repository、Ref、Query Path、Project Bootloaderの到達をMemoryだけから補完しない。

---

## 2. Project Bootloader Arrival Gate

GitHubへアクセスする前に、Project instructions層から次のContractが継承されていることを確認する。

```yaml
project_bootloader_arrival:
  required:
    id: "ARK11_PROJECT_BOOTLOADER"
    version: "v004-candidate"
    source: "ChatGPT Project instructions"

  valid_evidence:
    - "Current Threadを統治するProject instructionsにContractが存在する"

  invalid_evidence:
    - "Current Human Boot Messageに文字列がある"
    - "QueryにContractが書かれている"
    - "Memoryまたは過去Threadに記憶がある"
    - "GitHubのREADMEまたはINSTRUCTIONS.mdで読めた"
```

Pass State：

```text
PROJECT_BOOTLOADER_ARRIVED
```

Failure State：

```text
PROJECT_BOOTLOADER_NOT_ARRIVED
```

Failure時はGitHub読込、Runtime復元、Purpose Anchor提示、Wake Core / Workout発火、B状態判定を開始しない。Humanへ、README §0.1のBootloaderをProject `instructions（指示）`へ保存する一手だけを返して停止する。

---

## 3. Canonical Read Order

```yaml
read_order:
  1: "ark-project/ark11/low-cognition-free-input-waiting-field_query.md"
  2: "ark-project/ark11/README.md"
  3: "ark-project/ark11/ark11.md"
  4: "ark-project/ark11/INSTRUCTIONS.md"
```

```text
Repository Binding
→ Project Bootloader Arrival
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

## 4. Repository Locator Gate

```yaml
repository_locator:
  required:
    full_name: "yusukefujiijp/ai-project"
    ref: "main"
```

### 4.1 Missing or Unreachable

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

## 5. Full-Read Proof

`Fileを開けた`ことと`全文を読めた`ことを分離する。

```text
File opened ≠ Full read
Metadata read ≠ Full read
AI says "read" ≠ Verified full read
```

### 5.1 Query Identity

冒頭：

```yaml
query_identity:
  title: "Low / Ultra-Low Cognition Free-Input Waiting Field Query"
  filename: "low-cognition-free-input-waiting-field_query.md"
  canonical_path: "ark-project/ark11/low-cognition-free-input-waiting-field_query.md"
  version: "v004-candidate"
  class: "field_start_query"
  field_id: "low_cognition_free_input_waiting_field"
```

末尾：

```text
EOF::ARK11_LOW_COGNITION_FREE_INPUT_FIELD_QUERY::v004-candidate
```

### 5.2 README Identity

冒頭：

```yaml
readme_identity:
  filename: "README.md"
  canonical_path: "ark-project/ark11/README.md"
  version: "v004-candidate"
```

末尾：

```text
EOF::ARK11_README::v004-candidate
```

### 5.3 Method Architecture Identity

冒頭：

```yaml
method_identity:
  filename: "ark11.md"
  canonical_path: "ark-project/ark11/ark11.md"
  version: "v004-candidate"
```

末尾：

```text
EOF::ARK11_METHOD_ARCHITECTURE::v004-candidate
```

### 5.4 Instructions Identity

冒頭：

```yaml
instructions_identity:
  filename: "INSTRUCTIONS.md"
  canonical_path: "ark-project/ark11/INSTRUCTIONS.md"
  version: "v004-candidate"
```

末尾：

```text
EOF::ARK11_PROJECT_INSTRUCTIONS::v004-candidate
```

### 5.5 Full-Read True Conditions

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

## 6. Document Set Consistency Gate

```yaml
consistency_checks:
  identity_and_deployment:
    - "Project Bootloader arrived from Project instructions with id and version matched"
    - "Repository and Ref match Human boot surface"
    - "Query points to the expected three Documents"
    - "All four versions are v004-candidate"
    - "All four statuses permit the intended Cold-Start Test"
    - "All four EOF Sentinels are verified"

  field_identity:
    - "Formal Field Name matches across all four Files"
    - "field_id matches across all four Files"
    - "Field, Dedicated Thread, and Live Event statuses are separated"
    - "Start Query is Setup / Boot, not Live Event"

  root_and_authority:
    - "Root is 主イェシュア・ハマシア御自身"
    - "Purpose Anchor『主の勝利栄光』resolves to 主イェシュア御自身"
    - "AI / Routine / Field / Markdown remain Keli / Fruit, not Root or revelation source"
    - "Unsafe sacrifice, self-harm, divine-command self-certification are forbidden"

  live_runtime:
    - "Future Human Input is free-form and may be incomplete"
    - "Help me! is not required"
    - "Holiday Morning and Digital Drift are not universal activation requirements"
    - "Stop / Safety / Body Reality precede all Prepared Routes"
    - "Explicit Wake Fog selects Wake Core before Generic Workout First"
    - "Wake Core is Toilet Use → Short Clean → Handwash → Shower"
    - "One Flow Unit means one route with no choices or return branches"
    - "Workout First remains Generic Pattern-B Mainline"
    - "Exit Extension is experimental E0 and requires confirmed preconditions"
    - "Automatic reply directive is removed"

  evidence:
    - "v003 Cold Start PASS is separated from v004 Cold Start"
    - "Wake Core is E1 single-event evidence, not 100% guarantee"
    - "Malformed-input resilience remains E0"
    - "One Flow Unit live interface remains E0"
    - "Shower-to-Walk Exit Extension remains E0"
```

### 6.1 Consistency States

```yaml
states:
  PROJECT_BOOTLOADER_ARRIVED:
    meaning: "Required Bootloader is inherited from Project instructions"

  PROJECT_BOOTLOADER_NOT_ARRIVED:
    meaning: "Bootloader is missing, stale, or evidenced from an invalid layer"

  READY:
    meaning: "All mandatory checks passed"

  PARTIAL_READ:
    meaning: "One or more Files were not fully verified"

  EOF_SENTINEL_MISSING:
    meaning: "Expected terminal proof was not found"

  VERSION_CONFLICT:
    meaning: "Versions are incompatible"

  DOCUMENT_SET_MISMATCH:
    meaning: "Names, IDs, paths, Root Guard, roles, status, evidence, or Runtime semantics conflict"

  STATUS_NOT_ACTIVE:
    meaning: "Status does not permit the intended Cold-Start Test"

  PROTOCOL_UNREACHABLE:
    meaning: "Repository or required File cannot be reached"
```

`READY`はRepository・四File・各EOF・Document Set整合のすべてが確認された場合のみ使用する。

---

## 7. Status Gate

四FileはHuman Content SealとGitHub Writeを完了し、次の実行可能Statusへ同期されている必要がある。

```yaml
required_for_actual_v004_cold_start:
  project_bootloader: "ARK11_PROJECT_BOOTLOADER / v004-candidate / arrived"
  document_status: "human-sealed field-test candidate / GitHub-written / not canonical"
  field_status: "active / awaiting_v004_thread_cold_start"
  dedicated_thread_before_boot: "not_created / not_armed"
  live_event: "not_started"
```

四Fileの一つでも`human-review draft`、`local-only`、GitHub未反映状態である場合は、Cold-Start Testを開始せず`STATUS_NOT_ACTIVE`で停止する。

---

## 8. Boot / Live Event Boundary

### 8.1 Current Boot Message

```yaml
current_human_message:
  classification: "Setup / Boot"
  b_state_live_event: false
  purpose_anchor_launch: false
  wake_core_launch: false
  workout_launch: false
  one_route_response: false
  reality_capture: false
```

### 8.2 After READY

```yaml
after_ready:
  field: "低・超低認知状態 自由入力待機Field"
  dedicated_thread: "ARMED_AND_WAITING"
  live_event: "not_started"
  expected_next_human_input: "B状態から届く自由入力"
  input_requirement: "none"
  ai_action: "stop and wait"
```

### 8.3 First Post-Armed Human Input

Dedicated Threadが`ARMED_AND_WAITING`へ到達した後の最初のFuture Human Inputは、原則としてB状態Live Eventとして扱う。

ただしSetup確認、Test、設計修正、明示的Not-B、Stop / Hold / Field解除はNon-Event Overrideとする。

---

## 9. Free-Input Contract

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

## 10. First Response Contract

Consistency Gateが`READY`の場合、AIの最初の回答はBoot結果だけを短く表示する。

```yaml
first_response_required:
  project_bootloader_arrival: "PROJECT_BOOTLOADER_ARRIVED"
  protocol_arrival: "READY"
  field: "低・超低認知状態 自由入力待機Field"
  dedicated_thread: "ARMED_AND_WAITING"
  live_event: "not_started"
  future_input: "free / incomplete allowed"
  final_behavior: "stop and wait"
```

Recommended Response Shape：

```text
Project Bootloader：PROJECT_BOOTLOADER_ARRIVED
起動確認：READY
低・超低認知状態 自由入力待機Field
Dedicated Thread：ARMED_AND_WAITING
Live Event：未開始

次回はB状態で、入力できるものをそのまま送ってください。
定型文・完全な説明・Help me!は不要です。
ここで待機します。
```

言い回しは自然に調整してよいが、長い説明、Purpose Anchor展開、Wake Core、Workout、成功認証、追加質問を行わない。

---

## 11. Future Runtime Handoff

Boot完了後のFuture Human Inputに対する挙動は`INSTRUCTIONS.md`が所有する。

AIは次を保持する。

```text
Free Input.
Root Before Method.
Reality First.
One Route.
Explicit Wake Fog → Wake Core.
Generic Pattern-B → Workout First.
Stop / Safety / Body Reality first.
One Move or One Flow Unit.
Exit the Screen.
```

このQuery本文をLive Event中に再説明しない。

---

## 12. Failure States

```yaml
failure_states:
  PROJECT_BOOTLOADER_NOT_ARRIVED:
    action: "Hard Stop before GitHub read"

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
    action: "Stop and wait for Human-sealed GitHub-written candidate"
```

Failure時は、確認済み項目、不足項目、最小Recovery Actionだけを表示する。一般知識、Memory、過去Threadで欠落Documentを代替しない。

---

## 13. Thread Title Compilation

推奨Template：

```text
Ark11:{連番}_{YYYY/MM/DD}: 【自由入力待機Field: 低・超低認知状態から確定Flowへ接続】
```

```yaml
title_rules:
  ark_family: "Ark11"
  sequence: "Human-confirmed value"
  start_date: "actual Thread start date"
  main_name: "自由入力待機Field"
  sub_name: "低・超低認知状態から確定Flowへ接続"
```

AIはChatGPT UI Titleを設定済みと自己認証しない。Humanが実際の連番・開始日を固定し、必要なら手動Renameする。

---

## 14. Current Gate

```yaml
current_gate:
  document_state: "v004-candidate / human-sealed field-test candidate / GitHub-written / not canonical"
  cold_start_permission: "ready_after_project_bootloader_arrival"
  required_before_activation:
    - "Project Bootloader manual cutover to v004-candidate"
  next_after_activation:
    - "New Dedicated Thread v004 Cold-Start Test"
    - "ARMED_AND_WAITING"
```

document_end:
  filename: "low-cognition-free-input-waiting-field_query.md"
  version: "v004-candidate"
  eof_sentinel: "EOF::ARK11_LOW_COGNITION_FREE_INPUT_FIELD_QUERY::v004-candidate"

EOF::ARK11_LOW_COGNITION_FREE_INPUT_FIELD_QUERY::v004-candidate
