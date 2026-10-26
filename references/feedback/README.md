---
title: "Shared Feedback — 反応と訂正から学び直す"
canonical_path: "references/feedback/README.md"
version: "v001"
created: "2026-10-26"
updated: "2026-10-26"
updated_reason: "Establish the shared feedback owner and reuse the existing Report schema 1 without moving domain records."
role: "Shared feedback scope, reading and JSONL contract owner"
row_schema_version: 1
change_record: "control-center/changes/STR-023-shared-references-three-pillars.md"
expected_eof: "EOF::SHARED_FEEDBACK::v001"
---

# Shared Feedback

領域横断の協働や共有基盤に対する反応・評価・希望・提案・訂正を、[feedback.jsonl](feedback.jsonl)へ対象と文脈を保って残す。AIがまだ教訓や成功事例へ整理していない反応も、後から読み直せる根拠にする。三本の分担と専門原本の選択は[References](../README.md)が所有する。

Report等の専門側は本書の行形式・読取・更新契約を参照できる。その参照だけで対象範囲・公開権限・Actor所有関係を共有側へ移さない。

## 1. 対象と反応を一緒に読む

一件の単位は、対象と意味を復元できる一まとまりのFeedbackとする。同じ発言の肯定・批判・提案を保ち、論点ごとの機械的な分割や、別の時点・対象の反応の無条件な統合をしない。Humanの反応を残すことは、その原因についてのAI解釈や、期待する改善効果の実証ではない。

現在の目的・対象・読者・条件に関係する記録と後続の訂正を選んで読む。対象、本文、出典、必要な補足を合わせ、Human原文とAIの編集・解釈、提案と採用、計画への評価と実利用の評価を区別する。利用時の全件読込、Humanによる再説明、lessonや成功事例への全件変換を前提にしない。取得できなかった記録を「Feedbackなし」と判断しない。

保存したFeedbackがそのまま残っていてもよく、未処理Task・追催・期限を発生させない。lessonや成功事例は、必要な記録のIDと出典へ参照で結び、同じ全文を独立して同期しない。既存の適切な根拠から直接判断を育てることもでき、Feedback登録をすべての学習の必須前工程にしない。

## 2. 行形式 — feedback schema 1

UTF-8のJSON Linesとし、一つの物理行に一つのfeedback objectを置く。行区切りはLF、非空ファイルは末尾LFを持つ。0件は0バイトとする。空行・BOM・管理行・配列の外枠・Markdown fence・EOF sentinelをデータへ入れない。本文内の改行等はJSON escapeし、一行を一文への短縮と取り違えない。

必須fieldは次の七つ。schema番号はこの行形式の互換性を示し、他のJSONLの版や更新回数とは別である。

- `schema_version`：整数`1`。
- `id`：新規は小文字・hyphen付きUUID v4。同じ記録の訂正で付け直さない。
- `created_at`／`updated_at`：実際の登録・意味更新を示す有効なUTC日時`YYYY-MM-DDTHH:mm:ssZ`。初回は同値、訂正ではcreated_atを保持し、updated_atはcreated_at以降とする。発言日時や対象作品の日付とは別である。
- `target`：非空の自然言語文字列。何への反応か、作品・作品群・方法・体験等の範囲が分かるようにする。必要な対象資料・確認版はsourcesへ結ぶ。
- `feedback`：`speaker`、`representation`、`text`を持つobject。speakerは確認できる発言者を示す非空文字列。representationは`verbatim`（原文）または`summary`（編集要約）。textは非空の本文。原文の本文へAIの説明を挿入せず、引用の外枠を除く場合も意味・表現・内部の改行を保持する。抜粋や要約は、その範囲と重要な留保が分かるようsourcesやcaveatで説明する。
- `sources`：一件以上のobject配列。各要素は非空文字列`locator`（所在・節・版等）と`supports`（誰の何を支えるか）を持つ。公開URLやmessage IDが未取得なら、会話上の所在説明であると明示し、架空のURL・日時を作らない。AIが確認した対象のsnapshotを、Humanが実際に閲覧した版と同一視しない。相対パスはこのJSONLの位置から解決する。

`title`や`caveat`を必要に応じて非空文字列で加えられる。caveatは出典上の限界やAIの補足を原文と分離するために使い、Humanの意味を上書きしない。後続の明示的な訂正・撤回は、その記録のsources等から対象IDと訂正範囲を辿れるようにする。固定タグ一覧、評価点、処理待ち欄、独立schemaファイルは必須にしない。未知field・ネスト値・配列順を保持する。

## 3. 出来事を保ち、必要な訂正を行う

転記ミスや対象の取り違えは同じIDの現行行を訂正し、変更理由と根拠を残す。更新前の内容はGit履歴で辿る。同一IDを重複追記して最後を最新版とする方式にしない。

後日届いた新しい反応は別の出来事として扱う。後の批判だけを理由に、以前の好評価を消したり、当時の発言を書き換えたりしない。評価対象や段階が異なる場合は共存できる。明示的な撤回・訂正では、対象と範囲を接続し、古い発言だけを現在へ再適用しない。Humanの現在のCorrection・STOPは、記録やlesson化を待たずに保持する。

更新前にRemoteの全文とrevisionを取得し、全行を検査する。不正JSON、object以外、重複key・ID、不正型・日時・出典、非JSON数値、未知schema、空行や改行規則違反を、空データに置き換えて処理しない。一行の消失は構文だけでは分からないため、基準revision・件数・保持すべき内容も照合する。

同じファイルの変更は一人の統合担当が扱い、最新の並行変更と未知fieldを保持する。送信前に選んだID・本文・基準revisionを照合可能にし、版条件付き・非forceで保存する。Timeout等ではRemoteと履歴から結果を確認し、保存済みの同じ記録を重複追加しない。IDが見つからない場合も削除・統合と未保存を区別し、結果不明のまま新IDで再送しない。保存先の近接ガイドと[AGENTS](../../AGENTS.md)に従い、保存後に全文・版を再取得する。専門側はその対象固有の配置契約へ接続する。

## 4. 形成と初期収録

共通形式は[Report Feedbackの確認済み版](https://github.com/yusukefujiijp/ai-project/blob/4869052151a33ce3b2f66b450686d462214ad0b7/artifacts/reports/references/feedback/README.md)のschema 1と読取・更新条件を継ぐ。Report固有の範囲・初期二件・Artifact保存接続は[Report側](../../artifacts/reports/references/feedback/README.md)に残る。初期の共有一件は、Ark28:07におけるHumanのReferences三本柱化への改善希望の原文抜粋である。周囲の会話、長期メモリ、他の私的Workを収集しない。発言の正確な日時・message IDは未確認とし、登録日時で代用しない。

初期収録・契約の分担・保存と検証の状態は[STR-023](../../control-center/changes/STR-023-shared-references-three-pillars.md)へ戻る。改善希望を効果実証や新しい継続実行権限へ変えない。

## 5. 権限と意味の境界

公開範囲と権限は[References](../README.md)と[AGENTS](../../AGENTS.md)に従う。承認された公開可能な対象だけを保存し、私的Work全体や長期メモリの収集・転記・同期へ広げない。過去の提案・承認やFeedback保存から、新しい実行・送信・自動収録の権限を作らない。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。HumanのMeaning／Correction／STOPと適用Guardを保持し、記録とAIはKeliとして扱う。

EOF::SHARED_FEEDBACK::v001
