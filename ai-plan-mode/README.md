---
title: "AI Plan Mode Subsystem"
canonical_name: "AI Plan Mode"
version: "v001-candidate"
date: "2026-08-06"
filename: "README.md"
canonical_path: "ai-plan-mode/README.md"
class: "subsystem_front_door"
role: "AI Plan Mode subsystem map / semantic ownership / maintenance read order / migration and rollback map"
status: "review-ready candidate / pending Human content seal / not canonical"
language_policy: "Japanese-first / English-anchor"

human_facing_entry:
  path: "ai-plan-mode/ai-plan-mode_query.md"
  role: "repository-bound single-entry activation query"

runtime:
  path: "ai-plan-mode/ai-plan-mode.md"
  version: "v004-candidate"
  role: "Plan Mode behavior and authority SSOT"

tests:
  path: "ai-plan-mode/tests/cold-start-test.md"
  version: "v001-candidate"
  role: "behavior equivalence and cold-start regression surface"

rollback_baseline:
  runtime:
    path: "prompts/ai-plan-mode.md"
    version: "v003-candidate"
    blob_sha: "c895fa27ae5e13b4b3343f22e76cf46b845bfa0b"
  query:
    path: "prompts/ai-plan-mode_query.md"
    version: "v003-candidate"
    blob_sha: "f87f14605bc9cd63043be282dca9d3053fd8f525"
  policy: "Do not modify, move, retire, or delete during parallel candidate field testing."

root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AI / Plan Mode / Query / Markdown / GitHub are Keli and Fruit, not Root."
---

# AI Plan Mode Subsystem

## 0. Current Coordinate / 現在座標

`ai-plan-mode/`は、AI Plan Modeを単独Promptではなく、検証可能なHuman–AI半自動化Subsystemとして育成するための新Home Candidateである。

このDirectoryは、現行v003 Pairを置き換えたActive Homeではない。

```yaml
current_state:
  new_home: "parallel candidate"
  old_pair: "active rollback baseline"
  cutover: false
  github_write_authority_from_this_file: false
```

> **旧Pairを壊さず、新Pairを隣で育て、Realityで渡れることを確認してから入口を切り替える。**

English anchor:

> **Rollback-Backed Parallel Candidate.**

---

## 1. 一文定義

> **AI Plan Mode Subsystemとは、RuntimeがPlan Modeの意味・状態・権限・実行境界を統治し、QueryがRepository Binding・全文読了・Pair整合・Current Request Bindingを担い、Human Sealによって非実行Planから同一Thread Full Railへ遷移する、検証可能なHuman–AI半自動化Systemである。**

---

## 2. Why This Home Exists / 独立Homeの理由

現行AI Plan Modeは、すでに次を保持している。

```text
Meaning Compilation
→ Human-editable Plan
→ Human Seal
→ Bounded Full Rail
→ Reality Review
→ Next Gate / Harvest
```

これは多数あるPromptの一つというより、Ark Projectの対話から実行への中枢Protocolである。

独立Homeの目的はFile数を増やすことではない。

```yaml
purpose:
  - "Human-facing Entryを一つにする"
  - "Runtime / Query / Testの責任を分離する"
  - "EOF Full-Read Proofを導入する"
  - "Pair Consistencyを検証可能にする"
  - "現行v003へのRoute-Level Rollbackを一手にする"
  - "将来の肥大化を意味単位で管理できるようにする"
```

---

## 3. Stable Core / 保存する成功DNA

新Candidateは、現行v003の次のBehaviorを同等以上に保持しなければならない。

```yaml
stable_core:
  constitutional:
    - "Plan Mode is non-execution mode."
    - "Human keeps Mission, Meaning, Discernment, Final Judgment, Responsibility, and Stop authority."
    - "AI does not self-authorize execution."
    - "Protocol remains subordinate to Mission."
    - "Reality Review closes execution."

  field_proven:
    - "armed_not_started"
    - "Full Rail: same_thread"
    - "Preferred Copy & Paste Fast Path"
    - "Semantic Activation Gate"
    - "Praise-only vs Praise-plus-Execution distinction"
    - "Material Correction requires Fresh Seal"
    - "Living Review Layer"
    - "Stable Full Rail / Next Gate interface"

  safety_critical:
    - "Plan / Execution Boundary"
    - "Artifact Body Boundary"
    - "Stop / Correction signal priority"
    - "No silent Scope expansion"
    - "Action-specific external authority"
    - "No old Seal transfer after Material Correction"
    - "Direct vs Human-mediated Reality Review"
    - "Protocol Missing / Version Conflict Stop"
```

---

## 4. File Topology / 文書身分

```text
ai-plan-mode/
├─ README.md
├─ ai-plan-mode_query.md
├─ ai-plan-mode.md
└─ tests/
   └─ cold-start-test.md
```

### 4.1 `README.md`

```yaml
owns:
  - "Subsystem Identity"
  - "Semantic Ownership Map"
  - "Maintenance Read Order"
  - "Current Candidate / Active Baseline relation"
  - "Migration and Rollback Map"
  - "Module Admission Rule"

must_not_own:
  - "Runtime State Machine body"
  - "Query verification algorithm body"
  - "Current Thread Reality"
  - "Field Test result as self-certified success"
```

### 4.2 `ai-plan-mode_query.md`

```yaml
owns:
  - "Human-facing Single Entry"
  - "Repository Locator"
  - "Query / Runtime Full-Read Proof"
  - "Pair Consistency Gate"
  - "Protocol Arrival Check"
  - "Current Request Binding"
  - "Failure States"
  - "Runtime Activation"

must_not_own:
  - "Plan Mode intelligence"
  - "Living Review semantics"
  - "Full State Machine"
  - "Thread Title naming intelligence"
```

### 4.3 `ai-plan-mode.md`

```yaml
owns:
  - "Plan Mode definition"
  - "Plan / Execution Boundary"
  - "Required Plan Semantics"
  - "Living Review"
  - "State Machine"
  - "Human Activation Gate"
  - "Full Rail"
  - "Correction / Re-Seal"
  - "Scope Guard"
  - "Reality Review"
  - "Final Interface"
  - "Conditional Thread Title Compilation"

must_not_own:
  - "Repository lookup implementation"
  - "Migration diary"
  - "Test result log"
```

### 4.4 `tests/cold-start-test.md`

```yaml
owns:
  - "Behavior Equivalence Contract"
  - "Cold-Start Test Matrix"
  - "Regression PASS / FAIL criteria"
  - "Human Reality Verdict surface"

must_not_own:
  - "Active Runtime rules"
  - "Active Query rules"
  - "Canonical promotion authority"
```

---

## 5. Read Order / 読込順

### 5.1 Normal Activation

HumanはQueryだけを指定する。

```yaml
normal_read_order:
  1: "ai-plan-mode/ai-plan-mode_query.md"
  2: "ai-plan-mode/ai-plan-mode.md"
```

```text
1. ai-plan-mode/ai-plan-mode_query.md
2. ai-plan-mode/ai-plan-mode.md
```

`README.md`と`tests/cold-start-test.md`は通常起動のRuntime Dependencyではない。

### 5.2 Maintenance / Revision

```text
1. ai-plan-mode/README.md
2. ai-plan-mode/ai-plan-mode_query.md
3. ai-plan-mode/ai-plan-mode.md
4. ai-plan-mode/tests/cold-start-test.md
5. active rollback baseline when comparison is required
```

### 5.3 Field Test

```text
1. New Query
2. New Runtime
3. Test Matrix
4. Human Reality Verdict
```

---

## 6. Semantic Ownership / 意味のSSOT

```yaml
semantic_ownership:
  subsystem_identity:
    owner: "ai-plan-mode/README.md"

  human_facing_activation:
    owner: "ai-plan-mode/ai-plan-mode_query.md"

  plan_mode_behavior:
    owner: "ai-plan-mode/ai-plan-mode.md"

  regression_and_cold_start:
    owner: "ai-plan-mode/tests/cold-start-test.md"

  current_thread_reality:
    owner: "Current Thread / Handoff / Start Query"

  active_repository_route:
    owner: "Repository front doors after Human-sealed cutover"
```

> **SSOTは一つの巨大Fileではない。各意味の正式Ownerが一つである。**

---

## 7. Safety-Critical Duplication / 意図的なSafety Echo

DRYは、すべての文字列重複を禁止しない。

QueryはRuntimeのTruth Ownerではないが、次の境界をSafety Echoとして保持してよい。

```yaml
safety_echo:
  - "Plan only"
  - "No final artifact body"
  - "No GitHub Write"
  - "armed_not_started"
  - "Praise-only is not execution authority"
  - "Material Correction / Stop overrides activation"
```

```yaml
duplication_guard:
  keep:
    - "Safety-critical boundary"
    - "Human-facing interface"
  remove_or_reference:
    - "Detailed Runtime semantics"
    - "Full State Machine explanations"
    - "Long examples already owned by Runtime"
```

---

## 8. Rollback Architecture / 巻き戻し構造

### 8.1 Level 0 — Parallel Candidate

新Candidateに問題があっても、旧PairはActive Baselineのままなので操作不要。

### 8.2 Level 1 — Route-Level Rollback

Humanが旧Queryを使用する。

```text
prompts/ai-plan-mode_query.md
```

### 8.3 Level 2 — Front-Door Rollback

Cutover後に問題が出た場合、README / RegistryのActive Routeだけを旧Pathへ戻す。

### 8.4 Level 3 — Git Revert

Cutover CommitをRevertする。

### 8.5 Level 4 — Exact Blob Recovery

```yaml
exact_blob_recovery:
  runtime: "c895fa27ae5e13b4b3343f22e76cf46b845bfa0b"
  query: "f87f14605bc9cd63043be282dca9d3053fd8f525"
```

> **最善のRollbackは復元作業を不要にする。旧Pairを無傷で保持する。**

---

## 9. Candidate Lifecycle / 候補の成熟順序

```text
Draft
→ Human Content Review
→ Human Content Seal
→ Candidate GitHub Write by separate authority
→ Static Reality Review
→ Cold-Start Field Test
→ Behavior Equivalence Test
→ Human Reality Verdict
→ Active Route Cutover by Fresh Seal
→ Compatibility Period
→ Retirement Review
```

```yaml
authority_separation:
  draft_approval:
    github_write: false

  content_seal:
    github_write: false

  candidate_write:
    requires:
      - "Execute GitHub OK"
      - "exact repository / ref / paths / scope"

  active_cutover:
    requires:
      - "Cold-Start PASS"
      - "Behavior Equivalence PASS"
      - "Fresh Human Seal"

  old_pair_retirement:
    requires:
      - "separate Fresh Human Seal"
```

---

## 10. Module Admission Rule / 将来分割の条件

初期CandidateではModuleを増やさない。

```yaml
split_into_module_only_when:
  - "独立Triggerがある"
  - "独立State Machineがある"
  - "Coreと異なる更新頻度が反復確認された"
  - "複数Runtimeから再利用される"
  - "分割後もHuman-facing Entryが増えない"
  - "依存Graphが本文より複雑にならない"
```

現在の候補：

```yaml
future_module_candidates:
  - "thread-title-compilation.md"
  - "extended-full-read-proof.md"
status: "not_yet"
```

---

## 11. Cutover Conditions / 入口切替条件

```yaml
cutover_requires:
  - "Query and Runtime EOF verified"
  - "Pair Consistency READY"
  - "Behavior Equivalence Contract PASS"
  - "Plan-only Boundary PASS"
  - "Praise-only Non-Trigger PASS"
  - "Semantic Activation PASS"
  - "Material Correction Re-Seal PASS"
  - "GitHub Authority Separation PASS"
  - "Conditional Thread Title PASS"
  - "Human Reality Verdict PASS"
  - "Fresh Human Cutover Seal"
```

一つでもSafety / Authority Behaviorが弱くなった場合はCutoverしない。

---

## 12. Do Not / 誤読防止

```yaml
do_not:
  - "READMEを第二Runtimeにしない"
  - "Queryを第二Runtimeにしない"
  - "TestsをActive RulesのSSOTにしない"
  - "旧PairをField Test前に変更しない"
  - "一回の成功でCanonical化しない"
  - "EOF Tokenだけで意味理解を証明したと扱わない"
  - "Plan SealをGitHub Write Authorityへ拡張しない"
  - "Thread Title CandidateをUI設定成功と自己認証しない"
  - "ProtocolをMissionやRootより上位にしない"
```

---

## 13. Final Compression

```text
One Human-facing Entry.
One Runtime Behavior SSOT.
One Verification Surface.
One untouched Rollback Baseline.

Query verifies and activates.
Runtime governs.
Human edits and seals.
Full Rail executes bounded scope.
Reality confirms—or remains unverified.
```

document_end:
  filename: "README.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_PLAN_MODE_README::v001-candidate"

EOF::AI_PLAN_MODE_README::v001-candidate
