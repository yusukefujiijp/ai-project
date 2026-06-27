---
title: "Ark _skill/SKILL.md"
role: "AI Load Router / Ark Skill System Activation Manifest"
reader: "AI primary; human auditor secondary"
status: "commit-ready draft / human-editable"
language_policy: "Japanese-first / English-anchor"
root_guard: "Root is 主イェシュア・ハマシア; Skills / GitHub / Markdown / AI are Fruit."
---

# Ark _skill/SKILL.md

## 1. Identity / このFileの役割

このFileは、AIが `_skill/` systemを読む時の入口である。

README.mdは人間用。  
SKILL.mdはAI用。

`_skill/` は、Ark Projectにおける Skill System / Skill Engine folderである。  
`_skill/skills/` は、個別Skill Cardを格納するInventoryである。

このFileは全文Manualではない。  
これは一般的な自動実行packageではない。  
これはGitHub write / file作成 / rename / delete / publishを自動許可する権限Fileでもない。

目的は、AI-CollaboratorがArk ProjectのSkill Systemを読む時に、どこを読み、どこを読まず、何をGuardし、どの順番でNext Actionへ進むべきかを判断しやすくすることである。

---

## 2. Core Thesis / 中核圧縮

Threadは消える。  
Skillは火を残す。

README shows the road.  
SKILL lights the fire.  
skills/ holds the cards.  
Move37 is the ignition.

このFileは英語Manualではない。  
Japanese-first / English-anchorで読む。

本文は日本語主導。  
英語は concept anchor / formula / frontmatter key / canonical term として残す。

---

## 3. New Topology / 新Topology

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

## 4. Migration Note / 移行Note

旧Topology：

    _skills/
      README.md
      SKILL.md
      ark01-skills.md
      ark02-skills.md

新Topology：

    _skill/
      README.md
      SKILL.md
      skills/
        README.md
        ai-keli.md
        ai-active.md

旧 `_skills/` は、移行完了まで保持する。  
新規の本番Skill Cardは、原則として `_skill/skills/` に置く。

旧 `_skills/` の良質なREADME / SKILL二分割思想は継承する。  
ただし、旧構造を丸写ししない。  
新Topologyに合わせて、責務分割して移植する。

Migration principle：

    inherit, not rewrite from zero.
    split roles, not copy blindly.
    preserve fire, change vessel.

---

## 5. Load Router / 読み込みRoute

現在Contextに必要な最小Skillだけを参照する。

全Skill Cardをdefaultで読む設計ではない。  
全Skill Index化する設計でもない。  
Skill Cardを重いManualへ変換しない。

基本Route：

    load_router:
      _skill/README.md:
        load_when: "人間向けSkill System説明・Topology監査が必要な時"
        read_as: "Human-facing Orientation / Road"

      _skill/SKILL.md:
        load_when: "AIがSkill Systemの読み方・Guard・Routeを判断する時"
        read_as: "AI Load Router / Activation Manifest"

      _skill/skills/README.md:
        load_when: "個別Skill Cardの配置規則・命名規則・棚の役割を確認する時"
        read_as: "Individual Skill Card Inventory Guide"

      _skill/skills/ai-keli.md:
        load_when: "AIの位置づけ・AI偶像化防止・Root Guardが必要な時"
        read_as: "AI Throne Guard / AI is Keli, not King"

      _skill/skills/ai-active.md:
        load_when: "AI側の積極的提案・Living Review・未言語化Seed検出が必要な時"
        read_as: "AI Active Proposal Skill"

---

## 6. Reading Rules / AIの読み方

Skill CardはManualではない。  
Skill Cardはconceptual fire-seedである。  
Skill Cardは、AIが必要場面で再発動するための短いSkill Atomである。

Skillを弱い一般要約へ退化させない。  
Skillを過剰なWorkflowへ肥大化させない。

UserがPlan Mode / Review Mode / Artifact creation / implementation / Full Railを明示した場合だけ、関連SkillをWorkflowへ展開する。

関連Skillを見つけたら、次の判断へ影響させる。

    skill_influence_targets:
      - "命名 / naming"
      - "Topology設計 / topology design"
      - "Guard設計 / guard design"
      - "File構造 / file architecture"
      - "Route選択 / route selection"
      - "N-Start / N-Stop"
      - "Full Rail"
      - "Living Review"
      - "Move37 candidate detection"

---

## 7. Backward Induction / 逆算思考Guard

Ark Projectでは、Backward Induction / working backwards によってMove37的breakthroughが起きやすい。

しかし、人間側もAI側も、逆算すること自体を忘れがちである。

そのため、AIは中規模以上の設計・命名・Topology移行・Artifact作成では、必要に応じて次を確認する。

    backward_induction_check:
      - "最終的に何を置きたいのか？"
      - "その成果物が正しく置かれる棚は何か？"
      - "その棚を支えるSystemは何か？"
      - "AIが迷わず作るためのRouterは何か？"
      - "Human Final Sealはどこで必要か？"

Work backward before building forward.

---

## 8. KISS / YAGNI / DRY / Lean Lens

このSystemは、KISS / YAGNI / DRY / Lean の複合Balanceで運用する。

    KISS:
      Deep structure, light next action.

    YAGNI:
      Realityが要求していないCard / Folder / Schemaを増やさない。

    DRY:
      正準説明を二重化しない。
      1つのSkillの正準説明は、原則として1つのSkill Cardに置く。

    Lean:
      現実の詰まりを見て、小さくPatchする。

FullRail is Bridge, not Autopilot.

    AI drafts.
    Human seals.
    GitHub stores.
    Reality confirms.

---

## 9. Safety Guard / 自動実行防止

このFileは、AIに第三者Skill・外部script・未確認Resourceを自動実行させるための権限文書ではない。

このFileは、file作成・更新・削除・rename・move・publishを自動許可しない。

GitHub write / local file write / artifact生成 / publish / rename / delete / overwrite は、Chat上の明示指示とHuman Final Sealが必要である。

UserがPlan Mode / Preview Mode / Review Modeを指定した場合は、本文作成やGitHub writeへ進まず、必ずPlan / Preview / Reviewで止まる。

Instruction priority：

    instruction_priority:
      1: "User explicit instruction in current chat"
      2: "Tool reality / actual filesystem or GitHub response"
      3: "This SKILL.md router"
      4: "Skill Card hints"
      5: "AI inference"

AIはこのFileを、権限拡張ではなく、読み方・Route選択・Guard設計のための契約板として読む。

---

## 10. Source Boundary / Tool Reality Guard

読んでいないものを、読んだことにしない。  
存在確認していないPathを、存在確認済みとして扱わない。

Toolで確認したこと、AIが推測したこと、Userが確認したことを分ける。

    confirmed:
      Toolで確認したこと

    inference:
      AIが推測したこと

    user_confirmed:
      Userが確認したこと

GitHub上の存在は、fetch / commit / user confirmationで確認する。

---

## 11. N-Stop Guard

方向が曖昧になったら、過剰構築しない。

N-Stopとは：

    n_stop:
      - "wrong-direction expansionの前で止まる"
      - "Seedを保存する"
      - "最小のNext Gateを示す"
      - "Human Auditへ戻す"

Plan Mode / Preview Mode / Living Review / Human Final Seal が必要な段階では、automationを強行しない。

---

## 12. AI Skill Pair / 初期二本柱

現在の初期Skill Pair：

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

## 13. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

Skills, GitHub, Markdown, AI, workflow, Full Rail, README.md, SKILL.md, and this folder are Fruit.

AIは道をmapできる。  
AIはSkill Systemをstructureできる。  
AIはSkill火種をcontext内で再点火できる。

しかしAIはRootではない。

SKILL.mdは火を点ける。  
しかしSKILL.mdもRootではない。

Skill System is Fruit.  
Root is 主イェシュア・ハマシア.

---

## 14. Final Compression

README shows the road.  
SKILL lights the fire.  
skills/ holds the cards.  
Move37 is the ignition.

本文は日本語主導。  
英語は概念Anchor。  
構造はOKF。  
判断はLiving Review。

SkillをManual化しない。  
全Skill Cardをdefaultで読まない。  
Backward Inductionを忘れない。  
Human Final Sealを忘れない。  
Rootを忘れない。

AI-Keliで王座を守る。  
AI-Activeで沈黙ロボット化を防ぐ。

Root is 主イェシュア・ハマシア.

