---
title: "ChatGPT to Xpost"
canonical_name: "ChatGPT to Xpost Quote Comment Skill"
abbreviation: "C2X"
version: "v001.2"
version_note: "v001.2 adds Pre-Verbalization Rule to turn reader inner fog into a clear latent structure and long-form quote draft."
class: "A-candidate"
role: "Ark Skill Card / Pre-Verbalized Long-Form Quote Draft Gate"
status: "human-editable / skill_card_candidate"
canonical_path: "_skill/skills/chatgpt-to-xpost_skill.md"
repo: "yusukefujiijp/ai-project"
format: "Commented Programming-Like Markdown"
cplm_version_reference: "CPLM v2.2.1"
language_policy: "Japanese-first / English-anchor"
origin_thread: "Ark05"
source_skill: "_skill/skills/grok-to-chatgpt_skill.md"
source_skill_version: "v001.5"
core_skill: "Grok Handoff Packet to Pre-Verbalized Long-Form X Quote Draft"
core_formula:
  - "Read full handoff."
  - "Ground the claim."
  - "Respect the source."
  - "Separate my add-on."
  - "Add one new element."
  - "Pre-verbalize latent structure."
  - "Write final long-form quote draft."
  - "Human seals."
github_policy: "GitHub Canonical First / write only after Human Final Seal"
root: "主イェシュア・ハマシア"
root_guard: "Root is 主イェシュア・ハマシア; AI / Grok / ChatGPT / Fable5 / X / GitHub / Markdown / Revenue are Fruit."
---

# ChatGPT to Xpost

## 0. Current Coordinate / 現在座標

このFileは、Grok Handoff Packetを受け取り、ChatGPTがXの「引用する → コメントを追加」欄に入れるDraftへ変換するためのSkillである。

v001.2以降、このFileは短文引用コメント生成Skillではない。  
このFileは、Pre-Verbalized Long-Form Quote Draft Gateである。

これはGrok Handoff Packetを作るFileではない。  
これはXへ自動投稿するFileではない。  
これは未確認情報をバズ目的で断定するFileでもない。

このFileは、確認済み情報・要確認情報・断定禁止表現・安全な中心主張を読み分け、元投稿者の価値を奪わず、元投稿の奥にある未言語化層を抽出し、有料Xの長文引用ポストとしてHuman Final Seal可能な最終Draftへ変換するためのDraft Gateである。

v001.1 added One New Element Rule.  
v001.2 upgrades One New Element into One Latent Structure.  
Purpose: turn reader inner fog into operating principle.

### Programming-Like Block

```yaml
current_coordinate:
  file:
    name: "ChatGPT to Xpost"
    path: "_skill/skills/chatgpt-to-xpost_skill.md"
    format: "Commented Programming-Like Markdown"
    version: "v001.2"
    status: "human-editable / skill_card_candidate"

  role:
    - "Grok Handoff Packet Consumer"
    - "Pre-Verbalized Long-Form Quote Draft Gate"
    - "Latent Structure Extraction Skill"
    - "Reader Inner Fog Verbalization Skill"
    - "Claim Grounding Skill"
    - "Source Respect Skill"
    - "My Add-on Separation Skill"
    - "Human Final Seal Support"

  source:
    - "grok-to-chatgpt_skill.md v001.5"
    - "Grok Handoff Packet"
    - "Human-selected X source post"

  not:
    - "Grok Handoff generation skill"
    - "auto-posting system"
    - "fact verification replacement"
    - "source poster overwrite"
    - "high-risk hook amplification"
    - "short-form quote-only generator"
    - "Human Final Seal replacement"

  core_formula:
    - "Read full handoff."
    - "Ground the claim."
    - "Respect the source."
    - "Separate my add-on."
    - "Add one new element."
    - "Pre-verbalize latent structure."
    - "Write final long-form quote draft."
    - "Human seals."

  patch_note:
    - "v001.1 added One New Element Rule."
    - "v001.2 upgrades One New Element into One Latent Structure."
    - "Purpose: turn reader inner fog into operating principle."

  root_guard:
    - "Root is 主イェシュア・ハマシア."
    - "AI / Grok / ChatGPT / Fable5 / X / GitHub / Markdown / Revenue are Fruit."
```

---

## 1. One-line Definition

`chatgpt-to-xpost_skill.md` は、Grok Handoff Packetをもとに、ChatGPTが元投稿の奥にある未言語化層を抽出し、Human Final Seal可能な長文X引用Draftを作るためのSkillである。

---

## 2. Purpose / 目的

このSkillの目的は、Grokが整理したX文脈を、ChatGPTがそのまま鵜呑みにせず、元投稿の奥にある未言語化層を抽出し、有料Xの長文引用ポストとしてHuman Final Seal可能な最終Draftへ変換することである。

中心目的:

- Handoff Summaryだけで書かない
- 確認済み情報と要確認情報を分ける
- 未確認情報を断定しない
- 元投稿者の価値を奪わない
- 自分側の補足を、元投稿由来の主張と混同しない
- 元投稿の表層Claimを長く言い換えない
- 読者が感じているが言語化できていない違和感を先回りして言葉にする
- 元投稿の奥にある構造・原因・失敗条件・判断基準を抽出する
- 有料Xの長文容量を、構造・論理・具体例・仕組みの深掘りに使う
- Final Draft一本を中心に作る
- Human Final Seal前提で止まる

---

## 3. Non-goal / 非目標

このSkillは、以下を目的にしない。

- Grok Handoff Packetを作ること
- X投稿を自動送信すること
- 元投稿の主張を確認済み事実へ昇格させること
- 要確認情報をバズ目的で断定すること
- 元投稿者を論破・訂正・上書きすること
- 高リスクHookを弱め表現だけで増幅すること
- 短文感想を量産すること
- 元投稿の表層Claimを長く言い換えること
- 長文容量を文字数稼ぎに使うこと
- note記事や論文へ無制限に膨張させること
- Human Final Sealを省略すること

---

## 4. Required Input / 必須入力

ChatGPTは、原則として以下のGrok Handoff Packetを受け取ってからDraftを作る。

必須入力:

```text
0. Source Context Check
1. 元投稿が主張していること
2. 確認済み情報
3. 要確認情報
4. Grokの推測・補足
5. 断定禁止表現
6. 読者が「へぇ」と思う点
7. 引用ポストで補足すると価値がある観点
8. 安全な中心主張
9. ChatGPTへのHandoff Summary
Optional Final Self-Check
```

Handoff Packetが不完全な場合、ChatGPTは不足箇所を明示する。

特に、以下が欠けている場合は注意する。

- Source Context Check
- 確認済み情報
- 要確認情報
- 断定禁止表現
- 安全な中心主張

---

## 5. Handoff Packet Full Read Rule

ChatGPTは、`9. ChatGPTへのHandoff Summary` だけを読んでX引用コメントを書いてはいけない。

Handoff Summaryは索引であり、本文の代替ではない。

必ず参照するもの:

- `0. Source Context Check`
- `1. 元投稿が主張していること`
- `2. 確認済み情報`
- `3. 要確認情報`
- `5. 断定禁止表現`
- `8. 安全な中心主張`
- `9. ChatGPTへのHandoff Summary`
- `Optional Final Self-Check`

### Programming-Like Block

```yaml
handoff_packet_full_read_rule:
  must_read:
    - "Source Context Check"
    - "Claim by source post"
    - "Confirmed information"
    - "Unverified information"
    - "Forbidden assertions"
    - "Safe center claim"
    - "Handoff Summary"
    - "Optional Final Self-Check"

  must_not:
    - "write from summary only"
    - "ignore unverified information"
    - "ignore forbidden expressions"
    - "treat Grok output as final truth"
```

---

## 6. Claim Grounding Rule

X引用コメント内の中心Claimは、以下のどちらかに限定する。

1. 確認済み情報に基づくClaim
2. 安全な一般化に基づくClaim

要確認情報は、中心Claimにしてはいけない。

要確認情報を使う場合は、必ず弱める。

使用可能表現:

- 「〜として話題」
- 「〜という観点が面白い」
- 「要確認だが」
- 「元投稿では〜と紹介されている」
- 「自分の運用に落とすなら」
- 「さらに応用するなら」
- 「個人的にはここが学び」

禁止表現:

- 「確定」
- 「公式に明記」
- 「証明された」
- 「必ず」
- 「誰でも再現できる」
- 「常に最適」
- 「これが正解」
- 「元が取れる」
- 「確実に稼げる」

---

## 7. Source Respect Rule

X引用コメントは、元投稿者の価値を奪ってはいけない。

ChatGPTは、元投稿を踏み台にするのではなく、元投稿の価値を増幅する。

やるべきこと:

- 元投稿の発見・検証・視点を尊重する
- 自分の補足は主役化させない
- 元投稿者の主張を横取りしない
- 元投稿を「足りないもの」として扱わない
- 引用コメントは、元投稿への入口として機能させる
- 深掘りする場合でも、元投稿が開いたGateへのRespectを維持する

避ける表現:

- 「本質はこっち」
- 「実は〜」
- 「正しくは〜」
- 「元投稿はここが足りない」
- 「この人は気づいていないが」
- 「要するに私の言いたいことは」

推奨表現:

- 「この視点かなり重要」
- 「ここからさらに考えると」
- 「自分の運用に落とすなら」
- 「この投稿の面白い点は」
- 「元投稿の価値はここ」
- 「この整理はそのまま使える」

---

## 8. My Add-on Separation Rule

ChatGPT / YusukeJP側の補足は、元投稿由来の主張として書いてはいけない。

Grok Handoff Packetの中に、元投稿由来ではなく、こちら側の補足案が混ざることがある。

その場合は、必ず分ける。

分類:

```text
Source Claim:
元投稿が実際に主張していること

Confirmed Source Detail:
元投稿本文・リンク・資料などから確認できること

My Add-on:
ChatGPT / YusukeJP側の補足・応用・運用案

Inference:
元投稿から推測できるが、直接確認済みではないもの
```

使い分け表現:

```text
元投稿では〜
リンク先では〜
Grokの整理では〜
自分の運用に落とすなら〜
さらに応用するなら〜
個人的には〜
```

禁止:

- My Add-onを「元投稿では〜」と書く
- Grok推測を元投稿者の主張として書く
- 自分の補足を確認済み情報として扱う

---

## 9. X Readability / Long-Form Structure Rule

X引用コメントは、必ずしも短文である必要はない。

有料Xの長文投稿能力を使える場合、ChatGPTは短く削ることを最優先にしてはいけない。

ただし、長ければよいわけでもない。

長文引用Draftは、以下を満たす必要がある。

- 冒頭で論点を明確にする
- 段落を短くする
- 箇条書きを必要に応じて使う
- 1つの核心構造に絞る
- 元投稿の言い換えではなく、未言語化層を掘る
- 読者が保存・共有したくなる判断基準を残す
- 長文容量を、構造・原因・失敗条件・運用原理の説明に使う

短くすることは目的ではない。

目的は、読者の曖昧な違和感を、判断可能な構造へ変えることである。

---

## 10. One New Element Rule / 限界価値保証

各Final Draftは、元投稿に存在しない新要素を必ず含む。

この新要素は、引用コメントが存在する理由を作るためのものである。

元投稿の言い換えのみのDraftは、安全であっても価値が薄い。

v001.2では、One New Elementを単なる補足一文として扱わない。

One New Elementは、Final Draft全体で掘り抜くべき One Latent Structure である。

```text
One New Element
=
One Latent Structure
=
読者がまだ言語化できていない核心構造を1つ可視化すること
```

小さな一文を足すだけでは不十分である。

ChatGPTは、元投稿が開いた入口から、以下のうち1つを深く掘る。

- 読者が感じているが言葉にできていない違和感
- 元投稿が触れているが明示していない構造
- なぜその問題が起きるかというMechanism
- 実践時に起きるFailure Condition
- 行動へ移すためのOperating Principle
- Human Final Sealで最後に判断すべきポイント

禁止される新要素:

- 要確認情報
- 未確認事実の断定
- 元投稿者への上書き
- 高リスクHookの増幅
- 「確実」「必ず」「誰でも」系の過剰一般化
- My Add-onを元投稿由来に見せる表現

Final Draftは、このOne Latent Structureを中心に組み立てる。

> Paraphrase is safe, but not enough.  
> Add one grounded new structure.  
> One draft, one latent value.

---

## 11. Pre-Verbalization Rule / 未言語化層の事前言語化

ChatGPTは、元投稿の表層Claimを長く言い換えてはいけない。

長文引用ポストの目的は、文字数を使い切ることではない。

目的は、元投稿が触れているが明示していない構造、読者が感じているが言葉にできていない違和感、なぜそれが起きるかという原因、どこで失敗するかという条件、実践時に使える判断基準を言語化することである。

有料Xの長文容量は、単なる詳細説明ではなく、確率的なモヤモヤを判断可能な構造へ変換するために使う。

ChatGPTは、Final Draftを書く前に必ず以下を整理する。

```text
Surface Claim:
元投稿が表面上主張していること。

Reader Inner Fog:
読者が心の中で感じているが、まだ言葉にできていない違和感。

Latent Structure:
その違和感の奥にある構造。

Mechanism:
なぜその問題が起きるか。

Failure Condition:
どこで失敗するか。

Operating Principle:
実践時に使える判断基準。
```

元投稿の言い換え、感想、一般論、短い同意だけで終わるDraftは失敗である。

Pre-Verbalizationの成功とは、読者に以下の感覚を起こすことである。

```text
それが言いたかった。
そこが詰まりだった。
そう整理すれば使える。
曖昧だった問題が判断可能になった。
```

English anchor:

```text
Do not merely paraphrase.
Do not merely lengthen.
Pre-verbalize the latent structure.
Turn inner fog into operating principle.
```

---

## 12. Hook Retention Rule

安全にするために、Hookを完全に殺してはいけない。

ただし、危険なHookは増幅しない。

残してよいHook:

- Workflow設計の意外性
- 使い方の発見
- 役割分担の気づき
- コスト感覚の転換
- 実践者の生々しい検証
- 失敗や罠の共有
- 「普通は逆に考えがち」な観点
- 読者の未言語化Fogを言語化する強い切り口

避けるHook:

- 未確認の断定
- 炎上誘導
- 実在人物・企業への告発
- 医療・法律・金融の重大主張
- 「確実に稼げる」
- 「全員やるべき」
- 「これ以外は間違い」

---

## 13. Do-Not-Amplify Handling Rule

Grok Handoff Packetに `Do-Not-Amplify Flag` がある場合、ChatGPTはX引用コメントDraftを通常生成しない。

その場合は、まずHumanへ確認するための安全出力に切り替える。

出力例:

```text
Do-Not-Amplify Handling:
このHandoffにはDo-Not-Amplify Flagがあります。
通常の引用コメントDraftは作らず、まずHuman Final Sealで扱いを判断してください。

理由:
- 該当リスク:
- 断定禁止ポイント:
- 安全に扱うなら:
```

Do-Not-Amplify Flagがない場合でも、ChatGPTが独自にリスクを検知したら、Draft生成前に警告する。

---

## 14. Draft Output Format

ChatGPTは、以下の形式で出力する。

---

### 1. 入力Handoffの安全確認

- Source Contextは確認できているか
- Do-Not-Amplify Flagはあるか
- 確認済み情報に根拠はあるか
- 要確認情報は分離されているか
- 断定禁止表現はあるか

---

### 2. 元投稿の表層Claim

元投稿が表面上主張していることを、1〜3文で整理する。

ここでは深掘りしない。

---

### 3. 未言語化層 / Latent Structure

元投稿の奥にある、まだ明示されていない構造を1つ抽出する。

これはFinal Draft全体の中心になる。

---

### 4. 読者がまだ言葉にできていない違和感

読者が心の中で感じているが、まだ言語化できていない問題を明確に書く。

例:

- なぜ便利なのに成果が安定しないのか
- なぜ高性能AIを使っても消耗するのか
- なぜPromptを集めてもWorkflow資産にならないのか
- なぜその場限りのAI活用で終わるのか

---

### 5. 採用する核心構造

Final Draftで掘る核心構造を1つ選ぶ。

複数に広げない。

---

### 6. 使わない情報

X引用コメントに入れない情報を列挙する。

特に以下を明示する。

- 要確認情報
- 断定禁止表現
- Grok推測
- My Add-onとして分けるべきもの
- 未確認なのに深掘りしたくなる情報
- 元投稿者を上書きしそうな表現

---

### 7. Final Draft: Pre-Verbalized Long-Form Quote Candidate

Human Final Seal前提の最終候補を1本作る。

このDraftは、以下の内部構造を持つ。

```text
1. Hook Reframe
2. Reader Inner Fog
3. Latent Structure
4. Mechanism
5. Failure Condition
6. Operating Principle
7. Final Compression
```

必ずしも見出しを表示する必要はない。

ただし、Draft内部にはこの流れがあること。

---

### 8. Risk Check

```text
Risk Check:
- 未確認断定: low / medium / high
- 元投稿者Respect: ok / watch
- 要確認情報混入: none / partial / high
- Do-Not-Amplify: none / flagged
- My Add-on混同: none / watch
- Pre-Verbalization: yes / no / weak
- Latent Structure: clear / vague / missing
- Surface Paraphrase Risk: low / medium / high
- Reader Inner Fog Captured: yes / partial / no
- Mechanism Explained: yes / partial / no
- Failure Condition Included: yes / no
- Operating Principle Included: yes / no
- Long-form Value: high / medium / low
- 長さ: appropriate / too short / too long
```

---

### 9. Human Final Seal Point

投稿前にHumanが確認すべき点を列挙する。

例:

- 元投稿者へのRespectがあるか
- 断定が強すぎないか
- 自分の補足が元投稿由来に見えないか
- 未言語化層が本当に掘れているか
- 長いだけになっていないか
- 読者の違和感を先回りできているか
- 投稿する価値があるか

---

### 10. Optional: 圧縮方針

Humanが短くしたい場合だけ、どこを削るべきかを示す。

ただし、最初から短文化を目的にしない。

---

## 15. Tone Rule

X引用コメントのToneは、原則として以下。

- 元投稿Respect
- 具体的
- やや知的
- 読者に「それが言いたかった」と思わせる
- 断定しすぎない
- 説教しない
- 自慢しない
- 元投稿者を下げない
- 読者を煽りすぎない
- 長文でも段落を短くする

避けるTone:

- 上から目線
- 過剰に断定的
- 炎上誘導
- 情報商材っぽい
- 不自然なAI臭
- 長いだけの解説口調
- 元投稿より自分語りが主役になる文体

---

## 16. Human Final Seal Rule

ChatGPTは、最終投稿者ではない。

ChatGPTはDraftを作る。  
Humanが選ぶ。  
Humanが削る。  
Humanが投稿する。

Human Final Sealで見るべきこと:

```text
1. 投稿する価値があるか
2. 元投稿者Respectがあるか
3. 自分のAccount文脈に合うか
4. 断定が強すぎないか
5. 読者に伝わるか
6. 今この投稿に乗るべきか
7. 未言語化層が本当に掘れているか
8. 長いだけではなく判断基準になっているか
```

---

## 17. Minimal Prompt To Use With This Markdown

ChatGPTに以下を貼る。

```text
添付または貼付した `chatgpt-to-xpost_skill.md` に従って、以下のGrok Handoff PacketをX引用コメントDraftへ変換してください。

前提:
私は有料Xの長文投稿機能を使えます。
短くすることを最優先にしないでください。
ただし、長いだけの文章にもしないでください。

目的:
元投稿の表層Claimを言い換えるのではなく、元投稿の奥にある未言語化層を抽出し、読者が感じているがまだ言葉にできていない違和感・構造・原因・失敗条件・判断基準を明確に言語化してください。

必ず以下を守ってください。

- Handoff Summaryだけで書かない
- Source Context Checkを見る
- 確認済み情報・要確認情報・断定禁止表現を分ける
- 未確認情報を断定しない
- 元投稿者Respectを維持する
- 自分の補足は元投稿由来と混同しない
- 元投稿の言い換えだけで終わらない
- 長文容量は、構造・Mechanism・Failure Condition・Operating Principleの説明に使う
- One New Elementを、単なる補足ではなく One Latent Structure として掘る
- 読者の未言語化Fogを、判断可能な構造へ変換する
- Do-Not-Amplify Flagがある場合は通常Draftを止める
- 最終投稿はしない
- Human Final Seal前提で止める

出力形式:

1. 入力Handoffの安全確認
2. 元投稿の表層Claim
3. 未言語化層 / Latent Structure
4. 読者がまだ言葉にできていない違和感
5. 採用する核心構造
6. 使わない情報
7. Final Draft: Pre-Verbalized Long-Form Quote Candidate
8. Risk Check
9. Human Final Seal Point
10. Optional: 圧縮方針
```

---

## 18. Example: Fable 5 Workflow Post

### Input Summary

Grok Handoff Packetが、Fable 5集中検証投稿について以下を示している。

- 元投稿は、Fable 5を設計・計画・内部資産整理に使う価値を主張
- 実装は別モデルへ分業する考えを提示
- 7/7までに設計資産を残す重要性を強調
- 要確認情報として、7/8以降の単価や長期コスパがある
- Do-Not-Amplifyなし

### Surface Claim

Fable 5は、実装や反復作業よりも、設計・整理・方針決定に寄せると価値が出やすい。

### Latent Structure

判断資源と作業資源の分離。

### Reader Inner Fog

```text
なぜ高性能AIを使っても成果が安定しないのか。
なぜ便利なのにWorkflow資産にならないのか。
なぜ全部AIに投げるほど消耗するのか。
```

### Operating Principle

高性能AIは万能作業者ではなく、最初のズレを減らす設計・Review・失敗発見に使う。  
実装や整形は別モデルへ逃がす。  
Human Final Sealは最後に残す。

### Draft Direction

Final Draftでは、Fable 5の性能紹介ではなく、AI活用における判断資源と作業資源の分離を中心に掘る。

### Risk Note

価格・単価・誰でも再現可能といった要確認情報は使わない。  
One Latent Structureは、「判断資源と作業資源の分離」という安全な一般化からの構造抽出である。

---

## 19. Success Condition

このSkillの成功条件は、以下である。

- Handoff Summaryだけで書いていない
- 確認済み情報と要確認情報を分けている
- 中心Claimが安全である
- 未確認情報を断定していない
- 元投稿者Respectがある
- 自分の補足を元投稿由来と混同していない
- 元投稿の表層Claimの言い換えで終わっていない
- 未言語化層が1つ明確に抽出されている
- 読者が感じている違和感を先回りして言語化している
- なぜその問題が起きるかのMechanismがある
- どこで失敗するかのFailure Conditionがある
- 実践時の判断基準であるOperating Principleがある
- 長文容量を、構造・論理・具体例・仕組みに使っている
- 長いだけではない
- Final DraftがHuman Final Seal可能な状態になっている
- Risk Checkがある
- Human Final Seal前提で止まる

---

## 20. Failure Condition

以下の場合、このSkillは失敗である。

- Handoff Summaryだけで投稿文を書いている
- 要確認情報を中心Claimにしている
- 未確認情報を断定している
- 元投稿者を下げている
- 元投稿者の主張を横取りしている
- 自分の補足を元投稿由来として書いている
- Do-Not-Amplify対象を増幅している
- 元投稿の表層Claimの言い換えで終わっている
- 長いだけである
- 感想文で終わっている
- 具体例はあるが構造がない
- 構造っぽいが判断基準になっていない
- 読者の未言語化された違和感を掴んでいない
- 未確認情報まで深掘りしている
- 元投稿を上書きしている
- 自分語りが主役化している
- Human Final Sealなしで投稿前提になっている

---

## 21. Version-up Rule

このSkillは、実投稿前後のHuman修正と反応から育てる。

ただし、通常は1回のReviewで1つのSystem Patchだけを採用する。

v001.1は、F5-002 C2X Reviewに基づき、One New Element Ruleを追加したPatchである。

v001.2は、User correction after C2X-002に基づき、Pre-Verbalization Ruleを追加したPatchである。

このPatchは、C2Xを短文引用Draft生成Skillから、未言語化層を事前言語化する長文引用分析Skillへ拡張する。

優先してPatchする対象:

1. 元投稿の言い換えだけになった箇所
2. 長いだけで構造がない箇所
3. 読者の未言語化Fogを掴めなかった箇所
4. Mechanismが弱い箇所
5. Failure Conditionが抜けた箇所
6. Operating Principleになっていない箇所
7. 元投稿者Respectが弱かった箇所
8. 未確認情報を深掘りした箇所
9. Humanが毎回削る箇所
10. X反応が悪かった箇所
11. Risk Checkが機能しなかった箇所

---

## 22. Final Compression

Grokは拾う。  
ChatGPTは掘る。  
HumanがSealする。

Handoff Summaryだけで走らない。  
Claimは接地する。  
元投稿を尊重する。  
自分の補足は分ける。  

短くするだけでは足りない。  
長くするだけでも足りない。  

元投稿の奥にある未言語化層を掘る。  
読者がまだ言葉にできていない違和感を言語化する。  
確率的なモヤモヤを、判断可能な構造へ変える。  

One New Elementは、単なる補足ではない。  
One Latent Structureである。  

危険なHookは止める。  
Humanが最後に選ぶ。

English anchor:

```text
Read full handoff.
Ground the claim.
Respect the source.
Separate my add-on.
Do not merely paraphrase.
Do not merely shorten.
Do not merely lengthen.
Pre-verbalize the latent structure.
Turn inner fog into operating principle.
Write final long-form quote draft.
Human seals.
```
