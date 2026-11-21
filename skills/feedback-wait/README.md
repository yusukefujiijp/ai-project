---
document_id: FEEDBACK_WAIT_README
title: Feedback待機Mode
version: v001
updated: "2026-11-22"
canonical_path: skills/feedback-wait/README.md
expected_eof: EOF::FEEDBACK_WAIT_README::v001
---

# Feedback待機Mode

Humanが一件の実践・観察へ移るときに対話を区切り、本人が戻ったときはその一言から協働を再開する。正式な一文定義・適用条件・応答手順は[共有SKILL.md](SKILL.md)にある。

## 日常の呼出し

文脈から対象が分かるときは、**「Feedback待機Modeでお待ち下さい」**。呼出し名は `feedback-wait`。待機の単位は指定された一件で、次の応答はHumanの入力を起点とする。短い感想、途中の問い、訂正も、その一件を続ける入口になる。

## 形成の背景

Ark100:08で、YusukeJPは「ベッド上スマホ禁止」を実践し、Feedbackで改善して、自家薬籠中化（受肉化的再現性）を目指した。実践へ移る合図として「Feedback待機Mode」を使ったあと、実験結果の報告に先立って、ベッド上スマホ禁止とTeshuvah・AI活用の優先順位について問いが届いた。対話を再開し、「心のTeshuvah ＞ ベッド上スマホ禁止 ＞ AIで深めるTeshuvah」と整理した。祈りをその場で始め、AIで文字化・明文化して深める場合はベッドの外へ移るという判断である。

この経緯から、結果が出る前の問いにも応じられることを定義に取り入れた。確認できたのは対話の再開と優先順位の言語化までで、実験結果と再現性は本人の報告から扱う。

## コピー用起動Query

このQueryは、対象の一件を話し合った会話で、実践に移るときに使う。別AIや新しい会話で使う場合は、対象が分かる文脈をその相手に伝える。

```text
【Feedback待機Mode：実践に移り、次の入力から再開する】

宛先：このQueryを直接受け取るAI（ChatGPT、Dots、Bots、Agentsなど）
Version：v002
Mode：会話内のFeedback待機

- 直前に話し合った一件の実践・観察に移ります。Feedback待機Modeでお待ち下さい。対象が明らかなら、切り替えを短く受け止めて応答を閉じてください。対象が分からない場合は、その一件を特定するために必要なことだけ確認してください。
- feedback-waitを使ってください。共有原本は次のURLです。スキルを直接使えない環境では、共有SKILL.mdをfrontmatterから実ファイル末尾まで全文読み、name: feedback-wait と見出し「Feedback待機Mode」を確認して適用してください。取得・表示が途中で切れた場合は未読箇所を回収してください。全文を確認できない場合は、未確認の範囲・影響・最小の回復方法を示してください。
  https://github.com/yusukefujiijp/ai-project/blob/main/skills/feedback-wait/SKILL.md
- 次に私から届く結果報告・一言の気づき・途中の質問・訂正のどれからでも、前回の目的と採用した判断を踏まえて同じ一件を続けてください。実践の有無・進み具合・結果は、私が伝えた範囲で扱ってください。
```

EOF::FEEDBACK_WAIT_README::v001
