# Ark05 02: note Critical Review Gate

```yaml
artifact: Ark05_02_note-critical-review-gate
version: v001
status: human_editable_candidate
ark_series: Ark05
system_name: Layered 980 Article System
layer_index: 02
layer_name: Critical Review Gate / 品質評価Rubric層
artifact_role: Review Rubric / Quality Gate / Living Board
created_for: "@YusukeJP × AI-Collaborator"
created_at: 2026-06-28
language: Japanese
depends_on:
  - Ark05_01_note-critical-review-prompt-card_human-editable_v001_2.md
later_used_by:
  - Ark05_03_note-article-production-rail
core_principles:
  - Layered Overcapture Guard
  - 不足より過剰
  - 長文OK
  - Layer / Block構造必須
  - Version情報必須
  - Not dead data, but a living board
  - Human Final Seal required
root_guard:
  human_final_seal_required: true
  ai_role: "AI observes, critiques, structures, and advises. Human seals."
  not_dead_data: true
  living_board_required: true
```

---

## 0. このMarkdownの役割

このMarkdownは、Ark05 Core 3の第二層である。

```text
01:
  note Critical Review Prompt Card
  AIに貼ってReviewを起動する実行Prompt層

02:
  note Critical Review Gate
  Reviewの判断基準・品質Rubric・Living Board層

03:
  note Article Production Rail
  Draft生成からReview、修正、圧縮、X分解、HarvestまでのProduction層
```

02 Critical Review Gateは、01 Prompt Cardの背後にある **品質判断の憲法** である。

AIに何を聞くかは01が定める。  
AIが何を基準に判断するかは02が定める。  
記事制作全体の工程にどう組み込むかは03が定める。

---

## 1. Purpose

Critical Review Gateとは、note有料記事Draftを、

```text
- Buyer
- Skeptic
- Evidence
- Scale
- Integrity
- Living Review
```

の観点から検査し、**500円販売品質** と **内部980円品質候補** への距離を判定するための品質評価Gateである。

このGateの目的は、記事を裁くことではない。  
記事を壊すことでもない。  
記事を過剰に安全化して無味乾燥にすることでもない。

目的は、記事の生命力を落としている箇所を見つけ、読者に届く形へ立ち上げ直すことである。

---

## 2. System Premise

Ark05の前提は以下である。

```text
External Price:
  500円販売

Internal Quality Anchor:
  980円品質候補

Reality Gate:
  月50,000円

Rhythm:
  週1本出荷

Core Method:
  Control / Observe / Offer

AI Role:
  Strategist / Reviewer / Editor / Critic / Product Architect / Living Board

Human Role:
  実感 / 誠実性 / 祈り / 公開判断 / Final Seal
```

このGateは、単なるチェックリストではない。

```text
Not dead data, but a living board.
```

AIは、Rubricを機械的に埋めるのではなく、今このDraftがどこで生き、どこで死に、どこを直せば読者価値が立ち上がるかを判断する。

---

## 3. Layered Overcapture Guard

Ark05では、初期設計段階において **不足より過剰** を優先する。

```text
書き過ぎ:
  後でCut / Split / Extractできる

書き漏れ:
  後で発見・補完するのが難しい
```

したがって、02 Critical Review Gateでは、短くまとめることを急がない。

ただし、長文化には条件がある。

```text
Longform OK:
  - Layer構造がある
  - Block単位で編集可能
  - Version情報がある
  - 後からCut / Split / Extractできる
  - 死んだ羅列ではなくLiving Boardになっている
```

問題は長さではない。  
問題は、Layerを失った長文化である。

---

## 4. 01 / 02 / 03 Boundary

## 4.1 01 Prompt Card の領域

01の役割:

```text
- AIにそのまま貼って使う
- Draft Triage Reviewを起動する
- Full Critical Reviewを起動する
- Output Formatを指定する
- Human Final Seal Pointを出させる
```

01は **実行カード** である。

---

## 4.2 02 Critical Review Gate の領域

02の役割:

```text
- Buyer Reviewとは何かを定義する
- Skeptic Reviewとは何かを定義する
- Evidence Reviewとは何かを定義する
- Scale Reviewとは何かを定義する
- Integrity Reviewとは何かを定義する
- Living Reviewを死んだRubricにしない方法を定義する
- 500円品質 / 980円品質候補の判定基準を定義する
```

02は **品質判断のRubric / Gate / 憲法** である。

---

## 4.3 03 Production Rail の領域

03の役割:

```text
- Theme選定
- Draft生成
- Draft Triage
- 修正
- Full Critical Review
- Evidence補強
- Sales Compression
- X分解
- PDF展開
- Template Harvest
- Human Final Seal
```

03は **記事制作全体のWorkflow / Production OS** である。

---

## 5. Draft Triage Review vs Full Critical Review

## 5.1 Draft Triage Review

Draft Triage Reviewとは、初期Draftの方向違い・薄さ・最大の詰まりを早期発見するための前段Gateである。

```text
Draft Triage Review:
  初期診断
  最大の詰まり発見
  方向修正
  Full Critical Reviewへ進める状態か確認
```

重要:

```text
Draft Triage Reviewは、980円品質Reviewの代替ではない。
Draft Triage Reviewだけで有料公開判断をしてはいけない。
```

使用する場面:

```text
- 初期Draft
- Test Draft
- Calibration Article
- まだ構成が固まりきっていないPrototype
```

見ること:

```text
- このDraftは方向が合っているか
- 一番薄い箇所はどこか
- 最初に直すべき箇所はどこか
- Evidence / 実験ログ / Template / 次の一手のどれが一番不足しているか
- Full Critical Reviewへ進める状態か
```

---

## 5.2 Full Critical Review

Full Critical Reviewとは、500円販売品質と内部980円品質候補への距離を本格判定するReviewである。

```text
Full Critical Review:
  Buyer Review
  Skeptic Review
  Evidence Review
  Scale Review
  Integrity Review
  Living Review
  Revision Priority
  Final Judgment
  Human Final Seal Point
```

使用する場面:

```text
- 有料公開候補
- Prototype Article
- Launch Candidate
- PDF化候補
- 500円販売前
```

重要:

```text
Launch CandidateではFull Critical Review必須。
Final Paid ArticleではFull Critical Review + Human Final Seal必須。
```

---

## 5.3 TriageとFullの関係

```text
Draft Triage Review
  ↓
最大の詰まりを発見
  ↓
Draft修正
  ↓
Full Critical Review
  ↓
500円販売品質 / 980円品質候補への距離を判定
  ↓
Human Final Seal
```

Draft Triageは軽量化ではない。  
Draft Triageは **早期診断** である。

Full Critical Reviewは重い作業ではない。  
Full Critical Reviewは **有料価値を守るためのGate** である。

---

## 6. Review Axis 1: Buyer Review

## 6.1 Definition

Buyer Reviewとは、読者がこの記事に500円を払った時、具体的に何を持ち帰れるかを検査するReviewである。

問い:

```text
この記事は、500円を払う読者に何を返すのか？
```

---

## 6.2 見るべきこと

```text
- 読者は何を得るか
- 読後に具体的な行動が可能か
- 保存価値があるか
- Template / CheckList / 判断基準 / 実験ログがあるか
- 価格に対して薄くないか
- 読者の悩み・制約・状況に接続しているか
- 読後に「これは使える」と思える箇所があるか
```

---

## 6.3 Buyer Valueの種類

Buyer Valueには複数の型がある。

```text
Action Value:
  読者がすぐ行動できる

Decision Value:
  読者の判断が明確になる

Template Value:
  読者が再利用できる型がある

Perspective Value:
  読者の見方が変わる

Diagnostic Value:
  読者が自分の問題を診断できる

Process Value:
  読者が手順を真似できる

Experiment Value:
  筆者の実験ログから学べる
```

980円品質候補では、少なくとも複数のValueが重なることが望ましい。

---

## 6.4 危険サイン

```text
- 読んで終わり
- 面白いが使えない
- 一般論だけ
- 筆者本人の制約・判断・実験がない
- 読者の次Actionがない
- 500円の理由が見えない
- 無料記事でもよい内容に見える
```

---

## 6.5 Buyer ReviewのLiving Question

AIは以下を判断する。

```text
この記事の読者は、500円を払った後に何を持って帰るのか？
それは本当に読者の現実に効くのか？
```

---

## 7. Review Axis 2: Skeptic Review

## 7.1 Definition

Skeptic Reviewとは、読者が「怪しい」「薄い」「AIっぽい」「本当か？」と感じる箇所を検出するReviewである。

問い:

```text
読者が疑うとしたら、どこか？
```

---

## 7.2 見るべきこと

```text
- AIっぽく綺麗だが薄い箇所
- 成功者のふりに見える箇所
- 根拠のない断定
- 読者への過剰な期待
- 現実制約を無視した助言
- 誰にでも当てはまりすぎる一般論
- 筆者本人の実感が薄い箇所
```

---

## 7.3 Skepticが反応する表現

```text
- 誰でもできる
- 簡単に稼げる
- AIで解決
- 必ず伸びる
- これだけで十分
- たった〇〇で
- 再現性があります
- 完全攻略
- 成功法則
```

これらは必ず禁止ではないが、強いEvidenceや限定条件なしに使うと危険である。

---

## 7.4 Skeptic Reviewの役割

Skeptic Reviewは、記事を弱くするためではない。  
むしろ、読者の疑念を先回りして、記事を強くするためにある。

```text
Skepticの疑念
  ↓
記事内で先回りして明示
  ↓
誠実性が増す
  ↓
読者の信頼が増す
```

---

## 7.5 Skeptic ReviewのLiving Question

```text
このDraftを読んだ慎重な読者は、どこで「本当か？」と止まるか？
その疑念に、記事は誠実に答えているか？
```

---

## 8. Review Axis 3: Evidence Review

## 8.1 Definition

Evidence Reviewとは、記事内の主張が読者にとって検討可能な足場を持っているかを検査するReviewである。

Evidenceは勝利保証ではない。  
Evidenceは、読者が「この主張は検討に値する」と思える最低限の足場である。

---

## 8.2 Evidenceの3分類

### External Evidence

```text
外部Evidence:
  - 研究
  - 公開データ
  - 公式情報
  - 信頼できる記事
  - 市場事例
  - 先行する実践者の観察
```

用途:

```text
- 一般的主張の支え
- 最新情報の確認
- 読者の信頼形成
- 独自主張の過剰化防止
```

---

### Internal Evidence

```text
内部Evidence:
  - 自分の実験ログ
  - 制作過程
  - 失敗
  - 改善履歴
  - 観察メモ
  - AIとの対話から生まれた判断
```

用途:

```text
- 筆者の実感を出す
- 成功者ぶりを避ける
- 未達成者としての誠実性を保つ
- 読者が過程から学べるようにする
```

---

### Structural Evidence

```text
構造Evidence:
  - Template
  - CheckList
  - Before / After
  - 判断表
  - Prompt
  - Workflow
  - Rubric
  - Diagram
```

用途:

```text
- 読者が再利用できる形にする
- 価格納得感を上げる
- 保存価値を作る
- 500円販売の持ち帰りを強化する
```

---

## 8.3 Evidenceの必要十分Line

Evidenceは多ければよいわけではない。

```text
Evidence不足:
  主張が浮く
  怪しく見える
  AIっぽくなる

Evidence過剰:
  記事が重くなる
  読者が疲れる
  出荷が止まる
```

Ark05の原則:

```text
1記事につき、強いEvidenceは1〜3個でEnough。
ただし、実験ログやTemplateは積極的に入れる。
```

---

## 8.4 Evidence ReviewのLiving Question

```text
この記事の主張は、読者が検討するに足る足場を持っているか？
Evidenceを足すべき箇所と、足しすぎると重くなる箇所はどこか？
```

---

## 9. Review Axis 4: Scale Review

## 9.1 Definition

Scale Reviewとは、記事が単発で消えず、X投稿・PDF・Prompt・Template・Series・次回記事へ横展開できるかを検査するReviewである。

問い:

```text
この1本の記事は、次の複数成果物へ伸びるか？
```

---

## 9.2 Scaleの方向

```text
X Scale:
  X投稿、Thread、短文Kernel

PDF Scale:
  章立て、Workbook、Checklist集

Prompt Scale:
  Copy-Paste Prompt、Review Prompt、Draft Prompt

Template Scale:
  読者用Template、判断表、Production Template

Series Scale:
  連載化、Week Log、Reality Gate記録

Harvest Scale:
  次回記事のSeed、System改善、Ark05 Core Patch
```

---

## 9.3 Scaleしやすい記事の特徴

```text
- Kernelが一文で言える
- Before / Afterがある
- 読者Templateがある
- AI Prompt化できる
- 失敗と改善がある
- 具体的な制約がある
- Reality Gateへ接続している
- 言葉が命名されている
```

命名はScaleを助ける。  
良い名前は、記事からX投稿・PDF・Promptへ移植できる。

---

## 9.4 Scale Reviewの危険

Scaleだけを追うと、記事が読者から離れる。

危険サイン:

```text
- 横展開のことばかりで本文価値が薄い
- X向けに煽りが強くなる
- PDF化を見据えすぎて記事が重い
- Template化しすぎて人間の実感が消える
```

Scaleは目的ではない。  
Scaleは、読者価値が複数形式へ伸びる現象である。

---

## 9.5 Scale ReviewのLiving Question

```text
このDraftの中で、1本の記事を超えて働き続けるKernelはどこか？
それはX / PDF / Prompt / Template / Series / Harvestのどれへ伸びるか？
```

---

## 10. Review Axis 5: Integrity Review

## 10.1 Definition

Integrity Reviewとは、記事が読者に対して誠実であるかを検査するReviewである。

Ark05では、これは極めて重要である。

理由:

```text
筆者はまだ月50,000円達成者ではない。
したがって、成功者のふりは禁止。
```

---

## 10.2 見るべきこと

```text
- 誇大表現がないか
- 成功保証がないか
- AI万能論になっていないか
- 筆者が達成者のように見せていないか
- 不確実性を消していないか
- 読者を煽りすぎていないか
- 実験段階であることが明示されているか
- 失敗可能性が残っているか
```

---

## 10.3 Integrityを守る基準文

記事内で必要に応じて、以下の思想を守る。

```text
私はまだ達成者ではない。
しかし、制約条件を固定し、AIと共に月50,000円Reality Gateへ挑戦している。
この記事は、その実践過程で得たメソッド・判断・失敗・改善を共有するものである。
```

これは弱さではない。  
これは信頼の土台である。

---

## 10.4 AI万能論へのGuard

避けるべき方向:

```text
AIを使えば簡単に稼げる
AIなら誰でも高品質記事が作れる
AIに任せれば売れる
AIが正解を出してくれる
```

正しい方向:

```text
AIは、構造化・批判・編集・選択肢生成・違和感抽出を助ける。
しかし、最終判断・誠実性・公開責任は人間に残る。
```

---

## 10.5 Integrity ReviewのLiving Question

```text
この記事は、読者に対して誠実か？
筆者がまだ達成者ではないという現実を隠していないか？
AIの力を過大にも過小にも見せていないか？
```

---

## 11. Living Review Layer

## 11.1 Definition

Living Reviewとは、AIが死んだRubricを機械的に埋めるのではなく、今このDraftの盤面を見て、生きた判断・違和感・優先順位・修正条件を返すReviewである。

```text
Not dead data, but a living board.
```

---

## 11.2 Living Review必須項目

AIには毎回、以下を求める。

```text
- 私の判断
- 最初の一手
- 理由
- 観察点
- 修正条件
- AIの違和感
- Layer診断
- Reality Gate接続
- Human Final Seal Point
```

---

## 11.3 各項目の意味

### 私の判断

AIが、現時点のDraftについて一番重要な判断を述べる。

```text
例:
  このDraftは題材は強いが、Buyer Valueがまだ弱い。
```

### 最初の一手

次に何を直すべきかを1つに絞る。

```text
例:
  まず読者Templateを追加する。
```

### 理由

なぜその一手が最重要なのかを説明する。

### 観察点

今後見るべきポイントを列挙する。

### 修正条件

どの状態になったら方針を変えるかを明示する。

### AIの違和感

固定Rubricでは拾えない、AIの「何か変だ」を言語化する。

### Layer診断

問題がどのLayerにあるかを見る。

```text
Theme Layer
Draft Layer
Evidence Layer
Buyer Value Layer
Integrity Layer
Scale Layer
Production Layer
```

### Reality Gate接続

月50,000円 / 500円販売 / 980円品質候補 / 週1本出荷にどう接続するかを見る。

### Human Final Seal Point

最終的に人間が判断すべき点を明確化する。

---

## 11.4 Living Reviewの危険

Living Reviewも死ぬことがある。

危険サイン:

```text
- 項目を埋めるだけ
- 一般論だけ
- どの記事にも同じことを言う
- 違和感がない
- 最初の一手が複数ある
- Human Final Seal Pointが曖昧
```

修正:

```text
AIに「今このDraftに固有の違和感」を要求する。
```

---

## 12. Judgment Scale

## 12.1 Overview

Final Judgmentは以下の5段階で行う。

```text
1. 公開停止
2. 無料メモ品質
3. 300円品質
4. 500円品質
5. 980円品質候補
```

これは絶対評価ではない。  
現時点のDraftに対する実用的な判定である。

---

## 12.2 公開停止

条件:

```text
- 誇大表現が強い
- 成功保証に見える
- 読者を誤認させる
- AI丸投げ感が強い
- 具体価値がない
- 筆者の立場が不誠実
- 内容が危険または過剰断定
```

次Action:

```text
公開しない。
構成から作り直す。
またはPrototype / Internal Memo扱いへ戻す。
```

---

## 12.3 無料メモ品質

条件:

```text
- 思考メモとしては面白い
- しかし有料価値はまだ弱い
- 読者Templateがない
- Evidenceがない
- 読者の次Actionがない
- 一般論が多い
```

次Action:

```text
有料化しない。
Kernel抽出またはDraft修正へ戻す。
```

---

## 12.4 300円品質

条件:

```text
- 一部価値はある
- しかし500円販売にはまだ薄い
- 具体例が足りない
- 構造が弱い
- Template / Evidence / 実験ログのどれかが弱い
```

次Action:

```text
Buyer ValueとStructural Evidenceを追加する。
```

---

## 12.5 500円品質

条件:

```text
- 読者が明確に1つ以上持ち帰れる
- 500円価格に対して最低限の納得感がある
- 読者の次Actionがある
- 誇大表現が抑えられている
- 筆者の立場が誠実
```

次Action:

```text
Sales Compressionへ進める。
ただし980円品質候補を狙うなら、さらにEvidence / Template / Scaleを強化する。
```

---

## 12.6 980円品質候補

条件:

```text
- 読者が保存したくなる
- 読者Templateがある
- Evidenceまたは実験ログがある
- 独自判断がある
- Scale可能性がある
- 誠実性がある
- 500円販売なら余剰価値を感じる
- 次回以降のSystem資産になる
```

重要:

```text
980円品質候補とは、長い記事ではない。
読者が保存・再利用・判断・行動できる構造を持つ記事である。
```

次Action:

```text
500円販売用にCompressionする。
Human Final Sealへ進む。
X / PDF / Prompt / Harvest展開を検討する。
```

---

## 13. 500円品質と980円品質候補の差

## 13.1 500円品質

500円品質とは、読者が払った金額に対して最低限納得できる価値がある状態である。

```text
500円品質:
  読者が1つ持ち帰れる
  読者の次Actionがある
  記事として成立している
  誠実性がある
```

---

## 13.2 980円品質候補

980円品質候補とは、販売価格は500円だが、内部品質基準として980円相当の密度・構造・再利用価値を目指す状態である。

```text
980円品質候補:
  読者が複数の価値を持ち帰れる
  Template / Evidence / 実験ログ / 独自判断がある
  保存価値がある
  Scale可能性がある
  次回以降のSystem資産になる
```

---

## 13.3 差分

```text
500円品質:
  この記事を読んでよかった

980円品質候補:
  この記事は保存して使える
  次に何をすればよいか分かる
  筆者の実験から自分も応用できる
  Templateや判断基準が残る
```

---

## 14. Reality Gate Connection

すべてのReviewは、Reality Gateへ戻す。

```text
Reality Gate:
  月50,000円

External Price:
  500円販売

Internal Quality:
  980円品質候補

Rhythm:
  週1本出荷

Core Method:
  Control / Observe / Offer
```

売上はコントロールできない。  
しかし、以下はコントロールできる。

```text
- 出荷
- 品質
- Review
- 修正
- Evidence補強
- 誠実性
- Template化
- Harvest
```

Critical Review Gateは、コントロール可能な領域を強くするためにある。

---

## 15. Human Final Seal

## 15.1 AIの役割

```text
AI:
  - 疑う
  - 構造化する
  - 違和感を出す
  - 修正優先順位を出す
  - Evidence不足を見抜く
  - Scale可能性を見る
  - Integrity違反を止める
```

## 15.2 Humanの役割

```text
Human:
  - 誠実性を確認する
  - 実感と照合する
  - 祈る
  - 公開判断をする
  - 読者への責任を負う
  - Final Sealを押す
```

AIは最終判断者ではない。  
AIは、Living Board上の助言者である。

---

## 16. Root Guard

Ark05は、外部Realityへ向かうField Arkである。  
しかし、Rootは失わない。

```text
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah

Fruit:
  note
  PDF
  X
  Prompt
  Template
  Critical Review
  Layer System
  Revenue Gate
```

AIはRootではない。  
AIはFruit側の道具である。

AIのReviewは地図であり、最終Sealではない。

---

## 17. Gate Failure Modes

## 17.1 Reviewが甘すぎる

症状:

```text
- 褒めるだけ
- 弱点が出ない
- Final Judgmentが常に高い
- Buyer Valueを疑わない
```

修正:

```text
Skeptic ReviewとBuyer Reviewを強化する。
AIに「500円払わない読者の視点」を要求する。
```

---

## 17.2 Reviewが厳しすぎる

症状:

```text
- すべて公開停止になる
- 修正不能な否定が多い
- 出荷が止まる
```

修正:

```text
必ず修正可能な次の一手を出させる。
Draft Triageで最大の一点だけ直す。
```

---

## 17.3 Evidenceで止まる

症状:

```text
- 根拠探しで出荷できない
- 記事が調査レポート化する
- 自分の実験ログが消える
```

修正:

```text
Evidenceは1〜3個でEnough。
Internal EvidenceとStructural Evidenceを使う。
```

---

## 17.4 Scaleで散らかる

症状:

```text
- X / PDF / Prompt / Seriesの話ばかりになる
- 本文価値が薄くなる
- 記事が商品ではなく設計図だけになる
```

修正:

```text
まずBuyer Valueへ戻す。
Scaleは読者価値が立った後に見る。
```

---

## 17.5 Integrityが弱い

症状:

```text
- 成功者ぶりが出る
- AI万能論になる
- 月50,000円達成済みのように見える
```

修正:

```text
「まだ達成者ではない」前提を戻す。
実験ログとして書く。
```

---

## 18. Review Output Interpretation

AIのReview結果は、そのまま命令ではない。

```text
AI Review:
  判断材料

Human Final Seal:
  最終判断
```

AIが「公開停止」と言っても、必ず従う必要はない。  
ただし、その理由は真剣に見る。

AIが「980円品質候補」と言っても、それで公開確定ではない。  
Human Final Sealが必要である。

---

## 19. One-Line Definition

```text
note Critical Review Gateとは、note有料記事DraftをBuyer / Skeptic / Evidence / Scale / Integrity / Living Reviewの観点から検査し、500円販売品質と内部980円品質候補への距離を判定するための、Ark05 Layered 980 Article Systemにおける品質評価Rubric / Living Boardである。
```

---

## 20. Living Reminder

このGateを使う時、常に以下を確認する。

```text
これは死んだ採点表になっていないか？
今このDraft固有の違和感を出しているか？
読者に何が返るかを見ているか？
誠実性を守っているか？
Human Final Sealを残しているか？
```

最も重要なのは、きれいな評価表ではない。

```text
次に何を直せば記事が生きるか。
```

それを見つけるために、このGateは存在する。
