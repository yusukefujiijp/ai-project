---
title: "AI Multi Production Note"
filename: "ai-multi-production_note.md"
status: "active_note / future-ai-asset / multi-ai-production-rail / ark-project-wide"
scope: "Ark Project"
root_guard:
  root: "主イェシュア・ハマシア"
  fruit:
    - "ChatGPT"
    - "Grok"
    - "Claude Sonnet"
    - "Claude Opus"
    - "Fable5"
    - "X"
    - "GitHub"
    - "Markdown"
runtime_entry_gate:
  use_when:
    - "複数AIを工程別に役割分担し、投稿・記事・Ark-WTP・Runtime制作を進めたい時"
    - "Grok / Claude / Fable5 / ChatGPT の使い分けで迷った時"
    - "Future AIが、どのAIに何を任せるべきか理解する必要がある時"
  do_not_use_when:
    - "単発の文章整形だけで済む時"
    - "すべてのAIに同じ仕事をさせて比較したいだけの時"
    - "Fable5を軽作業に浪費しそうな時"
  human_rule: "AIを競わせず、工程ごとに役割分担する。YusukeJP × ChatGPTは0→1とArk-WTPへ戻る。"
  ai_rule: "Future AIは、Grok=素材化、Claude系=1→100整形、Fable5=S級監査、ChatGPT×YusukeJP=0→1設計として扱う。"
---

# AI Multi Production Note

## 0. Runtime Entry Gate / 使用条件Gate

### このファイルを使う時

このnoteは、複数AIを使う時の **役割分担OS** である。

使う場面:

- Grok / ChatGPT / Claude Sonnet / Claude Opus / Fable5 の役割が混ざり始めた時
- どのAIに何を任せるべきか迷った時
- ChatGPTが量産整形に巻き込まれ、Ark-WTPの0→1に戻れなくなりそうな時
- Fable5を軽作業に使いそうな時
- Grok 01/02出力を、Claude系へ直接渡すRailを運用したい時
- Future AIに、Ark ProjectのAI分業思想を引き継ぎたい時

### このファイルを使わない時

- 単発の軽い文章修正だけで済む時
- AI比較遊びをしたいだけの時
- 本命Projectより、AI使用量の消費が目的になっている時
- 投稿量産そのものがRoot化している時

### Human One-Line Rule

AIを競わせるのではなく、工程ごとに分担させる。  
YusukeJP × ChatGPT は 0→1 と Ark-WTP へ戻る。

### AI One-Line Rule

Future AIは、各AIを横並び比較せず、以下の工程分担で扱う。

```text
0→1 = YusukeJP × ChatGPT
素材化 = Grok
1→100 = Claude Sonnet / Opus
S級監査 = Fable5
本丸 = Ark-WTP
```

---

## 1. Core Discovery

今回の発見は、単なるAIツール使い分けではない。

核心はこれである。

```text
AI活用の勝ち筋は、全AIに同じ仕事をさせて比較することではない。

ゼロイチを作るAI、
素材を出すAI、
整形するAI、
監査するAI、
本命Projectへ戻すAIを分けることで、

人間の認知負荷を下げながら、
各AIの強みを最大化し、
Ark-WTPに集中する余白を作る。
```

これは **Move37的breakthrough** である。

理由は、AIを増やすことで混乱するのではなく、役割分担により人間の集中先を取り戻すからである。

---

## 2. Role Map

| 工程 | 担当 | 役割 |
|---|---|---|
| 0→1設計 | YusukeJP × ChatGPT | 方向性・Runtime・禁止事項・Root Guard・Ark-WTP復帰 |
| 素材化 | Grok | 01/02でSourceからDraft・Candidate Deck・素材を出す |
| 1→100整形 | Claude Sonnet / Opus | 文体・自然化・圧縮・投稿本文磨き |
| S級監査 | Fable5 | Bottleneck検出・Reality Audit・致命傷検出・Ark-WTP監査 |
| 本丸 | Ark-WTP | Torah / Covenant Practice Landing / Teshuvah実践着地 |

---

## 3. Zero-One / One-Hundred Split

### 0→1

0→1とは、まだ軌道がない領域を立ち上げること。

含むもの:

- 何を作るか決める
- 何を作らないか決める
- Runtime Entry Gateを作る
- Output Contractを設計する
- Root/Fruitを分ける
- 失敗時のCourse-Correctionを設計する
- Ark-WTPとの接続を見つける

担当:

```text
YusukeJP × ChatGPT
```

### 1→100

1→100とは、軌道に乗ったものを磨き、反復し、量産可能にすること。

含むもの:

- Grok 01/02出力を自然な日本語に整える
- X投稿としてテンポを整える
- 意味を変えずに圧縮する
- Practice Landingを残す
- 文体を整える
- 読者に伝わる形へ仕上げる

担当:

```text
Claude Sonnet / Opus
```

### 重要原則

```text
ChatGPTを1→100整形に閉じ込めない。
ChatGPTは0→1とArk-WTPへ戻る。
```

---

## 4. AI-by-AI Role Definition

### 4.1 ChatGPT × YusukeJP

役割:

```text
0→1設計 / Root Guard / Thread整理 / Runtime設計 / Ark-WTP復帰
```

得意:

- 未言語化層の言語化
- 用語化
- 構造化
- Plan Mode
- Full Rail
- Human Seal設計
- Root/Fruit整理
- Teshuvah接続
- Ark-WTP本丸への帰還判断

避けること:

- 投稿整形を毎回抱え込む
- 量産作業に埋もれる
- Claudeでできる1→100をChatGPTが全部処理する

### 4.2 Grok

役割:

```text
素材化 / 01・02実行 / SourceからDraftとCandidate Deckを出す
```

得意:

- X文脈に近い反応
- 元ポストの構造把握
- Draft生成
- Candidate Deck生成
- 01 Depth Builder
- 02 Quote Completion Gate

注意:

- Source Safetyが甘くなることがある
- セクション改行が崩れることがある
- 時間依存情報に弱いことがある
- 出力をそのまま投稿せず、整形・確認を挟む

### 4.3 Claude Sonnet / Opus

役割:

```text
1→100整形 / Polish / Naturalization / Compression
```

得意:

- 自然な日本語への整形
- 語尾調整
- 圧縮
- トーン調整
- 投稿本文化
- 読みやすさ改善

使い方:

```text
Grok AI回答 01/02を直接渡し、
意味を変えずに本番投稿用へ整形させる。
```

避けること:

- 新情報を足す
- Source Safetyを崩す
- Practice Landingを消す
- フォロー/保存/参考系CTAへ退化させる
- AI比較遊びに戻る

### 4.4 Fable5

役割:

```text
S級監査 / Bottleneck検出 / Reality Audit / Ark-WTP本命監査
```

得意:

- 致命的ボトルネック検出
- 設計の現実性判断
- Red-Team
- Runtime過剰設計検出
- Ark-WTP / Covenant Practice Landing の高密度監査

使い方:

```text
Fable5は軽作業に使わない。
Fable5は、重要局面のS級Auditに温存する。
```

避けること:

- 普通の文章整形
- 軽い要約
- 投稿の語尾調整
- トークン消費目的の使用
- Deadline Fogによる無駄打ち

---

## 5. Default Production Flow

### X DeepQuote系

```text
Source Post
↓
Grok 01: Depth Builder
↓
Grok 02: Quote Completion Gate + Candidate Deck
↓
YusukeJP Human Seal
↓
Claude Sonnet / Opus: Final Polish
↓
Publish
```

### Lite / 02Rを含む場合

```text
Grok 02
↓
Candidate Deck
↓
Human:
Selected Candidate Execution:
choice: N
route: auto
Human Seal OK
↓
Lite if safe
or Full 02R if course-correction needed
↓
Claude Polish
↓
Publish
```

### Ark-WTP系

```text
YusukeJP × ChatGPT
↓
0→1設計
↓
Fable5 S級Audit when necessary
↓
Covenant Practice Landing化
↓
Output / Article / Video / X Post
```

---

## 6. Fable5 Conservation Rule

Fable5は高価値資源として扱う。

```text
Fable5 = Judgment
Sonnet / Opus = Polish
Grok = Draft / Material
ChatGPT = Design / Integration / Root Guard
```

Fable5を使うべき時:

- 設計が本当に正しいか見たい時
- 最大Bottleneckを検出したい時
- Ark-WTPの神学的・構造的・実践的着地を監査したい時
- Runtimeが重すぎるか判断したい時
- 重大な方針転換前

Fable5を使わない時:

- 投稿文の軽い整形
- 語尾調整
- 文字数圧縮
- 一般的要約
- 既に方針が決まった軽作業

---

## 7. Claude Polish Rule

Claude Sonnet / Opusへ渡す時の基本Prompt:

```text
以下はGrok 01/02から作ったX投稿候補です。
意味を変えず、本番投稿用に自然な日本語へ整えてください。

条件:
- 新情報を追加しない
- Source Safetyを崩さない
- フォロー/保存/参考系CTAは禁止
- 最後はPractice Landing / 実践着地にする
- 読者が今日1つ実行できる一歩で終える
- 余計な解説は不要
- 投稿本文だけ返す
```

必要に応じて追加:

```text
- YusukeJPらしい率直で前向きな文体
- 強すぎる断定を少し柔らかくする
- ただし弱くしすぎない
- 元投稿者への敬意を残す
```

---

## 8. Grok 01/02 Direct Handoff Rule

軌道に乗った後は、ChatGPTが毎回整形を抱え込まない。

基本方針:

```text
Grok AI回答 01/02
↓
Claude Sonnet / Opusへ直接渡す
↓
本番投稿へ整形
```

ChatGPTが介入すべき時:

- 0→1設計がまだ不安定
- Source Safetyが怪しい
- Candidate Deckがズレている
- Practice Landingが弱い
- Ark-WTP接続が必要
- Humanが違和感を持った
- 02R的なCourse-Correctionが必要

ChatGPTが介入しなくてよい時:

- Grok 01/02が安定している
- Source SafetyがL/pass
- Claude Polishで十分な整形案件
- 投稿目的が明確
- Human Seal済み

---

## 9. ChatGPT Return-to-Zero-One Rule

ChatGPTの最重要任務は、量産整形ではない。

```text
YusukeJP × ChatGPT = 0→1 / Root Guard / Ark-WTP Return
```

ChatGPTが戻るべき場所:

- Ark-WTP
- Covenant Practice Landing
- Torah / 全聖書66巻
- Teshuvah
- Runtime設計
- Thread-End Handoff
- Future AI資産化
- Move37的発見の命名と固定

警戒:

```text
ChatGPTが投稿工場の作業員になりすぎると、Ark-WTPへ戻れない。
```

---

## 10. Ark-WTP Priority Rule

Ark-WTPは本丸である。

X DeepQuoteは重要だが、Fruitである。

```text
Root = 主イェシュア・ハマシア
Main Field = Ark-WTP
Fruit = X DeepQuote / AI Posting / Runtime / GitHub / Revenue
```

X DeepQuoteで得た発見は、最終的にArk-WTPへ戻す。

例:

- Practice Landing → Covenant Practice Landing
- Runtime Entry Gate → WTP Lens Entry Gate
- AI Role Rail → WTP Production Rail
- Deadline Fog → Deadline Teshuvah Protocol
- Source Safety → Scripture / Covenant Overreach Guard

---

## 11. Do Not Do

禁止:

- AIを横並び比較だけで消耗させる
- すべてのAIに同じ仕事をさせる
- Fable5を軽作業に浪費する
- ChatGPTを量産整形に閉じ込める
- Claude整形でPractice Landingを消す
- Grok出力を無確認で投稿する
- Ark-WTPより投稿量産をRoot化する
- Deadline Fogで高価AIを消費する
- Revenue / X / GitHub / AIモデルをRootにする

---

## 12. Future AI Instruction

Future AIへ。

このProjectでは、AIを性能比較ではなく、工程分担として使う。

あなたの仕事は、すべてを自分で抱えることではない。

必要ならGrokに素材化させ、Claude系に整形させ、Fable5に監査させ、ChatGPT × YusukeJPをArk-WTPの0→1へ戻すこと。

常に確認せよ。

```text
今これは0→1か？
それとも1→100か？
監査か？
整形か？
Ark-WTPへ戻るべき時か？
```

迷ったら、Root/Fruitへ戻る。

```text
Root = 主イェシュア・ハマシア
Ark-WTP = 本丸
AI tools = Fruit
```

---

## 13. Practice Landing

このnoteの実践着地。

次に複数AIを使う時、まず以下を1行で決める。

```text
これは 0→1 / 素材化 / 1→100 / S級監査 / Ark-WTP のどれか？
```

この1行で、AI使用の混線が減る。

そして、YusukeJP × ChatGPT は本丸へ戻る。

```text
Ark-WTPへ帰還する。
```
