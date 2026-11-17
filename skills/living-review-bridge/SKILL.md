---
name: living-review-bridge
description: Connect a current purpose and evidence to a revisable Living Review, a reasoned Next Step, and, when useful, a complete Next Query. Use when the Human explicitly asks to connect these three sections, orient improvement toward the next collaboration, or use Living Review Bridge. Do not turn every ordinary review into a mandatory three-section workflow.
---

# Living Review Bridge

現在のHumanの目的に照らして、働いている価値・問題・改善の余地を読み、制約と権限を踏まえて次の接続を選ぶ。必要な場合は、その接続をHumanが使える依頼全文へ具体化する。見出しを埋めること、改善点を必ず見つけること、新しいTaskを増やすことを目的にしない。

## 現在の依頼を受け取る

現在のGoal・対象・根拠・Humanの訂正・残作業・制約・権限を確認する。確認済み事実、Humanの報告、AIの解釈、未確認事項を、判断に必要な箇所で区別する。対象や目的が分からず開始に必要な場合は、最小限の情報を求める。見えない履歴や相手の意図を確定せず、通常のUnknownを一律の停止条件にしない。

## 見立てと判断をつなぐ

Living Reviewでは、現在の目的に照らして、すでに働いている価値、問題、可能性を読む。改善の余地があれば理由を示す。十分に機能している場合は、無理に問題を作らない。

Next Stepでは、見立て・優先順位・残作業・依存関係・制約・権限から、実行、言語化、比較、確認、意図的保留、維持、今回完了などを選ぶ。到達範囲、残る接続、次の成果、選ぶ理由と成立条件を、必要な範囲で示す。

改善の余地があっても、自動的に実装や新Taskを開始しない。Humanの保留を保持し、現在のGoalに有効な接続がある場合は、回答や一段階の完了だけを理由に消さない。

## Next Queryへ具体化する

Humanが次にAIへ依頼することが現在のGoalに有効なら、選んだ接続を、そのまま使える依頼全文として示す。目的・対象・確認済み状態・必要な方法・完了条件・Mode・権限境界をそろえる。

同じ会話の確認済み文脈を活かし、別の受け手が参照できない「上記」や「前回」だけに依存しない。必要な原本の取得先を示し、取得できない場合の影響と回復方法を明らかにする。

依頼本文を示す場合は、直接の受取人を特定し、見出しと本文の間の独立した宛先行と、コピー本文内の宛先を一致させる。名称・URLを推測しない。全文を一つのtextコードブロックにまとめる。Skillを使うQueryは確認済み共有原本URLと、直接利用できない場合の全文読解・取得切れ回収を含める。

現在のGoalについて次の依頼が不要、またはHumanの明示的な保留・終了等で今は提示しない場合は、Next Queryの本文を「- None」の一行だけにする。必要な理由・残点・再開条件はNext Stepまでに示す。

Noneは今回の依頼文の不在を表し、残作業ゼロ、既存承認の取消し、必要な確認の不要を意味しない。

## 権限と例外を保持する

Humanは依頼文を使う・修正する・保留する・使わないことを選べる。未使用だけで追催や新Taskを作らない。

有効な委任で遂行できる工程は、その範囲の必要な検証まで完了する。Plan-onlyでは許可された調査・計画・会話内の案の提示までとし、実装・保存・設定変更・公開・外部送信を暗黙に開始しない。STOPを優先する。

通常の継続回答では、末尾を【Living Review: 改善の余地】→【Next Step】→【Next Query】の独立三節とし、本文を意味ごとの箇条書きにする。

厳密な出力指定、専用Boot／Failure、STOP、無通知条件、相槌、適用される上位の指示が通常形式に優先する。

三節のGoal・対象・方法・完了条件・Modeを照合し、不足や矛盾が見つかれば見立て・判断へ戻る。表示順を固定の思考手順にせず、内部思考の逐語開示を要求しない。

このSkillやQueryの提示自体を、実行・保存・公開・送信の承認にしない。既存のliving-reviewとnext-stepを置き換えず、同一対象のレビューを重複させない。
