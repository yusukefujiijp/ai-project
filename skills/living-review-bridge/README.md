---
title: "Living Review Bridge / living-review-bridge"
version: v001
updated: 2026-11-18
status: human-authorized shared skill / behavioral validation pending
---

# Living Review Bridge

現在の目的に照らして働く価値・問題・改善の余地を読み、制約・権限を踏まえて次の接続を選び、必要ならHumanが使える依頼全文へつなぐ。見出しの再現だけを目的にせず、三節のGoal・対象・方法・条件をそろえる。

## 起動Query

```text
【Living Review Bridge：見立てから次の協働へ】
宛先：このQueryをHumanが直接入力する会話のCurrent AI
Version：v001

- $living-review-bridge を使い、現在の目的・対象・根拠・制約を踏まえて、働いている価値、問題、改善の余地から、次の接続と必要な依頼全文へつないでください。
- Humanの選択と保留、現在の権限、Plan-only、STOP、厳密形式、次の依頼が不要な場合のNoneを保持してください。すでに承認された工程は、その範囲で必要な検証まで進めてください。
- Skillを直接利用できない場合は、次の共有SKILL.mdを実際に全文読み、指示資料として適用してください。取得・表示が切れた場合は未読箇所を回収し、必須資料が取得できなければ未確認範囲・影響・最小の回復方法を示してください。
  https://github.com/yusukefujiijp/ai-project/blob/main/skills/living-review-bridge/SKILL.md
- このQueryの提示自体は、保存・設定変更・公開・外部送信などの新しい実行承認を与えません。現在のHumanの依頼と有効な権限に従ってください。
```

## 役割と境界

[SKILL.md](SKILL.md)は三節の意味の接続と判断を担う。既存の[living-review](../living-review/README.md)は見立て、[next-step](../next-step/README.md)は次の接続の選択を支える。全Skillの連続起動や同じレビューの重複を求めず、通常の対話へ毎回の起動を強制しない。

HumanのCorrection・STOP・選択と適用Guardを保持し、AIや方法を権限者にしない。共有保存、個人登録、実際のAIの理解・挙動、生活上の効果は別々に確認する。共有原本を読めることは個人登録を意味しない。

## 形成と確認の範囲

Humanは、【Living Review】を【Living Review: 改善の余地】へ方向づけ、Next StepとNext Queryを同じ目的へつなぎたいと述べた。Ark00での一件の限定確認ではA・Bが事前条件に未達、Cの厳密形式が合格だった。Aでは受け手に確認Threadの正式名を伝えた時点などの制約があり、原因や一般性を確定できない。

その後、Humanは、元会話や設計を持たないAIにも意味を渡せる自己完結Promptを高く評価し、Skill化と起動Queryの作成を依頼した。今回のSkillはその候補に基づく。元の一件は本Skillの試験ではなく、自然発動・他AIの理解・長期再現性・実生活効果は未確認である。

EOF::LIVING_REVIEW_BRIDGE_README::v001
