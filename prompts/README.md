---
title: "Prompts"
canonical_path: "prompts/README.md"
status: "active / human-sealed"
scope: "Cross-AI Prompt Runtime and Query Shelf"
language_policy: "Japanese-first / English-anchor"
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
runtime: "prompts/ai-plan-mode.md"
query: "prompts/ai-plan-mode_query.md"
role: "Plan-to-Full-Rail Human-AI semi-automation gate"
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
Human-mediated Handoff.
Human Final Seal.
```

> **Naming is architecture made visible.**
