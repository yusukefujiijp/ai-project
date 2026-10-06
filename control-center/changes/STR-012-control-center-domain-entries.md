---
title: "STR-012 — control-centerの共通入口とGitHub専門入口"
version: "v001-human-authorized"
canonical_path: "control-center/changes/STR-012-control-center-domain-entries.md"
role: "Scoped structure-change rationale, authority, implementation and verification record"
status: "scoped implementation published and remotely verified; independent reader and field effects unobserved"
created: "2026-10-06"
updated: "2026-10-06"
repository: "yusukefujiijp/ai-project"
ref: "main"
actor: "Ark27:08 / Work"
base_commit: "fb5f1d2bae683154ed87ffbb8e03acada780f18e"
expected_eof: "EOF::STR_012_CONTROL_CENTER_DOMAIN_ENTRIES::v001"
---

# STR-012 — control-centerの共通入口とGitHub専門入口

## 1. 目的・形成・Human Correction

GitHub整理に使ってきたcontrol-centerについて、Humanは範囲の広い名前からGitHub専用名へ改め、刷新する案を示した。その後、整理整頓自体を深めながら居室等へ横展開したいという意味を明確にし、**共通の親`control-center/`と、その下の`github/`専門領域**を分ける方向へ訂正した。以下は本会話からの編集要約であり、逐語引用や独立した実証ではない。

対象別にfocusを絞ることと、知恵を他領域へ活かすことを両立させる。共通入口は領域と既存Ownerを案内し、GitHub側は具体的な診断・計画・案件・証拠へ接続する。同じ可変状態や方法全文を二重管理しない。分類するのは整理対象であり、居室の記録をGitHubに保存すること自体はGitHub整理への分類理由にならない。

AIが自由に構成・方法を判断し、Humanが意味・優先順位・Correction・STOP・Final Sealを保持する。複数回のPlan Modeは、Humanの閃き・良い案・重大な誤りの訂正を取り込む機会として求められた。今回、対象の明確な実行承認を受けた後までPlan-onlyを維持したり、通常判断の再承認を増やしたりしない。

## 2. 承認と変更範囲

2026-10-06 JST、本会話で提示した「共通入口の再定義＋GitHub専用入口の新設＋既存PLANの再編＋必要な現役案内と変更記録の整合」に対し、YusukeJPは「まずはcontrol-center/自体の整理整頓から始めましょう」と述べ、GitHub実行・Human Seal・継続遂行を承認した。会話URLは未提示であり作らない。Root、Teshuvah、Human Foreground One、適用Guard、AIはKeliという関係を保持する。

今回の変更は次の五パス。

- `control-center/README.md`：共通目的・領域選択・横展開の境界へ再編。
- `control-center/github/README.md`：GitHub専門入口を新設。形成史と既存の全STR原本への索引を引き継ぐ。
- `control-center/PLAN.md`：GitHubの現在の判断を前へ置き、既存の診断・再設計・補足接続本文を履歴として読み分ける。
- `README.md`：共通入口とGitHub専門入口を区別して案内。
- 本記録：形成、承認、設計理由、実装・検証・残る条件を保存。

既存のARCHIVE、STR-001–011、時点付き整理指針、__archives、Handoff／State、AGENTS／ARK／Domain、Skills、Actorログ等は変更しない。物理移設、固定Binding移行、Skill改訂・導入、他領域の着手、Board送信、Pet、Reset、新Taskは含まない。並行成果を巻き戻さず、ChatGPT長期メモリは保存素材に使わない。

## 3. 調査基点と設計判断

実行基点は[fb5f1d2bae683154ed87ffbb8e03acada780f18e](https://github.com/yusukefujiijp/ai-project/tree/fb5f1d2bae683154ed87ffbb8e03acada780f18e)。再帰Treeは469既存blob、truncated:false。control-centerには15既存ファイルがあり、GitHub専門入口と本記録は未作成だった。対象三既存ファイルは前回の計画基点ab9599bから変わっていない。

計画時の`control-center`検索は82ファイルに一致したが、現役案内・必須Source・固定証拠・履歴を含む。82ファイルすべてを編集する判断にはしなかった。実行基点には、Ark99-00入口、chocoZAPの足部学習資料、Dotsの地図・lesson等の並行変更がある。全件を本作業の意味読解対象にせず、対象外blob/modeとして保持する。

再編前の直接確認Source：

- [control-center README v0.3.8](https://github.com/yusukefujiijp/ai-project/blob/fb5f1d2bae683154ed87ffbb8e03acada780f18e/control-center/README.md)、blob `23b9b8c2d692e54b3c564ac02e50a80437c4547d`。
- [PLAN v0.12.0](https://github.com/yusukefujiijp/ai-project/blob/fb5f1d2bae683154ed87ffbb8e03acada780f18e/control-center/PLAN.md)、blob `982417008ca2ceb88e93a29608e426dde389e836`。
- Root README v006、blob `4fc925c9a195227e20ce6bf945e697adfc0bc68e`。
- ARCHIVE v0.9.0、blob `4dc9a6a0e6f07893c49e9b0ce83767177bf3083f`。必要な案件と後続状態を照合し、今回の再実装証拠へ借用しない。

**入口と原本の所在を分けた理由。** Ark27:08のRequired Sourcesでは、整理指針は固定commit、STR-009はCurrentである。原本の一斉移設はこれらを同じ文字置換で解決できない。今回必要な専門化は入口と責務を明示して実現し、従来の原本住所と必要契約を保持する。親に原本が残ることを隠さず、GitHub専用の原本であると両入口に記す。物理移設は完了したとも永久禁止とも扱わない。

**PLANの判断盤面。** 旧冒頭のSTR-003と過去の「現在地」に加えて最新案件が蓄積していた。現行の判断を前半に置き、§0以降の旧本文は順序・語句・ID・見出し・固定証拠・補足接続契約を保持した履歴として後半へ分ける。D04の後続STR-003、ARC-007／009／010の完了、指針後のSTR-009、STR-011を区別する。ARC-002部分完了、Graph／One-Table未完了、旧Plan目的変更終了を同じPendingへまとめない。

**形成史と重複管理。** Player系からrootへ移した理由とHumanのSeedはGitHub入口へ引き継ぐ。旧共通READMEの形成本文は相対リンクの階層調整を除き保持し、元の全文にも固定URLを付ける。共通親は意味の要約と接続を持つ。PLANの案件案内は結果の索引、各ARC／STRは結果の原本であり、並行する承認台帳を作らない。旧索引から漏れていたSTR-003も、存在する原本への案内として加える。

## 4. 検証と証拠の境界

編集前のUTF-8本文からGit blob SHAを計算し、Remote返却SHA・基点Treeと照合する。編集中は五パスの変更範囲、YAML・自己パス・EOF、相対リンク、新規／変更見出し、既存アンカー、PLANの履歴本文と形成史の保持を確認する。意味の自己点検では、元会話なしに共通親とGitHub領域、Currentと履歴、完了と残点、次の権限を区別できるか確かめる。

公開時は整合したtree／commitを作り、候補本文・Treeを再取得する。mainの基点を再確認し、並行変更があれば保持して統合する。期待する基点を指定してmainを更新し、公開後に五本文・EOF・SHAと対象外blob/modeを再取得確認する。結果不明なら先にRemoteを確かめ、盲目的に同じ書込みを繰り返さない。

保存・文書整合・自己点検は、独立した別AIの実理解、個人Skill導入、UI変更、外部consumerの不存在、長期の探索負担軽減・生活効果を証明しない。これらの通常Unknownを全解消してから完了する契約は追加しない。

## 5. 再検討・復元・次の接続

旧構成の全体は上の基点commitで参照できる。復元が必要なら、その後の変更と現時点の権限を確かめ、対象差分だけを戻す。Repository全体の巻戻しや、並行成果の消去はしない。

親に残る原本の配置が実際の誤読・探索負担を生むなら、当該参照と必須契約に絞って物理移設を再検討する。別領域への横展開は具体的な依頼と既存Ownerから判断する。今回の結果を理由に、移設・居室整理・追加アーカイブを自動開始しない。

## 6. 実施・保存後確認

1. **実装公開。** [commit 74322bfc7f0e6aff9e79b75d81b0ba0a9ebd8083](https://github.com/yusukefujiijp/ai-project/commit/74322bfc7f0e6aff9e79b75d81b0ba0a9ebd8083)で五パスを公開した。公開親は`ba72abc436fb4e7b9301ba01a78c111b059ad2e5`。調査基点fb5f1d2の後に追加された`torah-project/README.md`を検出し、対象との競合がないことを確認して最新基点へ保持した。force:falseとexpected_shaを指定してmainを更新した。
2. **候補と公開後の直接再取得。** 候補Tree `bf43d31c6a2ba80a60524f61f04fe7a075db53fe`と五本文を公開前に再取得した。公開後は`2026-10-06T09:54:56Z`（2026-10-06 18:54:56 JST）までにmainの五本文を直接再取得し、意図した全文・blob・必要なEOFの一致を確認した。Toolの保存成功だけを完了証拠にしていない。
3. **変更範囲。** 公開親の470既存ファイル中、変更したのはRoot README・control-center README・PLANの三つ。新設はGitHub専門入口と本STRの二つで、公開Treeは472ファイル。対象外467ファイルのblob／modeを保持した。ARCHIVE、STR-001–011、整理指針、保管原本、Handoff／State、AGENTS／ARK／Domain、Skills、Actorログ、並行成果を含む。
4. **参照と保持。** 五本文の相対リンク157出現の行き先と、変更文書内の参照見出しを確認した。変更していない五Owner文書への19見出し参照もCurrent blobで確認した。再編前PLANの§0以降の履歴本文はそのまま保持し、旧見出しのアンカーも保持した。タイトル変更で失われる旧アンカー一件は互換アンカーで補った。Player由来の形成本文は、移した節の相対リンク階層調整以外を保持した。YAML・自己パス・版・EOFも照合した。これは全Repository・全外部サイトのリンク監査ではない。
5. **意味の自己点検。** 共通目的から専門入口、GitHub依頼からPLAN、退役判断からARC、構造変更理由からSTR、過去の原本から固定証拠へ戻れることを執筆AIが確認した。旧D04の残点と後続STR-003、完了ARCと部分完了ARC-002、指針当時のJSONL候補とSTR-009採用、STR-011の後続結果、旧Planの目的変更終了を読み分けた。独立した別AIの読解試験とは称さない。

ここまでで、承認された入口・判断盤面・必要な案内の整合とRemote検証を完了した。全原本の物理移設、他領域への実利用、長期効果、UI／個人Skillへの反映は成果に含めない。本追記は実際の確認を保存する記録更新であり、別Taskの開始ではない。追記自身の最終SHAは埋め込まず、記録commitと保存後再取得で最終本文を確認する。次の接続はHuman Reviewとし、新しい入力が既にあればその依頼へ戻る。

EOF::STR_012_CONTROL_CENTER_DOMAIN_ENTRIES::v001
