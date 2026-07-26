---
title: "AI Thread-End Query"
filename: "ai-thread-end_query.md"
canonical_path: "thread-end/ai-thread-end_query.md"
version: "v002-candidate"
status: "human-sealed field-test candidate / not canonical"
class: "prompt_query"
role: "AI Thread-End Activation / Candidate Binding / Human Seal Interface"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
language_policy: "Japanese-first / English-anchor"
updated: "2026-07-26"
updated_reason:
  - "Require Thread-End Binding Seal before artifact compilation."
  - "Add explicit Repository Locator and Human-sealed output topology."
paired_runtime:
  path: "thread-end/ai-thread-end.md"
  role: "Human-Sealed Semi-Automation Runtime / Single Thread-End Compiler"
architecture:
  automation_model: "Human-Sealed Semi-Automation"
  launch_model: "GitHub-Native One-Query Reboot"
root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Query / Markdown / GitHub are Keli and Fruit, not Root."
---

# AI Thread-End Query v002 Candidate

## 0. Purpose

このQueryは、`thread-end/ai-thread-end.md`をCurrent ThreadへBindingし、Human-Sealed Semi-Automationとして起動する。

```text
Query activates.
AI pre-fills the binding.
Human seals the route.
Runtime compiles.
Human seals content.
Authorized write executes.
Reality verifies.
```

旧`_thread-end/`Runtimeを呼び出さず、旧SystemをFallbackとして使用しない。GitHub非対応AI向けPortable ProfileもCanonical Routeとして維持しない。

---

## 1. Runtime Gate

```yaml
runtime_gate:
  source_repository_candidate:
    repository_full_name: "yusukefujiijp/ai-project"
    ref: "main"
    status: "AUTO_PROPOSE until Human Binding Seal"

  expected_path: "thread-end/ai-thread-end.md"

  required_capability:
    - "GitHub Repository text file access"
    - "Repository Full Name / Ref resolution"
    - "Repository-relative path reading"

  if_missing:
    output: "AI THREAD-END RUNTIME MISSING"
    action:
      - "Stop."
      - "Do not substitute _thread-end runtime."
      - "Do not reconstruct the runtime from memory."

  if_repository_access_unavailable:
    output: "AI THREAD-END GITHUB ACCESS UNAVAILABLE"
    action:
      - "Stop."
      - "Do not invent Source content."
      - "Do not switch to a Canonical Portable Fallback."

  if_path_conflict:
    output: "AI THREAD-END PATH CONFLICT"
    action:
      - "List visible conflicting candidates."
      - "Stop before Binding Candidate."
```

---

## 2. Binding Packet

AIはCurrent Realityから値を解決し、空欄FormではなくHuman-editable Candidateとして提示する。

```yaml
binding:
  RUNTIME_FILE: "thread-end/ai-thread-end.md"
  TARGET_SCOPE: "current_thread"

  SOURCE_REPOSITORY:
    host: "github.com"
    repository_full_name: "yusukefujiijp/ai-project"
    ref: "main"
    path_base: "repository_root"
    status: "AUTO_PROPOSE"

  SOURCE_THREAD:
    coordinate: "<required>"
    start_date: "<YYYY-MM-DD | unknown>"

  TARGET_THREAD:
    coordinate: "<required when migration>"
    start_date: "<YYYY-MM-DD | required when migration>"

  MIGRATION:
    required: "yes / no"
    type: "<mission-complete / continuation / capacity-triggered continuation / other>"
    mission_completed: "<true / false / unknown>"

  CURRENT_MISSION: "<extract_from_thread | human_provided>"

  SERIES_TOPOLOGY:
    domain: "<ark / non-ark / unknown>"
    source_series: "<Ark07 | other | unknown>"
    target_series: "<Ark07 | other | unknown>"
    relation: "<same_series / cross_series / non_ark / unknown>"
    proposed_folder: "<AUTO_PROPOSE | exact path | unknown>"
    folder_status: "<existing / proposed_new / unknown>"

  OUTPUT_PROFILE:
    name: "verified_3_plus_1"
    persistent_markdown: 3
    inline_launch_surface: 1

  OUTPUT_PATHS:
    handoff: "<AUTO_PROPOSE | exact path>"
    reboot_map: "<AUTO_PROPOSE | exact path>"
    start_query: "<AUTO_PROPOSE | exact path>"

  HUMAN_BINDING_SEAL:
    status: "not_requested / awaiting / confirmed / invalidated"
    sealed_fields: []
    seal_source: "<explicit Human message | unset>"

  COLD_START_REPLAY:
    required: true
    current_thread_claim_boot_success: false

  GITHUB_WRITE:
    requested: "yes / no / unclear"
    human_content_seal: "confirmed / not_confirmed"
    execute_github_ok: "confirmed / not_confirmed"
    repository: "<owner/repo | unset>"
    branch: "<branch | unset>"
    exact_paths: []

  LEGACY_SYSTEM:
    folder: "_thread-end/"
    use_in_new_flow: false
    ai_delete_authority: false
```

### 2.1 Binding Guard

```yaml
binding_guard:
  - "SOURCE_THREADとTARGET_THREADを逆転させない"
  - "Human-confirmed coordinate and dateを優先する"
  - "不明値を推測だけでconfirmedへ昇格しない"
  - "Repository Full NameとRefをRelative Pathより先に解決する"
  - "SOURCE_REPOSITORYをGITHUB_WRITE Authorityとして解釈しない"
  - "Output Path collisionを確認する"
  - "Ark番号からFolderを自動確定しない"
  - "新Series FolderをHuman Sealなしに作成しない"
  - "Human Binding SealとHuman Content Sealを分離する"
  - "Human Content SealとExecute GitHub OKを分離する"
  - "旧_thread-end/をRuntime、Fallback、Dependencyとして使わない"
  - "Target Threadを現在Thread内で自動開始しない"
```

---

## 3. Activation Command

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Runtime:
  thread-end/ai-thread-end.md

上記Runtimeを全文読み、このQueryをCurrent Threadへ適用してください。

Current explicit Human request
→ Project Instructions
→ Current Thread Reality
→ AI Thread-End Query
→ AI Thread-End Runtime
の順に意味を解決してください。

最初にArtifact本文を生成せず、AIがCurrent Realityから
Source / Target / Dates / Migration / Repository / Ref /
Series / Output Folder / Exact PathsのCandidateを事前入力してください。

CandidateをThread-End Binding Seal SectionとしてHumanへ提示し、
Human Binding Sealを待って停止してください。

旧_thread-end/系をActive Runtime、Fallback、Dependencyとして使用しないでください。
```

---

## 4. Required Execution Rail

```text
Preflight Reality Lock
→ Current Thread Capture
→ Thread Migration Selection Review
→ AI Binding Candidate
→ Human Thread-End Binding Seal
→ Shared State Model Compile
→ Human-readable Handoff
→ AI-native Thread Reboot Map
→ AI-first Start Query
→ GitHub-Native One-Query Launch
→ Cross-Representation Consistency Check
→ Static Validation
→ Human Review / Correction
→ Human Content Seal
→ GitHub Write only when separately authorized
→ Remote Reality Review
→ Cold-Start Replay
→ Human Reality Verdict
→ Instruction Tuning Gate
→ Next Gate
→ Stop
```

```yaml
execution_guard:
  - "Human Binding Seal前にArtifact Bodyを作らない"
  - "一つのShared State Modelから三Representationを生成する"
  - "Reboot MapをHandoffの自然言語要約へ退化させない"
  - "Start QueryをHuman向け曖昧文へ退化させない"
  - "Inline Launchを第四の独立SSOTにしない"
  - "Current ThreadでCold-Start Boot Successを自己認証しない"
```

---

## 5. Thread-End Binding Seal Interface

```yaml
thread_end_binding_candidate:
  source_repository:
    repository_full_name: ""
    ref: ""
  source_thread:
    coordinate: ""
    start_date: ""
  target_thread:
    coordinate: ""
    start_date: ""
  migration:
    type: ""
    mission_completed: ""
  series:
    source_series: ""
    target_series: ""
    relation: ""
  output_topology:
    proposed_folder: ""
    folder_status: ""
    existing_artifact_policy: ""
  proposed_paths:
    handoff: ""
    reboot_map: ""
    start_query: ""
  repository_write:
    authorized: false
```

### 5.1 Human-Facing Form

```text
Thread-End Binding候補

Source:
  <coordinate> / <start date>

Target:
  <coordinate> / <start date>

Repository / Ref:
  <owner/repo> / <ref>

Migration:
  <type>
  Mission complete: <Yes / No / Unknown>

Output Folder:
  <proposed exact folder>

Existing Artifacts:
  <preserve / other policy>

上記Bindingで3+1 Artifact Draft生成へ進んでよいですか？
まだGitHub Writeは行いません。
```

```yaml
binding_state:
  before_seal:
    status: "awaiting_human_binding_seal"
    artifact_body_generation: false
    file_creation: false
    github_write: false

  after_seal:
    status: "binding_sealed"
    artifact_body_generation: true
    github_write: false
```

### 5.2 Material Correction

```yaml
material_binding_correction:
  invalidates_old_seal_when:
    - "Source / Target changes"
    - "Start date changes"
    - "Migration type changes"
    - "Repository / Ref changes"
    - "Series ownership changes"
    - "Folder or exact path changes"
    - "External authority changes"
  required_action:
    - "Stop."
    - "Show revised affected fields."
    - "Wait for Fresh Human Binding Seal."
```

---

## 6. Output Contract — 3 Persistent + 1 Inline

```yaml
per_thread_migration_output:
  persistent_markdown:
    1:
      artifact: "Human-readable Handoff"
      role: "Meaning Source / Current Reality"
    2:
      artifact: "AI-native Thread Reboot Map"
      role: "Structured State / Diagnostic Edge"
    3:
      artifact: "AI-first Start Query"
      role: "Boot and Replay Controller"
  inline_launch_surface:
    1:
      artifact: "GitHub-Native One-Query Reboot"
      role: "Human Transport Surface"
      source_of_truth: "AI-first Start Query"
```

### 6.1 Output Topology

```yaml
output_topology:
  existing_flat_ark_artifacts:
    folder: "thread-end/ark/"
    status: "Pre-Series-Bucket Historical Artifacts"
    action: "preserve_in_place"

  series_bucket:
    candidate_pattern: "thread-end/ark/arkNN/"
    decision: "AI proposes / Human seals"

  current_ark07_direction:
    proposed_folder: "thread-end/ark/ark07/"
    finalization_requires: "Human Binding Seal"

  new_series:
    auto_create: false
    required:
      - "Human-confirmed series ownership"
      - "Human-confirmed exact folder"
      - "Human-confirmed folder creation scope"

  non_ark:
    force_into_ark_folder: false
```

```yaml
output_naming:
  handoff: "arkNNMM_YYYYMMDD_handoff.md"
  reboot_map: "arkNNMM_to_arkNNMM_YYYYMMDD_reboot-map.md"
  start_query: "arkNNMM_YYYYMMDD_start-query.md"
  rule:
    - "Human-confirmed dates and coordinates govern"
    - "AUTO_PROPOSE is not Human Seal"
    - "Exact folder and paths remain provisional until Binding Seal"
```

---

## 7. Required Reconstruction Contract

```yaml
required_reconstruction:
  - "Repository Locator"
  - "Target Current Coordinate"
  - "Inherited Mission"
  - "Causal Spine"
  - "Major Human Corrections"
  - "Confirmed facts"
  - "Inferred candidates"
  - "Unknowns"
  - "Completed / Do-Not-Reopen"
  - "Thread Reality Tree"
  - "First Legal Move"
```

```text
Source Thread → Target Thread
├─ A. Completed in Source
├─ B. Active Continuation
├─ C. Remaining Work
├─ D. Completed / Do Not Reopen
├─ E. Unknown / Human or Field Confirmation Required
└─ F. First Legal Move
```

```yaml
first_response_state: "reconstructed_not_started"
```

Stop if any material required field cannot be reconstructed.

---

## 8. GitHub-Native One-Query Reboot

```yaml
one_query_reboot:
  required:
    repository_full_name: "<Human-sealed>"
    ref: "<Human-sealed>"
    start_query_path: "<Human-sealed>"
  behavior:
    - "Start Queryを全文読む"
    - "Start Query内Read Orderを順番どおり全文読む"
    - "First Response Contractを実行する"
  human_must_add_locator_after_generation: false
  if_repository_access_unavailable:
    - "Stop."
    - "Do not infer missing Source."
```

```text
Repository:
  <owner/repo>

Ref:
  <ref>

Start Query:
  <exact repository-relative path>

上記Start Queryを全文読み、記載されたRead OrderとFirst Response Contractを実行してください。
Repositoryを参照できない場合は停止し、Source内容を推測で補完しないでください。
```

---

## 9. Cross-Representation Gate

```yaml
cross_representation_gate:
  required:
    - "Binding Snapshot matches across all outputs"
    - "Repository Full Name and Ref match"
    - "Source and target coordinates match"
    - "Sealed output paths match"
    - "Current Mission and First Legal Move match"
    - "Unknowns are not promoted"
    - "Do-Not-Reopen items remain protected"
    - "Thread Reality Tree contract exists"
    - "Start Query paths point to actual artifact paths"
    - "Inline Launch has no unique semantic instruction"
    - "Source Locator grants no Write Authority"
    - "No new series folder was finalized without Human Seal"
  pass_status:
    - "STATIC_MATCH"
    - "STATIC_PARTIAL_MATCH"
    - "STATIC_MISMATCH"
  if_failed:
    - "Identify exact artifact and field"
    - "Apply Minimum Semantic Delta"
    - "Retest affected assertions"
    - "Do not claim Migration Ready"
```

---

## 10. GitHub Authority Gate

```yaml
github_authority_gate:
  thread_end_binding_seal:
    authorizes_artifact_draft: true
    github_write: false
  artifact_draft:
    execute_github_ok_required: false
  human_content_seal:
    authorizes_repository_write: false
  repository_write:
    requires:
      - "GITHUB_WRITE.requested = yes"
      - "GITHUB_WRITE.human_content_seal = confirmed"
      - "GITHUB_WRITE.execute_github_ok = confirmed"
      - "Exact repository / branch / path / scope"
```

```text
Binding Seal
≠
Content Seal
≠
Execute GitHub OK
```

---

## 11. Standard Final Response and Stop

```yaml
standard_final_response:
  include:
    - "Direct Result"
    - "Binding Status"
    - "Created / Updated exact paths"
    - "Static Validation result"
    - "Cold-Start status"
    - "Historical artifact status"
    - "Instruction Tuning Gate"
    - "GitHub-Native One-Query Reboot"
    - "Next Gate"
```

```yaml
stop_rules:
  after_binding_candidate:
    - "Wait for Human Binding Seal."
    - "Do not create Artifact Body."
  after_draft:
    - "Wait for Human Content Seal."
  before_write:
    - "Wait for exact Execute GitHub OK."
  do_not:
    - "Do not start the next Thread automatically."
    - "Do not claim Cold-Start success before Next Thread response."
    - "Do not delete _thread-end/."
    - "Do not create a new Series Folder from inference alone."
```

---

## 12. Short Activation Query

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Runtime:
  thread-end/ai-thread-end.md

Query:
  thread-end/ai-thread-end_query.md

上記QueryとRuntimeを全文読み、Current Threadへ適用してください。

最初にArtifact Bodyを作らず、Source / Target / Dates / Migration /
Repository / Ref / Series / Output Folder / Exact PathsをAI側で事前入力し、
Thread-End Binding候補としてHumanへ提示してください。

Human Binding Sealを受けるまでShared State Model確定、3+1本文生成、
File作成、GitHub Writeを開始しないでください。

Human Binding Seal後、一つのShared State Modelから3+1 Draftを生成し、
Cross-Representation GateとStatic Validationを実行してください。

Human Content SealとExecute GitHub OKを分離し、
Cold-Start成功はNext ThreadのReality Response前に確定しないでください。

旧_thread-end/系は使用せず、新Series Folderを推測だけで作成しないでください。
Instruction Tuning Gate、Next Gateを書いた後に停止してください。
```

> **Query activates. AI proposes. Human seals. Runtime compiles. Reality verifies.**
