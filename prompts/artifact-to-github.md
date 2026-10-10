---
title: "Artifact → GitHub — 完成した成果を、担当原本へ確かに渡す"
version: "v001-human-authorized"
edition: "First explicit version in the modernized prompt series"
canonical_path: "prompts/artifact-to-github.md"
role: "Placement and result-verification prompt for completed artifacts"
status: "active / Human-authorized modernization / field effects unverified"
created: "2026-10-10"
updated: "2026-10-10"
source_path: "ss_super-special/artifact-to-github.md"
source_commit: "0d21990a126948703eca517c65017f2038d4393c"
source_blob: "23ad62b54debb8af62d4eb62b8f3187afe98ab07"
change_record: "../control-center/changes/STR-014-super-special-prompt-modernization.md"
expected_eof: "EOF::ARTIFACT_TO_GITHUB::v001-human-authorized"
---

# Artifact → GitHub

**完成済みArtifactを、現在の目的・権限・保存先の契約に沿ってGitHubへ配置し、Remoteの実体まで確認するための共通Prompt。**

## 1. 入口と責務

本文生成のRailは成果の意味と品質を育て、本Promptは配置・必要な参照整合・保存確認を扱う。生成PromptのそれぞれへGitHubの操作条件を複製しない。保存のための通常の修正を行う場合も、原文・意味・Sourceを無断で別物へ変えない。

起動例：

> このArtifactをGitHubへ保存してください。現在の依頼・有効な承認・担当原本からRepository、Ref、Path、変更範囲を解決し、並行変更を保持して保存後の実体まで確認してください。

「どこへ置くべきか検討して」のようなPlan-onlyは、調査・配置案の提示で止める。このPromptの読取、完成Artifactの存在、Download Skipの指定は、書込承認ではない。Humanの現在の指示を意味で判断し、特定の合言葉や全Pathの手入力を毎回要求しない。

適用時はmetadataからExact EOFまで読む。同一会話で同一blobを全文確認済みなら再利用できる。GitHub作業の共通判断・権限・中断回復は[AGENTS](../AGENTS.md)、文書選択は[Prompts](README.md)、保存データの契約は対象の近接ガイドが所有する。明示Handoff・Binding・必須Source・STOPを上書きしない。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanはMeaning・Correction・STOP・Final Sealを保持する。Artifact・GitHub・このPromptはKeliである。適用Guardと公開範囲を保持し、ChatGPT長期メモリをGitHubへの転記・同期Sourceにしない。

## 2. 入力を現在の文脈から束縛する

次を利用できるSourceから解決する。固定の入力フォームをHumanに書かせる義務ではない。

- **目的と権限**：保存・更新・移動・削除・公開・PR作成等のどこまでが今回の依頼か。最新Correction／STOPと継続委任。
- **Source**：完成本文または実ファイル、元の版・範囲・文字列／バイトの同一性、必要な付属物。単なるファイル名を本文取得済みとしない。
- **Target**：正確なRepository、Ref、ファイル名を含むPath。既存Owner、CREATE／UPDATE／NO_CHANGE、変更する箇所と保持する箇所。
- **成立条件**：Required Read、Metadata、Identity、必要なExact EOF、参照先、形式、公開可否。
- **Current実体**：存在、内容、blob／commit、並行変更。APIのsuccessだけで本文一致を推測しない。

不足があれば、既存の資料から回復できるものを先に調べる。AIが通常の配置判断を引き受けられる場合は具体化する。曖昧さが上書き・公開範囲・別Ownerへの変更に影響する場合だけ、その差分をHumanへ返す。必須Sourceの欠落はそのFailure Contractを使い、旧版や要約で埋めない。

完成していないSourceは、未完成の部分を明示する。現在の依頼に制作・補修まで含まれるなら担当の生成工程へ戻って完成させる。含まれなければ、保存済み・準備完了と扱わない。Binaryや添付物の実体を、Markdownの説明だけで置換しない。

## 3. 保存先と変更単位を決める

既存の担当原本を優先し、同等の現役原本を増やさない。成果物、経験、再利用lesson、Actorの出来事、Board通信、構造変更記録の担当を区別する。必要なら[save Skill](../skills/save/SKILL.md)が保存対象とOwnerを選ぶ入口になる。本書は完成ArtifactのGitHub配置を具体化し、Skill本文を複製しない。

main・指定Ref・隔離作業の扱いはAGENTSと現在の承認に従う。作業用Branchは公開・merge承認と別であり、mainへの反映が目的なら未統合のBranchだけで完了にしない。PR作成までの依頼をmergeまで拡張しない。

相互依存する本文・案内・移動・削除は、参照が整合する一組として扱える。「1ファイル1コミット」「必ず一つずつ公開」を全案件に強制しない。同一Pathへの並行書込は避け、統合担当が内容と順序を管理する。対象外の変更・未知フィールド・既存履歴を保持する。

一括tree／commitを使う場合は、未公開の変更全体を確認してからRefを更新する。存在しない新Pathを指す入口だけ先に公開することを避ける。公開直前のhead／blobを照合し、競合したら現状を読んで必要な差分を統合する。古いRepository全体の巻戻しで解決しない。

## 4. 実行前のLiving Review

短い自己点検で、今回何が良くなり、どの価値が失われ得るかを確認する。

1. Sourceが今回保存する完成物であり、Humanの最新Correctionを含むか。
2. Targetが意味を持つOwnerであり、不要な重複・削除・公開範囲の拡大がないか。
3. 現在の承認で必要な変更と確認まで進めるか。
4. 参照・版・形式・必須条件と、並行変更を保持できるか。
5. 完了を何で観察でき、失敗・結果不明ならどこから回復するか。

既に満たす条件を毎回Humanの再承認へ戻さない。保存先や方法の変更が承認の実質を広げる時は、その部分だけ止める。適用Guardやアクセス拒否を、別のTool・Manual Pack・改名等で迂回しない。

## 5. 保存・確認の流れ

### 5.1 準備と保存

現在利用できる正規のConnector・API・CLI等から、その環境で許可された経路を選ぶ。必要なら利用可能な`resolve-github-runtime` Skillを使い、存在しない旧Pluginの探索を繰り返さない。Skillがない環境でも、実際に利用できる正規の能力と適用契約から判断する。

Remoteの対象を読み、作成・更新・変更不要を判定する。ソースと同一ならNO_CHANGEにできるが、必要な配置・参照・成立条件が満たされていることも確認する。更新は最新内容を基点に、承認された差分だけを適用する。

変更を準備し、本文・参照・必要なmetadata／EOF等を検査した後、現在の権限で保存する。DownloadファイルやZIPを毎回生成する規則は置かない。Humanが受け取るファイル自体を依頼している場合は、その成果も満たす。

### 5.2 Remote確認

書込後は対象Ref／Pathの実体を再取得し、意図した全文またはバイト、必要なMetadata・Links・EOF、返却SHA／commitを照合する。rename／move／deleteを含む場合は、新住所、旧配置の消失、保持対象も確認する。

取得できない間は「保存応答あり・内容確認未完了」のように区別する。Tool successをRemote照合済みへ変換しない。検証が通ったら、その成果と実際の証拠を返す。判断を変えない追加検査を無期限に続けない。

## 6. 中断・失敗・結果不明を区別する

| 観測した状態 | 次の判断 |
|---|---|
| 保存成功の応答があり、Remoteの内容も一致 | 今回の完了条件を確認してVERIFIED |
| 応答が失われた／Timeout／実行結果が不明 | OUTCOME_UNKNOWN。先にhead・Path・Job等を調べ、既存結果と残作業を分ける |
| Remoteには意図した内容がある | 再送せず、残る参照・成立条件を確認。変更不要ならNO_CHANGE |
| Toolが失敗を明示し、未反映を確認できた | 原因を修正し、同じ権限内で再試行できるか判断 |
| head／同一項目に並行変更・矛盾がある | Currentを再読し、同じ差分を安全に統合できるか判断。分からない点を上書きしない |
| HumanのSTOP・取消し、承認拒否、アクセス制御の拒否 | 対象操作を停止。別経路で実行させる回復へ進めない |
| 正規の直接経路が技術的に使えず、手動保存は承認範囲にある | 現在内容と適用制約を確認した上でManual Commit Packを選べる |

単なる「非success」を一種類として扱わない。試行回数を一律1回に固定せず、状態・権限・回復可能性に基づいて進める。反復して同じ拒否を受ける場合や安全に状態を復元できない場合は、その操作を保留し、原因・達成部分・再開条件を示す。

## 7. Manual Commit PackとDownload

手動保存は、権限と実体を確認できる場合の正当な受渡し方法である。直接経路が失敗したというだけで、Humanへ危険な全文上書きを渡さない。

必要なPackは次を含める。

- 対象Repository／Ref／Path、操作種別、基点commit／blob。
- 完成本文または正確な実ファイル。省略記号・未完成placeholderを完成物に混ぜない。
- 明確なcommit説明と、保持する既存内容・必要な関連変更。
- 貼付け前に基点との差を確認し、並行編集があれば再統合する条件。
- 保存後に確認する場所と内容。AIが確認できない場合の未確認範囲。

Copy & Pasteする本文と説明を分離し、code fenceを壊さない。利用可能なファイル形式を選び、リンクを表示しただけでファイル提供・保存済みとしない。部分差分が適切な場面では適用箇所と基点を示す。全文置換が必要な場面では、最新内容との統合済み全文を渡す。

Download Skipは、不要なダウンロード工程を省く選択であり、本文欠落や後の適切なファイル提供禁止を意味しない。Manual Packの作成はMANUAL_READYであり、GitHub公開やHumanのCommit実施を示さない。Humanの実行報告とRemoteの確認も分ける。

## 8. 結果の返し方

次のうち判断に必要な情報を、現在の依頼に合う長さで返す。

- 何をどこへ保存・更新・移動・削除したか、またはNO_CHANGEか。
- commit／Pathへのリンクと、実際に確認した内容。
- 未完了・結果不明・保留があれば、影響範囲と最小の回復方法。
- 元の依頼が満たされたか。残る通常Unknownは何か。

保存先がBoardでも、それだけで相手への送達・既読・理解とはしない。文書の存在、整合、別AIの理解、自然選択、実生活効果は別々の成果である。保存完了から新Task・別文書の整備・新しいThread移行を開始しない。

## 9. 構造化補助版との関係

[Programming-like版](artifact-to-github-programming-like.md)は、この手順を状態・分岐・不変条件として理解・検討するためのPromptである。保存手順の意味は本書が所有し、補助版が別の許可条件を持たない。二つを常にセットで起動する必要はない。

補助版で不整合を発見したら、読んだ版と該当条件を示し、主カードに照らして判断する。発見だけから両ファイルの自動改訂やGitHub公開へ進めない。

## 10. 由来・版・確認範囲

[旧主カードの固定版](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/artifact-to-github.md)は、完成物の制作とGitHub配置を分離し、各生成Promptへ保存手順が増殖する問題を扱った。直接経路の制約下でも完成本文を失わないManual Full Body Recoveryも重要な核だった。

今回のHumanは、旧選抜棚の廃止と四Promptの改良・移行を指定し、計画後に実行を承認した。旧本文の「Humanが全exact pathを指定」「1ファイル1commit」「直接は1回」「原則Download」という固定条件を、現行AGENTSの通常判断・継続・結果確認へ整合させた。これはSourceが過去に失敗したという新しい観測ではなく、現在の契約との差の修正である。

旧本文に明示versionはなく、本v001は新しい現代化系列の最初の明示版。形式・意味の確認とRemote保存の証拠は[STR-014](../control-center/changes/STR-014-super-special-prompt-modernization.md)が所有する。ここに書いた回復分岐の全経路を実機試験した、全環境に互換、長期負担が減った、とは主張しない。

EOF::ARTIFACT_TO_GITHUB::v001-human-authorized
