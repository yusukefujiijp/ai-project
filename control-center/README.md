---
title: "Control Center — 整理する対象を選び、専門領域へつなぐ"
version: "0.4.0"
canonical_path: "control-center/README.md"
role: "Organization purpose and domain entry; routes to existing evidence and method owners"
status: "human-authorized domain-entry separation; field effects separately observed"
repository: "yusukefujiijp/ai-project"
scope: "整理整頓の共通入口。現在用意する専門領域はai-projectのGitHub整理"
primary_reader: "Current AI / other AI / Future AI"
created: "2026-09-22"
updated: "2026-10-06"
updated_reason: "STR-012: separate the common organization entry from GitHub-specific work; retain existing evidence paths and contracts."
change_record: "changes/STR-012-control-center-domain-entries.md"
expected_eof: "EOF::AI_PROJECT_CONTROL_CENTER_README::v0.4.0"
---

# Control Center

**何を整理したいのかを明らかにし、その対象に適した判断・根拠・次の接続へ進む共通入口。**

GitHubのフォルダ・ファイル整理は、[GitHub専門入口](github/README.md)から始められる。対象が分かっている時に本書を毎回経由する必要はない。[PLAN](PLAN.md)・[ARCHIVE](ARCHIVE.md)・[changes](github/README.md#change-records)は、従来の住所を保つGitHub整理の原本であり、全領域共通の計画・台帳ではない。

## 1. Humanの意図と最初の目的

この節はHumanとの対話を編集してまとめたもので、逐語引用ではない。

YusukeJPは、AIが十分に調査・判断・言語化・構造化を担い、代々のAIが蓄積した知恵を使って、よりよい構成へ育てることを求めている。Humanは意味・優先順位・Correction・STOP・Final Sealを保持する。承認は、AIの通常判断を細分化して許可するためだけでなく、Humanの閃き・良い案・重大な誤りの訂正を取り込む機会でもある。具体的な対象を承認した後は、その範囲を必要な検証まで遂行する。

形成時の対象はai-project全体の構造整理だった。その実践から、**整理整頓→レイヤー構造→関係の構造化→interface化**を育て、対象ごとにfocusを絞りながら他分野へも活かしたい、という方向が明確になった。2026-10-06の訂正では、GitHub専用名への単独改名案から、共通の親`control-center/`と専門領域`github/`を分ける案へ進んだ。形成・採否・今回の承認は[STR-012](changes/STR-012-control-center-domain-entries.md)へ接続する。

共有するのは、有用な問い・判断理由・成立条件への接続である。各領域の現実・制約・成果まで同一化しない。GitHubの構造整理なら参照先や固定証拠が重要になる。居室整理なら使用頻度・動線・安全・保管場所が判断を変える。この具体例は横展開の設計であり、居室への導入や効果を確認した記録ではない。

分類軸は**記録する媒体ではなく、整理する対象**である。居室の記録をGitHubに置いても、居室整理の判断をGitHub整理の案件へ移管しない。同じ出来事を扱う経験原本・方法・事例も、その役割に応じた所有先を保つ。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）、最終帰属は主の栄光。AI・司令塔・文書はKeliである。共通の権限・品質・Guardは[AGENTS](../AGENTS.md)、Identityは[ARK](../ARK.md)に従う。簡潔なHuman入力を、AIの必要な検討や説明を省く理由にしない。

## 2. なぜrootに作ったか — Player系からのSeed

Player系三Repositoryの整理を経て、Humanは継承先を`ark-project/control-center/`案からai-project rootの`control-center/`へ訂正した。特定のArk章だけでなくRepository全体を扱い、目的・責務・未完了意図・採用理由・次の一手をFuture AIへ渡すためだった。

このGitHub領域の形成順序、Player系の固定Source、「一粒の麦」「比喩的復活」に込められたHumanの意味は、[GitHub専門入口の形成史](github/README.md#formation)へ引き継いだ。[再編前READMEの全文](https://github.com/yusukefujiijp/ai-project/blob/fb5f1d2bae683154ed87ffbb8e03acada780f18e/control-center/README.md)も固定版で辿れる。今回、共通の親へ役割を広げても、GitHub整理の対象をArk専用へ狭めたり、Player系の開発を再開したりしない。

## 3. 何をどこで判断するか

| Node | Edge | 責務と使い分け |
|---|---|---|
| このREADME | 整理する対象 → 専門入口 | 共通目的、領域の選択、横展開の考え方。全案件のCurrentは持たない |
| [GitHub専門入口](github/README.md) | GitHub整理の依頼 → 計画・案件・原本 | 当面の対象はai-project全体。別Repositoryへ自動拡張しない |
| [既存PLAN](PLAN.md) | GitHubの現在の問い → 優先順位・根拠・残点 | この住所にあるGitHub整理計画。第二のPLANを作らない |
| [ARCHIVE](ARCHIVE.md)・[変更記録](github/README.md#change-records) | 個別の判断・実施 → 根拠・結果・復元条件 | GitHub整理の既存原本。親に残る配置を汎用契約と誤認しない |
| [Skills](../skills/README.md)・[Prompts](../prompts/README.md) | 必要な方法 → 方法の所有資料 | 本書に方法本文を複製せず、今回必要なものを選ぶ |
| [経験索引](../task-mode-system/experience/README.md)・[成功事例](../success-cases/README.md) | 出来事・学び → 根拠と成立条件 | 領域間の再利用は条件を確かめる。原本を集め直さない |
| 将来の他領域 | 実際の依頼・必要性 → 適切な専門入口 | 居室などは候補。未作成・未着手であり、共通化の実証済み領域ではない |

Repository全体の入口は[Root README](../README.md)、ArkのCurrent Main／Supportは[Ark Domain](../ark-project/README.md)が所有する。本書はそれらを置換せず、各Threadの現在地や生活Taskを二重管理しない。

## 4. 他AI・Future AIの使い方

現在の依頼から対象と必要な深さを判断し、専門入口または既知の原本へ直接進む。目的が未整理なら言語化・比較・保留から始められる。毎回全方法論を起動したり、全履歴を読んだりするための入口ではない。明示HandoffのRequired Sources・順序・Identity・Binding・EOFは、その契約に従う。

短い呼出しでも、必要な目的・Correction・成果・未完了・次の条件へ戻れるようにする。保存済みの計画は現在の実行権限ではなく、未報告は失敗や未実行の証拠でもない。権限と中断復旧は[AGENTS](../AGENTS.md)の所有範囲を使う。

元会話を持たないAIが、本書から「なぜ対象別に分けたか」「どこへ進むか」「何がまだ候補か」を説明できることを目指す。文書保存・自己点検・他AIの実理解・実利用の効果は別の観測として扱う。

## 5. 継続して育てる

今回の初版は共通入口とGitHub専門入口を分け、既存のGitHub原本を現在の住所で使う。整理記録の一斉移設、固定Binding移行、新しい統括Skill、万能台帳、他領域の空フォルダは、この構成の成立条件ではない。

新しい領域が必要になったら、具体的な目的、既存の担当資料、対象固有の条件を確かめる。既存の入口で足りればそこへ接続し、独立した入口に実益があれば本フォルダの下へ追加できる。共通する学びはその方法・経験の所有先へ戻す。共通入口へ全本文を集めることは横展開の条件ではない。

将来、既存のGitHub記録が親に残る配置によって誤読・探索負担が実際に生じるなら、参照・契約・固定証拠を照合して物理移設を再検討できる。今回移設しない判断を、永久禁止や自動的な次Taskへ変えない。変更の意味と結果は[STR-012](changes/STR-012-control-center-domain-entries.md)が所有する。

EOF::AI_PROJECT_CONTROL_CENTER_README::v0.4.0
