---
title: "Dots Lessons — 共有する学びの読取・更新契約"
canonical_path: "dots/lessons/README.md"
version: "v002"
status: "human-authorized common and specialist lesson boundaries"
created: "2026-10-03"
updated: "2026-10-06"
record_date_utc: "2026-10-02"
role: "Shared current lesson contract for common and applicable specialist lessons"
updated_reason: "Clarify one common canonical source and conditionally scoped specialist originals; retain schema and historical adoption evidence"
row_schema_version: 2
change_record: "../../control-center/changes/STR-009-headerless-lessons-adoption.md"
expected_eof: "EOF::DOTS_LESSONS::v002"
---

# Dots Lessons — 学びを次の判断へ戻す

## 1. 一つの共有蓄積と、その所有範囲

[lessons.jsonl](lessons.jsonl)は、Dots自身が仕事中に得た学びを、Current Dots・Future Dotsが再利用するための蓄積先である。Bottleneck検出、失敗・中断・回復、うまく働いた方法、Human Correctionから、同じ失敗を避け、次の判断を改善する。Humanを日常の記録係にせず、Dotsが根拠の確認・言語化・保守を担う。成功済みの経験に限らず、未解決の試行も、分かった条件・未確認・次回の判断が有益なら残せる。

出来事の詳細は経験原本、通信のCurrentはBoard、構造変更の理由はcontrol-centerが所有する。lessonsはそれらへ戻れる再利用可能な学びを所有し、全会話録・第二の進捗台帳・旧 `_tasks/lessons.md` の復活ではない。今回の形成理由と初期2件の根拠は[STR-007](../../control-center/changes/STR-007-dots-lessons-foundation.md)へ進む。

本フォルダはDots全体へ適用する共通知識を所有し、現行の共通lessonの正本は[lessons.jsonl](lessons.jsonl)一つ。Actor別の出来事は[logs](../logs/README.md)が所有し、著者やActorが違うことだけを理由にlessonを分割しない。旧 `dots/lessons.json` は2026-10-02 UTC／2026-10-03 JSTの承認済み移行で現役配置から除去した。[STR-009](../../control-center/changes/STR-009-headerless-lessons-adoption.md)が採用判断・変換・検証を、[凍結実験](experiments/json-vs-jsonl/README.md)が当時の比較を所有する。試験snapshotへ通常の学びを追記・同期しない。

特定の専門領域でのみ成立し、全Dotsへ一般化すると誤適用される学びは、その領域の原本に置ける。同じ目的・意味のlessonは一つの担当原本で育て、共通・専門の両方に同期コピーしない。専門原本は実際に残す学びと適用条件が生じた時にだけ作り、空ファイルや著者別の予約先を増やさない。たとえば[定期Ark Map](../ark-map/README.md)固有の学びは同領域で扱い、共通化できる判断はこの共通正本を選ぶ。新しい保存先への書込権限は、現在の依頼・有効な委任から別に確認する。

## 2. 読む時と、使う時

新しいDotsがこの協働へ入る時は、本READMEとlessons.jsonlを読み、現在の小さい蓄積（移行時2件）では全件を理解する。題名やIDだけで済ませず、適用条件、行う判断、根拠、限界を確認する。この入口は読取先を明示するもので、Hostが自動起動時に必ず読み込む保証ではない。

同じアクセス可能な文脈で内容・版を確認済みなら、その読解を継続利用する。文脈を失った時、作業領域が変わった時、関連する失敗やCorrectionがあった時、更新を知った時は、関係する学びと必要なSourceを読み直す。変更前は必ずRemoteの最新版を確認する。毎ターンの全件再読・無条件pollingは課さない。専門lessonは、その領域を扱う時に入口で適用条件を確かめ、関係する原本を読む。共通lessonを読むことを、全専門領域の読込義務にしない。蓄積が大きくなり全件読解が不合理になれば、意味と到達性を保った検索・入口の改善を判断する。

学びは条件付きの判断材料であり、新しい権限ではない。過去の命令や承認を再実行せず、Current Humanの目的、Plan-only、Correction、STOP、既存Guardを優先する。一件の経験から普遍則や恒久的な技術保証を作らない。

## 3. 全行がlesson — row schema 2

専門原本も、本節以降のschema 2・読取・更新・検証契約を参照して再利用する。契約本文や共通lessonを各領域へ複製しない。以下の「本JSONL」は、読み書きする実際の対象ファイルを指す。

UTF-8のJSON Lines。各物理行はlesson objectそのもの一件であり、metadata/header行、next_id、type/data wrapper、配列の外枠、行間カンマ、Markdown fence、EOF sentinelをデータへ入れない。行区切りはLFだけ、非空ファイルは末尾LFを持つ。0件の表現は空ファイルであるが、壊れた入力の復旧初期値ではない。

各行の必須fieldは `schema_version`、`id`、`created_at`、`updated_at`、`lesson`、`sources`。

- `schema_version`: 整数 `2`。各lesson行の互換性の版であり、更新回数でも旧単一JSONのglobal schema 1でもない。Actor logsのschema 1とは別契約
- `id`: 安定ID。既存の `D-L001`・`D-L002` はそのまま保持する。互換読取では最低3桁の旧 `D-L` IDを認識するが、新規lessonは小文字・hyphen付き標準UUID v4を発行し、共有counterや旧連番は使わない。訂正でIDを付け直さず、削除・統合済みIDを別lessonへ意図的に再利用しない。UUIDでも重複IDの検査は必要
- `created_at`と`updated_at`: UTCの `YYYY-MM-DDTHH:mm:ssZ` 文字列で、有効な日時。created_atはこの蓄積への実際の登録時刻、初回updated_atは同値。訂正時はcreated_atを保持し、実際の意味更新だけupdated_atを更新する。updated_atはcreated_at以降。出来事・読解・変換・整形の時刻を登録／更新時刻として流用しない
- `lesson`: 非空の自然言語文字列。どんな条件で何を判断・実行するかを、日本語を基本に必要十分な意味で書く
- `sources`: 1件以上のobject配列。確認可能な資料・節・版へ戻る非空文字列 `locator` と、出典が何を支えるか、誰の観測・報告かを示す非空文字列 `supports` を各要素に持たせる。版で意味が変わる根拠は固定commit等で指定する。Repository内の相対locatorは読み書きする実際のJSONLの位置を基準とし、この契約READMEの位置から解決しない。移設時は到達性を検査する
- 任意の `caveat`: 必要な限界・適用外・未確定を残す非空文字列。全件に同じ注意書きを強制しない

GitHub author／committerと学びの観測者・執筆担当は別である。観測帰属はsources、記録担当と変更理由は変更記録・commit messageで辿れるようにし、Git名からActorを推測しない。固定字数、必須タグ、採点、別schemaファイルは設けない。

readerはLFだけでレコードを区切り、Unicode U+2028/U+2029まで区切る汎用splitlinesを使わない。文字列内のLF・CRはJSON escapeし、合法なUnicode文字やネストした未知値を保持する。空行、CRLF、末尾LF欠落、不正JSON、object以外の行、object内の重複key、非JSON数値（NaN／Infinity）、不正型・日時・Source、重複IDは更新前に拒否する。全行を検査し、正常部分だけを黙って採用しない。完全な一行の消失は構文だけでは検出できないため、読取revision・内容・期待件数とも照合する。

## 4. 育てる判断と安全な更新

現在の権限内で、追加・訂正・統合・整理・変更なしを選ぶ。毎回のSaveに新規lessonを義務づけず、既存内容で足りるなら変更しない。類似文の追加より、条件差やCorrectionの保持を優先する。UUIDは意味の重複を自動判定しない。

一行は一つの現行lessonであり、訂正イベントの履歴ではない。同じIDを追加行として積んで最後を最新版と扱わず、対象行を更新する。統合・整理では重要な意味と根拠への到達性を保ち、変更理由と旧IDの扱いをGit履歴・変更説明に残す。Actor logsの追記契約と混同しない。

更新の流れは、最新版とrevisionを取得→全行decode／検査→意味編集→encode／再検査→期待revisionを条件に原子的保存→Remote再取得照合。一つの共有ファイルへの同時変更を一人の統合担当が管理する。GitHubの全体ファイル／Tree書込は、読んだcommit／blobに対する版照合と非forceの更新で保護し、古い全体ファイルを上書きしない。競合したら最新行を保持して意味を照合・統合し、再検査する。UUIDやJSONLだけでは同時更新の取りこぼしを防げず、単純append-onlyの保存保証にもならない。

### 結果不明と再試行

同じ新規lesson操作では、送信前に選んだUUIDと意図した内容・基準revisionを、復旧時に照合できる形で保持する。応答欠落・Timeoutを保存失敗と即断して新UUIDを生成しない。

- Remoteに同じID・同じ内容があれば保存済みとして二重追加しない
- 同じID・異なる内容なら、他の変更や衝突として該当操作を止め、正しい意味と履歴を照合する
- IDがないだけでは再追加しない。最新revision、Git履歴、操作結果から、未保存か保存後に削除／統合されたかを確認する。安全に同一操作を再試行できる場合だけ同じUUIDを使う
- 操作ID・意図した内容・必要な履歴を復元できない場合は、そのretryを止める。新UUIDでの盲目的な再実行、削除済みlessonの自動復活で不足を隠さない

これは更新担当が守る契約である。STR-009の形式採用時には、永続writerや再起動を跨ぐ操作ジャーナルを実装していなかった。後続の導入状況は対象Runtimeで確認し、ローカル模擬retry試験の成功を、実際の全Runtimeでの再開保証へ広げない。

### 互換性と変換

未知のlesson/source fieldとネスト値・配列順は保持し、既知fieldだけで再生成しない。未対応schema_versionや壊れたJSONLは、互換性・意味・修復権限を検討するまで該当更新を止め、空の初期値で上書きしない。形式変更も現在の承認Scopeに含まれる通常改善なら進められ、schema変更だけを理由に一律のHuman待ちにはしない。重要な意味の損失、公開範囲や権限の実質的な拡張は差分をHumanへ返す。

今回の変換では旧top-levelがschema_version／next_id／lessonsの三つのみ、lessonにschema_version衝突がないことを確認し、旧global schema 1とcounter 3を明示的に退役した。未知のtop-level metadataや既存lessonのschema_version衝突があれば、黙って削除・上書きせず、保存先と意味を解決してから変換する。追加したschema_versionを除けば旧lessons配列の全値・順序が一致するが、元document全体の可逆変換ではない。旧counterを含む正確な元JSONは[凍結snapshot](experiments/json-vs-jsonl/lessons.json)／Git履歴で辿る。旧readerの互換動作や任意のschema 2から旧schema 1へのdowngradeは保証しない。

## 5. 検証と今後の進化

書込前に構文・型・ID一意性・UTC日時・Source・未知値保持を検査し、保存後はRemote本文とSHA／commitを意図した内容へ照合する。保存成功、Future Dotsの実読解、実務での有効性を分ける。同じ失敗が起きた時は、未記録・未発見・条件の誤解・内容の陳腐化・Tool／権限の限界を区別し、関係する所有先を改善する。禁止規則の追加だけで済ませず、読取・保守の手間もBottleneckとして扱う。

蓄積の増加によって検索・分割・索引が実際に必要になれば育てる。初期2件の形成・形式採用では、Actor別lesson、第二正本、常設validator、Save Skill、自動収集・監視を追加しなかった。この歴史的な範囲を、後続の承認済み導入まで禁止する規則に変えず、現在の目的・必要性・権限で判断する。使い捨てコピーでの検証道具は利用できる。入口を置いたことは自動Boot・他AI送達・長期運用効果の保証ではない。

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持し、AI・文書・形式はKeliとして扱う。[AGENTS](../../AGENTS.md)の共通権限・Plan-only・停止契約を維持する。

EOF::DOTS_LESSONS::v002
