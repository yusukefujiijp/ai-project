---
title: "AI Thread-End Query"
filename: "ai-thread-end_query.md"
canonical_path: "thread-end/ai-thread-end_query.md"
status: "active_candidate / topology-first field-test"
class: "prompt_query"
role: "AI Thread-End Binding + Activation Query"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
language_policy: "Japanese-first / English-anchor"
paired_runtime:
  path: "thread-end/ai-thread-end.md"
  role: "Single Thread-End Compiler / Multi-Representation Migration Runtime"
architecture:
  canonical_control_system:
    sets: 1
    files: 2
  per_thread_migration_output:
    persistent_markdown: 3
    inline_launch_surface: 1
legacy_boundary:
  folder: "_thread-end/"
  use_in_new_flow: false
  runtime_dependency: false
root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Query / Markdown / GitHub are Fruit and Keli, not Root."
---

# AI Thread-End Query

## 0. Purpose

このQueryは、`thread-end/ai-thread-end.md`を現在ThreadへBindingし、AI Thread-End Runtimeを起動する。

```text
Runtime governs.
Query binds and activates.
One shared state becomes three representations.
Human transports with one Copy & Paste launch.
Reality verifies.
Thread stops.
```

このQueryは旧`_thread-end/`Runtimeを呼び出さず、旧SystemをFallbackとして使用しない。

---

## 1. Binding Packet

実行時に以下をCurrent Realityから解決する。

```yaml
binding:
  RUNTIME_FILE: "thread-end/ai-thread-end.md"
  TARGET_SCOPE: "current_thread"

  SOURCE_THREAD:
    coordinate: "<Ark coordinate | required>"
    start_date: "<YYYY-MM-DD | unknown>"

  TARGET_THREAD:
    coordinate: "<Ark coordinate | required when migration>"
    start_date: "<YYYY-MM-DD | required when migration>"

  CURRENT_MISSION: "<extract_from_thread | human_provided>"
  THREAD_MIGRATION_REQUIRED: "yes / no"

  OUTPUT_PROFILE:
    name: "verified_3_plus_1"
    persistent_markdown: 3
    inline_launch_surface: 1

  OUTPUT_PATHS:
    handoff: "<AUTO_PROPOSE | exact path>"
    reboot_map: "<AUTO_PROPOSE | exact path>"
    start_query: "<AUTO_PROPOSE | exact path>"

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

### 1.1 Binding Guard

```yaml
binding_guard:
  - "SOURCE_THREADとTARGET_THREADを逆転させない"
  - "Human-confirmed coordinate and dateを優先する"
  - "不明値を推測だけでconfirmedへ昇格しない"
  - "Output Path collisionを確認する"
  - "Human content sealとExecute GitHub OKを分離する"
  - "旧_thread-end/をRuntime、Fallback、Dependencyとして使わない"
  - "Human local backupをAIが完了認証しない"
  - "Target Threadを現在Thread内で自動開始しない"
```

---

## 2. Runtime Gate

```yaml
runtime_gate:
  expected_path: "thread-end/ai-thread-end.md"

  if_missing:
    output: "AI THREAD-END RUNTIME MISSING"
    action:
      - "Stop"
      - "Do not substitute _thread-end runtime"
      - "Do not reconstruct the runtime from memory"

  if_path_conflict:
    output: "AI THREAD-END PATH CONFLICT"
    action:
      - "List visible conflicting canonical candidates"
      - "Stop before artifact generation"

  if_legacy_dependency_detected:
    output: "AI THREAD-END LEGACY DEPENDENCY DETECTED"
    action:
      - "Identify the exact dependency"
      - "Do not continue until removed or Human-reviewed"
```

---

## 3. Activation Command

```text
thread-end/ai-thread-end.mdをActive Runtimeとして全文読み、
このQueryのBinding Packetを現在Threadへ適用して下さい。

旧_thread-end/配下のRuntime、Query、Mini、Handoff Builderを
Active RuntimeまたはFallbackとして使用しないで下さい。

Current explicit Human request
→ Project Instructions
→ Current Thread Reality
→ AI Thread-End Query
→ AI Thread-End Runtime
の順に意味を解決して下さい。
```

---

## 4. Required Execution Rail

```text
Preflight Reality Lock
→ Current Thread Capture
→ Thread Migration Selection Review
→ Shared State Model Compile
→ Human-readable Handoff
→ AI-native Thread Reboot Map
→ AI-first Start Query
→ Cross-Representation Consistency Check
→ Inline Copy & Paste Launch Query
→ Static Validation
→ Human Review / Correction
→ Human Content Seal
→ GitHub Write only when separately authorized
→ Delivery
→ Instruction Tuning Gate
→ Next Gate
→ Stop
```

```yaml
execution_guard:
  - "三つのPersistent Markdownを別々のCurrent State解釈から作らない"
  - "一つのShared State Modelから三Representationを生成する"
  - "Reboot MapをHandoffの自然言語要約へ退化させない"
  - "Start QueryをHuman向け曖昧文へ退化させない"
  - "Inline Launchを第四の独立SSOTにしない"
  - "Current ThreadでCold-Start Boot Successを自己認証しない"
```

---

## 5. Output Contract — 3 Persistent + 1 Inline

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
      artifact: "Copy & Paste Next Thread Launch Query"
      role: "Human Transport Surface"
      source_of_truth: "AI-first Start Query"
```

### 5.1 Output Path Default

```yaml
output_path_default:
  folder: "thread-end/ark/"

  handoff:
    pattern: "arkNNMM_YYYYMMDD_handoff.md"

  reboot_map:
    pattern: "arkNNMM_to_arkNNMM_YYYYMMDD_reboot-map.md"

  start_query:
    pattern: "arkNNMM_YYYYMMDD_start-query.md"

  rule:
    - "Human-confirmed dates and coordinates govern"
    - "AUTO_PROPOSE is not Human Seal"
```

---

## 6. Required Reconstruction Contract

The Start Query and Reboot Map must require the Next Thread AI to reconstruct:

```yaml
required_reconstruction:
  - "Target Current Coordinate"
  - "Inherited Mission"
  - "Causal Spine"
  - "Major Human Corrections"
  - "Confirmed facts"
  - "Inferred candidates"
  - "Unknowns"
  - "Completed / Do-Not-Reopen"
  - "First Legal Move"
```

Stop if any material required field cannot be reconstructed.

---

## 7. Cross-Representation Gate

```yaml
cross_representation_gate:
  required:
    - "Source and target coordinates match across all outputs"
    - "Current Mission matches"
    - "First Legal Move matches"
    - "Unknowns are not promoted"
    - "Do-Not-Reopen items remain protected"
    - "Start Query paths point to actual artifact paths"
    - "Inline Launch has no unique semantic instruction"

  pass_status:
    - "STATIC_MATCH"
    - "STATIC_PARTIAL_MATCH"
    - "STATIC_MISMATCH"

  if_failed:
    - "Identify exact artifact and field"
    - "Apply Minimum Semantic Delta"
    - "Retest only the affected assertions and dependencies"
    - "Do not claim Migration Ready"
```

---

## 8. GitHub Authority Gate

```yaml
github_authority_gate:
  artifact_draft:
    execute_github_ok_required: false

  repository_write:
    requires:
      - "GITHUB_WRITE.requested = yes"
      - "GITHUB_WRITE.human_content_seal = confirmed"
      - "GITHUB_WRITE.execute_github_ok = confirmed"
      - "Exact repository / branch / path / scope"

  legacy_folder:
    backup_actor: "Human"
    delete_actor: "Human"
    ai_delete_authority: false
```

`Human Seal OK`だけを旧Folder削除権限へ拡張しない。

---

## 9. Topology-First Guard

```yaml
topology_first_guard:
  required_order:
    1: "Create thread-end/ canonical topology"
    2: "Verify Query–Runtime pair"
    3: "Run Ark Thread migration field test"
    4: "Human canonical seal"
    5: "Patch active references"
    6: "Human local backup"
    7: "Human legacy deletion"
    8: "Post-delete broken-reference sweep"

  reference_policy:
    active_route: "patch"
    canonical_documentation: "patch"
    historical_record: "preserve"
    obsolete_instruction: "remove or replace"
    uncertain: "Human review"
```

---

## 10. Standard Final Response

```yaml
standard_final_response:
  include:
    - "Direct Result"
    - "Created / Updated exact paths"
    - "Static Validation result"
    - "Cold-Start status"
    - "Legacy folder status"
    - "Instruction Tuning Gate"
    - "Copy & Paste Launch Query"
    - "Next Gate"

  launch_query_rule:
    - "Migration artifacts readyなら必ず回答内へ直接表示する"
    - "一つのCopyable Blockにする"
    - "Humanの追記を要求しない"
```

---

## 11. Stop Rule

```yaml
stop_after:
  - "Required outputs generated"
  - "Static validation completed"
  - "Human authority boundary recorded"
  - "Inline Copy & Paste Launch returned"
  - "Instruction Tuning Gate recorded"
  - "Next Gate written"

do_not_after_stop:
  - "Do not start the next Thread automatically"
  - "Do not claim Cold-Start success before Next Thread response"
  - "Do not delete _thread-end/"
  - "Do not expand into unrelated repository cleanup"
```

---

## 12. Short Activation Query

```text
thread-end/ai-thread-end_query.mdを読み、
paired Runtimeであるthread-end/ai-thread-end.mdをActive Runtimeとして
現在Threadへ適用して下さい。

一つのShared State Modelから、次の3+1を生成して下さい。

1. Human-readable Handoff
2. AI-native Thread Reboot Map
3. AI-first Start Query
+1. 回答内Copy & Paste Next Thread Launch Query

Cross-Representation Gateを実行し、
Current ThreadではStatic Validationまで行って下さい。
Cold-Start Boot SuccessはNext ThreadのReality Response前に確定しないで下さい。

旧_thread-end/系は使用せず、削除もしないで下さい。
GitHub WriteはHuman content sealとExecute GitHub OKが別々に確認された場合のみ実行して下さい。
Instruction Tuning Gate、Next Gateを書いた後に停止して下さい。
```

> **Query binds. Runtime compiles. Three representations cross-check. Human launches. Reality verifies.**
