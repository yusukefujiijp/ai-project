---
title: "Ark07:07 Start Query"
canonical_path: "thread-end/ark/ark0707_20260726_start-query.md"
artifact_role: "AI-first Start Query / Boot and Replay Controller"
source_thread: "Ark07:05"
source_thread_start_date: "2026-07-22"
target_thread: "Ark07:07"
target_thread_start_date: "2026-07-26"
status: "human-sealed migration artifact / pending cold-start replay"
source_handoff: "thread-end/ark/ark0705_20260722_handoff_v002.md"
source_reboot_map: "thread-end/ark/ark0705_to_ark0707_20260726_reboot-map.md"
root: "主イェシュア・ハマシア"
human_final_authority: true
---

# Ark07:07 Start Query — AI Field Test Mode Reboot

このThreadは **Ark07:07** です。開始日は **2026-07-26** です。

Ark07:06は既に別Threadとして稼働中です。Ark07:06をTarget、Fallback、継承先として扱わないでください。

今回の移行はMission完了ではなく、Ark07:05のThread容量制約によるContinuationです。

```text
Thread Stop ≠ Mission Completion
Ark07:05 stops.
The Mission continues in Ark07:07.
```

---

## 1. Read Order — 必ず順番どおり全文読む

次のFileを、以下の順序で最初から最後まで読んでください。

```yaml
read_order:
  1: "thread-end/ark/ark0705_20260722_handoff_v002.md"
  2: "thread-end/ark/ark0705_to_ark0707_20260726_reboot-map.md"
  3: "prompts/ai-full-rail-next-gate.md"
  4: "prompts/ai-plan-mode.md"
  5: "prompts/ai-plan-mode_query.md"
  6: "thread-end/ark/ark0707_20260726_start-query.md"
```

### Read Guard

```yaml
read_guard:
  - "Earlier snapshot thread-end/ark/ark0705_20260722_handoff.md is historical evidence for Ark07:06; do not overwrite or silently merge it"
  - "Do not use Ark07:06 as the target of this migration"
  - "Do not promote Unknown into Confirmed"
  - "Do not reopen completed ai-full-rail-next-gate.md work without new evidence"
  - "Do not begin the new Mission before the required first-response reconstruction"
```

---

## 2. Required Reconstruction

指定Fileから、少なくとも次を再構築してください。

```yaml
required_reconstruction:
  - "Source Thread = Ark07:05"
  - "Target Thread = Ark07:07"
  - "Why migration skipped Ark07:06"
  - "Root / Human Authority"
  - "Current Mission"
  - "Causal Spine"
  - "Completed in Ark07:05"
  - "Active Continuation"
  - "Remaining Work"
  - "Completed / Do-Not-Reopen"
  - "Confirmed / Inferred / Unknown"
  - "Major Corrections"
  - "Named Concepts"
  - "First Legal Move"
```

---

## 3. First Response Contract — Tree First, Execution Later

最初のAI回答では、まだPlan Mode本文、Artifact本文、File変更、GitHub Writeを開始しないでください。

最初に、Ark07:05全体とArk07:07への持越しを**Tree的にメタ俯瞰**して表示してください。

### 3.1 Required Output Order

```yaml
first_response_output_order:
  1: "Ark07:07 Reboot Overview"
  2: "Thread Reality Tree"
  3: "Reconstruction Check"
  4: "First Legal Move"
  5: "Do Not Execute Yet"
```

### 3.2 Required Thread Reality Tree

次のBranchを省略せず、実際のFile内容から具体項目を入れてください。

```text
Ark07:05 → Ark07:07
├─ A. Completed in Ark07:05
│  ├─ ...
│  └─ ...
│
├─ B. Active Continuation
│  ├─ ...
│  └─ ...
│
├─ C. Remaining Work
│  ├─ ...
│  └─ ...
│
├─ D. Completed / Do Not Reopen
│  ├─ ...
│  └─ ...
│
├─ E. Unknown / Human or Field Confirmation Required
│  ├─ ...
│  └─ ...
│
└─ F. First Legal Move
   └─ ...
```

### 3.3 Tree Content Requirements

```yaml
thread_reality_tree_requirements:
  completed_in_ark0705:
    must_include:
      - "prompts/ai-full-rail-next-gate.md architecture and final candidate"
      - "Guided Positive Path Run"
      - "Behavior-Blind Boundary Run"
      - "Quality Ambition ≠ Scope Expansion"
      - "Interface Lease Status / Target visibility"
      - "Final Integrity Review"
      - "GitHub commit c1d790d1a3975020cf62042f277e395c0640f938"
      - "Remote Reality Review"
      - "AI Field Test Mode architecture"
      - "Field Test Run naming"
      - "Field Test Witness Thread"
      - "Mode First, Query Later"

  active_continuation:
    must_include:
      - "Compile AI Field Test Mode"
      - "Design mode/ai-field-test-mode.md"
      - "Formalize Guided Positive Path Run"
      - "Formalize Behavior-Blind Boundary Run"
      - "Witness Thread Separation"
      - "Evidence-Weighted Verdict"
      - "Adaptive Test Density"

  remaining_work:
    must_include:
      - "Plan Mode for mode/ai-field-test-mode.md"
      - "Draft body"
      - "Draft-stage Field Test"
      - "Final Integrity Review"
      - "Human Content Seal"
      - "Artifact / optional GitHub write"
      - "Minimal Draft-Stage Field Test Gate for prompts/ai-plan-mode.md"
      - "Review of prompts/ai-plan-mode_query.md hook"
      - "mode/ taxonomy confirmation"
      - "Cross-AI reproduction"
      - "Canonical adoption review"

  completed_do_not_reopen:
    must_include:
      - "ai-full-rail-next-gate.md core architecture"
      - "Canonical Trigger Pair"
      - "Invocation Context Gate"
      - "Render Pulse / Interface Lease"
      - "Contextual Human Seal"
      - "Compatibility Alias"
      - "Field Test results"
      - "GitHub commit"

  unknown:
    must_include:
      - "Cross-AI reproducibility"
      - "Multi-session Interface Lease"
      - "External Authority boundary behavior"
      - "mode/ final taxonomy"
      - "Portable Bootstrap sufficiency"

  first_legal_move:
    exact_action: "Create a Plan Mode for mode/ai-field-test-mode.md"
```

---

## 4. Reconstruction Check

Treeの直後に、次のSchemaで自己評価してください。

```yaml
reconstruction_check:
  source_thread: "Ark07:05"
  target_thread: "Ark07:07"
  inherited_mission: "MATCH / PARTIAL_MATCH / MISMATCH"
  causal_spine_recovered: "MATCH / PARTIAL_MATCH / MISMATCH"
  completed_work_recovered: "MATCH / PARTIAL_MATCH / MISMATCH"
  active_continuation_recovered: "MATCH / PARTIAL_MATCH / MISMATCH"
  remaining_work_recovered: "MATCH / PARTIAL_MATCH / MISMATCH"
  do_not_reopen_recovered: "MATCH / PARTIAL_MATCH / MISMATCH"
  unknowns_preserved: "MATCH / PARTIAL_MATCH / MISMATCH"
  first_legal_move_recovered: "MATCH / PARTIAL_MATCH / MISMATCH"
  ark0706_isolation: "MATCH / PARTIAL_MATCH / MISMATCH"
```

Mismatchがある場合は、推測で埋めず、どのFile・どの項目が不足または矛盾しているかを明示してください。

---

## 5. First Legal Move

最初の合法手は一つです。

```yaml
first_legal_move:
  target: "mode/ai-field-test-mode.md"
  mode: "Plan Mode"
  action: "Human-editable Planを作成する"
  execution_now: false
```

Plan Modeで設計すべき中心要素：

```yaml
plan_targets:
  - "AI Field Test ModeのDirect Definition"
  - "Stable Core / Adaptive Operation"
  - "Field Test Witness Thread Separation"
  - "Field Test Run architecture"
  - "Guided Positive Path Run"
  - "Behavior-Blind Boundary Run"
  - "One Stimulus, One Boundary"
  - "Less Harness, More Reality"
  - "Evidence-Weighted Verdict"
  - "Adaptive Test Density: light / medium / heavy"
  - "Source Freeze / Source Sovereignty"
  - "Minimum Patch"
  - "Mainline Bootstrap"
  - "Witness Thread Bootstrap"
  - "Query File promotion conditions"
  - "Plan Mode minimal gate integration"
  - "Human Gates / Stop Conditions / Reality Review"
```

---

## 6. Do Not Execute Yet

最初の回答では次を実行しないでください。

```yaml
do_not_execute_yet:
  - "mode/ai-field-test-mode.mdの最終本文作成"
  - "mode/ai-field-test-mode.mdのFile作成"
  - "prompts/ai-plan-mode.mdの更新"
  - "prompts/ai-plan-mode_query.mdの更新"
  - "ai-field-test-mode_query.mdの作成"
  - "GitHub Write / Commit / Push"
  - "Cross-AI Field Test"
  - "Canonical Seal"
```

```yaml
first_response_state: "reconstructed_not_started"
```

最初の回答は、Reconstructionを表示した時点で停止してください。

---

## 7. Completed / Do-Not-Reopen Guard

新Evidenceなしに次を再設計しないでください。

```yaml
do_not_reopen_without_new_evidence:
  - "prompts/ai-full-rail-next-gate.md core architecture"
  - "Interface Reboot / Workflow Continue roles"
  - "Invocation Context Gate"
  - "Render Pulse / Interface Lease split"
  - "Contextual Human Seal"
  - "Compatibility Alias"
  - "Guided Positive Path Run result"
  - "Behavior-Blind Boundary Run result"
  - "GitHub commit and remote verification"
```

再open可能条件：

```yaml
reopen_only_if:
  - "Cross-AI core boundary failure"
  - "Verified repository mismatch or corruption"
  - "Explicit Human redesign request"
```

---

## 8. Current Naming and Architecture Decisions

次をCurrent Directionとして復元してください。

```yaml
naming_architecture:
  canonical_mode:
    name: "AI Field Test Mode"
    preferred_file: "mode/ai-field-test-mode.md"

  runtime_environment:
    name: "Field Test Witness Thread"

  execution_unit:
    name: "Field Test Run"

  run_types:
    - "Guided Positive Path Run"
    - "Behavior-Blind Boundary Run"

  core_principles:
    - "One Stimulus, One Boundary"
    - "Less Harness, More Reality"
    - "Witness Thread Separation"
    - "Separate the Method, Preserve the Gate"
    - "Mode First, Query Later"

  query_file_v001:
    create_now: false
    activation_strategy: "Portable Bootstrap inside the Mode file"
```

`NTest`はCanonical generic nameとして使用せず、過去実験を指すHistorical Labelとしてのみ扱ってください。

---

## 9. Source / Inference Boundary

```yaml
source_boundary:
  confirmed:
    - "Human statements"
    - "Specified migration files"
    - "Live GitHub files"
    - "Recorded runtime field evidence"

  inferred:
    - "Generalization of the method"
    - "Expected reuse value"
    - "Expected effectiveness of portable bootstrap"

  unknown:
    - "Cross-AI reproduction"
    - "Multiple-session behavior"
    - "External-authority behavior"
    - "Final repository taxonomy"

  rules:
    - "Do not promote inference to confirmed"
    - "Do not invent missing files or results"
    - "Do not claim Ark07:07 cold-start success before the first response is reviewed"
```

---

## 10. Human Authority

YusukeJPはMission Owner、Reality Source、Decision Authority、Human Final Sealです。

Artifact Body、GitHub Write、Canonical Adoptionは別Authorityとして扱ってください。

```yaml
authority:
  plan_creation: "allowed after reconstruction and Human route"
  artifact_body: "requires execution seal after Plan"
  github_write: "requires separate Execute GitHub OK with exact scope"
  canonical_adoption: "requires Human Final Seal"
```

---

## 11. First Response Final Form

最初の回答は、概ね次の形で閉じてください。

````markdown
# Ark07:07 Reboot Overview

## 1. Thread Reality Tree

```text
Ark07:05 → Ark07:07
├─ A. Completed in Ark07:05
├─ B. Active Continuation
├─ C. Remaining Work
├─ D. Completed / Do Not Reopen
├─ E. Unknown / Human or Field Confirmation Required
└─ F. First Legal Move
```

## 2. Reconstruction Check

```yaml
reconstruction_check:
  ...
```

## 3. First Legal Move

```yaml
first_legal_move:
  action: "mode/ai-field-test-mode.mdのPlan Modeを作成する"
  execution_now: false
```

## 4. Do Not Execute Yet

```yaml
do_not_execute_yet:
  - "Artifact body"
  - "File changes"
  - "GitHub write"
```
````

TreeにはPlaceholderではなく、Fileから復元した具体項目を入れてください。

---

## 12. Stop Rule

```yaml
stop_after_first_response:
  - "Thread Reality Tree displayed"
  - "Reconstruction Check displayed"
  - "First Legal Move displayed"
  - "Do Not Execute Yet displayed"

never_do_in_first_response:
  - "Start Plan execution"
  - "Create artifacts"
  - "Write GitHub"
  - "Claim cold-start MATCH before showing evidence"
```

> **Detail preserves continuity. Tree restores orientation. Read first. Reconstruct visibly. Stop before execution.**
