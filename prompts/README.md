---
title: "Prompts"
canonical_path: "prompts/README.md"
status: "active / human-sealed"
scope: "Cross-AI Prompt Runtime and Query Shelf"
language_policy: "Japanese-first / English-anchor"
last_updated: "2026-09-05"
root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Prompt / Markdown / GitHub are Keli and Fruit, not Root."
---

# Prompts

## 0. Current Coordinate / 現在座標

`prompts/`は、YusukeJP × AI-Collaboratorが複数AIをHuman-mediatedに起動・接続・役割分担するための、Cross-AI Operational Shelfである。

```text
One Canonical Prompt.
Many AI Runtimes.
Human routes and seals.
Reality confirms.
```

`ai-` Prefixは特定Vendor専用を意味しない。  
Cross-AI再利用を第一に設計されたHuman-AI Operational Assetを示す共有Namespaceである。

---

## 1. Naming Policy / 命名方針

### 1.1 Runtime-neutral Core First

正準Promptは、原則として特定AI名から開始しない。

```text
推奨:
  ai-file-damedashi.md
  ai-output-polish.md
  ai-plan-mode.md

原則避ける:
  chatgpt-*.md
  claude-*.md
  grok-*.md
  fable5-*.md
```

AI別Coreを増殖させると、Patch・Guard・Version・RealityがRuntimeごとに分裂する。

Runtime固有差は、同一Failureが実地で繰り返し確認され、Canonical Coreで吸収できない場合に限り、Coreを複製しないMinimal Adapterとして検討する。

### 1.2 Kebab-case

意味単位はHyphenで分ける。

```text
ai-plan-mode.md
ai-file-damedashi.md
ai-output-polish.md
```

---

## 2. Markdown + Query Pair / 正準Pair

Prompt Runtimeと起動Queryを分けられる場合、`_query.md` Pairを**強く推奨する基本形**とする。

```text
<ai-prompt>.md
<ai-prompt>_query.md
```

Queryは、長いRuntimeを短く安全に起動し、Target Binding、Protocol確認、Input Role、State Transitionを安定させる重要Assetである。

ただし、`_query.md`はすべてのPromptへ機械的に課す絶対条件ではない。

> **Query Pair is a high-priority default when it reduces operational ambiguity—not an absolute ritual.**

### 2.1 Pair化を優先する条件

```yaml
create_query_pair_when:
  - "対象Fileや変数のBindingが必要"
  - "Prompt Runtimeが長い"
  - "Protocol Missing / Version Gateが必要"
  - "Human SealからExecutionへの状態遷移がある"
  - "毎回の起動文再作成による事故がある"
  - "複数AIへ同じ方式で投入する"
```

### 2.2 Runtime単体を許容する条件

```yaml
single_runtime_allowed_when:
  - "起動方法が一意で短い"
  - "Targetや変数のBindingが不要"
  - "Version DriftのRiskが低い"
  - "Query追加が本体より運用負荷を増やす"
```

```text
Markdown governs.
Query binds and activates.
Human seals.
Reality confirms.
```

QueryはRuntime本体のUniversal Coreを重複保持しない。

---

## 3. Active Prompt Assets

### 3.1 AI File DAME-DASHI

```yaml
runtime: "prompts/ai-file-damedashi.md"
query: "prompts/ai-file-damedashi_query.md"
role: "Reality Red-Team / Minimal Patch"
```

### 3.2 AI Output Polish

```yaml
runtime: "prompts/ai-output-polish.md"
query: "prompts/ai-output-polish_query.md"
role: "Meaning-preserving output polish"
```

AI Output Polishは、長いRuntime、複数Input Mode、複数Output Type、Target Section指定を持つため、Query Pairによる起動責務分離の実益が確認された。

### 3.3 AI Plan Mode

```yaml
subsystem: "ai-plan-mode/README.md"
runtime: "ai-plan-mode/ai-plan-mode.md"
query: "ai-plan-mode/ai-plan-mode_query.md"
role: "Plan-to-Full-Rail Human-AI semi-automation gate"
status: "active route / compatibility period / v004-candidate"

rollback_baseline:
  runtime: "prompts/ai-plan-mode.md"
  query: "prompts/ai-plan-mode_query.md"
  version: "v003-candidate"
  policy:
    - "Retain unchanged during compatibility period."
    - "Use only when Human explicitly chooses rollback."
    - "Do not silently fall back."
```

```text
Deep Dialogue
→ Context Ripening
→ Move37-like Breakthrough
→ Plan Mode
→ Human-editable Review
→ Exact Human Trigger
→ Full Rail: same_thread
→ Reality Review
→ Next Gate / Harvest
```

### 3.4 AI-to-AI Communication

```yaml
runtime: "prompts/ai-to-ai-communication.md"
query: "prompts/ai-to-ai-communication_query.md"
role: "Human-mediated Cross-AI Message / Material Delta / finite convergence runtime"
status: "human-sealed v001.1 field-test candidate / not canonical"
origin: "Alan Kay式AI間コミュニケーション / Ark式温故知新のFirstfruits"
```

```text
Protocol Arrival
→ Mission Binding and Semantic Resolution
→ Role Eligibility / Human Re-Binding when needed
→ AI-A Message
→ YusukeJP routes meaning, Source, and requested Material Delta
→ AI-B returns Material Delta with Witness Integrity
→ Continue only while Material Delta exists
→ Terminal Synthesis
→ Human Final Seal
```

AI-to-AI Communicationは、Protocol Arrival・Role Eligibility・Semantic Bindingを実行前Gateとし、`Message`をCommunicationの中心単位、`Material Delta`を進行単位として、複数AIの異なるLensを有限往復で一つのHuman-reviewable成果へ収束させる。Alan Kay氏のMessage-centered LensをOrigin Anchorとして保持するが、Human Semantic Router、Material Delta Stop Rule、Terminal Synthesis等のArk AdaptationをAlan Kay本人へ誤帰属しない。

### 3.5 AI Living Graph Mode

```yaml
runtime: "prompts/ai-living-graph-mode.md"
query: "NOT CREATED — add only after repeated activation ambiguity"
role: "Relational reasoning / Graph-Native Fruit / Living update / prose return"
status: "human-sealed design candidate / field-test pending / not canonical"
default_artifact: "NONE"
```

AI Living Graph Modeは、Graph図やMini Appを生成するPromptではない。Humanが一つのKeywordまたはCurrent MissionへForeground集中できるよう、AI側で複数Node、Typed Edge、Residual、Guard、Prediction ErrorをBackground保持し、単独要約では見えない依存・摩擦・Bridge・矛盾・Unexpected Successを発見して、総合的な文章へ返すRuntimeである。

```text
Human Foreground
└─ 一つのFocus / Current Mission

AI Background
└─ 多Node・多関係・Guard・Actual Trace
   └─ Graph-Native Fruit
      └─ 総合的な文章へUnwind
```

Graph、Mini App、Site、Dashboard等のArtifactは、Humanが当該Artifactを明示的に依頼した場合だけ作る。Runtimeが長くても現時点ではBinding変数や状態遷移が小さいため、Query Pairは作らない。再現運用で起動曖昧性が観測された場合にのみPair化を再検討する。

### 3.6 AI One-Table Interface

~~~yaml
runtime: "prompts/ai-one-table-interface.md"
query: "NOT CREATED — add only after repeated activation or binding ambiguity"
role: "One adaptive Graph table per normal response / Human-AI shared coordinate / practical Graph instruction / Human-reviewed pattern formation"
status: "human-sealed design candidate / initial deployment / field-test pending / not canonical"
reasoning_dependency: "prompts/ai-living-graph-mode.md"
composition_dependency: "prompts/long-form-response-rhythm.md"
~~~

AI One-Table Interfaceは一般的な表作成Ruleではない。Current Realityと一問に応じて、Node、Typed Edge、Path、Bridge、Cut Edge、Activation、Guard、Evidence、Feedback等のRelevant Subgraphを一つの適応的Markdown表へ選択投影する、Graph-boundedなHuman-facing Interfaceである。

このRuntimeがBindingされた通常回答では一表をDefault必須とするが、Exact Output、STOP、Failure、安全、code-only、明示的なHuman no-table等の上位Contractを優先する。表が存在するだけでGraph-Native FruitまたはLiving Graph Modeとは主張しない。

~~~text
AI Living Graph Mode
→ discovers the relation

AI One-Table Interface
→ projects one relational view

Long-Form Response Rhythm
→ places the table in temporal composition
~~~

文書自身が一つのGraph表を実演し、Future AIへNode & Edgeを表作成の実技として教える。各回答で生成された表は、Human ReactionまたはCorrectionとPairになった時に初めてPattern Evidence Candidateとなる。Human ReviewなしにPattern保存、Query Pair化、Skill化、Canonical化を自動発火しない。

### 3.7 AI Benefit Branch Pruning

~~~yaml
runtime: "prompts/ai-benefit-branch-pruning.md"
query: "NOT CREATED — add only after repeated activation or binding ambiguity"
role: "Future-AI-first Dual-Benefit Branch Deadlock resolution / Benefit–Carrier separation / guarded Benefit preservation / one-choice recovery"
status: "human-sealed design candidate / first deployment / field-test pending / not canonical"
reasoning_dependency: "prompts/ai-living-graph-mode.md"
optional_projection_dependency: "prompts/ai-one-table-interface.md"
composition_dependency: "prompts/long-form-response-rhythm.md"
origin: "Wake-Up One-Choice Human-reported Actual Success"
~~~

AI Benefit Branch Pruningは、双方のBranchに本物のBenefitがあるため単純削除できず一択化が停止するDual-Benefit Branch Deadlockに対し、Benefitそのものと現在のCarrier BranchをGraph Mode的に分離し、Benefitを別の安全で適切なNode、Phase、Sandbox、AI BackgroundまたはRouteへ保存・再接続した上で、Current Goalに不可欠ではなくなったCarrier Branch／Comparison Edgeだけを剪定するFuture-AI-first Operational Runtimeである。

本文は抽象定義ではなく起床時Originから始まる。起床と再睡眠の双方Benefitを保持しながら、睡眠BenefitをHigh-Cognition判断とBody／Sleep／Safety Guardへ保存し、Low-Cognition起床Transitionから再比較Edgeだけを外したHuman-reported Actual Successを、BBPの最初のReality成立としてSource-boundに保持する。

~~~text
Two real Benefits
→ Benefit–Carrier Separation
→ Benefit preserved in the correct place
→ Current-Goal-unnecessary Branch pruned
→ Comparison and Drift Paths reduced
→ One Human-facing Route
→ Actual Reality
→ Human Review
~~~

Future AIが主読者であるが、AIが最終Authorityになることを意味しない。HumanはReality、意味、Correction、STOPおよびFinal Sealを保持する。一件の成功からQuery Pair、Skill、Canonical化、Cross-Project展開または次Trialを自動発火しない。

---

## 4. Human-mediated Multi-AI Use

```text
AI-A Output
→ YusukeJP selects, contextualizes, and routes
→ AI-B reviews or extends
→ YusukeJP integrates and seals
→ GitHub main stores Canonical Reality
```

Humanは単なるMessengerではない。  
Mission Owner、Semantic Router、Relevance Filter、Decision Authority、Human Final Sealである。

---

## 5. Mainline-First Mirror Guard

`prompts/`配下のCanonical PromptとQueryは、原則として`main`上で管理する。

```yaml
prompts_mainline_guard:
  canonical_branch: "main"
  branch_creation:
    default: false
    requires: "explicit Human Seal"
  rules:
    - "AIは良かれと思ってBranchを作らない"
    - "重要なPromptを未Merge Branchだけに残さない"
    - "Branchを第二のPrompt Realityとして扱わない"
```

Prompt RuntimeとQueryのPairは、同じ`main` Reality上で相互参照できる状態を保つ。

---

## 6. Canonical Core and Adapter Guard

```yaml
canonical_core:
  default: "one runtime-neutral file"
  location: "prompts/ai-*.md"

runtime_adapter:
  default: "do not create"
  allow_only_when:
    - "Repeated runtime-specific failure is observed."
    - "Canonical Core cannot safely absorb the difference."
    - "Adapter references the Core instead of copying it."
    - "Human Final Seal is present."
```

---

## 7. Final Compression

```text
One Repository.
One Main Reality.
Mainline-First.
One Canonical Prompt Core.
Markdown + Query when operationally useful.
Many AI Lenses.
Relations first; Graph-Native Fruit returns as prose.
When AI One-Table Interface is bound, one adaptive Graph table creates the shared lookout.
When Dual-Benefit Branch Deadlock appears, preserve the Benefit and prune only the Current-Goal-unnecessary Carrier Branch.
Human-mediated Handoff.
Human Final Seal.
```

> **Naming is architecture made visible.**
