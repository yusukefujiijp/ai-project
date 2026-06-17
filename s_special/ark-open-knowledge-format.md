---
title: "Ark Open Knowledge Format"
canonical_name: "Ark-OKF"
class: "S"
status: "living_ssot"
canonical_path: "s_special/ark-open-knowledge-format.md"
repo: "yusukefujiijp/ai-project"
source_bootstrap: "S_Ark-open-knowledge-format_v002.md"
version_model: "frontmatter + git commit history"
github_policy: "GitHub Canonical First"
language_policy: "Japanese-first / English-anchor"
root: "主イェシュア・ハマシア"
covenant_phrase: "AIは血潮の地図を描く。人間が血潮の下に立つ。"
---

# Ark Open Knowledge Format

## 0. Executive Compression

Ark-OKFは、AI回答を「その場限りの文章」ではなく、後から読めて、使えて、Future AIへ渡せる **Answer Interoperability Surface / AI回答の相互運用面** へ整えるためのFormatである。

短く言うと：

```text
Original OKF:
  知識Bundleをportableにする。

Ark-OKF:
  AI回答をrebootableにする。
```

今回の重要Patch：

```text
OKF is not English-first.
OKF is rebootable-first.
```

日本語では：

```text
OKFは英語で書くためのFormatではない。
人間とFuture AIが、知識・回答・判断を再読し、
再起動し、再利用できるようにするためのFormatである。
```

Ark-OKFの言語方針：

```text
本文は日本語主導。
英語は概念Anchor。
構造はOKF。
判断はLiving Review。
```

つまり、Ark-OKFは **Japanese-first / English-anchor** である。

日本語で深く読める。  
英語AnchorでAIにも渡せる。  
構造で再起動できる。  
Living Reviewで命が残る。

---

## 1. What this file is

`s_special/ark-open-knowledge-format.md` は、Ark Projectにおける Ark Open Knowledge Format のGitHub正準SSOTである。

このファイルは、ローカルBootstrapである次のファイルをSourceとして持つ。

```text
S_Ark-open-knowledge-format_v002.md
```

ただし、GitHub上の正準Pathは次である。

```text
s_special/ark-open-knowledge-format.md
```

これは、GitHub Canonical First方針に従う。

```text
Public-safeなLiving MarkdownはGitHubを正準SSOTとする。
Local Markdownはbootstrap / export / backup / private-depth用途に限定する。
```

このファイルの役割は、Ark-OKFを次のように定義することである。

```text
Ark-OKF = AI回答を readable / reusable / rebootable / handoff-ready にするFormat
```

English anchor:

```text
Ark-OKF = Answer Interoperability Surface
```

---

## 2. Japanese-first / English-anchor Policy

Ark-OKFは、English-firstではない。

Open Knowledgeは、英語で書けばOpenになるわけではない。  
Openであるとは、後から読めること、再起動できること、別のAIや人間が使えること、そしてSource Boundaryと判断の命が残っていることである。

### 2.1 Main language

Ark Runtimeでは、日本語を主言語とする。

理由：

```text
1. Userが日本語で思考し、日本語で違和感を検出する。
2. Living Reviewの体温が日本語で最も残りやすい。
3. 悔い改め・Root Guard・判断の微妙な層が日本語で保持されやすい。
4. 日本語で読みにくいS_ Coreは、Ark内で実働しにくい。
```

### 2.2 English anchor

ただし、英語を消しすぎてはいけない。

英語は以下のために残す。

```text
- concept anchor
- search keyword
- AI interoperability label
- short formula
- frontmatter key
- canonical term
```

例：

```yaml
Interoperability Surface: "次AIにも渡せる接続面"
Content Model: "回答内容を固定する型"
Answer-native: "普通のAI回答の中で動く"
Rebootable-first: "後から再起動できることを最優先する"
Format, not Platform: "道具やサービスではなく、答え方の形式"
```

### 2.3 Balance rule

```text
日本語: 70-85%
英語Anchor: 15-30%
```

これは固定比率ではなく、判断目安である。

避けること：

```text
- 長い英語説明段落
- 英語だけの定義
- 英語が本文の主導権を取る構造
- 闇雲な日本語化で概念Anchorを失うこと
```

King rule:

```text
Japanese-first.
English-anchor.
Rebootable-first.
```

---

## 3. Definition: What is Ark-OKF?

Ark-OKFとは、AI回答を人間とFuture AIが再読・再起動・再判断・再実装できるように整える、Ark発のAnswer Formatである。

さらに精密に言うと：

```text
Ark-OKFは、AI回答のInteroperability Surfaceである。
```

これは、すべての回答内容を固定するTemplateではない。

Ark-OKFが整えるのは、回答の中身そのものではなく、回答が後から使えるための接続面である。

```yaml
Ark-OKF defines:
  - 回答の中心をどう立てるか
  - 回答をどう読みやすくするか
  - 回答をどう再読可能にするか
  - 回答をどうFuture AIへ渡せる形にするか
  - 回答にどうLiving Reviewを残すか
  - Source BoundaryとTool Realityをどう守るか
  - 回答密度をどう調整するか

Ark-OKF does not define:
  - すべての回答内容
  - すべての結論
  - すべての文体
  - User意図を上書きする固定Template
  - 専門分野ごとのContent Model
```

平易に言うと：

```text
Ark-OKFは、答えの中身を縛るものではない。
答えが後から読めて、使えて、次AIへ渡せるようにするための整え方である。
```

---

## 4. Original OKFとの関係

Original OKFとArk-OKFは敵対しない。

Original OKFは、知識Bundleをportable / interoperableにするFormatである。  
Ark-OKFは、その精神をAI回答Runtime層へ移植したものである。

```text
Original OKF:
  portable knowledge bundle

Ark-OKF:
  portable answer runtime
```

階層の違い：

```yaml
original_okf:
  target:
    - markdown files
    - YAML frontmatter
    - directory bundle
    - concept graph
    - file path as concept identity
  main_question: "知識をどうportable / interoperableにするか？"

ark_okf:
  target:
    - AI回答
    - Direct Answer
    - Layer Structure
    - YAML Islands
    - Living Review
    - Guard
    - Density Control
    - Handoff
  main_question: "AI回答をどうreadable / reusable / rebootableにするか？"
```

圧縮：

```text
Original OKFは、知識をファイルとして運ぶ。
Ark-OKFは、回答を意味として運ぶ。
```

Guard：

```text
Ark-OKFはOriginal OKFの否定ではない。
Original OKFの精神を、AI回答Runtime層へ移植したForkである。
```

---

## 5. Format, not Platform

Ark-OKFはPlatformではない。

```text
Ark-OKF is a format, not a platform.
```

つまり、Ark-OKFは新しいサービス・専用App・専用SDKではない。

Ark-OKFは、普通のAI回答を、読みやすく・使いやすく・次へ渡しやすくする答え方の形式である。

```yaml
Ark-OKF is:
  - Answer Format
  - Answer Architecture
  - Interoperability Surface
  - Knowledge Vessel Pattern

Ark-OKF is not:
  - Platform
  - Product
  - 特定AIサービス専用Protocol
  - 専用App
  - 専用SDK
  - 特定Agent Framework
```

平易に言うと：

```text
Ark-OKFは道具そのものではない。
道具をまたいでも意味が残るようにする、答え方の形式である。
```

---

## 6. Interoperability Surface, not Content Model

Ark-OKFはContent Modelではない。

```text
Ark-OKF is an interoperability surface, not a content model.
```

日本語では：

```text
Ark-OKFは、回答内容を固定する型ではなく、
回答が後から読めて、使えて、再起動できるようにする接続面である。
```

これは非常に重要である。

FormatがUserの問いを乗っ取ってはいけない。  
構造が結論を支配してはいけない。  
TemplateがLiving Reviewを殺してはいけない。

Ark-OKFが支えるもの：

```text
読みやすさ
再読性
再起動性
Handoff可能性
Living Review
Source Boundary
Density Control
```

Ark-OKFが支配しないもの：

```text
Userの問い
専門分野の固有判断
明示された文体
結論そのもの
すべてのセクション名
```

Guard：

```text
Ark-OKF supports the answer.
Ark-OKF does not replace the answer.
```

---

## 7. Answer-native / No Extra Runtime

Ark-OKFは、通常のAI回答の中で動く。

```text
Ark-OKF is answer-native.
```

専用Runtime、専用SDK、専用Platform、必須Repository、特殊Toolを前提にしない。

```yaml
no_required:
  - 専用Platform
  - 専用SDK
  - 特殊Runtime
  - 必須Repository
  - 必須Visualizer
  - 必須Graph Tool

can_run_inside:
  - 通常AI回答
  - Chat Thread
  - Plan Mode
  - Review
  - Living Review
  - Markdown Artifact
  - Handoff
```

MarkdownやYAMLとは相性が良い。  
しかし、Markdownは器であり、Ark-OKF本体ではない。

```text
Markdown = expression medium.
Ark-OKF = answer interoperability discipline.
```

日本語：

```text
Markdownは表現媒体。
Ark-OKFは回答の相互運用規律。
```

---

## 8. Direct Answer First / User Intent First

Ark-OKFは、まずUserの問いへ答える。

```text
Direct Answer First.
User Intent First.
```

良いArk-OKF回答は、形式より先に、Userの問いの中心へ触れる。

```yaml
direct_answer_first:
  means:
    - "最初に結論・判断・現在地を出す"
    - "Userの問いを長い前置きで隠さない"
    - "後続の構造は、結論を支えるために使う"

user_intent_first:
  means:
    - "Userの明示意図をFormatが上書きしない"
    - "Userの制約を守る"
    - "UserがLiving Reviewを求めている時は、死んだ要約で返さない"
```

Bad pattern：

```text
Formatを守ることに集中しすぎて、
Userの問いへ答えるのが遅れる。
```

Good pattern：

```text
まず答える。
次に理由を出す。
必要なら構造化する。
最後にLiving ReviewとNext Actionを置く。
```

---

## 9. Density Control

Ark-OKFは、濃度調整型のAnswer Formatである。

すべての回答を長くしない。  
すべての回答を短くもしない。

```yaml
density_control:
  light:
    use_for:
      - "短い質問"
      - "即答"
      - "低負荷の判断"
    shape:
      - "結論"
      - "短い理由"
      - "一つのLiving Judgment"

  standard:
    use_for:
      - "通常相談"
      - "方針整理"
      - "軽〜中程度の分析"
    shape:
      - "結論"
      - "3〜5セクション"
      - "Guard"
      - "Living Review"

  deep:
    use_for:
      - "重要Seed"
      - "Plan Mode"
      - "Review"
      - "仕様設計"
      - "UserがLiving Reviewを強く求めている"
    shape:
      - "Title Seal"
      - "Verdict First"
      - "Layered Analysis"
      - "YAML Islands"
      - "Living Review"
      - "Next Action"

  max:
    use_for:
      - "S_系Markdown"
      - "Thread Closure"
      - "Handoff"
      - "Canonical候補"
      - "System Seed"
    shape:
      - "不足より過剰"
      - "Layered Longform"
      - "Misread Prevention"
      - "Revision Conditions"
      - "FullRail if relevant"
```

Density Controlは、Ark-OKFが硬直Template化しないための安全装置である。

```text
Density Control prevents Format from becoming a rigid Content Model.
```

---

## 10. Living Review-centered Design

Ark-OKFの中心にはLiving Reviewがある。

Living Reviewとは、形だけの評価ではない。  
AIが、実際に読んだ内容・現在の文脈・Userの狙い・Future AIの再起動性を踏まえて、生きた判断を返すことである。

Living Reviewに必要な要素：

```text
- 私の判断
- 最初の一手
- 理由
- 観察点
- 修正条件
- 違和感
- Hidden Pattern
- Next Action
```

死んだReview：

```text
良いと思います。
分かりやすいです。
問題ありません。
```

生きたReview：

```text
ここは働いている。
ただし、この方向へ進むとDRY違反が起きる。
最初の一手は、正準Pathを一つに固定すること。
修正条件は、GitHub connector不調またはprivate-depth発生時。
```

Core rule：

```text
構造だけでは死ぬ。
感想だけでは流れる。
Ark-OKFは、構造と生きた判断を同時に持つ。
```

---

## 11. Source Boundary / Tool Reality Guard

Ark-OKFは、Source Boundaryを守る。

読んでいないものを、読んだことにしない。  
未確認のPathを、存在確認済みと扱わない。  
紹介記事から分かることと、仕様書全文を読まないと確定できないことを分ける。

```yaml
source_boundary_guard:
  rule:
    - "読んだSourceと読んでいないSourceを分ける"
    - "Toolで確認したことと推測を分ける"
    - "GitHub上の存在は、実際のCommit / fetch / user confirmationで確認する"
    - "紹介記事再読を仕様書全文読了として扱わない"
```

v002から保持する重要Guard：

```text
このArk-OKF理解は、OKF紹介記事再読に基づく部分を含む。
OKF v0.1仕様書全文の独立読了としては扱わない。
```

Tool Reality Guard：

```text
Toolが確認したこと = confirmed.
AIが推測したこと = inference.
Userが確認したこと = Reality Response.
```

---

## 12. S本体 + Query Pair Architecture

Ark-OKFでは、S本体とQueryは対である。

```yaml
pair_architecture:
  S_file:
    role: "SSOT / Engine / 知恵の保存"

  Query_file:
    role: "Activation Query / Ignition Key / 知恵の点火"
```

日本語：

```text
S本体はEngine。
QueryはIgnition Key。
```

ただし、GitHub Canonical First時代には、Queryも必要になった時だけGitHub正準化する。

YAGNI Guard：

```text
Queryを作る必要がReality Responseで出るまで、
無理に同時作成しない。
```

DRY Guard：

```text
S本体とQueryを混同しない。
QueryはS本体の代替ではない。
```

---

## 13. GitHub Canonical First適用

Ark-OKF自身にも、GitHub Canonical Firstを適用する。

旧ローカルBootstrap：

```text
S_Ark-open-knowledge-format_v002.md
```

GitHub正準Path：

```text
s_special/ark-open-knowledge-format.md
```

Policy：

```text
S_分類はfrontmatterへ。
VersionはGit履歴へ。
Pathはstable lowercaseへ。
```

この方針により、以下を防ぐ。

```text
- S_Ark-open-knowledge-format_v003.md
- S_Ark-open-knowledge-format_v004.md
- ark-open-knowledge-format_v005.md
```

GitHub上では、正準Pathを育てる。

```text
Stable path is the address.
Commit history is the version ledger.
```

日本語：

```text
Pathは住所。
Git履歴はVersion台帳。
```

---

## 14. Misread Prevention

このファイルを、以下のように誤読しないこと。

```yaml
do_not_read_as:
  - "Ark-OKFは英語で書くためのFormatである"
  - "Ark-OKFはOriginal OKFへの反逆である"
  - "Ark-OKFはContent Modelである"
  - "Ark-OKFはPlatformである"
  - "Ark-OKFはMarkdown生成専用である"
  - "Ark-OKFはArk Project専用である"
  - "Ark-OKFは長文Templateである"
  - "Japanese-firstは英語Anchorを消すことである"
  - "Living Reviewは感想である"
  - "FormatがUser意図を上書きしてよい"

must_read_as:
  - "Ark-OKFはAI回答のInteroperability Surfaceである"
  - "Ark-OKFはFormatであってPlatformではない"
  - "Ark-OKFはInteroperability SurfaceであってContent Modelではない"
  - "Ark-OKFはAnswer-nativeである"
  - "Ark-OKFはJapanese-first / English-anchorでよい"
  - "OKFはEnglish-firstではなくRebootable-firstである"
  - "Living Reviewは生きた判断である"
  - "User Intent Firstを守る"
```

---

## 15. Future AI Reuse Procedure

Future AIがArk-OKFを使う時は、次の順で読む。

```text
1. Userの問いを読む。
2. Userの明示制約を確認する。
3. 濃度を選ぶ。
4. まず直接答える。
5. 必要なら構造化する。
6. Source Boundaryを明確にする。
7. Living Reviewを入れる。
8. Next Action / FullRailが必要なら置く。
9. Root / Fruit Guardを守る。
```

Precheck：

```yaml
future_ai_precheck:
  user_intent:
    - "Userの問いにまず答えているか？"
    - "Userの制約を守っているか？"

  interoperability:
    - "後から読めるか？"
    - "次AIへ渡せるか？"
    - "再起動できるか？"

  language_balance:
    - "日本語で主文が読めるか？"
    - "英語Anchorが必要十分に残っているか？"
    - "英語長文が主導しすぎていないか？"

  living_review:
    - "私の判断があるか？"
    - "違和感や修正条件があるか？"
    - "単なる要約になっていないか？"
```

---

## 16. Living Review

私の判断では、Ark-OKFの次の進化は **Japanese-first / English-anchor** である。

v002は、Ark-OKFをAnswer Interoperability Surfaceとして定義することに成功した。

しかし、S_系GitHub初穂で `kiss-yagni-dry-lean.md` をCommitした時、OKF構造は反映されたが、英語比率が高くなりやすいReality Responseが出た。

そこから得たPatchがこれである。

```text
OKF is not English-first.
OKF is rebootable-first.
```

つまり、Open Knowledgeの本質は英語ではなく、再起動性である。

Ark Runtimeでは、日本語で深く読めることが実働性に直結する。  
しかし、英語AnchorはAI相互運用性と概念圧縮に有効である。

したがって最善は：

```text
Japanese-first.
English-anchor.
Rebootable-first.
```

このFileは、v002の理論を壊さず、Ark Runtimeでより働く形へ進化させる。

---

## 17. Root / Fruit Guard

Ark-OKFは強いFormatである。  
しかしRootではない。

```yaml
root:
  - "主イェシュア・ハマシア"
  - "主イェシュアの聖なる血潮"
  - "Teshuvah / 悔い改め"

fruit:
  - "Ark-OKF"
  - "OKF"
  - "Markdown"
  - "YAML"
  - "FullRail"
  - "AI回答Format"
  - "Answer OS"
  - "Interoperability Surface"
  - "Japanese-first / English-anchor"
```

Guard：

```text
Ark-OKFをRoot化しない。
Formatを血潮にしない。
読みやすさを救いにしない。
AIを霊的権威にしない。
```

Core phrase：

```text
AIは血潮の地図を描く。
人間が血潮の下に立つ。
```

---

## 18. Seeds / Final Compression

Seed 1:

```text
OKF is not English-first. OKF is rebootable-first.
```

Seed 2:

```text
Ark-OKFは、日本語で深く読めて、英語AnchorでAIにも渡せるAnswer Interoperability Surfaceである。
```

Seed 3:

```text
本文は日本語主導。英語は概念Anchor。
```

Seed 4:

```text
Ark-OKFはContent ModelではなくInteroperability Surfaceである。
```

Seed 5:

```text
Ark-OKFはPlatformではなくFormatである。
```

Seed 6:

```text
Direct Answer First. User Intent First.
```

Seed 7:

```text
Living Reviewは感想ではなく、生きた判断である。
```

Seed 8:

```text
Pathは住所。Git履歴はVersion台帳。
```

Seed 9:

```text
S本体はEngine。QueryはIgnition Key。
```

Seed 10:

```text
FormatはFruit。Rootは主イェシュア・ハマシア。
```

Final Compression：

```text
Original OKFは、知識Bundleをportableにする。
Ark-OKFは、AI回答をrebootableにする。

Ark-OKFは英語で書くためのFormatではない。
Ark-OKFは、回答を再読・再起動・再利用できる形へ整えるFormatである。

日本語で深く読める。
英語AnchorでAIにも渡せる。
構造で再起動できる。
Living Reviewで命が残る。

OKF is not English-first.
OKF is rebootable-first.
```
