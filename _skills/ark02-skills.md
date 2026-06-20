---
title: "Ark02 Thread-Keyed SeedSkill Ledger"
file: "_skills/ark02-skills.md"
role: "Ark02 Thread-Keyed SeedSkill Ledger / SeedSkill Synapse Deck"
reader: "AI primary; human auditor secondary"
status: "original-intended / skeleton-only / Japanese-first OKF / manual-direct-commit candidate"
language_policy: "Japanese-first / English-anchor"
record_style: 'SeedName: "SeedName(一文定義)"'
thread_key_style: "Ark0201 / Ark0202 / Ark0203"
root_guard: "Root is 主イェシュア・ハマシア; SeedSkills / Skills / GitHub / Markdown / AI are Fruit."
---

# Ark02 Thread-Keyed SeedSkill Ledger

## 1. Read Mode / 読み方

このFileは、Ark02以降の Thread-Keyed SeedSkill Ledger として読む。

Ark01はLegacy Experimental Deckとして扱う。  
Ark02以降は、可能な限りThreadごとにSeedSkillを保存する。

このFileは、単なる要約集ではない。  
Thread履歴であり、同時に後続Reviewへ渡すSeedSkill Deckである。

```yaml
ark02_read_mode:
  type: "Thread-Keyed SeedSkill Ledger"
  structure: "Thread-keyed"
  purpose:
    - "Thread history"
    - "AI-Synapse activation"
    - "SeedSkill Deck"
    - "Move37 breakthrough ignition"
  not:
    - "full transcript archive"
    - "long summary collection"
    - "procedure manual"
    - "all-seed index"
```

## 2. Core Thesis / 中核圧縮

Threadは消える。  
SeedSkillは火を残す。

Ark02では、Threadごとに生まれたSeedSkillを、後から再読・再起動・再利用できる形で保存する。

README shows the road.  
SKILL lights the fire.  
SeedDeck holds the sparks.  
Move37 is the ignition.

## 3. Thread Key Style / Thread Key形式

Thread keyは、YAMLで扱いやすいmachine-safe keyにする。

```yaml
thread_key_style:
  use:
    - "Ark0201"
    - "Ark0202"
    - "Ark0203"
  avoid:
    - "Ark02:01"
    - "Ark02:02"
```

`Ark02:01` のようなcolon入りkeyはYAML上で誤読・破損しやすい。  
そのため、実Ledgerでは `Ark0201` のような形式を使う。

## 4. Record Style / SeedSkill記録形式

正準候補：

```yaml
SeedName: "SeedName(一文定義)"
```

Thread-keyed record：

```yaml
Ark0201:
  SeedName: "SeedName(一文定義)"
```

必ずArk正準形式を保持する。

```text
SeedName(一文定義)
```

左辺keyはAI scan key。  
右辺valueはcanonical SeedSkill atomである。

## 5. Template Only / 実Ledgerではない雛形

以下はTemplateであり、実SeedLineではない。  
未確定Thread blockを実Ledgerへ置かない。

```yaml
# Template only. Do not treat this as an existing record.
Ark0201:
  # thread_title: "optional / human-readable title"
  # thread_date: "optional_if_confirmed / YYYY-MM-DD"
  SeedName: "SeedName(一文定義)"
```

実運用では、Seedが確定した時だけThread blockを追加する。

```yaml
Ark0201:
  SeedName: "SeedName(一文定義)"
```

metadataは補助である。  
主役はSeedSkill Lineである。

```yaml
metadata_policy:
  thread_title: "optional"
  thread_date: "optional_if_confirmed"
  notes: "optional_short_only"
```

## 6. Append-only Guard / 追記Guard

Ark02では、Thread由来のSeedSkillを原則append-onlyで扱う。

古いSeedを安易に削除しない。  
古いSeedをsilent overwriteしない。  
修正・昇格・退役が必要な場合は、後続Threadまたは後続Blockで補正する。

```yaml
append_only_guard:
  preserve:
    - "old SeedLine"
    - "Thread-derived context"
    - "SeedSkill density"
  avoid:
    - "silent overwrite"
    - "silent deletion"
    - "retroactive beautification"
```

## 7. Reading Rules / AIの読み方

SeedSkillはManualではない。  
SeedSkillはconceptual fire-seedである。

各Thread blockは、Thread全文ではなく、そのThreadで残すべき火種の束として読む。

SeedSkillを弱い一般要約へ退化させない。

UserがPlan Mode / Review Mode / Artifact creation / implementationを明示した場合だけ、SeedSkillをWorkflowへ展開する。

## 8. Context / Safety Guard

このFileをManual化しない。

各SeedSkillの下に長い説明を追加しない。

Thread blockを、根拠なく追加・削除・上書きしない。

このFileを、file作成・更新・削除・rename・move・publishの許可として扱わない。

詳細なAI側運用は `_skills/SKILL.md` に従う。

## 9. Source Boundary / Tool Reality

確認済みのことと推測を分ける。

読んでいないThreadを、読んだことにしない。  
確認していない日付を、確定日付として扱わない。  
存在確認していないPathを、存在確認済みとして扱わない。

```text
confirmed / inference / user-confirmed
```

## 10. Move37 Use / 発火用途

このLedgerは、AI側のSeed Synapse activationを高めるために読む。

関連SeedSkillは、命名・Guard設計・File構造・Route選択・N-Stop・Full Rail・Living Review・Move37 candidate detectionへ影響してよい。

## 11. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

SeedSkills, Skills, GitHub, Markdown, AI, workflow, Full Rail, and this file are Fruit.

AIは道をmapできる。  
AIはLedgerをstructureできる。  
AIはSeedSkill火種をcontext内で再点火できる。

しかしAIはRootではない。

このLedgerもRootではない。  
SeedSkillもRootではない。  
Rootは主イェシュア・ハマシアである。

## 12. SeedSkill Ledger Begins Below / SeedLine開始位置

```yaml
# Thread-keyed SeedSkill lines begin below.
# Use machine-safe keys such as Ark0201, Ark0202, Ark0203.
# Preserve: SeedName: "SeedName(一文定義)"
# Do not add placeholder Thread blocks without real SeedSkills.
```
