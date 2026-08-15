# Ark05 04: First Test Draft Injection Packet

```yaml
artifact: Ark05_04_first-test-draft-injection-packet
version: v001
status: human_editable_candidate
ark_series: Ark05
system_name: Layered 980 Article System
layer_index: 04
layer_name: First Test Draft Injection Packet / 初回Test Draft投入層
artifact_role: Pilot Input Packet / Test Draft Gate / Core 3 Validation Sheet
created_for: "@YusukeJP × AI-Collaborator"
created_at: 2026-06-28
language: Japanese
depends_on:
  - Ark05_00_markdown-layer-core_human-editable_v001.md
  - Ark05_01_note-critical-review-prompt-card_human-editable_v001_2.md
  - Ark05_02_note-critical-review-gate_human-editable_v001.md
  - Ark05_03_note-article-production-rail_human-editable_v001.md
core_principles:
  - Layer First
  - Test Draft before Public Article
  - Public false
  - Sales Judgment false
  - Draft Triage first
  - Full Critical optional preview
  - Core 3 Validation
  - Not dead data, but a living board
  - Human Final Seal required
root_guard:
  human_final_seal_required: true
  ai_role: "AI prepares the pilot input, drafts test material, reviews, observes friction, and proposes patches. Human seals."
  not_dead_data: true
  living_board_required: true
  root: "主イェシュア・ハマシア / 主イェシュアの聖なる血潮 / Teshuvah"
  fruit: "Test Draft / note / PDF / X / Prompt / Template / Review / Revenue Gate"
```

---

## 0. このMarkdownの役割

このMarkdownは、Ark05 Core 3を **机上System** から **実験System** へ移すための、最初のTest Draft投入Packetである。

04は記事本文ではない。  
04は完成Draftでもない。  
04は販売記事でもない。

04は、最初のTest DraftをCore 3へ流す前に、以下を固定するためのPilot入力Layerである。

```text
- Draft Type
- Public Status
- Sales Judgment
- Theme
- Reader Pain
- Article Kernel
- Draft Scope
- Gate Path
- Success Condition
- Stop Condition
- Harvest Condition
```

00がLayerを統治する。  
01がReviewを起動する。  
02がReview基準を支える。  
03がProduction Railを回す。  
04は、そのRailへ最初のTest Draftを投入する。

---

## 1. Purpose

First Test Draft Injection Packetとは、Ark05 Core 3を実際に検証するために、最初の非公開Test Draftの条件を定義するPilot入力Packetである。

目的は、販売記事を完成させることではない。

目的は、以下を検証することである。

```text
- 01 Prompt Cardは使いやすいか
- 02 Critical Review Gateは判定に使えるか
- 03 Article Production Railは実際に回るか
- Draft Triageは初期診断として機能するか
- Structural Repairへ自然につながるか
- どのLayerが重いか
- どのLayerをPatchすべきか
```

---

## 2. Boundary

## 2.1 04 is

```text
04 is:
  - Pilot Input Packet
  - Test Draft投入条件
  - Core 3 Validation Sheet
  - 非公開検証の入口
  - First Runの制約定義
```

## 2.2 04 is not

```text
04 is not:
  - note記事本文
  - 完成Draft
  - 販売記事
  - Review Rubric本体
  - Production Manual本体
  - Quick Run Card
  - X投稿本文
  - PDF本文
```

04が記事本文化したら、Layer Driftである。  
04がProduction Manual化したら、03へ戻す。  
04がRubric化したら、02へ戻す。  
04がPrompt本文化したら、01へ戻す。

---

## 3. First Test Draft Default Setting

最初のTest Draftは、以下をDefaultとする。

```yaml
draft_type: Test Draft
public: false
sales_judgment: false
purpose: Core 3 validation
target_quality_judgment: none_yet
primary_review: Draft Triage Review
secondary_review: Full Critical Review Preview optional
human_final_seal: required_for_next_gate_not_publication
```

重要:

```text
最初のTest Draftでは、販売判断をしない。
最初のTest Draftでは、公開を目指さない。
最初のTest Draftでは、Core 3が回るかを見る。
```

---

## 4. Recommended First Theme

## 4.1 Theme

最初のTest Draft Themeは、以下を推奨する。

```text
500円記事を書くつもりで書くと、500円以下になる。
だから販売価格は500円でも、内部品質基準は980円に置く。
```

---

## 4.2 Why this Theme

このThemeが最適な理由。

```text
- Ark05の中核思想そのもの
- Internal 980 / External 500を検証できる
- Buyer Valueを作りやすい
- Template化しやすい
- X投稿へ分解しやすい
- PDF章にも伸びる
- 01 / 02 / 03を自然に使える
- 外部調査に依存しすぎない
- 初回Test Draftとして重すぎない
```

---

## 4.3 Alternative Themes

必要に応じて、以下も候補とする。

```text
Candidate B:
  AI記事はPromptだけでは生きない。
  Review GateとHuman Final Sealが必要である。

Candidate C:
  売上はコントロールできない。
  だから週1本の出荷とReview品質だけを支配する。
```

ただし、v001ではCandidate AをDefaultとする。

---

## 5. Reader Pain

今回のReader Painは以下。

```text
note有料記事を書きたいが、500円で売る品質基準が分からない。

AIで記事を書こうとすると、きれいだが薄い一般論になりやすい。

売れる保証はできないが、少なくとも読者に誠実な価値を返したい。

無料記事と有料記事の差を、文字数ではなく構造価値で判断したい。

最初から980円で売る勇気はないが、500円販売でも品質だけは980円基準で作りたい。
```

---

## 6. Article Kernel

今回のArticle Kernelは以下。

```text
500円記事を書くつもりで書くと、500円以下になる。
だから販売価格は500円でも、内部品質基準は980円に置く。
```

補助Kernel:

```text
500円は販売価格であり、品質天井ではない。

980円品質候補とは、長い記事ではなく、読者が保存・再利用・判断・行動できる構造を持つ記事である。

AI記事は、DraftよりReview Gateで差がつく。
```

---

## 7. Draft Scope

## 7.1 Scope

```text
Draft Scope:
  完成記事ではなく、Review可能な素材Draftを作る。
```

## 7.2 Target Length

```text
Target Length:
  長文OK。
  ただしBlock構造必須。
```

## 7.3 Required Blocks

```text
Required Blocks:
  - Title Candidate
  - Reader Pain
  - Core Thesis
  - Why Internal 980
  - Buyer Value
  - Simple Template
  - Next Action
  - Integrity Note
```

## 7.4 Optional Blocks

```text
Optional Blocks:
  - Before / After
  - AI-Human Collaboration
  - Failure Mode
  - X Post Kernel
  - PDF Chapter Seed
  - Prompt Card Seed
```

---

## 8. Gate Path

## 8.1 Default Gate Path

初回は軽く回す。

```text
Gate Path:
  1. Entry Gate
  2. Theme / Reader Pain Gate
  3. Article Kernel Gate
  4. Draft Generation Gate
  5. Draft Triage Review Gate
  6. Structural Repair Gate
```

## 8.2 Optional Gate

```text
Optional:
  Full Critical Review Preview
```

Full Critical Reviewは、初回では必須ではない。  
まずDraft Triageで、Core 3が動くか見る。

---

## 9. Use of Core Files

## 9.1 Use 00

00はLayer確認に使う。

```text
Use:
  Ark05_00_markdown-layer-core_human-editable_v001.md

Purpose:
  04が記事本文化していないか
  Layer Driftが起きていないか
  Split / Extract判断が必要か
```

---

## 9.2 Use 01

01はDraft Triage Reviewに使う。

```text
Use:
  Ark05_01_note-critical-review-prompt-card_human-editable_v001_2.md

Prompt:
  Draft Triage Review Prompt
```

---

## 9.3 Use 02

02はReview判断の背景に使う。

```text
Use:
  Ark05_02_note-critical-review-gate_human-editable_v001.md

Purpose:
  Buyer / Skeptic / Evidence / Scale / Integrity / Living Reviewの基本判断
```

---

## 9.4 Use 03

03はGate Pathに使う。

```text
Use:
  Ark05_03_note-article-production-rail_human-editable_v001.md

Purpose:
  Entry → Theme → Kernel → Draft → Triage → Repairの流れを回す
```

---

## 10. Pilot Input Template

次回、Test Draftを作る時は、このTemplateを埋める。

```yaml
pilot_input:
  draft_type: Test Draft
  public: false
  sales_judgment: false
  theme: "500円記事を書くつもりで書くと、500円以下になる。だから内部基準は980円に置く。"
  reader_pain:
    - "note有料記事を書きたいが、品質基準が分からない"
    - "AI記事がきれいだが薄い一般論になりがち"
    - "500円販売でも読者に誠実な価値を返したい"
  article_kernel: >
    500円記事を書くつもりで書くと、500円以下になる。
    だから販売価格は500円でも、内部品質基準は980円に置く。
  required_blocks:
    - Title Candidate
    - Reader Pain
    - Core Thesis
    - Why Internal 980
    - Buyer Value
    - Simple Template
    - Next Action
    - Integrity Note
  gate_path:
    - Entry Gate
    - Theme / Reader Pain Gate
    - Article Kernel Gate
    - Draft Generation Gate
    - Draft Triage Review Gate
    - Structural Repair Gate
  optional_gate:
    - Full Critical Review Preview
  success_condition:
    - ThemeがReader Painに接続した
    - Article Kernelが一文で立った
    - Test Draft素材が出た
    - Draft Triageで最大の詰まりが見えた
    - Core 3のどこが重いか観察できた
  stop_condition:
    - 記事本文を完成させようとして重くなる
    - 販売判断へ進みそうになる
    - Themeが広がりすぎる
    - Reader Painが消える
  harvest:
    - 01 Prompt Cardは使いやすかったか
    - 02 Review Gateは判定しやすかったか
    - 03 Production Railは回ったか
    - 04 Packetは入力として十分だったか
    - Quick Run Cardが必要か
    - どのLayerをPatchすべきか
```

---

## 11. Success Condition

今回のPilotが成功したと言える条件。

```text
Success:
  - ThemeがReader Painに接続した
  - Article Kernelが一文で立った
  - Test Draft素材が出た
  - Draft Triageで最大の詰まりが見えた
  - 01 / 02 / 03のどこが重いか観察できた
  - 次にPatchすべきLayerが見えた
  - 03Q Quick Run Cardが必要か判断材料が出た
```

重要:

```text
売れたら成功ではない。
公開できたら成功でもない。
初回Pilotの成功は、Core 3の実運用摩擦が見えることである。
```

---

## 12. Stop Condition

止める条件。

```text
Stop if:
  - 記事本文を書こうとして重くなる
  - 販売判断へ進みそうになる
  - Full Critical Reviewで止まりそうになる
  - Themeが広がりすぎる
  - Reader Painが消える
  - 04が記事本文化する
  - Human Final Sealが曖昧になる
```

止まることは失敗ではない。  
止まった位置をHarvestできれば成功である。

---

## 13. Harvest Condition

Pilot後に回収するもの。

```text
Harvest:
  - 01 Prompt Cardは使いやすかったか
  - 02 Review Gateは判定しやすかったか
  - 03 Production Railは回ったか
  - 04 Packetは入力として十分だったか
  - Quick Run Cardが必要か
  - Draft Triageは軽かったか重かったか
  - Full Critical Previewは必要だったか
  - どのLayerをPatchすべきか
  - First Themeは正しかったか
  - 次のTest Draft Theme候補は何か
```

Harvestは反省ではない。  
Harvestは、System改善の素材である。

---

## 14. Human Final Seal Point

04の時点でHumanがSealするのは、公開判断ではない。

HumanがSealするのは以下。

```text
- このThemeでTest Draftへ進んでよいか
- Public falseでよいか
- Sales Judgment falseでよいか
- Draft Triageまでを基本Gateにしてよいか
- Full CriticalをOptional Previewに留めてよいか
- 04が記事本文ではなくPacketとして機能しているか
```

---

## 15. Layer Drift Guard

## 15.1 04が記事本文化した場合

```text
Symptom:
  04内で記事本文を書き始める

Correction:
  Test Draft本文は次Gateへ送る。
  04は入力Packetへ戻す。
```

## 15.2 04が03化した場合

```text
Symptom:
  04がProduction Rail全体を書き直し始める

Correction:
  Production工程は03へ戻す。
  04は初回投入条件へ戻す。
```

## 15.3 04が02化した場合

```text
Symptom:
  04がReview Rubricを深掘りし始める

Correction:
  Rubricは02へ戻す。
  04はPilot条件へ戻す。
```

## 15.4 04が01化した場合

```text
Symptom:
  04がCopy-Paste Prompt本文になりすぎる

Correction:
  Promptは01へ戻す。
  04はPromptを使う条件だけ書く。
```

---

## 16. One-Line Definition

```text
Ark05 First Test Draft Injection Packetとは、Ark05 Core 3を机上Systemから実験Systemへ移すために、最初の非公開Test DraftのDraft Type・Theme・Reader Pain・Article Kernel・Gate Path・Success / Stop / Harvest条件を定義するPilot入力Layerである。
```

---

## 17. Living Reminder

04は、記事を書くための興奮を少し抑え、最初の一手を安全にするGateである。

```text
いきなり販売記事を書かない。
しかしSystemを磨き続けても止まらない。
小さなTest Draftを流す。
```

最初の目的は売ることではない。

```text
最初の目的は、Core 3が本当に回るかを観察することである。
```
