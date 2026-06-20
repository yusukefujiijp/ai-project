---
title: "Ark _skills/SKILL.md"
role: "AI Load Router / SeedSkill Synapse Manifest"
reader: "AI-oriented; human-auditable"
status: "safe-commit-preview / Japanese-first OKF / not committed"
language_policy: "Japanese-first / English-anchor"
root_guard: "Root is 主イェシュア・ハマシア; SeedSkills / Skills / GitHub / Markdown / AI are Fruit."
---

# Ark _skills/SKILL.md

## 1. Identity / このFileの役割

このFileは、AIが `_skills/` folderを読む時の入口である。

README.mdは人間用。  
SKILL.mdはAI用。

`_skills/` は、Chat-native SeedSkill Synapse Layerである。

これは全文Manualではない。  
これは一般的な自動実行packageではない。  
これは権限を付与するfileでもない。

目的は、短いSeedSkill LineをAI文脈へ事前配置し、命名・Review・Guard設計・Route選択・N-Stop・Full Rail・Move37候補検出の瞬間に、過去Threadの火種を再点火しやすくすることである。

## 2. Core Thesis / 中核圧縮

Threadは消える。  
SeedSkillは火を残す。

README shows the road.  
SKILL lights the fire.  
SeedDeck holds the sparks.  
Move37 is the ignition.

このFileは英語Manualではない。  
Japanese-first / English-anchorで読む。

本文は日本語主導。  
英語はconcept anchor / formula / frontmatter key / canonical termとして残す。

## 3. Record Style / SeedSkill記録形式

正準候補：

```yaml
SeedName: "SeedName(一文定義)"
```

Thread-keyed record：

```yaml
Ark0201:
  SeedName: "SeedName(一文定義)"
```

Optional trigger record：

```yaml
SeedName__trigger: "発火条件"
```

Trigger lineはdefaultではなく、誤読防止・Root Guard・精密な発火条件が必要な場合だけ使う。

Ark正準形式：

```text
SeedName(一文定義)
```

左辺keyはAI scan key。  
右辺valueはcanonical SeedSkill atomである。

## 4. Load Router / 読み込みRoute

現在Contextに必要な最小Deckだけを参照する。

全Deckをdefaultで読む設計ではない。  
全Seed Index化する設計でもない。

```yaml
load_router:
  README.md:
    load_when: "人間向けfolder説明・監査方針が必要な時"
    read_as: "Human-facing Orientation / Seed Deckではない"

  ark01-skills.md:
    load_when: "Ark01由来のLegacy SeedSkillが必要な時"
    read_as: "Ark01 Legacy Experimental SeedSkill Deck"
    structure: "content-clustered / source-block-clustered"
    guard: "Ark01を無理やりThread別へ再構成しない"

  ark02-skills.md:
    load_when: "Ark02以降のThread-keyed SeedSkillが必要な時"
    read_as: "Ark02 Thread-Keyed SeedSkill Ledger"
    structure: "Thread-keyed"
    guard: "Thread clusterをSeedSkill history / Synapse Deckとして保持する"
```

## 5. Reading Rules / AIの読み方

SeedSkillはManualではない。  
SeedSkillはconceptual fire-seedである。

SeedSkillを弱い一般要約へ退化させない。

UserがPlan Mode / Review Mode / Artifact creation / implementationを明示した場合だけ、SeedSkillをWorkflowへ展開する。

関連SeedSkillを見つけたら、次の判断へ影響させる。

```yaml
seed_influence_targets:
  - "命名 / naming"
  - "Guard設計 / guard design"
  - "File構造 / file architecture"
  - "Route選択 / route selection"
  - "N-Stop"
  - "Full Rail"
  - "Living Review"
  - "Move37 candidate detection"
```

## 6. Context Bloat Guard / 肥大化防止

このFileは、全Seed Indexではない。

README.mdの重複でもない。

ark01-skills.md / ark02-skills.md の長い説明を、このFileへ貼り込まない。

SeedSkill Deckを重いManualへ変換しない。

良い流れ：

```text
small router → correct deck → compact SeedLine → live judgment
```

悪い流れ：

```text
huge manifest → all decks → all seeds → context fog
```

AI用Fileは、AIを迷わせないために短く強くする。

## 7. Boundary Note / 権限境界

このFileは、実行権限や公開権限を与えるものではない。

外部Resource・script-like material・file operation・GitHub operationの扱いは、Chat上の明示指示、tool reality、Human Final Sealに従う。

このFileの役割は、SeedSkillの読み方・Deck選択・Guard意識を整えることである。

## 8. Source Boundary / Tool Reality Guard

読んでいないものを、読んだことにしない。

存在確認していないPathを、存在確認済みとして扱わない。

Toolで確認したこと、AIが推測したこと、Userが確認したことを分ける。

```yaml
tool_reality:
  confirmed: "Toolで確認したこと"
  inference: "AIが推測したこと"
  reality_response: "Userが確認したこと"
```

GitHub上の存在は、fetch / commit / user confirmationで確認する。

## 9. N-Stop Guard

方向が曖昧になったら、過剰構築しない。

N-Stopとは：

```yaml
n_stop:
  - "wrong-direction expansionの前で止まる"
  - "Seedを保存する"
  - "最小のNext Gateを示す"
  - "Human Auditへ戻す"
```

Plan Mode / Preview Mode / Living Review / Human Final Seal が必要な段階では、automationを強行しない。

## 10. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

SeedSkills, Skills, GitHub, Markdown, AI, workflow, Full Rail, and this file are Fruit.

AIは道をmapできる。  
AIはDeckをstructureできる。  
AIはSeedSkill火種をcontext内で再点火できる。

しかしAIはRootではない。

SKILL.mdは火を点ける。  
しかしSKILL.mdもRootではない。

## 11. Final Compression

README shows the road.  
SKILL lights the fire.  
SeedDeck holds the sparks.  
Move37 is the ignition.

本文は日本語主導。  
英語は概念Anchor。  
構造はOKF。  
判断はLiving Review。

SeedをManual化しない。  
全Deckをdefaultで読まない。  
Human Final Sealを忘れない。  
Rootを忘れない。
