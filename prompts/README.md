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

`prompts/` は、YusukeJP × AI-Collaboratorが複数のAI RuntimeをHuman-mediatedに起動・接続・役割分担するための、Cross-AI Prompt Runtime Shelfである。

ここに置くPromptは、原則としてChatGPT、Claude、Grok、Fable5など特定Vendorや特定Modelだけに閉じない。

```text
One Canonical Prompt.
Many AI Runtimes.
Human routes and seals.
Reality confirms.
```

`ai-` Prefixは、特定AI専用という意味ではない。

`ai-` は、そのFileがAI Runtimeによって利用されるHuman-AI Operational Assetであり、Cross-AI再利用を第一に設計された共有Promptであることを示すNamespaceである。

---

## 1. Naming Policy / 命名方針

### 1.1 Runtime-neutral Core First

正準Promptは、特定AI名から開始しない。

```text
推奨:
  ai-plan-mode.md
  ai-file-damedashi.md
  ai-output-polish.md

原則避ける:
  chatgpt-plan-mode.md
  claude-plan-mode.md
  grok-plan-mode.md
  fable5-plan-mode.md
```

AI別Promptを最初から増殖させると、同じCoreに対するPatchがRuntimeごとに分裂し、意味上のBranchが発生する。

```text
Runtime Fork Fragmentation:
  Canonical CoreがAI名ごとに複製され、
  修正・Guard・Version・Realityが同期しなくなるFailure。
```

Runtime固有差は、同一Failureが実地で繰り返し確認され、Canonical Coreでは吸収できない場合に限り、Coreを複製しないMinimal Adapterとして検討する。

### 1.2 Kebab-case

意味単位はHyphenで分ける。

```text
ai-plan-mode.md
ai-file-damedashi.md
ai-output-polish.md
```

`ai-planmode.md`のような概念結合より、`plan`と`mode`の境界が明確な`ai-plan-mode.md`を優先する。

---

## 2. Markdown + Query Pair / 正準Pair

Prompt Runtimeと起動Queryを分けられる場合、次のPairを基本形とする。

```text
<ai-prompt>.md
<ai-prompt>_query.md
```

例:

```text
ai-file-damedashi.md
ai-file-damedashi_query.md

ai-plan-mode.md
ai-plan-mode_query.md
```

### 2.1 Role Separation

```yaml
markdown_runtime:
  role:
    - "定義"
    - "Mission"
    - "Workflow"
    - "State Machine"
    - "Guard"
    - "Stop Rule"
    - "Human Authority"

query:
  role:
    - "対象Binding"
    - "Protocol存在確認"
    - "短い起動命令"
    - "RuntimeへのRouting"
```

```text
Markdown governs.
Query activates.
Human seals.
Reality confirms.
```

QueryはRuntime本体の仕様を重複保持しない。重複すると、MarkdownとQueryのVersion Driftが発生する。

ただし、Protocol Missing Gate、Target Binding、実行禁止など、起動事故を防ぐ最小GuardはQuery側にも置ける。

---

## 3. Human-mediated Multi-AI Use

各AIは同じPrompt Runtimeを読み、異なるLensで作業する。

AI間Communicationは、原則としてYusukeJPを介した間接的・擬似的Communicationである。

```text
AI-A Output
→ YusukeJP selects, contextualizes, and routes
→ AI-B reviews or extends
→ YusukeJP integrates and seals
→ GitHub main stores Canonical Reality
```

Humanは単なるMessengerではない。

HumanはMission Owner、Semantic Router、Relevance Filter、Decision Authority、Human Final Sealである。

---

## 4. Active Prompt Assets

### 4.1 AI File DAME-DASHI

```yaml
runtime:
  path: "prompts/ai-file-damedashi.md"
  role: "target-file-paired Reality Red-Team / Minimal Patch"

query:
  path: "prompts/ai-file-damedashi_query.md"
  role: "Target Binding Query"
```

### 4.2 AI Output Polish

```yaml
runtime:
  path: "prompts/ai-output-polish.md"
  role: "既存AI Outputを意味変更なしで本番用へ整形"
```

現時点では独立Query Pairを必須化しない。Realityが必要性を示した場合のみ追加する。

### 4.3 AI Plan Mode

```yaml
runtime:
  path: "prompts/ai-plan-mode.md"
  role: "Human-AI Semi-Automation Protocol / Plan-to-Full-Rail Gate"

query:
  path: "prompts/ai-plan-mode_query.md"
  role: "Protocol Identity Gate + Plan Mode Activation"
```

AI Plan Modeは次の流れを支える。

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

## 5. Pair Creation Rule

すべてのPromptに機械的にQueryを作るわけではない。

次のいずれかが存在する場合にPair化を優先する。

```yaml
create_query_pair_when:
  - "対象Fileや変数のBindingが必要"
  - "Prompt Runtimeが長く、短い起動Commandが必要"
  - "Protocol Missing / Version Gateが必要"
  - "Human SealからExecutionへの状態遷移がある"
  - "毎回の起動文再作成による事故がある"
  - "複数AI Runtimeへ同じ方式で投入する"
```

QueryがPrompt本体と同程度に長くなる場合は、Role Separationが崩れている可能性を疑う。

---

## 6. Canonical and Adapter Guard

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

特定AIで一度挙動差が出ただけでは、AI別Fileを作らない。

まずCanonical Core、Query、Context、Instruction Precedence、Field Test条件を確認する。

---

## 7. Repository Principle

`prompts/` は、複数AIが同じGoalへ向かうためのShared Operational Layerである。

```text
One Repository.
One Main Reality.
One Canonical Prompt Core.
Many AI Lenses.
Human-mediated Handoff.
Human Final Seal.
```

Namingは整理後のLabelではない。

> **Naming is architecture made visible.**

File名とPair構造だけで、Future HumanとFuture AIがRole、再利用範囲、起動方法を推測できる状態を目指す。
