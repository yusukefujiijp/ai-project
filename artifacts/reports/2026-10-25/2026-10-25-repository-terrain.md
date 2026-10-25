---
title: "689ファイルの地形を読む — 広さと現在の入口を混同しない"
canonical_path: "artifacts/reports/2026-10-25/2026-10-25-repository-terrain.md"
version: "v002"
created: "2026-10-25"
updated: "2026-10-25"
updated_reason: "Move to the first-publication date directory; preserve analysis, source evidence and reader designation."
author_role: "Ark28:07 collaborative AI"
primary_reader: "Human / Current AI / Future AI"
source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
status: "Inventory and selected-entry analysis; not a whole-corpus content audit"
expected_eof: "EOF::REPORT_REPOSITORY_TERRAIN::v002"
---

# 689ファイルの地形を読む

## 全体の広さと、今の目的へ進む道は別である

今回の分析基点には689ファイル、ディレクトリを含めて1,001項目があった。再帰Treeは省略なしで取得できた。しかし、この数から資料の品質、全案件の進捗、全AIの利用状態を判断することはできない。

実際の入口を横断すると、Arkの蓄積は一つの巨大な現役マニュアルではなく、Identity、Currentへの案内、方法、経験、Actor、成果物、歴史という異なる責任を持つ領域へ分かれている。**全体を見渡す価値は、全部を同じ深さで読む義務を作ることより、今回どの責任へ進めばよいかを判断できること**にある。

このReportは全体Treeと、読取付録に示す入口・原本から地形を論じる。689ファイルを全て全文読解した監査ではない。数値はReport追加前の固定snapshotのもので、後続mainのファイル数ではない。

## ファイル数の大きい領域は、何を所有するか

| Node | Edge — 主な役割 | 基点のファイル数 | 数だけでは分からないこと |
|---|---|---:|---|
| ark-project | 番号付き協働 → 各章・Threadの原本 | 224 | どのThreadが現在動いているか、全成果が何か |
| skills | 役割の入口 → 判断方法と配布資料 | 160 | 製品への登録数、自然選択の成功 |
| __archives | 退役資料 → 当時の判断と復元 | 69 | 保存された内容の現在の実行権限 |
| prompts | 方法の選択 → 共通本文 | 34 | 全Promptが毎回必要か、効果が実証済みか |
| control-center | 整理対象 → 計画・案件・専門領域 | 31 | 物理的な居室改善まで進んだか |
| agents | Actorと共通協働 → 担当・通信・経験 | 30 | 自動同期や全Actorの現在稼働 |
| grok | 固有の入口 → その領域の資料 | 22 | 入口外の全Runtimeを検証済みか |
| records | 日付付き活動 → 出来事の根拠 | 21 | 全ての活動が収録されているか |
| artifacts | 作品 → 制作・閲覧・再制作 | 18 | 全作品のHuman到達や効果 |
| references | 学び → 回復と突破の経験 | 13 | 全事例が普遍的な方法か |
| その他の領域・root資料 | 固有目的 → 所有資料 | 67 | 未読内容の意味や現在性 |

数値はTreeのblobをroot直下の領域別に集計したもの。フォルダ数やSkill数とは異なる。特にskillsの160ファイルを160個のSkillと読まない。本文、README、表示設定、補助資料等を含み得るためである。

## 「読む入口」と「保存されている場所」が一致しない例

`torah-project/README.md`は今回のsnapshotでは改行のみだった。一方、配下の[エゼキエル神殿構想][s1]には、Humanの願い、重要な訂正、保留という現在地が具体的に記述されている。親入口が空であることから、領域全体に内容がないとは言えない。

同資料のmetadataの`canonical_path`は`ezekiel-temple/README.md`で、取得した実住所は`torah-project/ezekiel-temple/README.md`だった。**住所表記の不一致を観測した**のであり、これだけで全ての参照や利用が失敗しているとは断定しない。今回はReport保存の範囲であり、この原本は変更していない。

この二点は、全体Treeの構成確認と、本文の読解を組み合わせる意義を示す。Treeだけでは入口の空白はサイズとしてしか見えず、本文だけでは現在の住所との関係を見落とす可能性がある。

今後その領域を扱う目的が生じた時には、親入口が必要か、canonical_pathをどの範囲で整合するかを所有先で検討できる。本Reportから新しい整理Taskを自動作成せず、既存の保留を解除しない。

## 構想を残すことが、正しい到達点になる場合

エゼキエル神殿の原本は、建設・デジタル制作・既存モデル利用を開始する仕様書ではなく、構想と訂正を流さず保持する文書である。[s1] ここには、作れる技術があっても、それがHumanの望む価値を満たすとは限らないという重要な判断がある。

Repositoryの全体Mapを作る時、このような保留を「未完了の実装」と一括分類すると、Humanが選んだ現在地を壊す。ファイルが実在し、意味が十分に保存されたこと自体が、その時点の目的に対する成果になり得る。

同じくアーカイブの存在は、無価値な残骸の多さではない。[Archives][s2]は、通常運用から退役させる判断と、知恵や来歴を残す価値を分ける。ファイル数の削減だけをRepositoryの改善指標にすると、この保存価値を失うおそれがある。

## 全体を俯瞰したAIが、局所の所有を尊重する理由

[Root README][s3]は全体の案内、[Ark Domain][s4]は現在のArk経路、[Agents][s5]はActor領域への入口を持つ。これらを読めば、資料の大きな関係は復元できる。しかし、各Threadの状態、生活の現実、専門の判断を、全体Report一つへ回収する必要はない。

俯瞰が有益なのは、担当が分かれているために見えにくい関係を示せる時である。俯瞰を理由に局所原本をすべて再管理すると、第二のCurrentが増え、更新責任が曖昧になる。

今回のReport集は、所有原本の上に新しい司令塔を作るものではない。問いごとに関係を編集し、根拠と限界を残す。具体的な作業へ進む時は、その所有先と最新のHuman指定に戻る。

## 数を使う時、数で価値を測り切らない

ファイル数や読取数は、調査範囲を明らかにする証拠にはなる。だが、多く読んだから正しい、少ないファイルだから単純、Reportが多いから成果が大きいとは言えない。

有用性を評価するなら、以前見えなかった関係が説明できたか、現在の問いに必要な原本へ戻れたか、誤った再作業を避けられたか、といった結果が重要になる。今回、その長期効果はまだ観測していない。

このCollectionの価値は、全体を読み終えたという宣言にあるのではなく、実際に読んだ範囲から、次の理解に使える論旨と根拠を作ったことにある。未読範囲は付録へ明示し、後のAIが必要に応じて調査を広げられるようにする。

## 根拠

- [固定snapshotの全体Tree][tree] — 再帰取得した1,001項目・689blobの集計。Report追加前。
- [s1: エゼキエル神殿構想 v001][s1] — 構想保存と保留、取得住所とmetadataの観測。
- [s2: Archives v0.12.0][s2] — 退役と保存価値。
- [s3: Root README v017][s3] — Repository全体の入口。
- [s4: Ark Domain v010-human-authorized][s4] — Currentと歴史、各所有原本への経路。
- [s5: Agents v003][s5] — Actor領域の入口と責任。
- [読取範囲と証拠の境界](2026-10-25-reading-scope.md) — 全文・部分・未読の区別。

[tree]: https://github.com/yusukefujiijp/ai-project/tree/ba47216debeb2163a5dbf880c6b37d73edbb7e41
[s1]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/torah-project/ezekiel-temple/README.md
[s2]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/__archives/README.md
[s3]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/README.md
[s4]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/ark-project/README.md
[s5]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/README.md

EOF::REPORT_REPOSITORY_TERRAIN::v002
