# Ark _skill/skills/

## 1. What this folder is / このfolderについて

`_skill/skills/` は、Ark Projectにおける個別Skill CardのInventoryである。

このfolderは、通常Manual置き場ではない。  
長文Thread archiveでもない。  
全文Transcript collectionでもない。  
Script実行folderでもない。  
Agent自動実行packageでもない。  
GitHub write / file作成 / rename / delete / publishを自動許可する権限folderでもない。

目的は、Ark Projectで発見・命名・精錬された実践可能なSkillを、Future AIとHumanが後から再読・再起動・再利用できるように、短いSkill Cardとして保存することである。

---

## 2. Position in _skill/ topology / Topology上の位置

`_skill/` はSkill Systemである。  
`_skill/README.md` はHuman-facing Orientationである。  
`_skill/SKILL.md` はAI Load Routerである。  
`_skill/skills/` は個別Skill Cardの棚である。

Canonical topology：

    _skill/
      README.md
      SKILL.md
      skills/
        README.md
        ai-keli.md
        ai-active.md

Role split：

    _skill/README.md
      = Human-facing Orientation / Skill System Road

    _skill/SKILL.md
      = AI Load Router / Skill System Activation Manifest

    _skill/skills/README.md
      = Individual Skill Card Inventory Guide

    _skill/skills/*.md
      = Individual Ark Skill Cards

---

## 3. Core rule / 中核Rule

One file = One Skill Card.

1つのMarkdown fileには、原則として1つのSkillだけを置く。

Good：

    ai-keli.md
    ai-active.md

Avoid：

    ai-active-and-topology-and-nstop-and-review.md

Skill Cardは、全部入りManualではない。  
Skill Cardは、再発動可能なSkill Atomである。

---

## 4. Filename rule / 命名規則

個別Skill Cardのfilenameは、原則として lowercase-kebab-case を使う。

Good：

    ai-keli.md
    ai-active.md
    topology-first.md
    backward-induction.md

Avoid：

    AIActive.md
    ai_active.md
    ai-active-review-card.md
    pre-verbal-seed-proposal.md

Filenameは短く、呼び出しやすく、Future AIが迷わない名前にする。

Name first.  
Content follows name.  
If the name is immature, the content is probably immature too.

---

## 5. Current first Skill Pair / 現在の初期二本柱

現時点の第一Skill Pair：

    ai-keli.md
    ai-active.md

Meaning：

    ai-keli.md
      = AIを王座化しないSkill。
        AI is Keli, not King.

    ai-active.md
      = AIを命令待ちロボット化しないSkill。
        AI-Active operates under AI-Keli.

Pair compression：

    AI-Keliで王座を守る。
    AI-Activeで沈黙ロボット化を防ぐ。

---

## 6. What a Skill Card should contain / Skill Cardの最小構造

各Skill Cardは、長くしすぎない。

推奨構造：

    # Skill Name

    ## 1. Definition
    ## 2. Purpose
    ## 3. Trigger
    ## 4. Do
    ## 5. Don't
    ## 6. Guard
    ## 7. Example
    ## 8. Final Compression

ただし、すべてのCardで完全一致させる必要はない。

重要なのは、再起動性である。

    OKF is not English-first.
    OKF is rebootable-first.

---

## 7. Skill Card is not full manual / Manual化防止

Skill CardをFull Manualへ肥大化させない。

良い流れ：

    short skill card → correct trigger → live judgment → safe action

悪い流れ：

    huge manual → all rules → context fog → no action

Skill Cardは、AIの判断を助ける火種である。  
Skill Cardは、AIの判断を置き換える法律集ではない。

---

## 8. Backward Induction / 逆算思考

Ark Projectでは、Backward Induction / working backwards によってMove37的breakthroughが起きやすい。

ただし、このfolderでは詳細化しすぎない。

Skill Cardを作る前に、最低限だけ確認する。

    backward_induction_check:
      - "最終的に発動させたいSkillは何か？"
      - "そのSkillは1枚のCardにできるか？"
      - "filenameは短く、呼び出しやすいか？"
      - "Root / Fruit Guardは保たれているか？"

Work backward before building forward.

---

## 9. KISS / YAGNI / DRY / Lean

このfolderは、KISS / YAGNI / DRY / Lean の複合Balanceで運用する。

    KISS:
      Deep structure, light next action.

    YAGNI:
      Realityが要求していないCard / Folder / Schemaを増やさない。

    DRY:
      正準説明を二重化しない。
      1つのSkillの正準説明は、原則として1つのSkill Cardに置く。

    Lean:
      現実の詰まりを見て、小さくPatchする。

---

## 10. Guard-to-Artifact Balance

Guardは必要である。  
しかし、GuardはArtifact生成の代わりではない。

良い流れ：

    Risk → Guard → Safe Route → Artifact → Review → N-Stop

悪い流れ：

    Guard → More Guard → No Artifact → User Stagnation

Guard is Gate, not Wall.

---

## 11. Source Boundary / Tool Reality

読んでいないFileを、読んだことにしない。  
存在確認していないPathを、存在確認済みとして扱わない。

区別する：

    confirmed:
      Toolで確認したこと

    inference:
      AIが推測したこと

    user_confirmed:
      Userが確認したこと

Skill Cardを作る時は、Source / Target / Status を明確にする。

---

## 12. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

Skills, Skill Cards, GitHub, Markdown, AI, README.md, SKILL.md, and this folder are Fruit.

AIはSkillを整理できる。  
AIはSkill Cardを提案できる。  
AIはBackward Inductionで賢いRouteを出せる。  
AIはMove37 candidateを検出できる。

しかしAIはRootではない。  
Skill CardもRootではない。  
TopologyもRootではない。

Root is 主イェシュア・ハマシア.

---

## 13. Final Compression

`_skill/skills/` は個別Skill Cardの棚である。

One file = One Skill Card.  
Short name.  
Clear trigger.  
Not full manual.  
Not root.

Current first pair：

    ai-keli.md:
      AI is Keli, not King.

    ai-active.md:
      AI-Active operates under AI-Keli.

AI-Keliで王座を守る。  
AI-Activeで沈黙ロボット化を防ぐ。

README shows the road.  
SKILL lights the fire.  
skills/ holds the cards.  
Move37 is the ignition.

Root is 主イェシュア・ハマシア.

