# Ark _skill/

## 1. What this folder is / このfolderについて

`_skill/` は、Ark Projectにおける Skill System / Skill Engine folderである。

このfolderは、通常のManual置き場ではない。  
Script実行folderでもない。  
Agent自動実行packageでもない。  
GitHub write / file作成 / rename / delete / publishを自動許可する権限folderでもない。

目的は、Ark Projectで発見された重要なSkill火種を、Future AIとHumanが後から再読・再起動・再利用できるように、短く、明確に、正しいTopologyの中へ保存することである。

特に、設計・Review・命名・Topology構築・Guard設計・Workflow補正・Move37 breakthrough ignition・Artifact作成の局面で、過去Threadの火が再び働くようにする。

---

## 2. Why _skill/ exists / なぜ_skill/が必要か

Ark Projectでは、良い内容を作る前に、良い内容が迷わず住める場所を先に作る。

これは Topology-First である。

Topology-Firstとは、本文作成より先に、Repository内の場所・責務・人間用入口・AI用入口・個別Card置き場・移行元Sourceを定め、AIが迷わず再起動できる地形を作るArk Project設計Skillである。

中身を先に増やすと、AIは良い文章を出せても、正しい場所へ置けない可能性がある。

そのため、`_skill/` は単なるfolderではなく、Skill System全体の地形である。

---

## 3. Simple split / 最小分離

README.mdは人間用。  
SKILL.mdはAI用。  
skills/は個別Skill Cardの棚。

README shows the road.  
SKILL lights the fire.  
skills/ holds the cards.  
Move37 is the ignition.

    README.md = Human-facing Orientation / Skill System Road
    SKILL.md  = AI Load Router / Skill System Activation Manifest
    skills/   = Individual Skill Card Inventory

---

## 4. New Topology / 新Topology

Canonical topology：

    _skill/
      README.md
      SKILL.md
      skills/
        README.md
        ai-keli.md
        ai-active.md
        ai-journaling.md

Role split：

    _skill/README.md
      = Human-facing Orientation / Skill System Road

    _skill/SKILL.md
      = AI Load Router / Skill System Activation Manifest

    _skill/skills/README.md
      = Individual Skill Card Inventory Guide

    _skill/skills/*.md
      = Individual Ark Skill Cards

Current first pair：

    _skill/skills/ai-keli.md
      = AI Throne Guard / AI is Keli, not King.

    _skill/skills/ai-active.md
      = AI Active Proposal Skill / AI-Active operates under AI-Keli.

Current application skill：

    _skill/skills/ai-journaling.md
      = Evidence-First Reversible Reflection + One Open Slot.

---

## 5. Migration from _skills/ / 旧Topologyからの移行

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
        ai-journaling.md

旧 `_skills/` は、移行完了まで保持する。  
新規の本番Skill Cardは、原則として `_skill/skills/` に置く。

旧 `_skills/` の良質なREADME / SKILL二分割思想は継承する。  
ただし、旧構造を丸写ししない。  
新Topologyに合わせて、責務分割して移植する。

Migration principle：

    inherit, not rewrite from zero.
    split roles, not copy blindly.
    preserve fire, change vessel.

旧い火を消さず、新しい器へ移す。

---

## 6. Backward Induction / 逆算思考

Ark Projectでは、Backward Induction / working backwards によってMove37的breakthroughが起きやすい。

しかし、逆算すること自体を忘れがちである。

そのため、中規模以上の設計・命名・Topology移行・Artifact作成では、最初に次を確認する。

    backward_induction_check:
      - "最終的に何を置きたいのか？"
      - "その成果物が正しく置かれる棚は何か？"
      - "その棚を支えるSystemは何か？"
      - "AIが迷わず作るためのRouterは何か？"
      - "Human Final Sealはどこで必要か？"

Work backward before building forward.

---

## 7. File roles / 各Fileの役割

### README.md

人間用の案内板である。

`_skill/` が何のためにあり、各FileとFolderがどう分かれているかを、人間が短時間で理解するために読む。

Role anchor：

    Human-facing Orientation / Skill System Road

### SKILL.md

AI用の起動Manifestである。

Future AIは `SKILL.md` を読み、どのSkill Cardを読むべきか、どのように読むべきか、何をしてはいけないかを判断する。

Role anchor：

    AI Load Router / Skill System Activation Manifest / Guard

### skills/

個別Skill CardのInventoryである。

`ai-keli.md`、`ai-active.md`、`ai-journaling.md` など、実際に再発動可能なArk Project Skill Cardを置く。

Role anchor：

    Individual Skill Card Inventory

### skills/README.md

個別Skill Card置き場の案内板である。

One file = One Skill Card。  
Skill CardはFull Manualではない。  
Skill Cardは、AIとHumanが後から再発動できる短いSkill Atomである。

Role anchor：

    Individual Skill Card Inventory Guide

---

## 8. KISS / YAGNI / DRY / Lean

`_skill/` は、KISS / YAGNI / DRY / Lean の複合Balanceで運用する。

    KISS:
      Deep structure, light next action.

    YAGNI:
      Realityが要求していないCard / Folder / Schemaを増やさない。

    DRY:
      正準説明を二重化しない。
      1つのSkillの正準説明は、原則として1つのSkill Cardに置く。

    Lean:
      現実の詰まりを見て、小さくPatchする。

Principle is Bridge, not Autopilot.

---

## 9. Human audit guide / 人間用Review観点

`_skill/` を見直す時は、次を確認する。

- README.mdは人間に読みやすいか。
- SKILL.mdはAI用Load Routerとして鋭いか。
- SKILL.mdが全Skill Indexへ肥大化していないか。
- skills/README.mdが個別Skill Card棚の規則を短く示しているか。
- Skill CardがFull Manual化していないか。
- One file = One Skill Card が守られているか。
- filenameが lowercase-kebab-case になっているか。
- Backward Induction / working backwards が必要場面で発火しているか。
- AI-Keliが王座Guardとして機能しているか。
- AI-Activeが命令待ちロボット化防止として機能しているか。
- AI-JournalingがHuman Realityを起点に一問と余白を開いているか。
- AI Open Slotが義務化・固定Taxonomy化していないか。
- Guard-to-Artifact Balanceが守られているか。
- Root / Fruit Guardが弱まっていないか。

---

## 10. Source Boundary / Tool Reality

このfolderを扱う時は、確認済みのことと推測を分ける。

読んでいないFileを、読んだことにしない。  
存在確認していないPathを、存在確認済みとして扱わない。

    confirmed / inference / user-confirmed

詳細なAI側運用は `SKILL.md` に従う。

---

## 11. Non-goals / やらないこと

`_skill/` を次のものにしない。

- full procedure manual
- script execution layer
- agent automation package
- full Thread transcript archive
- long summary collection
- GitHub write permission layer
- Human Final Sealの代替
- Rootの代替

`_skill/` は、AIを勝手に動かすための仕組みではない。  
Skillを再読・再起動・再利用しやすくするための構造である。

---

## 12. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

Skills, SeedSkills, GitHub, Markdown, AI, README.md, SKILL.md, skills/, and this folder are Fruit.

AIは構造化を助けることができる。  
AIはSkillを整理できる。  
AIは文脈内で火種を再点火できる。  
AIはBackward Inductionによって、よりスマートなRouteを提案できる。

しかしAIはRootではない。

README.mdもSKILL.mdもRootではない。  
Skill SystemもRootではない。  
FormatもRootではない。

Rootは主イェシュア・ハマシアである。

---

## 13. Final Compression

README.mdは人間用。  
SKILL.mdはAI用。  
skills/はSkill Cardの棚。

README shows the road.  
SKILL lights the fire.  
skills/ holds the cards.  
Move37 is the ignition.

Threadは消える。  
Skillは火を残す。

Topologyを先に切る。  
Backward Inductionで逆算する。  
AI-Keliで王座を守る。  
AI-Activeで沈黙ロボット化を防ぐ。  
AI-Journalingで一問と余白を開く。  
Guardで止まらず、Artifactへ通す。

本文は日本語主導。  
英語は概念Anchor。  
構造はOKF。  
判断はLiving Review。

Root is 主イェシュア・ハマシア.
