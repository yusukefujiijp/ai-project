---
name: resolve-github-runtime
description: Resolve the usable GitHub route and applicable instructions when a plugin changes, a declared skill path is missing, metadata and tools disagree, or an upcoming GitHub operation lacks a current verified route. Separate capability, authorization, and uncertainty; avoid repeated stale-path searches and reuse unchanged observations.
---

# GitHub操作の事前確認

GitHubを使う際に、現在利用できる手段・適用される手順・環境の不整合を確認し、依頼に対して取れる次の行動を判断する。これは個人Skillであり、公式GitHub Pluginの同梱SkillやConnectorを置き換えるものではない。既に十分な確認がある通常操作へ、毎回の環境調査を追加しない。

## 現在の依頼と権限を受け取る

依頼の目的、読み取り・変更・計画の範囲、対象、最新のCorrection・STOPを確認する。Hostのsystem / developer指示、アクセス制御、適用されるRepository指示・必須Source契約に従う。本Skillを別の権限順位や承認者にしない。

**環境を示す証拠と、操作を許す権限を分ける。** 道具が呼べることは、現在の依頼で変更してよいことや、対象への書込権限の証明ではない。Plan-onlyでは調査・計画まで進め、外部変更を行わない。有効な実行承認があれば、その範囲で必要な操作と確認を続ける。

## 必要な現在の証拠を集める

現在の問いに必要なものだけを確認する。

- 要求された操作を提供する正規のConnector・API・CLI等と、その環境で定められた利用経路。
- 現在公開されているPlugin metadata、Skill宣言、正確な手順書の所在。Versionは公開されている場合に記録する。
- 適用される手順書が実際に読めるか、要求された対象でどの操作結果を観測したか。
- 操作対象が決まっていれば、正確な `owner/name`、ref、pathまたは対象ID。

metadataの項目が非公開・省略されている状態を、明示的な「Skillなし」と同一視しない。取得不能、未調査、宣言なし、存在確認済みを区別する。公開SourceにSkillがあるだけで、現在の環境にも導入済みと扱わない。

現在公開されたSkill pathが見つからなければ、現行の宣言・所在を一度再解決する。更新された正確なpathを確認し、同じ欠落pathや古いcacheの総当たりを繰り返さない。原因が分からなければ不整合またはUnknownとして残す。新しい証拠が得られた場合は、その差分から再確認できる。

適用される公式Skill・必須手順は、指定された全文読解や順序を守って読む。必須資料が取得できない場合は、その契約が止める操作を停止する。「Skillが明示的に同梱されていない」と「必読のSkillが欠落している」を混同して、別の道具でGateを迂回しない。

## 証拠から次の行動を選ぶ

次の観点を分けて判断し、一つのMode名に不足情報を押し込めない。

- **Instructions:** 何の手順が適用され、どこまで実際に読めたか。未完了の必須Gateがあるか。
- **Capability:** 要求された操作を行う手段が公開されているか。その対象で成功・拒否・結果不明のどれを観測したか。
- **Consistency:** 現在の宣言・ファイル・道具は整合するか。更新途中の不一致か、原因不明か。
- **Authorization:** 現在の依頼で、どの行動まで許可されているか。

手順書が読めるだけでは操作能力を認定しない。読み取り成功を、書き込み成功や全Repositoryへのアクセス成功へ広げない。要求された操作を提供する道具と適用条件が確認できれば、未実施であることを明示して承認済みの実操作へ進める。書込能力の証明だけを目的とした試し書きを前提にしない。

利用可能な経路と必要条件が揃えば、その経路を選ぶ。明示的に同梱SkillがなくConnectorが使えるなら、存在しないSkillを探し続けない。metadataが一部Unknownでも、必要な道具・適用契約が確認でき、未確認事項がその操作を妨げなければ進める。「Connectorが使える」と「Connector-onlyの製品構成が確認できた」は別の主張にする。

必要な能力や必須Sourceが不足する場合は、影響する操作、根拠、再開条件を示す。無関係な許可済みの調査まで一律に止めない。アクセス拒否や承認拒否を、別経路への切替で回避しない。

公開Sourceとの比較は、残る不整合の説明や来歴調査に必要な場合だけ行う。整合、製品・配布経路の違い、包装不整合の可能性、Unknownを区別し、公式説明がない原因は推論とする。一製品の観測から全製品のSkill廃止を断定せず、公開Skillのコピー・再作成・インストールを自動で始めない。

## 対象と実行契約へ接続する

確認済みの `owner/name`、ref、path / 対象IDを後続呼出しへそのまま渡す。依存する操作間で手入力し直して対象を変えない。対象が変わった場合は、その対象の条件を確認する。

ArkのGitHub変更では、現行の[AGENTS](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md)と、成果物の配置・更新なら[Artifact → GitHub](https://github.com/yusukefujiijp/ai-project/blob/main/prompts/artifact-to-github.md)を適用する。それぞれの読解契約を満たし、同一性確認済みの読解は再利用する。保存単位、競合保持、再試行、Remote再取得の詳細は共通契約が所有する。Ark以外では対象の契約に従い、この二資料を無条件の依存にしない。

`404` / `NOT_FOUND` では、Plugin故障と決める前に束縛した対象と呼出し引数を照合する。書込結果が不明なら現在のRemoteを確認してから次を決め、同じ変更を盲目的に再送しない。原因を修正でき、未反映と権限を確認できる場合の再試行は、適用契約に従う。同じ失敗を証拠なく反復せず、全エラー共通の固定試行回数も設けない。

操作成功の応答と、意図したRemote状態の確認を分ける。必要な再取得・照合を終えた範囲だけを完了と報告する。

## 確認結果を再利用する

後続判断に必要な確認結果を、会話内の短い記録等に保持する。新しい台帳やファイルを毎回作る必要はない。

- 確認時点、利用経路、要求された操作、対象。
- 適用手順と読解状況、利用権限の範囲、道具・実結果の根拠。
- 未確認事項と、それが操作を妨げるかどうか。
- 次に取れる行動と、再確認する条件。

Versionやpathが公開されている場合だけ添える。古いversion付きcache pathを将来の実体として固定しない。道具・Version・対象条件の変更、宣言との不一致、重要なエラー、Source変更があれば関係する部分を再確認する。変化がなければ確認結果を再利用し、各API呼出し前に全調査をやり直さない。

説明の深さは現在の依頼に合わせる。通常は判断に効く結果を返し、来歴・不整合・詳細説明を求められた場合は根拠と限界まで説明する。

## 共有原本・代替経路・来歴

現行の共有原本は[このSKILL.md](https://github.com/yusukefujiijp/ai-project/blob/main/skills/resolve-github-runtime/SKILL.md)。登録機構がない環境でも、取得した本文を指示資料として使えるが、導入済み・自然発動済みとは称しない。[このSkillのREADME](https://github.com/yusukefujiijp/ai-project/blob/main/skills/resolve-github-runtime/README.md)は、起動Query・来歴と、登録済みSkillが利用できない場合も共有原本へ辿れる入口を所有する。原本の保存、登録先反映、会話での取得、実際の挙動を別々に確認する。

[Ark23の代替記録](https://github.com/yusukefujiijp/ai-project/blob/51cb57189c95c53a0ca97282abf8cd3c100507b6/ark-project/ark23/ark23-03/github-plugin-runtime-best-practice.md)は、2026-08-22の判断・操作報告と成立経緯を示すHistorical Sourceである。Ark23で本Skillが利用できず代替記録が必要な場合、または当時の経緯を調べる場合に読む。適用されるArk23の読取契約があればそれに従う。全場面の追加必読資料にせず、当時のVersion・Mode・成功報告を現在の能力の証拠へ変えない。
