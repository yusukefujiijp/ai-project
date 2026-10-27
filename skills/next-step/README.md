# next-step / 次の接続を選ぶ

現在の目的・制約・根拠・依存関係から、今どこへつなぐとよいかを選び、理由と成立条件を返すスキルです。継続が有効なら、その判断を現在のModeに合うNext Queryへつなぎます。

このREADMEは使い方・起動Query・形成記録の入口です。実行時の判断は[SKILL.md](SKILL.md)、表示と標準起動文は[agents/openai.yaml](agents/openai.yaml)、共通の配布方針は[Skills Hub](../README.md#4-source-and-distribution)が所有します。

## 起動Query

現在の会話や対象資料とともに、次の文を使えます。

```text
$next-step を使い、現在の目的・制約・根拠から、今有効な次の接続を選んでください。Skillを直接利用できない場合は、次の共有原本を全文読んで適用してください。取得できなければ、未確認範囲・影響・最小の回復方法を示してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/next-step/SKILL.md
```

現在の権限を保持し、必要時だけ[Living Review](../living-review/README.md)や[Plan Mode](../plan-mode/README.md)へつなぎます。実行、言語化、比較、確認、意図的保留、維持、今回完了のいずれも有効な結果になり得ます。新しいTaskを増やすことを目的にせず、有効な実行委任があればその範囲の必要な仕事へ進みます。

[load](../load/README.md)は意味の回復、[next-step](../next-step/README.md)は次の接続の選択、[save](../save/README.md)は担当原本への保存、[board](../board/README.md)は目的と相手のある通信を担います。四つを毎回順番に使う規則はなく、必要な入口だけを使います。

<a id="formation"></a>

## 形成・確認の記録

以下は[移行前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)から移した記録です。「今回」や確認済み・未確認の記述は、各記録の当時の対象と範囲を表し、現在の全環境への反映や実生活効果を保証しません。2026-10-20に使い方とQueryの所有先をこのREADMEへまとめました。

2026-10-03、Ark27:08でYusukeJPが四Skillの作成・検証・GitHub共有・個人Skill導入を承認しました。共通の形成理由と限定試験の条件は[loadの形成記録](../load/README.md#formation)に残しています。四Skillを個人Skillとして一つずつ扱い、Work用／Dots用に複製しません。

当時のHubカタログは、STOP・旧Gate・通常Unknown・後続実行承認を限定確認の対象として記録しています。限定した試験では、初期Goより最新STOPを保持し、相談後の明確な実行承認で見出しだけを修正して完了しました。統合担当が前後の現物を比較し、saveの試験と合わせた変更が承認された二ファイルだけであることを確認しました。

**導入と証拠の境界。** 各Skillを一件ずつ正規経路で保存し、保存先から再取得した本文と初版共有本文の一致、表示名・短い説明・起動文の一致を確認しました。自然選択を許可する設定と、実際に選択された観測は別です。四SkillのDotsでの取得・呼出し、全UIへの反映、全AI互換性、実生活での効果は今回の限定試験で確認済みにしていません。Humanが報告した既存SkillのWork／Dots共用経験を、未観測の新規四Skillの動作証明へ借用しません。

初版SKILL.mdのSHA-256は `78bf8455ec23941ef1552d1efde97f5526b63ee1a091ff240d9397332ac83ff4`。これは当時の同一性確認用であり、将来のCurrent本文を固定するBindingではありません。共有版はSKILL.mdと最小のagents/openai.yamlです。2026-09-12のexport-manifestは当時の記録として保持します。

## 2026-10-21：Next Queryへの接続

Ark27:11のHuman承認に基づき、共通形式は[AGENTS](../../AGENTS.md#next-query)、接続の選択とGoal・Modeとの一致は[SKILL.md](SKILL.md)が所有する構成へ改訂しました。段階完了とGoal全体の達成を区別し、現在有効な継続先を失わないようにします。出来事・Human評価・同じThreadでの本文再利用は[成功事例](../../references/success-cases/next-query-as-continuation-interface.md)を参照します。文面の改訂・共有保存・導入・他AIの理解・実利用効果は別々に確認します。

## 2026-10-27：継続先の保持と共有原本への入口

Humanは、現在のGoalに有効な接続がある場合のNext Query提示、到達範囲と次の成果、Noneの選択条件を整合する改訂を採用し、14共有原本と既存3 Skillへの反映を承認した。共通判断は[AGENTS §6.2](../../AGENTS.md#next-query)、本Skill固有の判断は[SKILL.md](SKILL.md)が所有する。コピー用起動文とUI起動文に共有原本URL・全文読解の代替経路を含め、導入状況別の本文組立をHumanへ戻さない。共有保存・登録先反映・会話での取得・設定欄・独立読者の理解・実利用効果は別々に確認する。
