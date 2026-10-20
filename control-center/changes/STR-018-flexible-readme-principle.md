---
title: "STR-018 — AIが育てる柔軟なREADME原則"
canonical_path: "control-center/changes/STR-018-flexible-readme-principle.md"
record_id: "STR-018"
version: "v001"
record_date: "2026-10-20"
repository: "yusukefujiijp/ai-project"
ref: "main"
base_commit: "57cd94b83ea3ba15e8d6e701c478100eb61bf3e8"
actor: "Work / Ark27:10"
status: "Implemented and remotely verified; behavioral and field effects unverified"
expected_eof: "EOF::STR_018_FLEXIBLE_README::v001"
---

# STR-018 — AIが育てる柔軟なREADME原則

**HumanがREADMEの指定・Seed作成を思い出さなくても、AIが承認範囲で必要な入口を育てられるようにする。** 共通原則は[AGENTS §1.1](../../AGENTS.md#11-readmeをaiが育てる)、Rootの保守案内は[README §9.1](../../README.md#91-readme-delta-check)へ接続する。原則本文を各入口へ複製しない。

## Humanの意図とCorrection

Current Ark27:10対話でHumanは、READMEがあればAIとHumanが最低限の理解や復元へ戻れ、READMEがないと書く場所自体が認識されず後で困る経験を述べた。初案は改行のみでも一フォルダ一READMEだった。その後、100%例外なしの問題を認め、「なるべくならば」という柔軟さと、AIが自由に作成・書き直せる設計を最重要とした。Humanが作成を忘れることを、事前のinstructionsで補いたいという意図である。

本節はこのThreadの直接入力の編集要約であり、外部の公開会話URLや別Actorの観測は追加していない。Plan Modeを繰り返して検討した後、Current Humanは「Execute GitHub OK!」「Human Seal OK!」と実行・継続を承認した。過去のPlan-onlyは検討時点として保持し、現在の実装禁止へ戻さない。

## 変更と境界

- AGENTS §1.1が、活動中の意味あるフォルダでAIが必要なREADMEを判断・作成・改善する原則を所有する。
- 内容・構成・詳しさはAIが目的から工夫する。意味が分かれば書き、情報がない段階では改行のみのSeedも許容する。
- 生成物・第三者構成・固定歴史・親だけで十分な機械的分割等は例外を判断する。固定Template・設置率・全件点検・一括空ファイル生成を課さない。
- 編集の自由は、HumanのMeaning・Correction、歴史の事実・根拠、Binding、現在の権限を消す自由ではない。
- Root READMEの保守節は共通原則へ接続する。今回の対象以外のフォルダを一斉に改訂しない。

[STR-019](STR-019-references-learning-memory.md)は、この原則を使うreferencesの具体的な構成変更であり、本原則の一般的有効性を実証する試験ではない。二件の実装は同じ承認の中で進められるが、全READMEの整備完了を移設や他の仕事の必須Gateにしない。

## 確認と残る観測

公開前に差分・リンク・metadataを確認し、公開後はAGENTSとRoot READMEをRemoteから全文再取得して照合する。具体的なcommitと確認は後続の観測欄へ記す。Git履歴は差分・保存時刻、ここは理由・Human Correction・検証範囲を所有する。保存確認を全AIの遵守、自然な作成行動、復元成功や保守負担減少へ格上げしない。

## 公開後の直接確認

2026-10-20、Work / Ark27:10が[実装commit 66daf53e](https://github.com/yusukefujiijp/ai-project/commit/66daf53e23d54be6bf52341bc7cb3cdcdd7f2170)をmainへ非forceで公開した。AGENTS v004.3-candidateとRoot README v015を含む変更28本文をmainから再取得し、公開候補との全文一致を直接確認した。同時公開のreferences移行はSTR-019が所有する。

AGENTSの変更は§1.1の原則・対応metadata・現用参照、Rootは保守節への接続・references案内・直接成功入口・限定metadataであり、Identity・Human Authority・Guardの意味を維持した。対象外581ファイルのblob/modeが実装基点と同じことをTreeで確認した。文書レビューはAIの限定確認であり、Future AIの実利用試験ではない。

本追記は上記観測の保存である。追記自身の保存後再取得は現在の完了報告で扱い、自己SHAや検証追記の無限循環を作らない。HumanにREADME指定を忘れないよう求める設計から、AIが承認範囲で入口を育てる設計へ進めたが、長期の負担減少や全AIの遵守は未観測である。

EOF::STR_018_FLEXIBLE_README::v001
