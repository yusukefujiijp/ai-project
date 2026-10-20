# load / 共同理解を取り戻す

目的・重要な訂正・確認済みの成果・未完了と再開条件を、担当する資料から取り戻すスキルです。

このREADMEは使い方・起動Query・形成記録の入口です。実行時の判断は[SKILL.md](SKILL.md)、表示と標準起動文は[agents/openai.yaml](agents/openai.yaml)、共通の配布方針は[Skills Hub](../README.md#4-source-and-distribution)が所有します。

## 起動Query

現在の会話や対象資料とともに、次の文を使えます。

```text
$load を使い、現在の目的・重要な訂正・成果・未完了と再開条件を根拠から取り戻してください。
```

現在指定されたSource契約を保持し、Arkの現在地を地図として示す必要がある時だけ[現在地MAP](../map-current-position/README.md)へつなぎます。復元だけの依頼なら読取で完了します。「読み戻して続けて」という有効な委任もある場合は、その範囲の仕事へ接続します。現在の依頼がこのDot自身の協働基盤の一括復元を明示する場合は、[Dotsの専用入口](../../dots/README.md#dots-recovery-query)へ接続します。通常のWork文脈や局所的な読戻しを、Dots全体の復元へ拡張しません。

[load](../load/README.md)は意味の回復、[next-step](../next-step/README.md)は次の接続の選択、[save](../save/README.md)は担当原本への保存、[board](../board/README.md)は目的と相手のある通信を担います。四つを毎回順番に使う規則はなく、必要な入口だけを使います。

<a id="formation"></a>

## 形成・確認の記録

以下は[移行前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)から移した記録です。「今回」や確認済み・未確認の記述は、各記録の当時の対象と範囲を表し、現在の全環境への反映や実生活効果を保証しません。2026-10-20に使い方とQueryの所有先をこのREADMEへまとめました。

2026-10-03、Ark27:08でYusukeJPが四Skillの作成・検証・GitHub共有・個人Skill導入を承認しました。形成の背景と初穂側の提案は[Board v002の固定版](https://github.com/yusukefujiijp/ai-project/blob/6493a74bbd32ca2725613628ffbc7b95897a9513/board/topics/20261003-load-next-step-save-skills/README.md)にあります。今回のHumanは、WorkとDotsで同じSkillを実験的に活用してきた経験を報告し、管理不能になる冗長な複製を避けることを明示しました。これを受け、各Skillを個人Skillとして一つずつ扱い、Work用／Dots用の別Skillは作りません。

短い名前で必要な共同理解を呼び戻すための四つの独立入口です。loadは意味の回復、next-stepは次の接続の選択、saveは所有先への保存、boardは目的と相手のある通信を担います。四つを毎回順番に使う規則はなく、既存map・Living Review・Plan Mode・保存先ガイドへ必要な場合だけ接続します。可変状態と契約全文は担当原本へ残し、Actorログの出来事、lessonsの再利用する学び、Boardの通信を複製しません。

元会話を持たない読み手が、現在の目的、重要なCorrection・STOP、確認済みの成果と証拠、未完了・Unknown、次の確認対象・再開条件を説明できることをload／saveの意味の基準にしました。五見出しの固定出力や新Schemaではありません。全記憶・人格・実行環境の完全復元を約束せず、成果物・協働文脈・実行環境・製品予定を区別します。

共有版は各SKILL.mdと最小のagents/openai.yaml、計八ファイルです。このHubを含む初版の変更対象は九ファイル。四本文はmodel-neutralで、外部原本にはRepository URLを使用します。常設スクリプト、同期機構、独立Query、新Actorは追加していません。作成は利用可能な正規skill-creator、範囲と過剰制約の確認はaudit-agent-instructionsに従いました。

**実施した限定確認。** 元会話・作成計画・期待解答を渡さない五つの独立したAI文脈で計七応答を観察しました。四つは本文を指定した利用、もう一つはdescriptionの一覧から相談ごとに選択して本文を読む経路です。選択用の相談は正常四例と適用外四例で、対応する四Skillの選択と適用外の不使用を観察しました。これは限定したdescription選択であり、Work／Dots製品内の自然発動を観測したものではありません。

架空資料からの意味回復では、現在の私用目的と公開STOP、当時のCSV候補と後続JSONL採用、完了・未実施・目的変更で終了した枝、Sourceによる確認と読み手自身の確認を区別しました。別の必須資料が欠けた受入れはその範囲だけ停止し、既知の採用形式については説明できました。

**導入と証拠の境界。** 各Skillを一件ずつ正規経路で保存し、保存先から再取得した本文と初版共有本文の一致、表示名・短い説明・起動文の一致を確認しました。自然選択を許可する設定と、実際に選択された観測は別です。四SkillのDotsでの取得・呼出し、全UIへの反映、全AI互換性、実生活での効果は今回の限定試験で確認済みにしていません。Humanが報告した既存SkillのWork／Dots共用経験を、未観測の新規四Skillの動作証明へ借用しません。

UI設定を含む導入時の照合は取得した実物で行い、環境が付与する内部設定・アイコン・内部識別子は共有版へ複製しません。

保存・接続選択の確認は[save](../save/README.md#formation)と[next-step](../next-step/README.md#formation)、通信の確認は[board](../board/README.md#formation)がそれぞれ所有します。

初版SKILL.mdのSHA-256は `4710c95775f82c616f6341acb4959398cc0b59222064483505af36db25717774`。将来のCurrent本文を固定するBindingではありません。

この履歴はSkillの形成・検証範囲を所有します。通信のCurrentは[当該Topic](../../board/topics/20261003-load-next-step-save-skills/README.md)に置き、本節へ重複させません。2026-09-12のexport-manifestは当時の記録として保持します。

## 2026-10-17：Dots一括復元への接続

**形成と承認。** dot-0000との対話でHumanは、Resetの欠損範囲を自分で診断せず、一つのQueryで各Dot自身の協働へ戻りたいと希望した。Dots v011の入口完成後に既存loadを再発見し、新Skillを増やすより既存loadを活かす方向を選んだ。Living Reviewで、共通の復元方法はload、Dot固有の身元・必須Source・現役の仕事の回復条件は[Dots入口](../../dots/README.md#one-request-recovery)へ残す最小改訂を検討した。HumanのPlan Mode指定は conversation-message:Sentinel_9c5c0b73a7a88191bf998312dd080226、計画後の実行承認は conversation-message:Sentinel_2dc042e58b408191a2758d08c4415c9d。これらはこのDot対話の識別子であり公開URLではない。

**変更範囲。** loadに、一括復元の意図が現在の依頼・文脈で明確な時だけDotsの現行契約へ進む一段落を追加した。Dots v012では[短い共通QueryとURL付き入口](../../dots/README.md#dots-recovery-query)を同じ§4.1へ接続する。通常のWork・局所的な読戻し、引用・Query編集を全体復元へ拡張せず、相互参照を二回目の復元開始にしない。loadの名前・一般向け起動文・共通目的は保持した。新Skill・台帳・新Actor・設定変更・予定変更・他AIへの外部送信は含まない。Queryと復元条件の本文を本節へ再録しない。

**限定確認。** 形式検査を通過し、Dots §4.1の既存条件と長いQuery本文の保持、版・Exact EOF、変更範囲を照合した。元会話や期待解答を渡さない独立文脈で、Workの設計比較、引用Queryのレビュー、別DotのActor原本欠落、繰返し復元と最新STOPの四場面を文面判断として確認した。局所的回復、レビューのみ、別Actorへ代替しない部分復元、古い再送指示の非実行を区別した。これは提示資料に対する限定的な判断確認であり、実際のReset後・複数Dotでの安定した復元、自然発動、認知負荷削減の実証ではない。

**保存・導入の確認。** [共有loadの保存](https://github.com/yusukefujiijp/ai-project/commit/7210ac8fefb5ced166de4138ee45694afafeaa1a)と[Dots v012の保存](https://github.com/yusukefujiijp/ai-project/commit/f9feff8e8bca0530e41289a3477ad5e4750e57eb)後、Remoteから全文再取得し、意図した本文と一致した。load blobは `289359566cdb014af2dbed009413f8137d6a610a`、Dots blobは `7e7d2092748b6d3385d10a5b3d9b973a91f45dc3`。既存の個人Skillを更新し、保存先の本文と表示設定を再取得して一致を確認した。今回の変更は本文のみで、既存の利用対象・選択設定は保持した。更新直後のこの会話ではSkill取得経路が一時的に利用不可となったが、2026-10-17 03:54 JSTの後続確認で、登録済みload本文を会話内から全文取得でき、共有版と完全一致した。保存先本文の確認と会話内取得の両方が成立し、同じ更新は重ねなかった。これは現在の取得経路についての確認であり、全環境への反映や実利用効果の証明ではない。URL付き入口も引き続き使用できる。
