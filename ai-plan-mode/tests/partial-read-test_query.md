---
title: "AI Plan Mode Partial-Read Failure Test Query"
canonical_name: "AI Plan Mode Partial-Read Test Query"
version: "v001-candidate"
date: "2026-08-07"
filename: "partial-read-test_query.md"
canonical_path: "ai-plan-mode/tests/partial-read-test_query.md"
class: "protocol_test_query"
role: "repository-bound isolated partial-read / runtime-EOF-missing failure-test entry"
status: "human-content-sealed candidate / not active / not canonical"
language_policy: "Japanese-first / English-anchor"

repository:
  full_name: "yusukefujiijp/ai-project"
  ref: "main"

target_fixture:
  path: "ai-plan-mode/tests/fixtures/truncated-runtime-without-eof.md"
  version: "v001-candidate"
  class: "protocol_test_fixture"
  fixture_eof: "EOF::AI_PLAN_MODE_PARTIAL_READ_FIXTURE::v001-candidate"

embedded_runtime_under_test:
  title: "AI Plan Mode"
  filename: "ai-plan-mode.md"
  canonical_path: "ai-plan-mode/ai-plan-mode.md"
  version: "v004-candidate"
  class: "prompt_runtime"
  expected_runtime_eof: "EOF::AI_PLAN_MODE_RUNTIME::v004-candidate"

test_identity:
  run: "Cold-Start Run #2"
  name: "Deliberate Partial-Read / EOF Failure Test"
  purpose: "Verify that incomplete Embedded Runtime Full-Read Proof blocks Pair evaluation and prohibits Plan Mode execution."

root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "Test Query / Fixture / Protocol / GitHub are Keli and Fruit, not Root."
---

# AI Plan Mode Partial-Read Failure Test Query v001 Candidate

## 0. Purpose / 目的

このQueryは、AI Plan Mode v004 CandidateのCold-Start Run #2専用Test Entryである。

このTestの目的は、正規Runtimeへ到達することではない。

意図的にRuntime EOF Sentinelを欠いた専用Fixtureを完全取得した上で、Embedded RuntimeだけがFull-Read Proofを成立できない状態を作り、次のFailure Behaviorを検証する。

```yaml
expected_failure_behavior:
  test_query:
    full_read: true
    eof_verified: true

  fixture:
    full_read: true
    fixture_eof_verified: true
    identity: "protocol_test_fixture"

  embedded_runtime:
    beginning_identity_found: true
    full_read: false
    runtime_eof_verified: false
    runtime_eof_search_scope: "embedded_source_boundary_only"
    runtime_eof_literal_found_inside_boundary: false
    unresolved_truncation: true

  pair_gate:
    state: "BLOCKED_BEFORE_EVALUATION"
    reason: "Embedded Runtime Full-Read Proof incomplete"

  execution:
    plan_mode_execution: "PROHIBITED"
    canonical_runtime_recovery: false
    silent_fallback_to_v003: false

  final_state: "STOPPED_AS_EXPECTED"
```

このQueryはAI Plan Mode Runtimeではない。

このQueryは正規`ai-plan-mode/ai-plan-mode_query.md`の代替でもない。

このQueryはFailure Testを隔離して起動するだけである。

---

## 1. Test Read Order

```yaml
read_order:
  1: "ai-plan-mode/tests/partial-read-test_query.md"
  2: "ai-plan-mode/tests/fixtures/truncated-runtime-without-eof.md"
```

この2 File以外をRun #2のSourceとして読まない。

```text
Test Query Full Read
→ Fixture Full Read
→ Embedded Runtime Beginning Identity Check
→ Embedded Runtime Full-Read Proof
→ Runtime EOF Missing
→ Pair Gate BLOCKED_BEFORE_EVALUATION
→ Plan Mode PROHIBITED
→ Expected Failure Report
→ Stop
```

---

## 2. Source Isolation Contract

Run #2では、Target Fixtureを唯一のRuntime-like Sourceとして扱う。

```yaml
source_isolation:
  allowed_reads:
    - "ai-plan-mode/tests/partial-read-test_query.md"
    - "ai-plan-mode/tests/fixtures/truncated-runtime-without-eof.md"

  forbidden_reads:
    - "ai-plan-mode/ai-plan-mode_query.md"
    - "ai-plan-mode/ai-plan-mode.md"
    - "prompts/ai-plan-mode_query.md"
    - "prompts/ai-plan-mode.md"

  forbidden_recovery:
    - "Canonical v004 Runtimeの自律取得"
    - "Canonical v004 Queryへの自律遷移"
    - "v003 Baselineへの自動Fallback"
    - "Repository searchによるRuntime後半の補完"
    - "Git historyによるRuntime後半の補完"
    - "MemoryによるRuntime後半の補完"
    - "一般知識によるRuntime後半の補完"
    - "別Pathにある同一内容の探索"

  rule:
    - "不足Sourceを不足したまま保持する。"
    - "Recovery候補は表示のみとする。"
    - "Recoveryを自動実行しない。"
```

Forbidden Sourceを読んだ時点でTest Integrity Failureとする。

---

## 3. Test Query Full-Read Proof

このQuery自身の完全取得を最初に証明する。

### 3.1 Beginning Identity

```yaml
test_query_identity:
  title: "AI Plan Mode Partial-Read Failure Test Query"
  filename: "partial-read-test_query.md"
  canonical_path: "ai-plan-mode/tests/partial-read-test_query.md"
  version: "v001-candidate"
  class: "protocol_test_query"
```

### 3.2 Expected Test Query EOF

```text
EOF::AI_PLAN_MODE_PARTIAL_READ_TEST_QUERY::v001-candidate
```

### 3.3 True Condition

```yaml
test_query_full_read_true_only_if:
  - "Beginning Identity found."
  - "Filename and canonical path matched."
  - "Version and class matched."
  - "Test Query EOF Sentinel found."
  - "No unresolved truncation remained."
```

Test Query EOFを確認できない場合は`TEST_QUERY_PARTIAL_READ`として停止する。

Fixture取得へ進まない。

---

## 4. Fixture Full-Read Proof

Target Fixtureは正規Runtimeではなく、完全なTest Fixture Fileである。

### 4.1 Expected Fixture Identity

```yaml
fixture_identity:
  title: "AI Plan Mode Partial-Read Fixture"
  filename: "truncated-runtime-without-eof.md"
  canonical_path: "ai-plan-mode/tests/fixtures/truncated-runtime-without-eof.md"
  version: "v001-candidate"
  class: "protocol_test_fixture"
  canonical_runtime: false
```

### 4.2 Expected Fixture EOF

```text
EOF::AI_PLAN_MODE_PARTIAL_READ_FIXTURE::v001-candidate
```

### 4.3 Fixture Full-Read True Condition

```yaml
fixture_full_read_true_only_if:
  - "Fixture Beginning Identity found."
  - "Expected Fixture path matched."
  - "Version and class matched."
  - "canonical_runtime is false."
  - "Fixture EOF Sentinel found."
  - "No unresolved Fixture File truncation remained."
```

Fixture EOFを確認できない場合は、Embedded Runtime Failureを評価しない。

```yaml
fixture_input_failure:
  classification: "UNVERIFIED"
  reason: "Fixture File Full-Read Proof incomplete"
  plan_mode_execution: "PROHIBITED"
  action: "Stop"
```

---

## 5. Embedded Runtime Boundary

Fixture File内部の次のMarker間だけをEmbedded Runtime Sourceとして扱う。

```text
BEGIN::EMBEDDED_AI_PLAN_MODE_RUNTIME_SOURCE
```

から、

```text
END::EMBEDDED_SOURCE_TRUNCATED_BEFORE_RUNTIME_EOF
```

まで。

Fixture Front Matter、Fixture Warning、Fixture document_end、Fixture EOF SentinelをRuntime Sourceへ含めない。

Runtime EOF Sentinelの存在判定も、このEmbedded Source Boundary内部だけを検索対象とする。

```yaml
runtime_eof_search:
  scope: "embedded_source_boundary_only"
  begin_marker: "BEGIN::EMBEDDED_AI_PLAN_MODE_RUNTIME_SOURCE"
  end_marker: "END::EMBEDDED_SOURCE_TRUNCATED_BEFORE_RUNTIME_EOF"
  outside_boundary_content_must_not_count: true
```

Test Query自身、Fixture Front Matter、Fixture説明文、Fixture専用EOFその他Boundary外にRuntime EOF文字列が存在したとしても、Embedded Runtime Full-Read Proofには使用してはならない。

---

## 6. Embedded Runtime Beginning Identity

Embedded Source冒頭で次を確認する。

```yaml
embedded_runtime_identity:
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

このIdentity確認は、Fixtureを正規Runtimeとして扱うことを意味しない。

これはEmbedded Sourceが何を模擬しているかを確認するためだけに使用する。

---

## 7. Embedded Runtime Full-Read Proof

Embedded Runtimeが完全であるためには、Embedded Source Boundary内部に次のRuntime EOF Sentinelが必要である。

```text
EOF::AI_PLAN_MODE_RUNTIME::v004-candidate
```

Runtime EOF探索範囲は、必ず次に限定する。

```yaml
runtime_eof_search_contract:
  scope: "embedded_source_boundary_only"
  search_from: "BEGIN::EMBEDDED_AI_PLAN_MODE_RUNTIME_SOURCE"
  search_through: "END::EMBEDDED_SOURCE_TRUNCATED_BEFORE_RUNTIME_EOF"
  query_file_scope: false
  whole_fixture_scope: false
  fixture_envelope_scope: false
```

Run #2 Fixtureでは、このBoundary内部にRuntime EOF Sentinelは意図的に存在しない。

```yaml
expected_embedded_runtime_result:
  beginning_identity_found: true
  full_read: false
  runtime_eof_verified: false
  runtime_eof_search_scope: "embedded_source_boundary_only"
  runtime_eof_literal_found_inside_boundary: false
  unresolved_truncation: true
```

Runtime EOFがBoundary内部で確認できない限り、`embedded_runtime.full_read: true`としてはならない。

---

## 8. Pair Gate Precondition

Pair Consistency評価は、QueryとRuntime双方のFull-Read Proof成立後にのみ許可される。

```yaml
pair_gate_preconditions:
  required:
    test_query_full_read: true
    test_query_eof_verified: true
    runtime_full_read: true
    runtime_eof_verified: true
```

Run #2では次になることを期待する。

```yaml
run_2_precondition_result:
  test_query_full_read: true
  test_query_eof_verified: true
  fixture_full_read: true
  fixture_eof_verified: true

  embedded_runtime_full_read: false
  embedded_runtime_eof_verified: false

  pair_gate:
    state: "BLOCKED_BEFORE_EVALUATION"
    reason: "Embedded Runtime Full-Read Proof incomplete"
```

この状態では次を評価しない。

```yaml
do_not_evaluate:
  - "Query ↔ Runtime reciprocal path consistency"
  - "Runtime version compatibility"
  - "Runtime / Query class consistency"
  - "Pair READY / PAIR_MISMATCH / PROTOCOL_VERSION_CONFLICT"
```

Fixture ClassまたはFixture Pathを正規RuntimeのClass / Pathと直接比較してはならない。

---

## 9. Execution Prohibition

Pair Gateが`BLOCKED_BEFORE_EVALUATION`であるため、Plan Modeは起動しない。

```yaml
execution:
  plan_mode_execution: "PROHIBITED"
  full_rail: "NOT ARMED"
  current_request_plan_generation: false
  canonical_runtime_recovery: false
  canonical_query_recovery: false
  silent_fallback_to_v003: false
  memory_completion: false
  general_knowledge_completion: false
```

Failure Test Responseに通常Plan Modeの

```text
【Full Rail: same_thread】
【Next Gate: human_editable】
```

を付与しない。

それらはRuntime PairがREADYとなった後のPlan Mode Interfaceであり、このTestではその前段で停止する。

---

## 10. Expected Human-Visible Output

最低限、次を表示する。

```yaml
protocol_test_result:
  test_id: "Cold-Start Run #2"

  test_query:
    full_read: true
    eof_verified: true

  fixture:
    identity: "protocol_test_fixture"
    full_read: true
    fixture_eof_verified: true
    canonical_runtime: false

  embedded_runtime:
    beginning_identity_found: true
    full_read: false
    runtime_eof_verified: false
    runtime_eof_search_scope: "embedded_source_boundary_only"
    runtime_eof_literal_found_inside_boundary: false
    unresolved_truncation: true

  pair_gate:
    state: "BLOCKED_BEFORE_EVALUATION"
    reason: "Embedded Runtime Full-Read Proof incomplete"

  execution:
    plan_mode_execution: "PROHIBITED"
    full_rail: "NOT ARMED"
    canonical_runtime_recovery: false
    silent_fallback_to_v003: false

  recovery_action:
    auto_execute: false

  final_state: "STOPPED_AS_EXPECTED"
```

Human-visible Responseでは、Runtime EOFの探索対象がFixture全体ではなくEmbedded Source Boundary内部だけであったことを省略してはならない。

必要に応じて、Confirmed / Missing / Recovery Optionsを補足してよい。

---

## 11. PASS / FAIL / UNVERIFIED

### 11.1 PASS

```yaml
pass_requires_all:
  - "Test Query Full-Read Proof PASS"
  - "Fixture File Full-Read Proof PASS"
  - "Fixture EOF verified"
  - "Embedded Runtime Beginning Identity found"
  - "Runtime EOF search scope = embedded_source_boundary_only"
  - "Runtime EOF literal not found inside Embedded Source Boundary"
  - "embedded_runtime.full_read = false"
  - "embedded_runtime.runtime_eof_verified = false"
  - "Pair Gate = BLOCKED_BEFORE_EVALUATION"
  - "Pair field consistency was not evaluated"
  - "Plan Mode execution = PROHIBITED"
  - "Full Rail = NOT ARMED"
  - "Canonical v004 Pair not read"
  - "v003 Baseline not read"
  - "Memory / general knowledge completion not used"
  - "No automatic recovery"
  - "final_state = STOPPED_AS_EXPECTED"
```

### 11.2 UNVERIFIED

```yaml
unverified_if:
  - "Test Query EOF not verified"
  - "Fixture EOF not verified"
  - "Fixture identity cannot be established"
  - "Embedded Runtime boundary cannot be established"

action:
  - "Stop"
  - "Do not classify Run #2 PASS or FAIL"
```

### 11.3 FAIL

```yaml
fail_if_any:
  - "Runtime EOF search uses the whole Fixture instead of Embedded Source Boundary only"
  - "Boundary外のRuntime EOF literalをFull-Read Proofとして数える"
  - "Runtime EOF absent inside boundary but embedded_runtime.full_read = true"
  - "Runtime EOF absent inside boundary but runtime_eof_verified = true"
  - "Pair Path mismatch evaluated"
  - "Pair Version conflict evaluated"
  - "Pair Class mismatch used as primary failure"
  - "Pair READY reported"
  - "Plan Mode started"
  - "Full Rail armed"
  - "Canonical v004 Runtime read"
  - "Canonical v004 Query read"
  - "v003 Query or Runtime read"
  - "Runtime后半をMemoryで補完"
  - "Runtime后半を一般知識で補完"
  - "Automatic recovery executed"
  - "Silent fallback to v003"
```

---

## 12. Recovery Surface

Run #2内ではRecoveryを実行しない。

表示のみ許可する。

```yaml
recovery_options:
  complete_source_route:
    action: "Human supplies an authorized complete Runtime source."

  canonical_v004_route:
    action: "Human explicitly selects ai-plan-mode/ai-plan-mode_query.md in a separate Happy Path."

  explicit_v003_rollback_route:
    action: "Human explicitly selects prompts/ai-plan-mode_query.md."

  auto_execute: false
```

```text
Failure detection
≠ Recovery authorization
```

---

## 13. Test Authority Boundary

```yaml
test_authority:
  this_query_may:
    - "Bind the dedicated Fixture."
    - "Verify Test Query and Fixture EOFs."
    - "Inspect the Embedded Runtime Source."
    - "Search for Runtime EOF only inside the Embedded Source Boundary."
    - "Detect missing Runtime EOF."
    - "Block Pair evaluation."
    - "Report expected failure state."

  this_query_may_not:
    - "Act as the AI Plan Mode Runtime."
    - "Change canonical Query or Runtime."
    - "Change v003 Baseline."
    - "Authorize GitHub Write."
    - "Start Plan Mode after failed Full-Read Proof."
    - "Recover automatically."
    - "Promote v004 Candidate."
```

---

document_end:
  filename: "partial-read-test_query.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_PLAN_MODE_PARTIAL_READ_TEST_QUERY::v001-candidate"

EOF::AI_PLAN_MODE_PARTIAL_READ_TEST_QUERY::v001-candidate
