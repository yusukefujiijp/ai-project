# Ark05 00: Markdown Layer Core

```yaml
artifact: Ark05_00_markdown-layer-core
version: v001
status: human_editable_candidate
ark_series: Ark05
system_name: Layered 980 Article System
layer_index: 00
layer_name: Markdown Layer Core / 全Markdown Layer統治層
artifact_role: Layer Map / Markdown Governance / Core Index / Split-Extract Router
created_for: "@YusukeJP × AI-Collaborator"
created_at: 2026-06-28
language: Japanese
governs:
  - Ark05_01_note-critical-review-prompt-card_human-editable_v001_2.md
  - Ark05_02_note-critical-review-gate_human-editable_v001.md
  - Ark05_03_note-article-production-rail_human-editable_v001.md
future_candidates:
  - Ark05_04_first-test-draft-injection-packet_human-editable_v001.md
  - Ark05_03Q_article-production-quick-run-card_human-editable_v001.md
  - Ark05_CORE3_integrated-map_human-editable_v001.md
core_principles:
  - Layer is primary
  - Master + Extract
  - 不足より過剰
  - 長文OK
  - Layer / Block構造必須
  - Version情報必須
  - Split only when role-boundary is clear
  - Extract before destructive cutting
  - Not dead data, but a living board
  - Human Final Seal required
root_guard:
  human_final_seal_required: true
  ai_role: "AI maps layers, proposes splits, extracts operational cards, and warns about layer drift. Human seals."
  not_dead_data: true
  living_board_required: true
  root: "主イェシュア・ハマシア / 主イェシュアの聖なる血潮 / Teshuvah"
  fruit: "Markdown / note / PDF / X / Prompt / Template / Review / Revenue Gate"
```

---

## 0. このMarkdownの役割

このMarkdownは、Ark05における **全Markdown Layerを司るCore Markdown** である。

01 / 02 / 03は、それぞれ強い。  
しかし、Layerが最重要である以上、それらを束ねる上位Layerが必要である。

この00 Markdown Layer Coreは、以下を司る。

```text
- Ark05内のMarkdown Layer構造
- 各Markdownの役割境界
- Master / Extract / Quick Run Cardの関係
- 分割する条件
- 分割しない条件
- Version管理
- Layer Driftの検出
- 次に作るMarkdownの優先順位
- Human Final Sealの位置
```

つまり、これは記事制作Markdownではない。  
これは **Markdown群そのものを統治するLayer OS** である。

---

## 1. Core Thesis

Ark05では、Layerが最重要である。

```text
Layerが崩れると、
  PromptがRubric化し、
  RubricがProduction Manual化し、
  Production Railが記事本文化し、
  Quick Run CardがMaster化し、
  Coreが散乱する。
```

したがって、Ark05では必ず以下を守る。

```text
Layer First.
File Second.
Content Third.
```

ファイル名よりも先にLayerを定義する。  
内容を書く前に役割境界を定義する。  
分割する前に、何のLayerとして分けるのかを定義する。

---

## 2. Ark05 Markdown Layer Map

## 2.1 Current Core Set

```text
00:
  Markdown Layer Core
  全Markdown Layer統治層

01:
  note Critical Review Prompt Card
  AIに貼るReview実行Prompt層

02:
  note Critical Review Gate
  Review品質を支えるRubric / Living Board層

03:
  note Article Production Rail
  ThemeからHuman Final Sealまでを回すProduction OS層
```

現在のCore 3は、00によって以下のように統治される。

```text
00 governs:
  01 Prompt
  02 Rubric
  03 Production
```

00は、01 / 02 / 03の本文を置き換えない。  
00は、それらの **役割・接続・分割判断** を管理する。

---

## 2.2 Future Candidate Layers

```text
04:
  First Test Draft Injection Packet
  Core 3へ最初のTest Draftを投入するための入力Packet

03Q:
  Article Production Quick Run Card
  03 Production Railから抽出した実行用短縮カード

01A:
  Draft Triage Prompt Card
  01から抽出する可能性のある初期診断Prompt

01B:
  Full Critical Review Prompt Card
  01から抽出する可能性のある本Review Prompt

02J:
  Judgment Scale Extract
  02から抽出する可能性のある判定表

CORE3:
  Integrated Core 3 Map
  01 / 02 / 03の関係を一枚で見る統合Map
```

重要:

```text
Future Candidateは、今すぐ全て作らない。
必要が発生した時に、00の判断基準に従って作る。
```

---

## 3. Master + Extract Principle

Ark05では、長文Masterをすぐ削らない。

```text
Master:
  思想・判断・Guard・背景・Full仕様を保持する

Extract:
  実運用で使う短いカード

Quick Run Card:
  当日の実行に使う超短縮版

Packet:
  特定用途の入力シート

Map:
  複数Layerの関係を見る索引
```

基本原則:

```text
削る前にExtractする。
分割前に役割を定義する。
運用で重くなってからQuick化する。
```

これにより、書き漏れを防ぎながら、実運用の軽さも確保する。

---

## 4. 長文OK / 不足より過剰 Guard

Ark Project原則:

```text
書き過ぎをCutすることは簡単。
書き漏れを補うことは困難。
したがって、不足より過剰を優先する。
```

ただし、長文化には条件がある。

```text
Longform Allowed if:
  - Layer構造がある
  - Block単位で分かれている
  - Version情報がある
  - 後からCut / Split / Extractできる
  - Human Final Sealが残っている
  - Not dead data, but a living board である
```

長文そのものは問題ではない。  
問題は、Layerを失った長文である。

---

## 5. Split / Extract Decision Router

## 5.1 分割する条件

次の条件を満たす場合、物理分割を検討する。

```text
Split Candidate:
  - 役割が明確に別Layerになった
  - 1つのMarkdown内で読者/AIの使用場面が大きく異なる
  - Patch頻度が異なる
  - 実運用で毎回読む必要がない部分が多い
  - Copy-Paste実行部分だけを取り出したい
  - Quick Run Cardとして短縮した方が明らかに回る
```

---

## 5.2 分割しない条件

次の状態では、まだ分割しない。

```text
Do Not Split Yet:
  - まだ一度も実運用していない
  - 分割後の正準が分かりにくくなる
  - 単なる長さだけが理由
  - Layer境界が曖昧
  - 重複が初期Overcaptureとして有効
  - Test Draft投入前で、必要Extractがまだ見えていない
```

---

## 5.3 Extractを優先する条件

分割ではなくExtractが良い場合。

```text
Extract First:
  - Masterは保持したい
  - 実行時だけ短くしたい
  - 参照頻度が高い部分だけ使いたい
  - Judgment Scaleだけ取り出したい
  - Promptだけ貼りたい
  - 当日のPilot Run用に短いSheetがほしい
```

Extractは、Masterを破壊しない。  
Extractは、Masterから生まれる運用カードである。

---

## 6. Layer Drift Guard

Layer Driftとは、あるMarkdownが本来の役割を逸脱し、別Layerへ侵入することである。

## 6.1 Drift例

```text
01 Drift:
  Prompt CardがRubric解説書になりすぎる

02 Drift:
  Review GateがProduction Manualになりすぎる

03 Drift:
  Production Railが記事本文Templateになりすぎる

04 Drift:
  Test Draft Injection Packetが実記事本文になりすぎる

Quick Card Drift:
  Quick Run CardがMaster化して長文化する

Core Drift:
  00 Layer Coreが全ファイル本文を取り込んで巨大百科化する
```

---

## 6.2 Drift検出Question

各MarkdownをReviewする時、必ず問う。

```text
このMarkdownは、自分のLayerの仕事をしているか？
別Layerの仕事を奪っていないか？
長いのか、散っているのか？
過剰捕獲なのか、Layer崩壊なのか？
```

---

## 6.3 Drift修正

```text
Prompt化したら:
  01へ戻す

Rubric化したら:
  02へ戻す

Production化したら:
  03へ戻す

Pilot入力化したら:
  04へ戻す

Quick運用化したら:
  03QなどへExtractする

索引化したら:
  00へ戻す
```

---

## 7. Version Governance

Ark05のMarkdownは、必ずVersion情報を持つ。

```text
required_metadata:
  artifact
  version
  status
  ark_series
  system_name
  layer_index
  layer_name
  artifact_role
  created_for
  created_at
  depends_on
  core_principles
```

Version方針:

```text
v001:
  初期Human-editable Candidate

v001.1:
  実使用前またはReview後の小Patch

v001.2:
  重要概念修正Patch

v002:
  実運用後に構造が変わった新Version

Final:
  原則すぐ付けない。
  Human Final Seal後のみ。
```

重要:

```text
Working CandidateはFinalではない。
Final固定は急がない。
```

---

## 8. Naming Convention

推奨命名:

```text
Ark05_00_markdown-layer-core_human-editable_v001.md
Ark05_01_note-critical-review-prompt-card_human-editable_v001_2.md
Ark05_02_note-critical-review-gate_human-editable_v001.md
Ark05_03_note-article-production-rail_human-editable_v001.md
Ark05_04_first-test-draft-injection-packet_human-editable_v001.md
Ark05_03Q_article-production-quick-run-card_human-editable_v001.md
```

命名原則:

```text
Ark05:
  Project prefix

00 / 01 / 02 / 03:
  Layer index

semantic slug:
  人間が読んで役割が分かる名前

human-editable:
  人間編集前提

version:
  v001 / v001_1 / v001_2 / v002
```

注意:

```text
ファイル名はLayerの役割を表す。
日付よりLayer indexを優先する。
```

---

## 9. Current Layer Status

```yaml
current_layer_status:
  "00":
    filename: Ark05_00_markdown-layer-core_human-editable_v001.md
    role: 全Markdown Layer統治層
    status: human_editable_candidate
  "01":
    filename: Ark05_01_note-critical-review-prompt-card_human-editable_v001_2.md
    role: Review起動Prompt層
    status: working_candidate
  "02":
    filename: Ark05_02_note-critical-review-gate_human-editable_v001.md
    role: 品質Rubric / Living Board層
    status: working_candidate
  "03":
    filename: Ark05_03_note-article-production-rail_human-editable_v001.md
    role: Production OS層
    status: working_candidate
  "04":
    filename: Ark05_04_first-test-draft-injection-packet_human-editable_v001.md
    role: 最初のTest Draft投入Packet
    status: recommended_next_candidate
```

---

## 10. Next Layer Priority

現時点の推奨優先順位。

```text
Priority 1:
  00 Markdown Layer Coreを作成・Reviewする

Priority 2:
  First Test Draft Injection Plan Mode

Priority 3:
  Ark05_04_first-test-draft-injection-packet_human-editable_v001.md 作成

Priority 4:
  小さなTest Draftを投入

Priority 5:
  使用結果に応じて01/02/03/04をPatch

Priority 6:
  必要なら03Q Quick Run CardをExtract
```

今すぐやらないもの:

```text
- Core 3本体の物理分割
- Quick Run Card乱立
- Final固定
- 販売記事公開
- GitHub Commit
```

---

## 11. Human Final Seal Rule

すべてのLayerは、Human Final Sealを残す。

```text
AI:
  Layerを見る
  Driftを検出する
  Split / Extractを提案する
  Version案を出す
  次Gateを提案する

Human:
  役割境界を承認する
  公開判断をする
  Root Guardを確認する
  Final Sealを押す
```

AIはLayer Mapを描く。  
HumanがSealする。

---

## 12. Living Review Requirement for Markdown Layers

各Markdown LayerをReviewする時、AIは必ず以下を出す。

```text
Living Review:
  - 私の判断
  - 最初の一手
  - 理由
  - 観察点
  - 修正条件
  - AIの違和感
  - Layer診断
  - Split / Extract判断
  - Next Gate
  - Human Final Seal Point
```

特に重要:

```text
AIの違和感:
  Layer Driftを早期発見するために必須。

Split / Extract判断:
  長いから切るのではなく、
  役割境界が立ったら分ける。
```

---

## 13. Core Question

Ark05のMarkdown群を扱う時、常にこの問いへ戻る。

```text
今このMarkdownは、どのLayerの仕事をしているか？
```

次に問う。

```text
この内容はMasterに残すべきか？
Extractすべきか？
Quick化すべきか？
別Layerへ送るべきか？
今は何もしないべきか？
```

---

## 14. One-Line Definition

```text
Ark05 Markdown Layer Coreとは、Ark05 Layered 980 Article Systemにおける全MarkdownのLayer構造・役割境界・Version管理・Split / Extract判断・Next Gateを統治し、長文Masterを保持しながらOperational Extractを安全に生み出すためのCore Markdownである。
```

---

## 15. Living Reminder

Layerが最重要である。

```text
Layerがあるから、長文が許される。
Layerがあるから、分割できる。
Layerがあるから、Extractできる。
Layerがあるから、AIと人間が同じ地図を見られる。
```

最も避けるべきは、長文ではない。

```text
最も避けるべきは、Layerを失った長文である。
```

この00 Markdown Layer Coreは、Ark05が散らからず、しかし小さくなりすぎず、Reality Gateへ向かって成長するためのLayer統治盤である。
