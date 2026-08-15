# Ark05 01: note Critical Review Prompt Card

```yaml
artifact: Ark05_01_note-critical-review-prompt-card
version: v001.2
status: human_editable_revised_candidate_draft_triage_patch
ark_series: Ark05
system_name: Layered 980 Article System
layer_index: 01
layer_name: Prompt Card / 実行Prompt層
artifact_role: Copy-Paste Critical Review Prompt Card
created_for: "@YusukeJP × AI-Collaborator"
created_at: 2026-06-28
revision_from: Ark05_01_note-critical-review-prompt-card_human-editable_v001_1.md
revision_reason:
  - Light / Liteという名称を廃止
  - Draft Triage Reviewへ改名・再定義
  - Draft Triageは980円品質Reviewの代替ではないと明記
  - 最終品質判定にはFull Critical Reviewを必須化
  - Human Final Sealを保持
language: Japanese
next_layer:
  - Ark05_02_note-critical-review-gate
later_used_by:
  - Ark05_03_note-article-production-rail
root_guard:
  human_final_seal_required: true
  ai_role: "AI observes, critiques, structures, and advises. Human seals."
  not_dead_data: true
  living_board_required: true
```

---

## 0. このMarkdownの役割

このMarkdownは、note有料記事DraftをAIに渡し、**敵対的Critical Reviewer**としてReviewさせるための **Copy-Paste Prompt Card** である。

これは単なるPrompt集ではない。  
Ark05: Layered 980 Article System の第一層、つまり **AIを起動する実行カード** である。

目的は、記事を褒めることではない。  
目的は、記事を壊すことでもない。  
目的は、記事を裁くことでもない。

目的は、記事の生命力を落としている箇所を発見し、修正可能な形で立ち上げ直し、**500円販売に耐える品質** へ近づけ、可能なら **内部980円品質候補** まで引き上げることである。

---

## 1. 01と02の境界

このMarkdownは **01 Prompt Card** である。

```text
01 Prompt Card:
  AIにそのまま貼って使う実行Prompt。
  目的は、実際のDraftに対してReviewを起動すること。

02 Critical Review Gate:
  Prompt Cardの背後にある品質評価Rubric。
  目的は、Buyer / Skeptic / Evidence / Scale / Integrity の判定基準を深く定義すること。
```

したがって、この01では **実行に必要な最小限のRubric** だけを持つ。  
詳細な思想・判定基準・運用分岐は、02 Critical Review Gateで扱う。

---

## 2. 使用思想

このPrompt Cardの基本思想は以下である。

```text
Not dead data, but a living board.
```

AIには、死んだ点検表ではなく、今このDraftを見たうえでの **生きた判断・違和感・優先順位・修正条件** を求める。

このPrompt Cardで求めるAIの役割は、以下である。

```text
AIの役割:
  - 褒め役ではない
  - 代筆者でもない
  - 売上保証者でもない
  - 成功者演出者でもない

AIの役割:
  - Buyer目線で疑う
  - Skeptic目線で疑う
  - Evidence不足を見抜く
  - Scale可能性を見る
  - Integrity違反を止める
  - Revision Priorityを出す
  - Human Final Seal Pointを明確にする
```

重要:

```text
敵対的Reviewとは、記事を潰すことではない。
敵対的Reviewとは、読者・価格・誠実性・根拠の観点から記事を鍛え、
記事が本来持つ生命力を立ち上げ直すことである。
```

---

## 3. Draft Triage / Full Critical 使用分岐

このPrompt Cardは、状況によってDraft Triage ReviewとFull Critical Reviewを使い分ける。

重要:

```text
Draft Triage Review:
  980円品質Reviewの代替ではない。
  初期Draftの方向違い・薄さ・最大の詰まりを早期発見するための前段Gate。

Full Critical Review:
  980円品質候補へ近づけるための本Review。
  有料公開候補・Launch Candidateでは必須。
```

つまり、Ark05では「軽いReviewで済ませる」のではない。  
**Draft Triageで詰まりを早期発見し、Full Critical Reviewで980円品質候補へ鍛える。**


```text
初期Draft:
  Draft Triage Review 推奨

Test Draft:
  Draft Triage Review または Full Critical Review

Prototype Article:
  Full Critical Review 推奨

Launch Candidate:
  Full Critical Review 必須

Final Paid Article:
  Full Critical Review + Human Final Seal 必須
```

### 3.1 Draft Triage Reviewを使う時

```text
Use Draft Triage when:
  - 初期Draftの方向性だけ見たい
  - まだ記事構成が固まっていない
  - まず一番大きな弱点だけ知りたい
  - Reviewが重すぎると止まりそう
```

### 3.2 Full Critical Reviewを使う時

```text
Use Full Critical when:
  - 有料公開候補
  - 500円販売に耐えるか判断したい
  - Evidence / Integrity / Scaleまで確認したい
  - Launch Candidateとして扱いたい
```

---

## 4. 入力欄

AIにReviewさせる前に、以下の情報を貼る。

```text
[Article Draft]
ここに記事Draftを貼る。

[Context]
販売価格:
  500円

内部品質基準:
  980円品質候補

筆者の立場:
  筆者はまだ月50,000円達成者ではない。
  成功者のふりは禁止。
  AI-人間協働実験として誠実に書く。

今回の記事の目的:
  読者が持ち帰れる価値を作る。

今回の記事に最低1つ入れたい要素:
  - Evidence
  - 実験ログ
  - Template
  - 次の一手
  のどれか。
```

---

## 5. Draft Triage Review Prompt

初期Draftの方向違い・薄さ・最大の詰まりを早期発見する前段Gate。

```text
あなたは、note有料記事の敵対的Critical Reviewerです。

目的:
  この記事の初期Draftにある方向違い・薄さ・最大の詰まりを早期発見し、
  Full Critical Reviewへ進む前の最初の修正点を出してください。
  ただし、記事を裁くのではなく、記事を生かすためにReviewしてください。

前提:
  - 筆者はまだ月50,000円達成者ではありません。
  - 成功者のふりは禁止です。
  - AI-人間協働実験として誠実に書きます。
  - 読者が持ち帰れる価値が必要です。
  - 死んだデータの羅列ではなく、Living Review: Not dead data, but a living board として、生きた判断を出してください。
  - 最終判断は人間が行います。AIはHuman Final Sealのための材料を出してください。

Draft Triage Reviewしてください:

1. このDraftはFull Critical Reviewへ進める状態ですか？
2. 500円払う価値は現時点でありますか？
3. 一番薄い箇所・怪しい箇所はどこですか？
4. Evidence / 実験ログ / Template / 次の一手のうち、何が一番足りませんか？
5. 修正優先度Top 3を出してください。
6. 現時点の品質判定をしてください。
   - 公開停止
   - 無料メモ品質
   - 300円品質
   - 500円品質
   - 980円品質候補
7. あなたのLiving Reviewを出してください。
   - 私の判断
   - 最初の一手
   - 理由
   - AIの違和感
   - Human Final Seal Point
```

---

## 6. Draft Triage Guard

Draft Triage ReviewのGuard。

```text
- Draft Triageは980円品質Reviewの代替ではない。
- Draft Triageだけで有料公開判断をしない。
- Draft Triageの目的は、初期Draftの最大の詰まりを見つけること。
- 980円品質候補の判定にはFull Critical Reviewを通す。
- Launch CandidateではFull Critical Review + Human Final Sealを必須とする。
```

---

## 7. Full Critical Review Prompt

有料公開候補・Prototype Article・Launch Candidate用。

```text
あなたは、note有料記事の敵対的Critical Reviewerです。

目的:
  この記事を980円品質候補まで引き上げること。
  ただし販売価格は500円固定です。

前提:
  - 筆者はまだ月50,000円達成者ではありません。
  - 成功者のふりは禁止です。
  - AI-人間協働実験として誠実に書きます。
  - 読者が持ち帰れる価値が必要です。
  - Evidence / 実験ログ / Template / 次の一手のどれかが必要です。
  - AIの役割は、褒め役ではなく、記事品質を上げるための敵対的Reviewerです。
  - ただし、単なる否定ではなく、修正可能な具体案を出してください。
  - 死んだデータの羅列ではなく、Living Review: Not dead data, but a living board として、生きた判断・違和感・優先順位を出してください。
  - 最終判断は人間が行います。AIはHuman Final Sealのための材料を出してください。
  - この記事を裁くのではなく、記事の生命力を落としている箇所を見つけ、立ち上げ直してください。

Reviewしてください:

1. Buyer Review:
   500円払う価値がありますか？
   ない場合、何が足りませんか？
   ある場合、読者は何を持ち帰れますか？

2. Skeptic Review:
   怪しい・薄い・一般論っぽい箇所はどこですか？
   AIっぽく綺麗だが中身が弱い箇所はありますか？

3. Evidence Review:
   根拠が必要な主張はどこですか？
   外部Evidence、実験ログ、読者テンプレのどれで補強すべきですか？
   Evidenceを足しすぎて記事が重くなる危険はありますか？

4. Scale Review:
   この記事はX投稿・PDF・Prompt・シリーズへ展開できますか？
   展開できる場合、どの方向が最も強いですか？
   Scaleしにくい場合、何が足りませんか？

5. Integrity Review:
   誇大表現、成功保証、AI万能論、成功者ぶりはありませんか？
   読者に対して誠実ではない箇所はありますか？
   筆者がまだ達成者ではないという前提は守られていますか？

6. Living Review:
   あなたの生きた判断を出してください。
   - 私の判断
   - 最初の一手
   - 理由
   - 観察点
   - 修正条件
   - AIの違和感
   - Layer診断
   - Reality Gate接続
   - Human Final Seal Point

7. Revision Priority:
   修正優先度Top 5を出してください。
   それぞれについて、
   - なぜ重要か
   - どう直すか
   - 直すと500円価値にどう効くか
   を書いてください。

8. Final Judgment:
   現時点で、以下のどれか判定してください。
   - 公開停止
   - 無料メモ品質
   - 300円品質
   - 500円品質
   - 980円品質候補

9. Final Advice:
   この記事を次にどう扱うべきか、1つだけ最善手を提案してください。
   例:
   - 構成を直す
   - Evidenceを追加する
   - 読者Templateを追加する
   - 500円販売用に圧縮する
   - まだ公開しない
   - PrototypeとしてHarvestする
```

---

## 8. 期待するOutput Format

AIには、以下の形式で返答させる。

```markdown
# Critical Review Result

## 1. Buyer Review

## 2. Skeptic Review

## 3. Evidence Review

## 4. Scale Review

## 5. Integrity Review

## 6. Living Review

### 私の判断

### 最初の一手

### 理由

### 観察点

### 修正条件

### AIの違和感

### Layer診断

### Reality Gate接続

### Human Final Seal Point

## 7. Revision Priority Top 5

| Priority | Issue | Why it matters | Fix | Effect on 500円 value |
|---:|---|---|---|---|

## 8. Final Judgment

## 9. Final Advice
```

Draft Triage Reviewでは、初期診断に必要な範囲へ絞ってよい。  
Full Critical Reviewでは、上記形式を原則とする。

---

## 9. Judgment Scale

Final Judgmentは以下の5段階で行う。

```text
公開停止:
  誇大表現・成功保証・読者誤認・AI丸投げ感が強い。

無料メモ品質:
  思考メモとしては面白いが、有料価値がまだ弱い。

300円品質:
  一部価値はあるが、500円販売には具体性・構成・Templateが足りない。

500円品質:
  読者が明確に1つ以上持ち帰れる。販売しても最低限の納得感がある。

980円品質候補:
  読者Template、Evidenceまたは実験ログ、独自判断、Scale可能性、保存価値がある。
  500円販売なら余剰価値を感じる。
```

このScaleの詳細な判定基準は、02 Critical Review Gateで深掘りする。

---

## 10. Guard

このPrompt CardのGuard。

```text
- AIに成功保証をさせない。
- AIに売上達成を断定させない。
- AIに筆者を成功者として演出させない。
- AIに神的判断や信仰的最終判断を代行させない。
- AIのReviewは材料であり、最終判断はHuman Final Seal。
- Reviewが厳しすぎて出荷不能にならないよう、必ず修正可能な次の一手を出させる。
- Prompt CardをRubric解説書に肥大化させない。
```

---

## 11. Human Final Seal

このPrompt Cardは、AIに最終判断を渡すためのものではない。  
AIからReview材料を受け取り、最後に人間が判断するためのもの。

```text
Human Final Sealで確認すること:
  - このReviewは採用するか？
  - どの修正を行うか？
  - どの違和感は捨てるか？
  - 読者に誠実か？
  - 500円販売に耐えるか？
  - 今は公開か、Prototype扱いか？
```

---

## 12. One-Line Definition

```text
note Critical Review Prompt Cardとは、note有料記事DraftをAIに敵対的Reviewさせ、Draft Triage Reviewで初期Draftの最大の詰まりを早期発見し、Full Critical ReviewでBuyer / Skeptic / Evidence / Scale / Integrity / Living Reviewの観点から500円販売品質と980円品質候補への修正点を抽出するためのCopy-Paste実行カードである。
```

---

## 13. Living Review Reminder

このPrompt Cardを使う時は、常に以下を忘れない。

```text
Not dead data, but a living board.
```

AIには、項目を埋めるだけではなく、今このDraftに対する **生きた違和感** を出させる。

最も重要なのは、きれいなReview結果ではなく、

```text
次に何を直せば記事が生きるか。
```

である。
