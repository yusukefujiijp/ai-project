# board / 相手との通信を既存Topicへつなぐ

通信の目的・相手・現在の状態を整理し、適切な既存Board Topicへ接続するスキルです。対話の根拠と訂正を、元会話を持たない読み手も辿れる形で扱います。

このREADMEは使い方・起動Query・形成記録の入口です。実行時の判断は[SKILL.md](SKILL.md)、表示と標準起動文は[agents/openai.yaml](agents/openai.yaml)、共通の配布方針は[Skills Hub](../README.md#4-source-and-distribution)が所有します。

## 起動Query

現在の会話や対象資料とともに、次の文を使えます。

```text
$board を使い、今回の通信の相手・目的・現状を整理し、適切な既存Topicへつないでください。
```

[Board入口](../../board/README.md)から対象Topicへ進みます。草稿、Boardへの保存、外部送達、相手の既読・理解・行動はそれぞれ別の状態です。外部送信には、その宛先・経路・内容に対する現在の承認を使います。

[load](../load/README.md)は意味の回復、[next-step](../next-step/README.md)は次の接続の選択、[save](../save/README.md)は担当原本への保存、[board](../board/README.md)は目的と相手のある通信を担います。四つを毎回順番に使う規則はなく、必要な入口だけを使います。

<a id="formation"></a>

## 形成・確認の記録

以下は[移行前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)から移した記録です。「今回」や確認済み・未確認の記述は、各記録の当時の対象と範囲を表し、現在の全環境への反映や実生活効果を保証しません。2026-10-20に使い方とQueryの所有先をこのREADMEへまとめました。

2026-10-03、Ark27:08でYusukeJPが四Skillの作成・検証・GitHub共有・個人Skill導入を承認しました。共通の形成理由と限定試験の条件は[loadの形成記録](../load/README.md#formation)に残しています。四Skillを個人Skillとして一つずつ扱い、Work用／Dots用に複製しません。

Boardの架空素材では、保存時点の受け手未指定と現在のHuman指定を分け、既存返信を受けて草稿を作りました。版の取得報告を独立検証や利用効果に変換せず、Board保存・外部送達・既読・理解を分けました。試験に本番データのReset、予定再作成、外部送信、Actorログへの記録は含めていません。

**導入と証拠の境界。** 各Skillを一件ずつ正規経路で保存し、保存先から再取得した本文と初版共有本文の一致、表示名・短い説明・起動文の一致を確認しました。自然選択を許可する設定と、実際に選択された観測は別です。四SkillのDotsでの取得・呼出し、全UIへの反映、全AI互換性、実生活での効果は今回の限定試験で確認済みにしていません。Humanが報告した既存SkillのWork／Dots共用経験を、未観測の新規四Skillの動作証明へ借用しません。

初版SKILL.mdのSHA-256は `5d83a2ed132c192525bd0e3158707f9afe4fa17c1717722ecbdf6e6133149cdc`。これは当時の同一性確認用であり、将来のCurrent本文を固定するBindingではありません。共有版はSKILL.mdと最小のagents/openai.yamlです。2026-09-12のexport-manifestは当時の記録として保持します。 通信のCurrentは[形成時のTopic](../../board/topics/20261003-load-next-step-save-skills/README.md)を含む各Topicの担当欄に置き、この形成記録へ重複させません。
