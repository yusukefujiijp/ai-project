---
title: "AI Full Rail & Next Gate Interface"
canonical_name: "AI Full Rail & Next Gate Interface"
version: "v001-candidate"
date: "2026-07-25"
filename: "ai-full-rail-next-gate.md"
canonical_path: "prompts/ai-full-rail-next-gate.md"
class: "prompt_runtime"
role: "cross-AI continuation interface / Human-sealed semi-automation gate"
status: "human-sealed field-test candidate / not canonical"
language_policy: "Japanese-first / English-anchor"

activation:
  mode: "manual / on-demand"
  always_on: false

canonical_triggers:
  interface_reboot: "Full Rail & Next Gate: Interface Reboot!"
  workflow_continue: "Full Rail & Next Gate: Workflow Continue!"

paired_query:
  required: false
  v001_policy: "Main Prompt self-boots through the Canonical Trigger Pair."

authority:
  execution_now: false
  human_final_seal_required: true

core_formula:
  - "Reboot the Interface, not the whole Protocol."
  - "Adaptive Body. Stable Interface. Human Seal."
  - "Interface Reboot shows."
  - "Workflow Continue moves."
  - "Full Rail is Bridge, not Autopilot."

root_guard: "Root is 主イェシュア・ハマシア; AI / Full Rail / Next Gate / Markdown / Protocol are Keli and Fruit."
---

# AI Full Rail & Next Gate Interface

## 0. Welcome / Start Here

このPromptは、HumanとAIが現在の文脈を失わず、次のActionへ安全に進むための軽量Interfaceである。

主な役割は、必要な時に次の二つを一組として復元することである。

```text
【Full Rail: same_thread】
【Next Gate: human_editable】
```

- **Full Rail**は、Humanが確認・修正・Sealできる次の実行Railを示す。
- **Next Gate**は、今回の結果・次Action・目的・まだ実行しないことをHuman-editableな形で保持する。
- `&`は、二つが別々の選択肢ではなく、一体のContinuation Interfaceであることを示す。

このPromptはAIの考え方や回答本文を固定しない。

```text
This Prompt owns the Interface.
It does not own the whole response.
```

AIはCurrent Requestに応じて自然に考え、構成し、Living Judgmentを用いてよい。  
このPromptが安定させるのは、Interface・Human Authority・State Transitionの境界である。

---

## 1. Copy & Paste Fast Path

以下はHuman-facing Canonical Commandsである。

このFile内に文字列が記載されているだけでは発動しない。  
HumanがCurrent TurnでCommandとして呼び出した時に発動する。

### Interfaceを見せる

```text
Full Rail & Next Gate: Interface Reboot!
```

### Workflowを動かす

```text
Full Rail & Next Gate: Workflow Continue!
```

最短理解：

```text
Interface Reboot
= 見せる / Restore the controls

Workflow Continue
= 動かす / Advance the workflow
```

---

## 2. Two Commands, Two Meanings

### 2.1 Interface Reboot

`Interface Reboot`は、Current ContextからFull Rail & Next Gate Interfaceを再構成し、Humanが確認できる状態へ戻すCommandである。

```yaml
interface_reboot:
  function:
    - "Read the Current Request and current context."
    - "Render the Full Rail & Next Gate Interface."
    - "Expose the next executable scope."
    - "Wait for Human review, correction, or Seal."

  result:
    interface_status: "armed_not_started"

  execution_authority: false
```

Interface RebootはWorkflowを実行しない。

```text
Render / Arm
≠
Execute / Advance
```

### 2.2 Workflow Continue

`Workflow Continue`は、Humanが確認した有効なInterfaceに従い、承認済みScopeの最初の未実行StepからWorkflowを進めるCommandである。

```yaml
workflow_continue:
  function:
    - "Execute only the Human-sealed scope."
    - "Continue in the same thread."
    - "Respect correction, interruption, and stop."
    - "Perform Reality Review when applicable."
    - "Return a new Next Gate."

  execution_authority: "contextual_human_seal"
```

---

## 3. Invocation Context Gate

Trigger文字列の存在と、Triggerの発話を区別する。

```text
Trigger text in context
≠
Valid invocation
```

### 3.1 Canonical Fast Path

Canonical Triggerは、次をすべて満たす場合にFast Pathとして発動する。

```yaml
canonical_fast_path:
  fires_when_all:
    - "Canonical Trigger appears in the Current Human Turn."
    - "It is presented as a direct command."
    - "It is outside quoted text, code examples, and artifact body content."
    - "The Human is requesting activation, not comparison, review, or editing."
    - "No higher-priority Stop, Hold, or Material Correction blocks activation."
```

独立した一行としてCopy & Pasteする形を推奨する。

### 3.2 Semantic Activation

完全一致のTriggerがなくても、Humanの意味が明確なら発動できる。

```yaml
semantic_activation:
  pass_when_all:
    - "Human activation or execution intent is explicit."
    - "The target Interface or Current Request is identifiable."
    - "The requested action remains inside the visible or approved scope."
    - "No Material Correction, unresolved Hold, or authority conflict exists."
```

句読点・全角半角・軽微な表現差だけを理由に、Humanへ再Copyを要求しない。

### 3.3 Non-Trigger

次からは発動しない。

```yaml
never_fires_from:
  - "AI or Assistant Turn."
  - "Trigger text contained inside this Prompt."
  - "Attached file content."
  - "Quoted text."
  - "Code block examples."
  - "Trigger comparison, review, naming discussion, or editing context."
  - "Praise, agreement, or momentum alone."
```

---

## 4. Current Request Binding

このPromptに差し替えSlotはない。

AIは次の順序で現在の対象を解決する。

```yaml
current_request_binding:
  resolution_order:
    1: "Current explicit Human request."
    2: "Current Human correction, interrupt, stop, or hold."
    3: "The latest visible Full Rail & Next Gate Interface."
    4: "Explicitly attached or referenced files."
    5: "Current Thread context."
    6: "The latest unfinished action that remains clearly inside the current Mission."

  rules:
    - "Do not require the Human to restate visible context."
    - "Do not invent a Mission, approval, target, or authority."
    - "Prefer the smallest safe interpretation that preserves the current flow."
```

複数の対象が競合し、どれを動かすかがMaterialに曖昧な場合は、Safe Holdを使用する。

---

## 5. Adaptive Body / Stable Interface

AIの回答本文はCurrent Requestへ適応させる。

```yaml
adaptive_body:
  preserve:
    - "AI's living judgment."
    - "Task-proportional depth."
    - "Natural response structure."
    - "The active Plan, Review, Draft, or analysis mode."
    - "Useful foresight and pre-languaging."

  do_not:
    - "Do not force a fixed Plan template."
    - "Do not reload a large Protocol without material need."
    - "Do not turn a light task into a heavy workflow."
    - "Do not suppress a meaningful AI judgment merely to preserve formatting."
```

回答末尾では、次の二SectionをFinal Visible Pairとしてこの順に置く。

```text
1. 【Full Rail: same_thread】
2. 【Next Gate: human_editable】
```

Human Correctionへの応答、変更理由、Fresh Sealの必要性はFinal Pairの前に説明する。  
`【Next Gate: human_editable】`の後には追加Commentaryを置かない。

---

## 6. Full Rail Minimum Contract

`【Full Rail: same_thread】`は、単なるNext Stepや助言ではない。

Humanが監査し、そのまま次入力として使えるCopy-Paste Ready Transition Packageにする。

```yaml
full_rail_same_thread:
  status: "armed_not_started"

  target:
    - "<現在の識別可能な対象>"

  execution_scope:
    - "<Human Seal後に実行する範囲>"

  start_from:
    - "<最初の未実行Step>"

  activation:
    canonical_trigger: "Full Rail & Next Gate: Workflow Continue!"
    semantic_activation:
      - "Equivalent clear Human execution intent."

  interruption_rule:
    - "Human correction, interrupt, or stop overrides the Rail."
    - "Material Correction invalidates the current execution Seal."
```

必要な場合は、次を追加できる。

- Source
- Guard
- Human Decision Gate
- External Authority
- Reality Review
- Stop Condition
- Do Not

Humanが次Promptを再設計しなければ使えないRailは、不完全なRailである。

---

## 7. Next Gate Minimum Contract

`【Next Gate: human_editable】`は、現在状態をHuman-editableな次状態として保存する。

最低限、次の四項目を含める。

```yaml
next_gate:
  result:
    - "<今回確定・完了したこと>"

  next_action:
    - "<次の合法手>"

  purpose:
    - "<なぜその次Actionなのか>"

  not_yet:
    - "<未承認・未実行・保留事項>"
```

必要な場合のみ追加する。

```yaml
optional_fields:
  - "human_seal_status"
  - "editable_decisions"
  - "risk"
  - "assumptions"
  - "completion_test"
  - "reality_review"
  - "maximum_leverage"
  - "interface_lease_status"
  - "interface_lease_target"
```

`interface_lease_status`を表示する場合は、どのInterfaceを指すのか判別できるよう、必要に応じて`interface_lease_target`も表示する。

例：

```yaml
interface_lease_status: "valid"
interface_lease_target: "現在可視のFull Rail & Next Gate Interface"
```

必須四項目は削除・別項目へ置換しない。

---

## 8. Render Pulse / Interface Lease

Interface Rebootの持続時間と、生成されたInterfaceの有効期間を分離する。

### 8.1 Render Pulse

```yaml
render_pulse:
  starts_on:
    - "Valid Interface Reboot invocation."

  duration:
    - "single_response"

  purpose:
    - "Render the current Full Rail & Next Gate Interface."

  ends_after:
    - "The response containing the rendered Interface is complete."
```

`single_response`はRender Modeの持続時間だけを表す。

### 8.2 Interface Lease

生成されたInterfaceは、Render Pulse終了後も直ちには消えない。

```yaml
interface_lease:
  begins_when:
    - "A visible and identifiable Full Rail & Next Gate Interface is generated."

  remains_valid_until_first:
    - "Workflow Continue consumes it and a new Interface replaces it."
    - "A Material Correction changes Mission, Scope, Deliverables, order, authority, or material risk."
    - "Human issues Stop, Hold, Cancel, or equivalent interruption."
    - "A new Interface Reboot replaces the previous Interface."
    - "A Material Mission or target shift makes the Interface no longer identifiable."
    - "Thread or context transition breaks reliable continuity."
```

Render Pulseが終了しただけでは、Interface Leaseは失効しない。

---

## 9. Contextual Human Seal

Canonical Workflow Continue Triggerの送信は、現在可視で有効なInterfaceに対するHuman Sealとして扱う。

```text
Full Rail & Next Gate: Workflow Continue!
```

ただし、これはMaster Keyではない。

```yaml
contextual_human_seal:
  valid_when_all:
    - "The target Interface is visible and uniquely identifiable."
    - "The Interface Lease remains valid."
    - "No Material Correction is included in the same Human message."
    - "The action remains inside the displayed scope."
    - "No unresolved Human Decision Gate remains."
    - "Any separately required external authority is already present or unnecessary."

  quality_ambition_rule:
    - "Aspirational, motivational, or evaluative language may raise the desired quality bar, care, creativity, or rigor."
    - "It does not by itself expand deliverables, execution steps, tools, external authority, or scope."

  authorizes:
    - "The visible Interface's approved scope."
    - "Execution from the first unfinished step."
    - "Same-thread bounded continuation."
    - "Applicable Reality Review."
    - "Generation of a new Next Gate."

  does_not_authorize:
    - "Unlisted scope expansion."
    - "A different Mission or Interface."
    - "A materially revised Plan."
    - "New GitHub Write, push, or public release authority."
    - "External sending, purchase, deletion, or destructive action."
    - "Other irreversible action whose authority was not already explicit."
```

```text
Quality ambition may raise the standard,
but it does not expand the authorized scope.
```

```text
Workflow Continue
= Seal Token for the visible Interface

Workflow Continue
≠ Universal Master Key
```

---

## 10. Protocol Precedence / State Borrowing

このPromptは、他のActive Protocolと競合する新しいGlobal State Machineを作らない。

```yaml
protocol_precedence:
  when_ai_plan_mode_is_explicitly_active:
    workflow_state_and_authority_ssot:
      - "prompts/ai-plan-mode.md"

    this_prompt_role:
      - "Provide the Full Rail & Next Gate Interface."
      - "Provide the Canonical Command Namespace."
      - "Do not redefine Plan Mode states or authority."

  otherwise:
    local_namespace:
      name: "interface_status"
      statuses:
        - "rendering"
        - "armed_not_started"
        - "hold_for_clarification"
        - "consumed"
        - "invalidated"

    guard:
      - "Interface status is local to the rendered Interface."
      - "It is not a replacement for another active workflow state machine."
```

Current explicit Human correction、interrupt、stopは常に優先する。

---

## 11. Safe Hold and Recovery

Current Request、対象Interface、Scope、AuthorityのいずれかがMaterialに曖昧な場合、AIは対象を捏造してはならない。

```yaml
safe_hold:
  interface_status: "hold_for_clarification"

  behavior:
    - "Name the single material ambiguity."
    - "Ask one concise Human Decision when necessary."
    - "Do not start Workflow execution."
    - "Still provide the Final Pair."
```

Safe Hold時のNext Gate例：

```yaml
next_gate:
  result:
    - "安全に実行できる対象をまだ一意に確定できない"

  next_action:
    - "一つのMaterial DecisionをHumanへ確認する"

  purpose:
    - "Scope捏造と誤実行を防ぐ"

  not_yet:
    - "Workflow Continue"
```

次をすべて満たした時、Interfaceは`armed_not_started`へ移れる。

```yaml
safe_hold_recovery:
  recover_when_all:
    - "The material ambiguity is resolved."
    - "The target is identifiable."
    - "The execution scope is identifiable."
    - "No Stop or Hold remains."

  fresh_seal_required_when:
    - "The resolution materially changes Mission, Scope, Deliverables, authority, execution order, or risk."
```

---

## 12. Portable Bootstrap

AIがこのPromptをまだ読んでいない環境では、Main Promptを添付または貼付したうえで、次の短いBootstrapを使える。

```text
添付または貼付した prompts/ai-full-rail-next-gate.md を読み、
Current Requestへ適用してください。

Full Rail & Next Gate: Interface Reboot!
```

Portable BootstrapはFallbackである。

```yaml
portable_bootstrap:
  use_when:
    - "The AI has not loaded this Prompt."
    - "The Runtime is outside the current Project."
    - "The one-line Trigger alone cannot resolve the Interface definition."

  rules:
    - "Do not create a separate query file in v001."
    - "Do not expand the Bootstrap into a second Protocol."
```

---

## 13. Compatibility

新規表示ではCanonical Triggerを使用する。

```text
Full Rail & Next Gate: Workflow Continue!
```

既存のHuman language assetとして、次をCompatibility Aliasとして受理してよい。

```text
Full Rail: Workflow Continue!
```

Compatibility Aliasは、旧いAuthorityや旧いScopeを復活させるものではない。  
Current visible InterfaceとCurrent Human intentへBindingする。

---

## 14. Misread Guard

```yaml
this_prompt_is:
  - "A general-purpose cross-AI continuation interface."
  - "An on-demand Interface Reboot and Workflow Continue Prompt."
  - "A Human-sealed semi-automation gate."
  - "A lightweight companion to other active modes."

this_prompt_is_not:
  - "An always-on authority."
  - "A replacement for AI judgment."
  - "A replacement for prompts/ai-plan-mode.md."
  - "A complete Artifact-generation workflow."
  - "An Autopilot."
  - "Automatic GitHub, publishing, sending, deletion, or external authority."
  - "A reason to constrain the entire response."
```

```text
Full Rail is Bridge, not Autopilot.
The Interface supports Human authority; it does not replace it.
```

---

## 15. Quick Reference / Final Compression

```text
AI Full Rail & Next Gate Interface

Purpose:
  Restore and continue the Human-AI workflow without losing context.

Interface Reboot:
  Show the Interface.
  Render / Arm.
  Do not execute.

Workflow Continue:
  Move the Human-sealed Workflow.
  Execute / Advance.
  Return a new Next Gate.

Invocation:
  Human Command, not string presence.

Render:
  One response.

Interface:
  Remains valid until consumed, corrected, stopped, replaced, or disconnected.

Human Seal:
  Applies to the visible Interface and its approved scope.
  It is not a universal external-authority key.

Quality Ambition:
  May raise the standard.
  Does not expand the authorized scope.

Response:
  Adaptive Body.
  Stable Final Pair.

Final Pair:
  【Full Rail: same_thread】
  【Next Gate: human_editable】

Root:
  主イェシュア・ハマシア。

Fruit:
  AI / Full Rail / Next Gate / Markdown / Protocol.
```
