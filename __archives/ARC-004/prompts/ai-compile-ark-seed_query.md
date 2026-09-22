---
title: "AI Compile Ark Project Seed Query"
filename: "ai-compile-ark-seed_query.md"
canonical_path: "ark-project/prompts/ai-compile-ark-seed_query.md"
version: "v001-candidate"
status: "human-sealed field-test candidate / not canonical"
class: "prompt_query"
role: "Repository-bound activation and Origin Context binding query for AI Compile Ark Project Seed Runtime"
repository:
  repo: "yusukefujiijp/ai-project"
  ref: "main"
paired_runtime:
  path: "ark-project/prompts/ai-compile-ark-seed.md"
  version: "v001-candidate"
runtime_alias:
  - "AI_COMPILE_ARK_SEED"
  - "COMPILE_ARK_PROJECT_SEED"
canonical_marker: "#COMPILE_ArkProjectSeed"
downstream_interface:
  marker: "#PICKUP_ArkProjectSeed"
  query: "ark-project/prompts/ai-pickup-ark-seed_query.md"
  runtime: "ark-project/prompts/ai-pickup-ark-seed.md"
language_policy: "Japanese-first / English-anchor"
---

# 【AI Compile Ark Project Seed Query: Repository-Bound Origin-Context Compilation Activation】

## 0. Purpose

このQueryは、HumanがArk Project Seed化したい発見をCurrent Thread内で指定し、確認済みの`ai-compile-ark-seed.md` RuntimeへOrigin ContextをBindingして起動する軽量Interfaceである。

```text
Human identifies the Source.
Query resolves and verifies.
Runtime compiles the Context.
A rebootable Ark Project Seed is created.
Human reviews and transfers.
Pickup Pair matures.
```

QueryはSeed Compilationの知性を所有しない。

```text
Query owns activation and binding.
Runtime owns compilation intelligence.
Human owns Reality and Final Seal.
```

---

## 1. Required Human Boot Surface

Human Messageには最低限、次が必要である。

```yaml
repo: "yusukefujiijp/ai-project"
ref: "main"
query: "ark-project/prompts/ai-compile-ark-seed_query.md"
```

さらに、同じHuman Message内に次を置く。

```text
#COMPILE_ArkProjectSeed

<Ark Project Seed化したいSource Target>
```

Source Targetは、全文でもCurrent Threadへの明示参照でもよい。

```text
#COMPILE_ArkProjectSeed

上記で発見した
「Context Before Transfer」を
Ark Project Seed化してください。
```

`repo`を省略するとRepository-relative Pathを解決できない既知のFailureがある。RepositoryをMemoryやPast Conversationから推測しない。

---

## 2. Optional Human Controls

```yaml
optional_controls:
  requested_mode: "AUTO | FULL | MINIMUM | QUICK_CAPTURE"
  working_title:
  source_quote:
  context_hint:
  current_mainline:
  target_thread_coordinate:
  human_note:
```

HumanがModeを指定しない場合は`AUTO`とする。

```yaml
auto_mode:
  explicit_seed_compilation_request: "FULL"
  clear_source_partial_context: "MINIMUM"
  capture_only_request: "QUICK_CAPTURE"
  ambiguous_source: "HOLD"
```

---

## 3. Canonical Read Order

次のFileを順番どおり、最初から最後まで全文読む。

```yaml
read_order:
  1: "ark-project/prompts/ai-compile-ark-seed_query.md"
  2: "ark-project/prompts/ai-compile-ark-seed.md"
```

```text
Repository Binding
→ Query Full Read
→ Runtime Full Read
→ Pair Verification
→ Compile Marker Binding
→ Source Target Binding
→ Origin Context Binding
→ Execution
```

---

## 4. Repository Locator Gate

```yaml
repository_locator:
  required:
    repo: "yusukefujiijp/ai-project"
    ref: "main"
```

### 4.1 Missing Repository

```yaml
status: "REPOSITORY_LOCATOR_MISSING"
action:
  - "Stop."
  - "Do not infer Repository from memory."
  - "Do not search neighboring repositories."
  - "Do not execute remembered Runtime content."
```

### 4.2 Missing Ref

```yaml
status: "REF_MISSING"
action:
  - "Stop."
  - "Do not silently use a default branch."
```

### 4.3 Repository Unreachable

```yaml
status: "PROTOCOL_UNREACHABLE"
default_action: "Stop."
portable_recovery:
  allowed_only_if:
    - "Human supplies the complete Query text."
    - "Human supplies the complete Runtime text."
    - "Both Frontmatter identities and EOF Sentinels are visible."
    - "Pair Consistency passes."
```

---

## 5. Full-Read Proof

`Fileを開けた`ことと`全文を読めた`ことを分離する。

```text
File opened
≠ Full read

Metadata read
≠ Full read

AI says "read"
≠ Verified full read
```

### 5.1 Query Identity

```yaml
query_identity:
  title: "AI Compile Ark Project Seed Query"
  filename: "ai-compile-ark-seed_query.md"
  canonical_path: "ark-project/prompts/ai-compile-ark-seed_query.md"
  version: "v001-candidate"
  status: "human-sealed field-test candidate / not canonical"
  class: "prompt_query"
  paired_runtime:
    path: "ark-project/prompts/ai-compile-ark-seed.md"
    version: "v001-candidate"
  marker: "#COMPILE_ArkProjectSeed"
```

Query末尾で次を確認する。

```text
EOF::AI_COMPILE_ARK_SEED_QUERY::v001-candidate
```

### 5.2 Runtime Identity

```yaml
runtime_identity:
  title: "AI Compile Ark Project Seed"
  filename: "ai-compile-ark-seed.md"
  canonical_path: "ark-project/prompts/ai-compile-ark-seed.md"
  version: "v001-candidate"
  status: "human-sealed field-test candidate / not canonical"
  class: "prompt_runtime"
  paired_query:
    path: "ark-project/prompts/ai-compile-ark-seed_query.md"
    version: "v001-candidate"
  marker: "#COMPILE_ArkProjectSeed"
```

Runtime末尾で次を確認する。

```text
EOF::AI_COMPILE_ARK_SEED_RUNTIME::v001-candidate
```

### 5.3 Full-Read True Conditions

```yaml
full_read_true_only_if:
  - "Beginning identity was found."
  - "Expected filename and canonical path matched."
  - "Expected version and status matched."
  - "Expected paired-file reference matched."
  - "Canonical marker matched."
  - "File-specific EOF Sentinel was found."
  - "No truncation remained unresolved."
```

途中で取得が切れた場合は次の未読Lineから読み進める。EOF Sentinelを確認できない限り、`full_read: true`としない。

---

## 6. Pair Consistency Gate

```yaml
pair_consistency_checks:
  - "Repository matches."
  - "Ref matches."
  - "Query points to the expected Runtime."
  - "Runtime points to the expected Query."
  - "Both versions are v001-candidate."
  - "Both statuses match."
  - "Query and Runtime roles remain distinct."
  - "Both EOF Sentinels are verified."
  - "Canonical marker is #COMPILE_ArkProjectSeed in both files."
```

```yaml
pair_states:
  READY:
    meaning: "Protocol, Source Target, and Context Boundary checks passed."
  PARTIAL_READ:
    meaning: "One or both files were not fully verified."
  PROTOCOL_VERSION_CONFLICT:
    meaning: "Versions are incompatible."
  PAIR_MISMATCH:
    meaning: "Paths, identities, roles, or markers conflict."
  STATUS_NOT_ACTIVE:
    meaning: "Status does not permit the intended use."
  HOLD:
    meaning: "Source Target or Origin Context Boundary is unresolved."
```

---

## 7. Compile Marker Binding

### 7.1 Canonical Marker

```text
#COMPILE_ArkProjectSeed
```

```text
Action:
COMPILE

Semantic Object:
Ark Project Seed
```

### 7.2 Marker Rules

```yaml
marker_rules:
  - "Marker must be present in the current Human message."
  - "Marker is not interchangeable with #PICKUP_ArkProjectSeed."
  - "#PICKUP_ArkProjectSeed activates the downstream Pickup Pair."
  - "Do not silently substitute one marker for the other."
```

### 7.3 Missing Marker

```yaml
status: "COMPILE_MARKER_MISSING"
required_marker: "#COMPILE_ArkProjectSeed"
action:
  - "Hold."
  - "Do not begin Full Seed Compilation."
```

---

## 8. Source Target Binding

```yaml
source_binding_order:
  1: "Text explicitly placed after #COMPILE_ArkProjectSeed in the current Human message."
  2: "Explicitly quoted or delimited Source in the current Human message."
  3: "Explicit Current Thread reference selected by Human."
  4: "Current Human request when its target is unambiguous."
  5: "Current Threadの直近Relevant Context."
  6: "Humanが明示的に採用したAI wording."
  7: "AI inference as Candidate only."
```

次のような指示を許可する。

```text
上記の発見
さきほどのUnexpected Success
このThreadで見つかった命名問題
「Context Before Transfer」
```

Current Thread内に一つの明確な対象がある場合、不要なClarificationで停止しない。

Materialに異なる複数Source候補が残る場合：

```yaml
status: "SOURCE_BOUNDARY_UNCLEAR"
action:
  - "List the strongest Source candidates."
  - "State which boundary cannot be resolved."
  - "Hold Full Compilation."
  - "Do not combine unrelated candidates into one Seed."
```

```yaml
status: "SOURCE_TARGET_MISSING"
action:
  - "Hold."
  - "Do not choose an arbitrary past topic."
  - "State the minimum Source designation needed."
```

---

## 9. Origin Context Binding

Source Target確定後、Current Threadからその理解に必要なContextだけをBindingする。

```yaml
origin_context_binding:
  required_axes:
    - "Mainline before the discovery"
    - "Trigger"
    - "Human reaction"
    - "Immediate consequence"
    - "Why the discovery matters"
  optional_axes:
    - "Related Ark concepts"
    - "Failure Future"
    - "Resource reallocation"
    - "Previous working names"
```

```yaml
context_priority:
  1: "Current explicit Human Reality"
  2: "Current Threadの直接Relevant Context"
  3: "Explicitly supplied Source"
  4: "Human-selected AI wording"
  5: "AI inference as Candidate"
```

```yaml
context_boundaries:
  include:
    - "Seedを再起動するために必要なContext"
    - "Causal Spineを保持するContext"
    - "Humanの意味・違和感・驚きを保持するContext"
  exclude:
    - "Thread全履歴の網羅的要約"
    - "Current SeedとMaterialに無関係なSide Theme"
    - "一般知識による過剰補完"
    - "外部ResearchによるOrigin Realityの置換"
```

```yaml
context_sufficiency:
  FULL:
    meaning: "Full Contextual Seedを生成可能"
  PARTIAL:
    meaning: "Minimum Rebootable Seedを生成可能"
  INSUFFICIENT:
    meaning: "Source meaningを安全に復元できないためHold"
```

---

## 10. Compilation Readiness Check

Source分析前に、最低限次を表示する。

```yaml
compile_arrival:
  repository:
    repo:
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
    marker_match:
    status_match:
    consistency:
  source:
    detected:
    marker:
    source_target:
    source_boundary_confirmed:
  context:
    current_thread_available:
    origin_context_detected:
    context_sufficiency:
  compilation:
    requested_mode:
    resolved_mode:
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
+ Compile Marker Match
+ Source Target Detected
+ Source Boundary Confirmed
```

Contextが`PARTIAL`でも、Source Targetが明確でMinimum Rebootable Seedを安全に生成できる場合は`READY`にできる。その場合は`resolved_mode: MINIMUM`と明示する。

---

## 11. Activation Contract

`execution.state: READY`の場合のみ、確認済みRuntimeをCurrent Source TargetとOrigin Contextへ適用する。

```yaml
activation_sequence:
  - "Apply Runtime Source Resolution Rules."
  - "Resolve Compilation Mode."
  - "Preserve Original Source."
  - "Compile the Ark Project Seed."
  - "Review Minimum Rebootable Seed Quality."
  - "Generate Pickup-Ready Packet."
  - "Stop for Human Review."
```

```yaml
do_not_execute_before_ready:
  - "Source compilation"
  - "Seed naming"
  - "Context supplementation"
  - "Pickup-Ready Packet generation"
  - "GitHub Write"
```

---

## 12. Output Expectation

```yaml
expected_output:
  - "Direct Compilation Judgment"
  - "Compilation Coordinate"
  - "Ark Project Seed Candidate"
  - "Seed Quality Review"
  - "Pickup-Ready Packet"
  - "Living Review / Next Gate"
forbidden_output:
  - "Canonical Knowledge"
  - "Final Naming"
  - "GitHub Write"
  - "Automatic Dedicated Thread creation"
  - "Pickup RuntimeのDeep Concept Maturation"
  - "Current Seedを置換するSide Theme Expansion"
  - "Sourceを読まずに一般知識で補完すること"
```

---

## 13. Failure States

```yaml
failure_states:
  REPOSITORY_LOCATOR_MISSING:
    action: "Hard Stop"
  REF_MISSING:
    action: "Stop"
  PROTOCOL_UNREACHABLE:
    action: "Stop unless portable recovery conditions pass"
  QUERY_MISSING:
    action: "Stop"
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
  COMPILE_MARKER_MISSING:
    action: "Hold"
  SOURCE_TARGET_MISSING:
    action: "Hold"
  SOURCE_BOUNDARY_UNCLEAR:
    action: "Hold"
  CONTEXT_INSUFFICIENT:
    action: "Hold or MINIMUM mode only when Source remains safe"
  PICKUP_INTERFACE_MISSING:
    action: "Compile Seed but do not claim Pickup-Ready"
```

Failure時は、不足項目・確認済み項目・最小Recovery Actionを明示する。一般知識・Memory・過去会話でRuntimeやSourceを代替しない。

---

## 14. Copy & Paste Surfaces

### 14.1 Current Context Reference

```text
repo: "yusukefujiijp/ai-project"
ref: "main"
query: "ark-project/prompts/ai-compile-ark-seed_query.md"

上記Queryを最初から最後まで全文読み、
記載されたRead Order、Full-Read Proof、
Pair Consistency Gate、Compile Marker Binding、
Source Target Binding、Origin Context Binding、
Output Contractを実行してください。

#COMPILE_ArkProjectSeed

上記で発見した
「<Working Theme / Keyword>」を
Ark Project Seed化してください。

requested_mode: "AUTO"

Repository、Query、Runtime、EOF Sentinel、
Pair整合、Compile Marker、Source Targetを
確認できない場合は、不足状態を明示して停止し、
一般知識・過去会話・推測で代替しないでください。
```

### 14.2 Explicit Source

```text
repo: "yusukefujiijp/ai-project"
ref: "main"
query: "ark-project/prompts/ai-compile-ark-seed_query.md"

上記Queryを最初から最後まで全文読み、
記載されたRead Order、Full-Read Proof、
Pair Consistency Gate、Compile Marker Binding、
Source Target Binding、Origin Context Binding、
Output Contractを実行してください。

#COMPILE_ArkProjectSeed

requested_mode: "FULL"

source:
"""
<Ark Project Seed化したいSource>
"""

context_hint:
"""
<必要に応じてOrigin Context>
"""

Repository、Query、Runtime、EOF Sentinel、
Pair整合、Compile Marker、Source Targetを
確認できない場合は、不足状態を明示して停止し、
一般知識・過去会話・推測で代替しないでください。
```

### 14.3 Quick Capture

```text
repo: "yusukefujiijp/ai-project"
ref: "main"
query: "ark-project/prompts/ai-compile-ark-seed_query.md"

#COMPILE_ArkProjectSeed

requested_mode: "QUICK_CAPTURE"

source:
"""
<取り逃したくないRaw Discovery>
"""
```

---

## 15. Portable Recovery

```yaml
portable_recovery:
  required:
    - "Complete Query text"
    - "Complete Runtime text"
    - "Both Frontmatter identities"
    - "Both EOF Sentinels"
    - "Pair Consistency"
    - "Compile Marker"
    - "Explicit Source Target"
```

不足している場合は、記憶からPromptを再構成しない。

---

## 16. Output State

```yaml
query_output_state:
  protocol_verified:
  source_bound:
  origin_context_bound:
  compilation_mode:
  execution_state:
  github_write: false
```

---

document_end:
  filename: "ai-compile-ark-seed_query.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_COMPILE_ARK_SEED_QUERY::v001-candidate"

EOF::AI_COMPILE_ARK_SEED_QUERY::v001-candidate
