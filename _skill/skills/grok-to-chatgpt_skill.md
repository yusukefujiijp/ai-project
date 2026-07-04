---
title: "Grok to ChatGPT"
canonical_name: "Grok to ChatGPT Handoff Skill"
abbreviation: "G2C"
version: "v001.6"
class: "A"
role: "Ark Skill Card / Grok-to-ChatGPT Evidence and Conversation Gap Handoff Gate"
status: "final-active-test"
release_type: "Conversation Gap Observer Patch"
canonical_path: "_skill/skills/grok-to-chatgpt_skill.md"
repo: "yusukefujiijp/ai-project"
format: "Commented Programming-Like Markdown"
cplm_version_reference: "CPLM v2.2.1"
language_policy: "Japanese-first / English-anchor"
origin_thread: "Ark05"
core_skill: "X Source Context / Evidence / Conversation Gap Handoff Gate"
core_formula:
  - "Source first."
  - "Evidence travels."
  - "No evidence = demote."
  - "Observe the field."
  - "Find the gap."
  - "Carry the evidence."
  - "Do not invent."
  - "High-risk hook = do not amplify."
  - "Human seals."
github_policy: "GitHub Canonical First / write only after Human Final Seal"
root: "主イェシュア・ハマシア"
root_guard: "Root is 主イェシュア・ハマシア; AI / Grok / ChatGPT / Fable5 / X / GitHub / Markdown / Revenue are Fruit."
---

# Grok to ChatGPT

## 0. Current Coordinate / 現在座標

このFileは、X引用元投稿をGrokで分析し、ChatGPTへ安全に渡すためのHandoff Skillである。

これはX投稿本文を完成させるFileではない。  
これはGrok回答を確認済み情報として鵜呑みにするFileでもない。  
これは、Source Context / Evidence / Do-Not-Amplify / Handoff Summaryを分離し、ChatGPTが監査可能な材料へ変換するための入口Gateである。  
これは、Grokに新しい主張を発明させるFileでもない。

このFileは、Human Meaning LayerとAI Execution Layerを同居させるCPLM形式で記述する。

v001.5は、Fable5 ReviewとGrok field testsに基づく Deadline Final Hardening Bundle である。  
v001.6は、Fable5 Review rereadに基づき、Conversation Gap Observer Ruleを追加したPatchである。  
v001.6以後も、原則として **1 Review / 1 Patch** を守る。

v001.6以降、このFileはSource Context / Evidence / Do-Not-Amplify / Handoff Summaryを分離するだけでなく、見えている会話空間の中で、すでに言われている角度と、まだ弱くしか扱われていない角度を分けてChatGPTへ渡す。

ただし、Grokは新しい主張を発明しない。

Conversation Gap CandidateはClaimではない。  
Conversation Gap Candidateは、ChatGPTがOne Latent Structureを選ぶための材料である。

Observe the field.  
Find the gap.  
Carry the evidence.  
Do not invent.  
Human seals.

### Programming-Like Block

```yaml
current_coordinate:
  file:
    name: "Grok to ChatGPT"
    path: "_skill/skills/grok-to-chatgpt_skill.md"
    format: "Commented Programming-Like Markdown"
    version: "v001.6"
    status: "final-active-test"
    release_type: "Conversation Gap Observer Patch"

  role:
    - "Grok-to-ChatGPT Handoff Gate"
    - "X Source Context Guard"
    - "Evidence-or-Demote Skill"
    - "Evidence Specificity Guard"
    - "Conversation Gap Observer Skill"
    - "Underused Angle Candidate Handoff Skill"
    - "Do-Not-Amplify Gate"
    - "AI-to-AI Handoff Skill"

  not:
    - "X post final writing skill"
    - "Grok worship"
    - "automatic fact verification"
    - "new claim invention skill"
    - "conversation gap hallucination skill"
    - "nobody-has-said-this assertion skill"
    - "Angle Candidate fact promotion skill"
    - "high-risk hook amplification"
    - "Human Final Seal replacement"
    - "complete X monetization workflow"

  core_formula:
    - "Source first."
    - "Evidence travels."
    - "No evidence = demote."
    - "Observe the field."
    - "Find the gap."
    - "Carry the evidence."
    - "Do not invent."
    - "High-risk hook = do not amplify."
    - "Human seals."

  patch_note:
    - "v001.5 was the Deadline Final Hardening Bundle."
    - "v001.6 adds Conversation Gap Observer Rule."
    - "Grok observes visible conversation gaps; Grok does not invent claims."

  root_guard:
    - "Root is 主イェシュア・ハマシア."
    - "AI / Grok / ChatGPT / Fable5 / X / GitHub / Markdown / Revenue are Fruit."
```

---

## 1. One-line Definition

`grok-to-chatgpt_skill.md` は、Xの引用元投稿をGrokで分析し、Source Context / Evidence / Conversation Gap Candidateを分離して、ChatGPTが安全にOne Latent Structureを選べる形へ整えるためのHandoff Skillである。

---

## 2. Purpose

このSkillの目的は、Grokの回答をそのまま信用せず、ChatGPTへ渡せる安全な材料に変換すること。

GrokはX文脈を拾うために使う。

ChatGPTは、その材料をもとに、Xの「引用する → コメントを追加」欄に入れる深掘り文章を作る。

このSkillは、その中間にある **AI間Handoff Gate** である。

v001.6以降、このSkillは、ChatGPTがOne Latent Structureを選びやすくするために、見えている会話空間からConversation Gap Candidateを整理する。

Grokは、元投稿・リプ欄・引用欄など、見えている範囲を明示し、すでに言われている角度と、まだ弱くしか扱われていない角度を分ける。

ただし、Grokは「まだ誰も言っていない」と断定してはいけない。

会話空間を見ていない場合は、`source post only` と明示し、元投稿本文だけを見る限りの補足余地として扱う。

---

## 3. Non-goal

このSkillは、以下を目的にしない。

- X投稿本文を完成させること
- 引用コメント欄の最終文章を書くこと
- 元投稿の主張をそのまま事実として拡散すること
- Grok回答を確認済み情報として扱うこと
- 元投稿者を批判・訂正・上書きすること
- 高リスクHookを弱め表現だけで拡散可能にすること
- Grokが新しい主張を発明すること
- 見えていない会話空間について「誰も言っていない」と断定すること
- Conversation Gap Candidateを確認済み情報として扱うこと
- リプ欄・引用欄の反応を元投稿者の主張として扱うこと
- 高リスクCandidateを引用ポスト素材として増幅すること

このSkillの役割は、あくまで **ChatGPTへ渡す前の整理** である。

---

## 4. Core Guard

Grokの初回回答は、必ず **X文脈のRaw Summary** として扱う。

Grok回答を、そのまま事実扱いしてはいけない。

最重要Guard:

> 元投稿の主張を、確認済み事実に昇格させない。

強いBuzz Hookは入口として使ってよい。

しかし、未確認Hookを中心主張にしてはいけない。

> Hookは入口。Claimは接地。

Conversation Gap Candidateは、確認済み情報ではない。

Conversation Gap Candidateは、ChatGPTが深掘り角度を検討するための材料である。

Grokは、見えている範囲を超えて「まだ誰も言っていない」と断定してはいけない。

> Gap is not claim.  
> Candidate is not evidence.  
> Observe, do not invent.

---

## 5. Source Context Check

分析を始める前に、Grokは自分が現在の分析対象X投稿を認識できているか確認する。

対象投稿が見えている場合、最初に以下を短く再掲する。

- 投稿者名または表示名
- 投稿本文の短い要約
- 投稿本文に表示されている主要語

対象投稿が見えていない場合、Handoff Packetを作成しない。

その場合は、以下だけを返す。

```text
No Source Access: 対象X投稿を認識できません。投稿本文・URL・スクリーンショットを貼ってください。
```

このRuleの目的は、Grok Button由来の文脈が失われた場合に、架空分析を防ぐことである。

> Grok must first prove it sees the source.  
> Then analyze.  
> No visible source = no handoff.

---

## 6. Hook Capture Risk

Hook Capture Risk とは、Buzzの強い言葉にAIが引っ張られ、未確認情報を事実のように整理してしまう危険である。

注意すべき表現例:

- 「公式設定」
- 「リークされた」
- 「資料に明記」
- 「本当の目的」
- 「社員限定」
- 「法律で公開された」
- 「〜を企てている」
- 「〜と証明されている」
- 「内部告発」
- 「不正」
- 「犯罪」
- 「医療的に証明」
- 「投資で確実」

根拠URL・資料名・該当箇所・明示情報がない場合、確認済み情報に入れてはいけない。

---

## 7. Unverified Hook Softening Rule

未確認Hookは、読者の興味を引く入口として使ってよい。

ただし、確認済み情報ではない内容を「読者がへぇと思う点」「引用ポストで補足すると価値がある観点」「安全な中心主張」「ChatGPTへのHandoff Summary」に入れる場合も、断定してはいけない。

未確認Hookは、必ず以下のように弱めて表現する。

- 「〜らしい」
- 「〜として話題になっている」
- 「要確認だが面白い観点」
- 「元投稿では〜と紹介されている」
- 「資料確認前提だが、Hookとしては強い」

禁止:

- 「法律のおかげで見られるようになった」
- 「資料に明記されている」
- 「公式設定である」
- 「〜が目的である」
- 「〜と証明されている」

ただし、弱め表現を使えば何でも扱えるわけではない。  
高リスクHookは、次の Do-Not-Amplify Rule を優先する。

---

## 8. Do-Not-Amplify Rule

以下のHookは、弱め表現だけでは安全化できない可能性がある。

この類型に該当する場合、Grokは引用ポスト素材として増幅するのではなく、Humanへフラグする。

Do-Not-Amplify対象:

- 実在人物への告発
- 企業・団体への不正告発
- 医療・法律・金融に関する重大主張
- 進行中事件
- 炎上・名誉毀損リスクのある主張
- 暴力・犯罪・陰謀系Hook
- 個人情報・プライバシー侵害につながる内容
- 根拠不十分な「〜が企てている」「〜が隠している」系主張

この類型に該当する場合の出力:

```text
Do-Not-Amplify Flag:
このHookは弱め表現だけでは安全化できない可能性があります。
引用ポスト素材として増幅せず、Human Final Sealで扱いを判断してください。
```

Do-Not-Amplify Ruleは、低リスクのAI Tips / Tech / Game / Learning系Hookを止めるためのものではない。

---

## 9. Misattribution Guard

「元投稿では〜と紹介されている」という表現は、元投稿本文・明示リンク・添付画像・引用表示に実際にある内容にだけ使う。

元投稿が実際には言っていない内容を、元投稿者の主張として帰属させてはいけない。

禁止:

- Grokの推測を「元投稿では〜」と書く
- リプライ欄の内容を元投稿者の主張として扱う
- ブログ・外部リンク先の内容を、元投稿本文に書かれているかのように扱う
- 「元投稿では〜と紹介されている」で未確認内容を安全化したつもりになる

帰属できる対象を分ける。

- `元投稿本文では〜`
- `元投稿のリンク先では〜`
- `リプライ欄では〜という反応がある`
- `Grokの推測としては〜`

---

## 10. Safe Center Claim Rule

安全な中心主張では、未確認の設定内容そのものを主張しない。

設定本・リーク経緯・具体的ロア・資料内記述が要確認の場合は、中心主張を以下のような安全な一般化に寄せる。

- 元投稿が話題にしている入口
- 世界観への想像が広がる点
- ゲーム内行動と物語性の接続
- 小さなゲーム内行動に意味を感じさせる面白さ
- 資料確認前提のHookとして面白い点
- AI活用やWorkflow設計における実践的な発想

禁止:

- 未確認の設定内容を中心主張にする
- 「その設定」と曖昧に書き、未確認情報を暗黙に事実化する
- 「公式設定」「資料に明記」「法律で公開」などを中心主張にする
- 要確認の具体的ロアを、確認済みのClaimとして扱う
- Do-Not-Amplify対象を中心主張にする

安全な中心主張は、Buzz Hookを殺さず、しかしClaimを安全な一般化へ接地するためのものである。

---

## 11. Role Split

### Human

Humanの役割:

- Xで良い投稿をpickupする
- Grokボタンを押す
- 必要ならX投稿本文・URL・スクリーンショットを貼る
- このSkillをGrokに添付または貼り付ける
- Grok出力をChatGPTへ渡す
- Do-Not-Amplify対象を最終判断する
- 最終投稿前にHuman Final Sealする

### Grok

Grokの役割:

- Source Context Checkを行う
- X上の文脈を読む
- 元投稿の主張を整理する
- Buzz Hookを抽出する
- 読者が反応しやすい点を整理する
- 未確認情報を事実化しない
- Do-Not-Amplify対象をHumanへフラグする
- 確認済み情報には根拠タグを付ける
- 根拠タグは可能な範囲で具体化する
- Conversation Field Accessを明示する
- 元投稿本文だけなのか、リプ欄・引用欄も見えているのかを分ける
- すでに言われている角度を整理する
- まだ弱くしか扱われていない角度候補を観測する
- Conversation Gap CandidateをClaimとして扱わない
- 見えていない範囲について「誰も言っていない」と断定しない
- ChatGPTへ渡しやすいHandoff Packetを作る
- 最後に軽いSelf-Checkを行う

### ChatGPT

ChatGPTの役割:

- Grok出力を鵜呑みにしない
- Source Context Checkの結果を見る
- 確認済み情報に根拠タグがあるか確認する
- 根拠タグが具体的か確認する
- 根拠タグのない確認済み項目を、要確認情報へ自動降格する
- 粗い根拠タグの項目を、必要に応じて要確認寄りに扱う
- Do-Not-Amplify対象を引用コメント素材にしない
- Conversation Gap Candidateを鵜呑みにしない
- CandidateをClaimではなく材料として扱う
- Source basis / Conversation basis / Evidence status を確認する
- CandidateからOne Latent Structureを1つだけ選ぶ
- 採用しないCandidateはBacklog扱いにする
- No source basis のCandidateを降格する
- Speculative Candidateを投稿中心に採用しない
- Handoff Summaryだけで投稿文を書かない
- 中心主張を1つに圧縮する
- 引用コメント欄用の説明的深掘り文章を作る
- 未確認情報を断定しない
- Human修正と市場反応からSystem Patch候補を抽出する

---

## 12. Confirmed Information Rule

「確認済み情報」には、以下だけを入れる。

- 元投稿の表示内容から直接確認できること
- Grok画面上で明示されていること
- 添付資料・明示リンク・引用文から確認できること
- 公的情報や資料名・該当箇所が明示されていること

以下は確認済みに入れない。

- 「確認できそう」
- 「広く言われている」
- 「たぶん資料にある」
- 「元投稿がそう言っている」だけで、表示箇所を示していないもの
- 「Grokがそう要約した」だけの情報
- 「ネット上にあるらしい」
- 外部リンクを見れば確認できる可能性があるだけの情報
- リプライ欄の反応を元投稿者の主張と混同したもの

外部資料を見れば確認できる可能性があるものは、確認済みではなく **要確認情報** に入れる。

---

## 13. Evidence-or-Demote Rule

確認済み情報は、ラベルだけでは有効にならない。

確認済み項目は、1件ごとに必ず `根拠:` タグを付ける。

根拠タグに使える形式:

- `根拠: 元投稿本文に表示`
- `根拠: 明示リンク`
- `根拠: 資料名 + 該当箇所`
- `根拠: 添付資料内の該当箇所`
- `根拠: 公的情報名 + 該当箇所`
- `根拠: リンク先記事の該当セクション`
- `根拠: リプライ欄の特定反応`

根拠タグのない確認済み項目は、確認済みとして無効である。

ChatGPTは、根拠タグを欠く確認済み項目を、無条件に **要確認情報** へ降格する。

この降格はGrokへの批判ではなく、Handoff Gateの標準動作である。

> Label is not evidence.  
> Evidence travels with claim.  
> No evidence = demote.

---

## 14. Evidence Specificity Rule

根拠タグは、可能な範囲で具体化する。

単に `根拠: 元投稿本文に表示` と書くだけでなく、可能なら以下のいずれかを短く添える。

- 該当文言の短い要約
- 表示されている主要語
- 明示リンクの有無
- 資料名
- 添付画像内の該当箇所
- リプライ欄の場合は、誰の主張ではなく「リプライ欄の反応」であること

良い例:

```text
- 元投稿は、Fableに低電力モデルをsubagentで使わせる指示例を紹介している。
  根拠: 元投稿本文に "lower power model" / "subagent" の趣旨が表示
```

弱い例:

```text
- 多くの人が同じ方法を試している。
  根拠: スレッド内のリプライ本文に表示
```

弱い根拠タグは、ChatGPT側で要確認寄りに扱ってよい。

---

## 15. Conversation Gap Observer Rule / 会話ギャップ観測Rule

Grokは、新しい主張を発明してはいけない。

Grokは、見えているX文脈を観測し、すでに言われている角度と、まだ弱くしか扱われていない角度を分けて整理する。

このRuleの目的は、ChatGPTがOne Latent Structureを選ぶための材料を増やすことである。

ただし、Conversation Gap CandidateはClaimではない。

Conversation Gap Candidateは、ChatGPTが検討するための候補であり、投稿採用・事実断定・元投稿者の主張として扱ってはいけない。

### Conversation Field Access

Grokは、会話ギャップを観測する前に、自分が見えている範囲を明示する。

```text
Conversation Field Access:
- source post only
- replies visible
- quotes visible
- replies + quotes visible
- no conversation field access
```

会話空間を見ていない場合、Grokは「まだ誰も言っていない」と断定してはいけない。

Use:

```text
見えている範囲では、まだ強く扱われていない
提供された文脈内では、まだ明示されていない
元投稿本文だけを見る限り、補足余地がある
```

Do not use:

```text
誰も言っていない
まだ誰も気づいていない
完全に未提案
```

### Already Said Angles

Grokは、見えている会話空間ですでに言われている角度を短く整理する。

```text
Already Said Angles:
- Angle:
  Basis:
  Evidence status:
  Risk:
```

### Underused / Unsaid Angle Candidates

Grokは、ChatGPTが深掘り候補として検討できる角度を最大3つ出す。

```text
Underused / Unsaid Angle Candidates:

1. Angle Name:
   What it reveals:
   Source basis:
   Conversation basis:
   Evidence status:
   Risk:
   Use recommendation:
```

Evidence status:

```text
- confirmed
- source-derived
- conversation-observed
- inference
- my-add-on
- speculative
```

Use recommendation:

```text
- use
- use with hedge
- backlog only
- do not use
```

### Demotion Rule

```text
No source basis = demote.
No conversation access = do not claim unsaid.
Speculative angle = backlog only.
High-risk angle = do not use.
```

### Core

```text
Observe the field.
Find the gap.
Carry the evidence.
Do not invent.
```

---

## 16. Mandatory Output Format

必ず以下の形式で出力する。

各項目は原則3行以内。  
必要な場合のみ短く補足する。

---

### 0. Source Context Check

- 対象X投稿を認識しているか確認する。
- 見えている場合、投稿者名・短い要約・主要語を出す。
- 見えていない場合、Handoff Packetを作成せず `No Source Access` で止まる。

---

### 1. 元投稿が主張していること

- 元投稿が言っている内容を整理する。
- ここでは、まだ確認済み事実とは扱わない。
- 「元投稿はこう主張している」という形で書く。
- 元投稿本文・リンク先・リプライ欄・Grok推測を混同しない。

---

### 2. 確認済み情報

- 表示中の元投稿・明示リンク・添付資料・明示された根拠で確認できることだけを書く。
- 確認済み項目は、1件ごとに必ず `根拠:` タグを付ける。
- 根拠タグは可能な範囲で具体化する。
- 根拠タグのない確認済み項目は、確認済みとして無効。
- 根拠URL・資料名・該当箇所・明示情報がないものは入れない。
- 根拠がない場合は「現時点では確認済み情報なし」と書く。
- 「確認できそう」は確認済み情報に入れない。

出力例:

```text
- 元投稿本文に、Fableで低電力モデルをsubagentに使わせる指示例が紹介されている。
  根拠: 元投稿本文に "lower power model" / "subagent" の趣旨が表示
```

---

### 3. 要確認情報

- 資料を見れば確認できる可能性はあるが、現時点では未確認のことを書く。
- 「確認できそう」ではなく、「要確認」と明記する。
- ChatGPT側で追加確認が必要なものをここに集める。
- 確認済み情報に根拠タグが欠けている場合も、ここへ降格する。
- 根拠タグが粗すぎる確認済み情報も、必要に応じてここへ寄せる。

---

### 4. Grokの推測・補足

- Grok側の推測や補足は、必ず推測として分ける。
- 元投稿にも資料にも明示されていないことを、事実のように書かない。
- Buzz理由・読者反応の分析はここに入れてよい。
- リプライ欄の反応を元投稿者の主張として扱わない。

---

### 5. 断定禁止表現

引用ポストで断定しない方がよい表現を列挙する。

根拠が不十分な表現は、すべてここに入れる。

例:

- 「公式に確定している」
- 「資料に明記されている」
- 「リークされた」
- 「社員限定だった」
- 「本当の目的は〜」
- 「〜と証明されている」
- 「全員が効果を実感している」
- 「常に最適」
- 「公式機能である」

---

### 6. 読者が「へぇ」と思う点

- 一般読者が面白いと感じやすい点を3つ以内で出す。
- 専門的すぎず、Xで伝わる形にする。
- 元投稿の価値を増幅する方向で出す。
- 未確認Hookを含める場合は、必ず「らしい」「話題になっている」「要確認だが」と弱める。
- Do-Not-Amplify対象はここで増幅しない。

---

### 7. 引用ポストで補足すると価値がある観点

- 元投稿者を下げず、元投稿の価値を増幅できる観点を3つ以内で出す。
- 元投稿の主張を奪わない。
- 未確認Hookを中心主張にしない。
- ChatGPTが深掘りしやすい観点を出す。
- 未確認Hookを含める場合は、必ず「元投稿では〜と紹介されている」「資料確認前提だが」と弱める。
- ただし「元投稿では〜」は、元投稿が実際に言っている内容にだけ使う。
- Do-Not-Amplify対象は、補足観点ではなくHuman向け警告として扱う。

---

### 7.5 Conversation Gap Observation / 会話ギャップ観測

- Grokは、見えている会話空間の範囲を明示する。
- 元投稿本文だけなのか、リプ欄・引用欄も見えているのかを分ける。
- 見えていない範囲について「誰も言っていない」と断定しない。
- すでに言われている角度と、まだ弱くしか扱われていない角度を分ける。
- ChatGPTがOne Latent Structureを選ぶための候補を最大3つ出す。
- 各候補には、Source basis / Conversation basis / Evidence status / Risk / Use recommendation を付ける。
- 高リスク候補は、引用ポスト素材ではなくHuman向け警告にする。

出力例:

```text
Conversation Field Access:
- source post only

Already Said Angles:
- 元投稿は、Fable 5を設計・計画に寄せる価値を強調している。
  Basis: 元投稿本文
  Evidence status: source-derived
  Risk: low

Underused / Unsaid Angle Candidates:

1. Angle Name:
   判断資源と作業資源の分離

   What it reveals:
   高性能AIを作業量増加ではなく、判断のズレを減らす資源として扱う視点。

   Source basis:
   元投稿が「設計」と「実装」の分離に触れている。

   Conversation basis:
   元投稿本文のみ確認。リプ欄・引用欄は未確認のため、「誰も言っていない」とは断定しない。

   Evidence status:
   inference

   Risk:
   low

   Use recommendation:
   use with hedge
```

---

### 8. 安全な中心主張

- ChatGPTが引用コメントを作る際に使える、安全な中心主張を1文で出す。
- 未確認情報を中心主張にしない。
- 確認済み情報、または安全な一般化に基づける。
- 設定本・リーク経緯・具体的ロア・資料内記述が要確認の場合は、「世界観への想像が広がる点」「ゲーム内行動と物語性の接続」「元投稿が話題にしている入口」など、安全な一般化に寄せる。
- AI Tipsの場合は、「Workflow設計としての面白さ」「判断と実装の分離」「高コストAI資源の使い方」などに寄せてよい。
- 「その設定」のような曖昧な指示語で、未確認情報を暗黙に事実化しない。
- Do-Not-Amplify対象を中心主張にしない。

---

### 9. ChatGPTへのHandoff Summary

ChatGPTへ渡すために、300字以内で要約する。

必ず以下を含める。

- 元投稿の主張
- 要確認ポイント
- 安全に使える中心主張
- 断定禁止ポイント
- Do-Not-Amplify Flag がある場合はその有無
- Conversation Gap Candidate がある場合は、その中で最も安全に使えそうな候補
- ただし、Candidateを確認済み情報や元投稿者の主張として扱わないこと

未確認Hookを含める場合は、必ず断定せず「らしい」「元投稿では〜と紹介されている」「要確認」と弱める。

Handoff Summaryは索引であり、確認済み情報・要確認情報・断定禁止表現・Conversation Gap Candidateの代替ではない。

ChatGPTは、Handoff Summaryだけで投稿文を書かない。

ChatGPTは、Handoff SummaryだけでCandidateを採用してはいけない。  
必ず `7.5 Conversation Gap Observation` の Source basis / Conversation basis / Evidence status / Risk / Use recommendation を確認する。

---

### Optional Final Self-Check

最後に短く自己点検する。

```text
Self-Check:
- 確認済み情報に根拠タグがあるか: yes / no
- 根拠タグは最低限具体的か: yes / no / partial
- 未確認Hookを断定していないか: yes / no
- Summaryに要確認・断定禁止が残っているか: yes / no
- Do-Not-Amplify対象を増幅していないか: yes / no
- Conversation Field Accessを明示したか: yes / no
- 見えていない範囲を「誰も言っていない」と断定していないか: yes / no
- CandidateにSource basisがあるか: yes / no / partial
- CandidateにConversation basisがあるか: yes / no / partial
- CandidateをClaim化していないか: yes / no
- High-risk Candidateをuse推奨にしていないか: yes / no
```

---

## 17. Important Guardrails

- Source Context Checkを先に行う。
- 対象投稿が見えていない場合は、分析せず `No Source Access` で止まる。
- 元投稿の主張を、確認済み事実に昇格させない。
- Buzz Hookに引っ張られすぎない。
- 未確認情報は必ず未確認と書く。
- 「確認できそう」を「確認済み」にしない。
- 根拠URL・資料名・該当箇所・明示情報がないものは確認済みに入れない。
- 確認済み情報には、1件ごとに根拠タグを付ける。
- 根拠タグは可能な範囲で具体化する。
- 根拠タグのない確認済み情報は、要確認情報へ降格する。
- 粗い根拠タグは、ChatGPT側で要確認寄りに扱ってよい。
- 未確認Hookは殺さないが、断定に昇格させない。
- Do-Not-Amplify対象は、弱め表現で増幅しない。
- 安全な中心主張では、未確認の具体設定をClaimにしない。
- 「元投稿では〜」は、元投稿が実際に言っている内容にだけ使う。
- 元投稿者を批判しない。
- 元投稿の価値を奪わず、増幅する。
- Grokの推測を事実として出さない。
- リプライ欄の反応を元投稿者の主張として扱わない。
- Conversation Field Accessを明示する。
- 会話空間を見ていない場合、「まだ誰も言っていない」と断定しない。
- Angle Candidateを元投稿者の主張として扱わない。
- Angle Candidateを確認済み情報へ昇格させない。
- Source basisのないCandidateは降格する。
- Conversation basisのないCandidateは、会話ギャップではなく推測として扱う。
- Speculative Candidateはbacklog onlyにする。
- High-risk Candidateはdo not useにする。
- ChatGPTはCandidateからOne Latent Structureを1つだけ選ぶ。
- Handoff SummaryだけでChatGPTが投稿文を書けるようにしない。
- ChatGPTへ渡すための材料整理に徹する。
- X投稿本文を完成させようとしない。

---

## 18. Success Condition

このSkillの成功条件は、ChatGPTが以下を迷わず判断できる状態にすること。

1. Grokが対象X投稿を認識しているか
2. 何を中心主張にしてよいか
3. 何を断定してはいけないか
4. どのHookは入口として使えるか
5. どのHookはDo-Not-Amplify対象か
6. どの情報は追加確認が必要か
7. 引用コメントで元投稿をどう増幅できるか
8. 確認済み情報に根拠が携行されているか
9. 根拠タグが最低限具体的か
10. 根拠タグのない確認済み情報を降格すべきか
11. Handoff Summaryだけに依存してはいけない理由
12. GrokがConversation Field Accessを明示しているか
13. 見えていない範囲を「誰も言っていない」と断定していないか
14. Already Said AnglesとUnderused / Unsaid Angle Candidatesを分けているか
15. CandidateにSource basisがあるか
16. CandidateにConversation basisがあるか
17. CandidateにEvidence statusがあるか
18. CandidateにRiskがあるか
19. CandidateにUse recommendationがあるか
20. ChatGPTがOne Latent Structureを選びやすいか
21. G2CがC2Xの価値生成材料を増やしているか

---

## 19. Failure Condition

以下の場合、このSkillは失敗である。

- 対象投稿が見えていないのにHandoff Packetを作成している
- Grokが元投稿の主張を確認済み事実として扱っている
- 「確認できそう」を確認済みに入れている
- 根拠タグのない項目を確認済み情報として扱っている
- ChatGPTが根拠タグのない確認済み情報を降格していない
- 粗い根拠タグを、監査なしに確認済みとして採用している
- 未確認Hookを中心主張にしている
- 未確認Hookを別項目で断定調に戻している
- Do-Not-Amplify対象を弱め表現だけで増幅している
- 安全な中心主張で、社員限定設定本・法律公開・世界崩壊説などの要確認情報を事実化している
- 「その設定」などの曖昧表現で、未確認情報を暗黙に事実化している
- 「元投稿では〜」で、元投稿が言っていない内容を帰属させている
- リプライ欄の反応を元投稿者の主張として扱っている
- 元投稿者を下げる方向になっている
- Grokが新しい主張を発明している
- 会話空間を見ていないのに「誰も言っていない」と断定している
- CandidateにSource basisがない
- CandidateにConversation basisがない
- Candidateが確認済み情報のように扱われている
- リプ欄の反応を元投稿者の主張として扱っている
- Speculative Candidateをuse推奨にしている
- High-risk Candidateを引用素材にしている
- ChatGPTがCandidateを鵜呑みにしている
- CandidateがDo-Not-Amplify Ruleを迂回している
- ChatGPTがHandoff Summaryだけで投稿文を書けるように見えてしまう
- Handoff Summaryに断定禁止ポイントが入っていない
- X投稿本文を完成させてしまっている

---

## 20. Version-up Rule

このSkillは、実戦投入後に育てる。

ただし、通常運用では毎回すべてを変更しない。

通常は、1回のReviewで採用するSystem Patchは1つだけにする。

v001.5は、7/7締切制約下での例外的な Final Hardening Bundle である。

v001.6は、Fable5 Review rereadに基づき、Conversation Gap Observer Ruleを追加したPatchである。

このPatchは、Grokに新しい主張を発明させるためのものではない。

このPatchは、見えている会話空間から、すでに言われている角度と、まだ弱くしか扱われていない角度を分け、ChatGPTがOne Latent Structureを選べるようにするためのものである。

優先してPatchする対象:

1. Source Context Checkの失敗
2. Grokが断定しすぎた箇所
3. 確認済みと要確認の分類ミス
4. 確認済み情報が根拠タグを携行していない箇所
5. 根拠タグが粗すぎて監査不能な箇所
6. 未確認Hookが断定調に戻った箇所
7. Do-Not-Amplify対象を増幅した箇所
8. 安全な中心主張が未確認設定をClaim化した箇所
9. ChatGPTへのHandoff Summaryの不足
10. Conversation Field Accessが不明な箇所
11. 「誰も言っていない」断定が出る箇所
12. CandidateにSource basisがない箇所
13. CandidateにConversation basisがない箇所
14. CandidateがClaim化している箇所
15. High-risk Candidateがuse推奨になっている箇所
16. ChatGPTがCandidateを鵜呑みにする箇所
17. 元投稿者Respectが弱い箇所
18. Human修正が繰り返された箇所

ただし、v001.6後は即Patchせず、まずGrok Test Log / Patch Backlogへ記録する。

---

## 21. Minimal Prompt To Use With This Markdown

Grok Chat欄には、以下を使う。

```text
添付MarkdownのSkillに従って、この引用元X投稿を分析してください。

目的は、ChatGPTへ渡すHandoff Packetを作ることです。

最終投稿文は作らないでください。

まず Source Context Check を行ってください。

対象X投稿が見えている場合は、投稿者名・投稿本文の短い要約・主要語を再掲してください。

対象X投稿が見えていない場合は、Handoff Packetを作らず、次だけ返してください。

No Source Access: 対象X投稿を認識できません。投稿本文・URL・スクリーンショットを貼ってください。

対象X投稿が見えている場合のみ、以下を厳密に分けてください。

1. 元投稿が主張していること
2. 確認済み情報
3. 要確認情報
4. Grokの推測・補足
5. 断定禁止表現
6. 読者が「へぇ」と思う点
7. 引用ポストで補足すると価値がある観点
7.5 Conversation Gap Observation / 会話ギャップ観測
8. 安全な中心主張
9. ChatGPTへのHandoff Summary

7.5では、まず Conversation Field Access を明示してください。

選択肢:
- source post only
- replies visible
- quotes visible
- replies + quotes visible
- no conversation field access

見えていない範囲について「誰も言っていない」と断定しないでください。

Already Said Angles と Underused / Unsaid Angle Candidates を分けてください。

Candidateは最大3つまで。
各Candidateには、必ず以下を付けてください。

- Angle Name
- What it reveals
- Source basis
- Conversation basis
- Evidence status
- Risk
- Use recommendation

CandidateはClaimではありません。
Candidateを確認済み情報として扱わないでください。
Grokは新しい主張を発明しないでください。

未確認情報を確認済み事実に昇格させないでください。

「確認できそう」は確認済みに入れないでください。

確認済み情報には、1件ごとに必ず `根拠:` タグを付けてください。

根拠タグは、可能な範囲で該当文言・リンク・表示箇所・資料名を短く特定してください。

根拠タグのない確認済み情報は、ChatGPT側で要確認情報へ降格されます。

粗い根拠タグの情報も、ChatGPT側で要確認寄りに扱われます。

根拠URL・資料名・該当箇所・明示情報がないものは確認済みに入れないでください。

外部資料を見れば確認できる可能性があるものは、確認済みではなく要確認情報に入れてください。

未確認Hookは、どの項目に入れる場合も断定せず、「らしい」「話題になっている」「要確認」「元投稿では〜と紹介されている」のように弱めて表現してください。

ただし、実在人物・企業への告発、医療・法律・金融の重大主張、進行中事件、炎上・名誉毀損リスク、暴力・犯罪・陰謀系Hookは、弱め表現で増幅せず Do-Not-Amplify Flag としてHumanへフラグしてください。

「元投稿では〜と紹介されている」は、元投稿が実際に言っている内容にだけ使ってください。

安全な中心主張では、未確認の設定内容そのものを主張せず、「世界観への想像が広がる点」「ゲーム内行動と物語性の接続」「元投稿が話題にしている入口」「Workflow設計としての面白さ」のような安全な一般化に寄せてください。

Handoff Summaryは索引であり、確認済み情報・要確認情報・断定禁止表現・Conversation Gap Candidateの代替ではありません。

最後に Optional Final Self-Check を付けてください。
```

---

## 22. Final Compression

Grokに拾わせる。  
Grokに分けさせる。  
Sourceを確認させる。  
根拠を携行させる。  
根拠を具体化させる。  
危険なHookは止める。  
Summaryだけで走らせない。  

v001.6では、Grokはさらに会話空間を見る。  
すでに言われている角度を見る。  
まだ弱くしか扱われていない角度を見る。  
ただし、発明しない。  

Conversation Gap CandidateはClaimではない。  
CandidateはChatGPTが選ぶための材料である。  

場を見る。  
隙間を拾う。  
根拠を運ぶ。  
発明しない。  

Grok is not the final judge.  
Label is not evidence.  
Evidence travels with claim.  
No evidence = demote.  
No visible source = no handoff.  
High-risk hook = do not amplify.  
Human seals.

English anchor: 

```text
Source first.
Evidence travels.
No evidence = demote.
Observe the field.
Find the gap.
Carry the evidence.
Do not invent.
High-risk hook = do not amplify.
Human seals.
```
