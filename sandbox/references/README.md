---
title: "Sandbox References — 小さな実験の経験を次へ渡す"
version: "v001"
created: "2026-11-11"
scope: "共通Sandboxで生まれる協働・実験の経験。仕様と実測の詳細は各実験が所有する"
---

# Sandbox References

小さな実験の反応・学び・価値ある成功を、元会話を知らないAIも根拠と条件から読み直せる入口です。[共通Sandbox](../README.md)から、今回の問いに関係する本文と後続訂正へ進みます。Threadや担当AIが変わっても、経験を同じ場所で利用・更新できます。

## 三本の役割と読む場面

| 本文 | 残す意味・読む場面 | 共通契約 |
|---|---|---|
| [feedback.jsonl](feedback.jsonl) | 実験や協働への反応・希望・訂正。次の進め方を選ぶ時、Humanが何に反応したかへ戻る | [Shared Feedback](https://github.com/yusukefujiijp/ai-project/blob/main/references/feedback/README.md)のschema 1・読取・更新契約 |
| [lessons.jsonl](lessons.jsonl) | 失敗・訂正・観測から得る、条件付きの再利用判断。次の比較を設計する時、似た結果を解釈する時に使う | [Shared Lessons](https://github.com/yusukefujiijp/ai-project/blob/main/references/lessons/README.md)、そこが指定する[既存形式契約の第3〜5節](https://github.com/yusukefujiijp/ai-project/blob/main/agents/dots/lessons/README.md#3-全行がlesson--row-schema-2)のschema 2 |
| [success-cases.jsonl](success-cases.jsonl) | Humanが特に価値を認めた成功の意味・形成経緯・成立条件。別条件で再利用したい時に読む | [Shared Success Cases](https://github.com/yusukefujiijp/ai-project/blob/main/references/success-cases/README.md)のschema 1・読取・更新契約 |

三本の共通の意味と専門原本の分担は[共有References](https://github.com/yusukefujiijp/ai-project/blob/main/references/README.md)が所有します。本書へschema全文や共通手順を複製しません。Dotsに置かれた形式契約の利用から、Dots固有のBoot・全件読込・権限を移植しません。

三本は必須の順番・排他的な分類・全件三重保存ではありません。同じ経験へ複数の意味から戻る時も、同じ根拠を独立した複数回の実証として数えません。

## 現在の問いへ使う

次の実験を選ぶAIは、現在のGoalに関係する記録と後続訂正を選び、対象・発言者・本文・sources・成立条件・未確認を読みます。今回に使う部分、条件が違う部分、なお確かめる必要がある部分を判断し、次の一件と理由をNext Queryへ具体化します。全件の精読やSQL仕様の組立をHumanへ戻しません。

現在のHuman Correctionは、保存やlesson化を待たずに反映します。記録の好評価や過去の承認を、現在の実行許可へ変えません。計画・実行・保存・再取得・別AIの理解・実利用効果を区別します。

## 所有先と更新先

- 入力、コード、実行環境、実測、誤りや限界の詳細は各実験のREADME・原本へ。初期の接続先は[SQLite Correction](../sqlite-correction/README.md)です。
- Sandbox内の協働への反応と、実験横断で再利用できる条件付き判断は本領域へ。対象を自然言語とsourcesで明らかにし、無条件の一般則にしません。
- 成果物の事実訂正は成果物の所有原本へ、共通方法の改訂はその所有先へ、根拠と現在の承認を伴う提案として戻します。共有referencesやSkillを自動更新しません。
- 同じ記録の訂正はIDを保持して現行行を更新し、新しい出来事と区別します。各共通契約に従い、更新前の全文・版・全行、並行変更と未知fieldを保持し、保存後に実体を再取得します。

必要な経験から育て、空の将来分類や毎回の記録義務を増やしません。記録へのリンクがあるだけで、全AIの自動読込や恒久記憶が成立したとは扱いません。

## 初期収録と確認範囲

2026-11-11の初期収録は、Humanが公開範囲を限定した進行方法へのFeedback一件と、それに基づく協働の判断・実測した関係付替え比較に基づく判断のlesson二件です。原文転載ではなく、Feedback行のrepresentationはsummaryです。公開会話URL・message ID・正確な発言時刻は未確認で、登録時刻を発言時刻にしません。

SQLite実験に対するHumanの成功評価は未確認です。success-cases.jsonlは0バイトの0件として準備し、例示・管理行・架空の評価を入れません。これは機械的な観測を否定する意味ではなく、その実測を実験原本へ保持する分担です。

配置・記録の構文・保存を確かめることと、別AIが実際に読み直して役立てることは別です。後者は今回未確認です。公開する会話由来の内容は今回認められた要約に限定し、別会話・長期メモリ・個人情報を収集しません。

## 個別実験を撤去する場合

個別実験の撤去は、ここに残す経験の自動削除を意味しません。経験の根拠を記録時点の固定commitへ結び、現在パスがなくても原文・コード・結果へ戻れるようにします。初期の技術lessonは、初回の固定版と今回の結果を記録した版へ接続します。履歴の完全消去や公開範囲の訂正が必要な場合は、その対象と影響を別に判断します。

本領域は共通Sandboxの経験を所有し、個別実験の撤去時も保持します。今回、撤去は行っていません。HumanのMeaning・Correction・STOP・Final Sealを保持し、AI・Referencesは協働を支える器として扱います。
