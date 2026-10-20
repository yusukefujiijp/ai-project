# save / 意味と根拠を担当原本へ残す

成果・訂正・根拠と再開に必要な文脈を、適切な所有先へ保存し、保存先から読み戻して結果を確かめるスキルです。

このREADMEは使い方・起動Query・形成記録の入口です。実行時の判断は[SKILL.md](SKILL.md)、表示と標準起動文は[agents/openai.yaml](agents/openai.yaml)、共通の配布方針は[Skills Hub](../README.md#4-source-and-distribution)が所有します。

## 起動Query

現在の会話や対象資料とともに、次の文を使えます。

```text
$save を使い、今回残す価値のある成果・訂正・根拠と再開情報を、適切な所有先へ保存してください。
```

既に必要な内容が残っていればNO_CHANGEで完了できます。保存する意味に応じて成果物・経験・日時記録・Actorログ・lessons・Boardを選び、同じ可変状態を複製しません。ChatGPT長期メモリの転記・バックアップ・同期は対象にしません。

[load](../load/README.md)は意味の回復、[next-step](../next-step/README.md)は次の接続の選択、[save](../save/README.md)は担当原本への保存、[board](../board/README.md)は目的と相手のある通信を担います。四つを毎回順番に使う規則はなく、必要な入口だけを使います。

<a id="formation"></a>

## 形成・確認の記録

以下は[移行前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)から移した記録です。「今回」や確認済み・未確認の記述は、各記録の当時の対象と範囲を表し、現在の全環境への反映や実生活効果を保証しません。2026-10-20に使い方とQueryの所有先をこのREADMEへまとめました。

2026-10-03、Ark27:08でYusukeJPが四Skillの作成・検証・GitHub共有・個人Skill導入を承認しました。共通の形成理由と限定試験の条件は[loadの形成記録](../load/README.md#formation)に残しています。四Skillを個人Skillとして一つずつ扱い、Work用／Dots用に複製しません。

隔離したメモ原本では、同一項目の訂正と出典追加を保存後に再読し、並行追加された項目・未知フィールド・順序を保持しました。応答喪失後に既に保存されていた同一結果はNO_CHANGE、保存後に取り消された項目は再作成せず、同一識別子の異なる内容は衝突として保留しました。統合担当が前後の現物を比較し、next-stepの試験と合わせた変更が承認された二ファイルだけであることを確認しました。

**導入と証拠の境界。** 各Skillを一件ずつ正規経路で保存し、保存先から再取得した本文と初版共有本文の一致、表示名・短い説明・起動文の一致を確認しました。自然選択を許可する設定と、実際に選択された観測は別です。四SkillのDotsでの取得・呼出し、全UIへの反映、全AI互換性、実生活での効果は今回の限定試験で確認済みにしていません。Humanが報告した既存SkillのWork／Dots共用経験を、未観測の新規四Skillの動作証明へ借用しません。

初版SKILL.mdのSHA-256は `e02e1e75eff059992ba642fbc6e6d2b5f539587b420394b2447c995ed7cff25b`。これは当時の同一性確認用であり、将来のCurrent本文を固定するBindingではありません。共有版はSKILL.mdと最小のagents/openai.yamlです。2026-09-12のexport-manifestは当時の記録として保持します。
