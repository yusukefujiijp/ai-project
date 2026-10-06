---
title: "Control Center — 整理する対象を選び、専門領域へつなぐ"
version: "0.5.0"
canonical_path: "control-center/README.md"
role: "Organization purpose and domain entry; routes to existing evidence and method owners"
status: "human-authorized domain-entry separation; field effects separately observed"
repository: "yusukefujiijp/ai-project"
scope: "整理する対象の共通入口。GitHubは運用資料あり、homeはHuman作成の入口Seed"
primary_reader: "Current AI / other AI / Future AI"
created: "2026-09-22"
updated: "2026-10-06"
updated_reason: "STR-013: locate GitHub plan and archive originals inside github; recognize the Human-created home seed and preserve legacy navigation."
change_record: "changes/STR-013-github-plan-and-archive-relocation.md"
expected_eof: "EOF::AI_PROJECT_CONTROL_CENTER_README::v0.5.0"
---

# Control Center

**何を整理したいのかを明らかにし、その対象に適した判断・根拠・次の接続へ進む共通入口。**

GitHubのフォルダ・ファイル整理は[GitHub専門入口](github/README.md)へ。家の中の整理へ横展開する方向は、Humanが作った[homeの入口Seed](home/README.md)へつながる。対象が分かっている時に本書を毎回経由する必要はない。GitHub専用のPLAN・ARCHIVEは`github/`の原本を使い、本書は全領域の計画・進捗台帳を持たない。

## 1. Humanの意図と最初の目的

この節はHumanとの対話を編集してまとめたもので、逐語引用ではない。

YusukeJPは、AIが十分に調査・判断・言語化・構造化を担い、代々のAIが蓄積した知恵を使って、よりよい構成へ育てることを求めている。Humanは意味・優先順位・Correction・STOP・Final Sealを保持する。承認は、AIの通常判断を細分化して許可するためだけでなく、Humanの閃き・良い案・重大な誤りの訂正を取り込む機会でもある。具体的な対象を承認した後は、その範囲を必要な検証まで遂行する。

形成時の対象はai-project全体の構造整理だった。その実践から、**整理整頓→レイヤー構造→関係の構造化→interface化**を育て、対象ごとにfocusを絞りながら他分野へも活かしたい、という方向が明確になった。2026-10-06の訂正では、GitHub専用名への単独改名案から、共通の親`control-center/`と専門領域`github/`を分ける案へ進んだ。この前段の形成・採否・承認は[STR-012](changes/STR-012-control-center-domain-entries.md)へ接続する。

同日の後続入力では、Human自身が`home/README.md`を改行のみで作り、家の中の整理へ横展開する方向を具体化した。GitHub側の構成と内容の改善をAIへ委任し、PLAN・ARCHIVEを`github/`へ置く案を示した。この訂正と実施根拠は[STR-013](changes/STR-013-github-plan-and-archive-relocation.md)が所有する。homeの存在は確認済みだが、具体的な生活整理や効果はまだ本入口で確認した事実ではない。

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
| [homeの入口Seed](home/README.md) | 家の中の整理というHumanの方向 → 今後の具体化 | 2026-10-06にHumanが作成した改行のみのREADME。GitHub整理の子案件にはせず、今回本文は変更しない |
| [Skills](../skills/README.md)・[Prompts](../prompts/README.md) | 必要な方法 → 方法の所有資料 | 本書に方法本文を複製せず、今回必要なものを選ぶ |
| [経験索引](../task-mode-system/experience/README.md)・[成功事例](../success-cases/README.md) | 出来事・学び → 根拠と成立条件 | 領域間の再利用は条件を確かめる。原本を集め直さない |
| その他の領域 | 実際の依頼・必要性 → 適切な専門入口 | 必要になった対象から判断する。空の領域や計画を先回りして増やさない |

Repository全体の入口は[Root README](../README.md)、ArkのCurrent Main／Supportは[Ark Domain](../ark-project/README.md)が所有する。本書はそれらを置換せず、各Threadの現在地や生活Taskを二重管理しない。

## 4. 他AI・Future AIの使い方

現在の依頼から対象と必要な深さを判断し、専門入口または既知の原本へ直接進む。目的が未整理なら言語化・比較・保留から始められる。毎回全方法論を起動したり、全履歴を読んだりするための入口ではない。明示HandoffのRequired Sources・順序・Identity・Binding・EOFは、その契約に従う。

短い呼出しでも、必要な目的・Correction・成果・未完了・次の条件へ戻れるようにする。保存済みの計画は現在の実行権限ではなく、未報告は失敗や未実行の証拠でもない。権限と中断復旧は[AGENTS](../AGENTS.md)の所有範囲を使う。

元会話を持たないAIが、本書から「なぜ対象別に分けたか」「どこへ進むか」「何がまだ候補か」を説明できることを目指す。文書保存・自己点検・他AIの実理解・実利用の効果は別の観測として扱う。

## 5. 継続して育てる

入口の分離を行ったSTR-012に続き、STR-013ではGitHub専用のPLAN・ARCHIVEの本文を`github/`へ一元化した。旧住所は短い案内のみを持ち、原本や可変状態を複製しない。既存の変更記録・整理指針の所在と役割は[GitHub専門入口](github/README.md#change-records)で分かるようにする。

新しい領域が必要になったら、具体的な目的、既存の担当資料、対象固有の条件を確かめる。既存の入口で足りればそこへ接続し、独立した入口に実益があれば本フォルダの下へ追加できる。homeのSeedから具体的な整理へ進む時も、GitHubのARC番号や計画形式をそのまま生活へ強制しない。共通する学びはその方法・経験の所有先へ戻す。

階層だけを揃えるために全原本を一斉移設せず、意味・所有先・参照の到達可能性を合わせて判断する。配置や方法は改善できる。各作業の承認と完了を分け、HumanのCorrection・STOP・Final Sealを保持する。

EOF::AI_PROJECT_CONTROL_CENTER_README::v0.5.0
