---
title: "Dots lessons: JSON / JSONL 実ファイル比較とLiving Review"
canonical_path: "dots/lessons/experiments/json-vs-jsonl/README.md"
version: "v002"
status: "two chronological frozen trials / not adopted as live storage"
created: "2026-10-02"
updated: "2026-10-02"
recorded_by: "dot-0000"
role: "Comparison contract, measured results, and revisable recommendation"
source_commit: "d0508cd29602c56f5da98f6c1e7f742f42c6389a"
source_blob: "e289326eef11010e0d4d89d243a0b4dfe17fedb3"
representation_contract: "json-vs-jsonl-v001"
headerless_contract: "lessons-headerless-row-v002"
headerless_base_commit: "aa1cf53c3af575b512388884fddc1add6bb31c9c"
expected_eof: "EOF::DOTS_LESSONS_JSON_VS_JSONL::v002"
---

# JSON / header付きJSONL / headerless JSONLを時系列で判断する

第1試験（§1–5）は当時の契約・実測・結論を保存するHistoricalな記録。後続Human Correction、headerless候補の契約・試験結果と現在の見立ては§6にある。§1の3パスは初回の変更範囲であり、後続試験の範囲ではない。旧契約は凍結した二候補だけへ適用し、新candidateには§6.2を適用する。

## 1. 今回の役割と境界

YusukeJPの「jsonとJSONLの2Versionを実際に作成してから内容をLiving Reviewする」という依頼と、その計画へのGitHub実行承認に基づく限定実験である。[JSON候補](lessons.json)と[JSONL候補](lessons.jsonl)は同じ2件を表す凍結比較資料。**現役の正本は引き続き [dots/lessons.json](../../../lessons.json)** であり、このディレクトリへ通常の学びを追記しない。候補を常時同期する運用も導入しない。

保存対象は本READMEと上記二ファイルの計3点だけ。既存の正本、学びの意味・日時、[保守契約](../../../README.md#5-dotsの学びを次の判断へ戻す)、Actorログ、Workへの連絡は変更しない。この実験の成功は本番形式の採用承認ではない。

入力は[固定commitの正本](https://github.com/yusukefujiijp/ai-project/blob/d0508cd29602c56f5da98f6c1e7f742f42c6389a/dots/lessons.json)。Git blobは `e289326eef11010e0d4d89d243a0b4dfe17fedb3`、`schema_version: 1`、`next_id: 3`、順序はD-L001、D-L002。両件は同じBoard対話から抽出した別判断であり、独立した二つの成功実験ではない。

## 2. 両候補に等しく適用する契約

内容の正しさと表現形式の違いを混ぜない。以下の意味上の契約は両候補へ同じ強さで適用する。

- 正本の全top-level field、各lesson、sources内を含む未知fieldとネストした値を保持する。配列順・ID・出典・caveat・日時を変換だけで変えない
- `schema_version`は整数1、`next_id`は正の整数で現役IDの番号より大きい。lessonは安定ID、UTC登録/更新時刻、非空のlesson、非空のsourcesを持つ。sourcesには非空のlocatorとsupportsが必要。caveatがあれば非空文字列
- IDはD-L001から最低3桁。訂正でIDとcreated_atを変えず、実際の意味更新時にupdated_atを更新する。読解・変換・整形だけで日時を増やさない
- 新規発行はnext_idを使い、追加とcounter増加を一体更新する。削除・統合でもcounterを減らさず、削除IDを再利用しない。現役最大IDだけから失われたcounterを復元しない
- 不明なschema版、型不正、ID重複、無効日時、逆転日時、不正counter、壊れた構文を更新前に拒否する。壊れた資料を空として上書きせず、正常行だけを黙って採用しない。JSON object内の重複keyもこの比較用readerは拒否する
- 更新は「最新版と版の取得→decode/検査→意味編集→encode/検査→期待版を条件に一体保存→再取得照合」の同じ6段階。競合は再取得・意味の照合・必要な再採番後に再試行する。形式自体は競合を防がない

### JSON表現

UTF-8の単一objectで、`lessons`配列とそれ以外のmetadata fieldを持つ。候補は入力のbyte完全コピーで、末尾の空行も保持した。一般のJSON parserで構文を読むことはできるが、上記意味契約の検査は別途必要である。

### JSONL表現

UTF-8、1行1 JSON object、行末LF、末尾LFあり。先頭の1行だけが `{"type":"metadata","data":{...}}`、続く各行が `{"type":"lesson","data":{...}}`。metadataのdataは元のtop-levelからlessonsだけを除いた全field、各lessonのdataは元のlesson objectそのもの。文字列内の改行はescapeし、物理行を分割しない。

これはJSONL一般仕様に規定されたheaderではなく、この実験のapplication contractである。表現契約版は本書の `json-vs-jsonl-v001`。data内の `schema_version: 1` は元の意味schemaを保持した値で、既存の単一JSON readerがこのJSONLをそのまま読めるという互換性宣言ではない。

readerはwrapperのkeyをtype/dataだけに限定し、dataをobjectとする。metadataは先頭にちょうど1個、metadata.data内にlessonsは置かない。重複metadata、metadata欠落、未知record type、空行、CRLFや末尾LF欠落、途中で切れた不正行を拒否する（この実験ではLFを正規encoder/reader双方の契約とする）。wrapperの未知keyは拒否するが、dataの未知fieldはそのまま保存する。復元はmetadata.dataにlesson行のdata配列をlessonsとして戻す。objectのkey順や再整形後のbyteは同値判定の条件ではなく、全値と配列順の意味一致を条件とする。

1行は一つの**現行lesson**であり、訂正イベントの追記履歴ではない。同じIDを再追記して最新版とみなす方式は採用しない。追加でも先頭metadataのnext_idが変わるため、単純append-onlyではない。counterと追加行は一体保存する。Actor logsもJSONLであることは処理道具の一部を共有できる可能性を示すが、schema・更新意味・metadataの取り扱いが同じになるわけではない。

## 3. 実測と試験方法

2026-10-02、作成担当が同じ入力からPythonの標準JSON処理と明示validatorを使い、ローカルの使い捨てコピーで実行した。JSON/JSONLに同じ意味validator・編集手順・版ガードを使い、表現のencode/decodeだけを分けた。テストscriptやsynthetic lessonは実験データ二ファイルへ混入させず、追加公開もしない。以下は実行観測であり、将来の本番writer実装やGitHub CIを検証したものではない。

### 凍結候補の実測

| 表現 | UTF-8 bytes | 物理行 / 非空行 | Git blob |
|---|---:|---:|---|
| 元の整形JSONそのまま | 3,752 | 41 / 40 | e289326eef11010e0d4d89d243a0b4dfe17fedb3 |
| JSONL | 3,502 | 3 / 3 | 942c0a7a0df2dc22efcdf569d86dc91977b3ca13 |
| compact JSON（メモリ内だけ、非公開） | 3,437 | 1 / 1 | 比較用、第三の候補ファイルではない |

JSONLは元の整形JSONより250 bytes少ないが、同じcompact表現のJSONより65 bytes多い。空白削減とwrapper費用を形式の優劣から分離する必要がある。速度、処理時間、token数は測定していない。2件から大量蓄積時の性能・検索効率を証明しない。

### 同一入力・同一安全条件の結果

| 実施した検査 | JSON | JSONL | 観測内容 |
|---|---|---|---|
| baseline | PASS | PASS | JSONは元byte完全一致。JSONL→元objectは全値・順序一致 |
| 未知field往復 | PASS | PASS | top-level、lesson、sourceの未知field、配列/object/null/bool/改行入り日本語/U+2028/U+2029を保持 |
| 追加→訂正→統合削除→追加 | PASS | PASS | D-L003発行→同ID訂正→D-L002へ意味/出典を統合してD-L003除去→D-L004発行。counterは4→4→4→5 |
| 日時の保持/変更 | PASS | PASS | 変換で元2件の日時を変更せず。synthetic訂正はcreated_at保持、updated_atのみ更新。統合先だけ更新 |
| stale更新→再試行 | PASS | PASS | 同版を読んだA/BのA保存後にBを拒否。Bは最新版へ戻って再採番し、D-L003/D-L004を保持 |
| 途中切断 | PASS | PASS | 末尾の構文要素を切り落とした不正入力を拒否。正常部分のみを保存しない |
| ID/counter/日時の不正 | PASS | PASS | 重複ID、現役ID以下counter、created_at以前のupdated_atを拒否 |
| JSONL固有のwrapper | 対象外 | PASS | metadata重複/欠落、未知type、未知wrapper key、重複key、空行、非正規行末を拒否 |

試験日時はsynthetic値で、現実の出来事の日付として公開候補へ入れていない。編集試験では未知fieldを付けた同じ初期値から4回ずつencode/decodeと同値照合を実行。出力のbytes/物理行は、JSONが順に4300/68、4310/68、4128/60、4442/72、JSONLが3853/4、3863/4、3713/3、3953/4だった。両者で意味操作は同じ4回、保存単位も4回である。JSONLの行単位変更と、GitHubでファイル/Treeを保存する単位を混同しない。

stale試験は同じ単一processのoptimistic revision guardを双方へ適用した**模擬競合**。形式固有の防止能力や、実際のGitHub同時multiwriter試験ではない。構文的に完全なlesson行全体が失われる場合はJSONL構文だけで検知できず、JSONでも配列から完全な要素が失われれば構文だけでは分からない。既知revision/content hash・期待件数等との照合が必要。今回の末尾不正試験をあらゆる欠損の検出保証へ拡張しない。

## 4. 限定した別AI読解

作成担当とは別のAI readerが両候補全文と本書を読み、元会話なしで同じ4問へ回答した。JSONとJSONLの双方で、次の回答が得られた。

1. 送信文・応答開始の観測後に取得だけが止まったら、送信と返信観測を分離し、重複送信より先に既存会話を確認する。再取得・再接続は現在の承認範囲と停止条件内で行う
2. 根本原因も、待機や開き直しの因果効果も確定していない
3. 旧未観測は当時の正しいHistoricalな記録として保持し、後の結果と観測時刻を追記する。読解時刻を生成完了時刻へ変えない
4. D-L001とD-L002は同じ一件の経験からの別判断で、独立した二実験ではない

当初は契約部分を先に読んでもらう段取りだったが、readerが最初にREADME全文を表示し、結果・推奨にもアクセスしていたことを自己申告した。そのため、これは盲検試験や形式だけの純粋な理解度比較ではなく、**説明を含む限定読解**として記録する。勝率・優越性の根拠にはしない。Future Dotsの全体理解や将来の実利用を保証しない。

独立監査では、最初の試験readerが汎用の `str.splitlines()` を使っており、未知field内の合法なUnicode文字U+2028/U+2029まで区切ってJSONL往復を壊す不具合を検出した。作成担当はLFだけで区切るreaderへ修正し、両文字を含む同一入力の往復をJSON/JSONLで再試験してPASSを確認した。末尾LFとCRLFの扱いも曖昧だったため、上記の正規LF契約へ明示し、不正行末の拒否を実行確認した。凍結baseline二件の値とSHAはこの是正で変わっていない。独立readerも修正版をread-onlyで再実行し、resultsとの一致、特殊文字保持、不正行末と構文破損の拒否、baseline二件の意味・byte・SHAを再計算して確認した。この発見はJSONL一般の欠陥ではなく、行処理実装を正確にする必要性を示す。

## 5. Living Review — 第1試験当時の判断（Historical）

両候補で最も重要な働きは、学びの文章だけでなく、条件・根拠・限界・Historicalな未観測を一緒に引き継ぐことだった。今回、その意味を落とさずJSONLへ写像して戻せることは実測できた。Humanが期待するJSONLは、現行lessonを1行ずつ扱う候補として成立している。

一方で、現在の2件と既存のJSON契約では、JSONはmetadata wrapperの識別や専用復元が不要で、実装上の追加取扱いが少ない。JSONLはlesson境界が物理行と一致するため行単位処理の入口を作りやすいが、長いlessonは長い一行になる。next_idを同じファイル内で保つ設計では追加も先頭更新を伴い、競合と原子的保存の仕事は消えない。今回の正常試験は同じvalidatorと安全な更新ロジックが働いた証拠であり、どちらかの保存形式が本質的に安全である証拠ではない。

**現時点の推奨は、JSONLを有効な比較候補として残し、本番は現状のJSONを維持すること。** 理由はJSONLが失敗したからではなく、今回確認した利点だけでは既存reader・更新契約・配置を切り替える追加費用を上回る根拠がまだないためである。共通JSONL化の見た目より、今後のSave処理が「全体を検査して更新する」のか「各lessonを行として処理する」のかが選択を変える。

判定が変わり得る条件は、実際のreader/writerで行処理が必要になること、現実の件数で検索/更新の費用や誤読が測定されること、metadataを含めた原子的更新と互換性が検証されること。その時も今回の2件を一般的性能の証明にせず、反例や新しいHuman Correctionを受けて再判断する。共有log形式との道具の共通化は可能性であり、運用効果は未観測。

次の判断は、本比較を踏まえて現行維持で閉じるか、具体的な利用側の要求が生じた時に本番採用を別途検討するかである。今回は採用・移設・Save Skill・自動化・他AIへの送達を開始しない。保存後の3本文・SHAと対象外保持はRemoteで再確認して会話へ報告し、確認のたびに本書を再追記する循環は作らない。

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。AI・文書・形式・ReviewはKeliであり、今回の形式選択がRootやHuman Authorityを置き換えるものではない。

## 6. 後続試験 — Headerless JSONL（2026-10-02）

### 6.1 Human Correctionで変わった評価軸

第1試験の後、Humanは「増えても1行1lessonで統一する」「日常の読者はAI」「運用しながら学ぶ」方向を優先した。これは第1試験の観測を否定する訂正ではなく、選択で重く見る価値の訂正である。既存JSONとの完全往復と初期の切替費用だけを中心に評価すると、この方向を過小評価する。後続のPlan-onlyでは計画で停止し、その後のGitHub実行承認を受けて、この試験だけを実施した。

新しい[headerless候補](lessons-headerless.jsonl)を追加し、本READMEを更新する2パスだけが今回の変更対象。[初回保存commit](https://github.com/yusukefujiijp/ai-project/commit/aa1cf53c3af575b512388884fddc1add6bb31c9c)のJSON・header付きJSONLは凍結したまま残す。現役正本とdots/READMEの保守契約、Actor logs、STR、Workへの連絡は変更しない。本番採用、移設、Save Skill実装ではない。

後続試験の基準mainは `aa1cf53c3af575b512388884fddc1add6bb31c9c`。正本blobは第1試験と同じ `e289326eef11010e0d4d89d243a0b4dfe17fedb3` で、実在する2件だけを変換した。UUID例示のための架空lessonや、この試験自体の新しい学びは候補へ追加していない。

### 6.2 Headerless row-format contract

この候補に適用する表現契約は `lessons-headerless-row-v002`。**各行の `schema_version: 2` は新しい行形式の版であり、元の単一JSONのglobal schema 1を維持した表示ではない。** 現役正本のschemaを2へ移行したという意味でもない。

- UTF-8、各物理行にlesson objectを直接1件。metadata行、next_id、type/data wrapperを置かない。今回のbaselineはD-L001、D-L002の順の2行で、両方がlesson
- 各行に整数 `schema_version: 2` を加える。既存のid、created_at、updated_at、lesson、sources、caveat、未知のlesson/source fieldとネスト値・配列順は保持する。整形・形式変換だけで日時を更新しない
- 行区切りはLFのみ、非空ファイルの末尾もLF。空行、CRLF、末尾LF欠落、壊れた行、object以外、重複key、不明なschema版、非JSON数値を拒否する。Unicode U+2028/U+2029を改行として扱う汎用splitlinesは使わず、LFだけで区切る。文字列内のLFはJSON escapeする。0件の場合は空ファイルを表現とするが、公開baselineは2件
- 必須field・source・UTC日時の型と意味検査は第1試験と同等。ID重複、無効日時、updated_atがcreated_atより前、空lesson/source、locator/supports欠落を拒否する。全行を検査してから保存し、正常な行だけ黙って採用しない
- 既存D-L001/D-L002を付け直さない。新規lessonには標準lowercase/hyphen表記のUUID v4を生成する。IDは訂正時も安定。新規にはD-L連番と共有counterを使わない。UUIDは衝突確率を小さくする設計であり絶対一意の保証ではないため、全IDの重複検査は残す。削除IDを別lessonへ意図的に再利用しない
- 新規のcreated_atは実際の登録時刻、初期updated_atは同値。実際の意味更新だけでupdated_atを更新する。出来事の日・後の読解時刻・試験日時を流用しない
- 1行は一つの現行lessonでありイベントlogではない。同じIDの訂正を追加行として積まず、対象行を置換する。統合・除去では意味と出典を必要な既存lessonへ保持し、理由と旧IDの扱いを変更履歴で辿れるようにする。UUIDも自動で重複意味を識別しない

**変換の情報境界。** 入力のtop-level keyがschema_version／next_id／lessonsだけであることと、lessonにschema_version衝突がないことを事前確認した。未知のtop-level metadataや既存lessonのschema_versionがあれば、黙って落としたり上書きせず変換を止め、保存先・意味を検討する。本試験で明示的に退役するのは元のglobal schema_versionとnext_idであり、未知のmetadataはない。lesson内の未知fieldはそのまま保持する。

各行から今回加えたschema_versionだけを除けば、元のlessons配列と値・順序が一致する。これは**lesson-level semantic equivalence**であって、元document全体の可逆変換ではない。削除・統合されたIDの発行履歴は現役IDに残らず、元のnext_idは生存IDだけから導けない。元JSONをbyte単位で正確に戻したい時は、凍結した[元snapshot](lessons.json)を使う。将来UUIDを含む任意のschema 2資料を旧schema 1へ一般的にdowngradeできるとは約束しない。

### 6.3 更新と結果不明時の再試行

最新版とrevisionを読む→全行decode/validate→意味編集→encode/validate→期待revisionを条件に原子的保存→Remote再取得、という更新責務は残る。counterを取り除くと採番のための先頭更新は不要になるが、訂正・削除・同時更新・ファイルの一体保存を不要にはしない。GitHubでの保存単位と論理的な行変更を混同せず、append-onlyやmultiwriter安全性を形式だけで保証しない。

送信後に応答だけ失われた時は、保存失敗と即断して新UUIDを生成しない。同じ新規lesson操作のUUIDを保持し、最新版でそのIDと内容を照合する。同じID・同じ内容があれば保存済みとして重複追加しない。同じID・異なる内容なら競合として止めて照合する。IDがなければ現在revisionと履歴・操作結果を確認し、同一の操作として再試行可能な時だけ同じUUIDで進める。すでに削除された可能性を無視して自動復活させる規則ではない。

stale更新は拒否して最新版へ戻り、別writerの変更を保持して意味を統合する。UUIDを使っても古い全体ファイルで上書きすれば更新を失う。この試験で実行したのはローカル単一processのrevision guardによる模擬競合であり、実際のGitHub同時multiwriter試験ではない。

### 6.4 実行観測と測定値

2026-10-02 UTC、作成担当がPython標準JSON処理と明示validatorを使い、使い捨てコピーで36項目を確認した。初回のU+2028/U+2029不具合を回帰入力に含め、今回はLFだけで分割した。試験scriptはローカルだけで、公開するlessonは実在の2件から増やしていない。

| 実施した検査 | 結果・範囲 |
|---|---|
| baseline・構造 | PASS：2行、末尾LF、各行object/schema 2、legacy IDの値・順序保持 |
| 意味の往復 | PASS：追加schema fieldを除くと元lessons配列と一致。ID・登録/更新日時・本文・sources・caveatを個別照合 |
| 未知field・特殊文字 | PASS：lesson/sourceのネスト値、配列、null、bool、日本語、文字列内LF、U+2028/U+2029を保持 |
| 不適切な変換 | PASS：未知top-level metadataとlesson schema_version衝突を拒否 |
| UUID追加→訂正→除去 | PASS：legacy IDを保持、新規UUIDとcreated_atを訂正で保持、除去後は元の行群へ戻る |
| 結果不明を模擬した再試行 | PASS：同じUUIDと内容を既存行に照合し二重追加しない。同一UUID・異内容は拒否。保存済みUUIDを除去した後の再試行も拒否して復活させない |
| stale更新と復旧 | PASS：古いrevisionの保存を拒否。最新版を読み直し、先行変更を保持して再試行 |
| 不正入力 | PASS：構文途中切断、末尾LF欠落、空行、CRLF、重複key、配列行、NaN、重複ID、schema型/版、無効/逆転日時、source欠落、ID不正を拒否 |

UUID操作の日時は `2000-01-01T00:00:00Z` と1秒後を使ったsynthetic fixture。実際の出来事・登録日ではなく、公開候補には入れていない。模擬stale編集は元のupdated_atから1秒後のsynthetic値を使い、これも公開候補には入れていない。UUID除去は使い捨てデータの操作で、現役lessonの削除ではない。削除後の再試行検査には模擬Store内の既出ID集合を使った。この集合は公開行に埋め込んでおらず、実際のwriterがGit履歴・操作結果から削除を照合できることと、process再起動を跨いで操作UUIDを保持することは別途検証が必要である。試験は構文的に完全な行そのものの消失を自動検出する証明ではなく、期待revision・内容hash・件数の照合が別途必要である。

| 同じ実在2lessonを使う表現 | UTF-8 bytes | LF物理行 / 非空行 |
|---|---:|---:|
| 凍結した元の整形JSON | 3,752 | 41 / 40 |
| 凍結したheader付きJSONL | 3,502 | 3 / 3 |
| 新しいheaderless JSONL | 3,430 | 2 / 2 |
| compact元JSON（ローカルのみ） | 3,437 | 1 / 1 |

新candidateのGit blob計算値は `e1df104c2e306990f30ffced03ea3775425208be`。旧header付きより72 bytes、compact元JSONより7 bytes小さい。ただし同じlesson内容でもmetadata契約は違い、これはcounter/wrapperの除去と各行schema追加を含む表現差である。JSONL一般がJSONより小さいという証明ではない。速度・処理時間・token数・大規模データの性能は測定していない。

### 6.5 結論を見る前の限定した別AI読解

今回の別AI readerは、最初に必要な中立契約（行形式、安定ID、試験境界）とheaderless候補の実物全文だけを、この順に読んだ。README・旧JSON・作成担当の結論にはアクセスせずに第1試験と同じ4問へ回答したと報告した。

1. 送信と返信観測を分離し、重複送信より先に既存会話を確認する。再接続・後の取得は現在の承認と停止条件内で行う
2. 根本原因はUnknown。待機や開き直しによる回復の因果効果、恒久保証、無期限待機の必要性は実証されていない。送信表示はサーバー側配信時刻の証明ではない
3. 旧「未観測」を当時の正しいHistoricalとして保持し、後の結果・観測時刻を追記する。14:26:20 UTCの読解時刻を生成完了・原因確定時刻にせず、lessonのcreated_at/updated_atとも区別する
4. 2件は同じ回復経験からの別判断であり、独立した二実験ではない。Ark27:07のReviewも独立再現実験ではない

readerはリンク先の出来事を独立検証しておらず、候補中のlesson/source-support/caveatが伝える主張として回答した。また、具体的な再試行時間・回数は候補に定義されていないと指摘した。これは今回の実物を用いた限定的source-artifact読解であり、盲検による普遍的比較、全AIの理解保証、将来の実運用成功ではない。

独立した技術監査では、当初の模擬retryが「UUIDが見つからない時」に過去の削除を確認せず再追加し得る検査不足を発見した。作成担当は模擬Storeへ既出IDの照合を加え、追加→除去→結果不明retryでも復活させず拒否する回帰試験を実行した。この修正は試験の安全条件を契約へ揃えたもので、本番writerの実装完了を意味しない。公開baselineの2行とblobは変更していない。

### 6.6 Living Review — 後続試験を踏まえた現在の見立て

**次に実利用候補として検討する形式は、headerless JSONLを優先する。現役正本はこの試験では変更しない。** これは全形式の普遍的ランキングではなく、Humanが明示した「増えても全行がlesson」という価値と、今回の意味保持・行構造・限定読解の観測を結んだ目的依存の提案である。

働いた価値は、どの行にも同じ扱いで入れること、lesson単位で根拠とcaveatが完結すること、UUIDで新規採番の共有counter依存を外せること。読者をAIとする今回の目的では、長い一行がHumanの目に読みづらいことを主な棄却理由にはしない。AI向けであっても入力の意味、未知field、時刻、sourceの責務は軽くならない。

第1試験は「既存documentの全metadataまで可逆に写せるか」を確認した。後続試験は「全行をlessonに統一するため、何を明示的に退役し、何を守るか」を確認した。比較している設計上の問いが変わったことが、推奨の変化を説明する。第1試験のJSON維持推奨を誤った実測として消去せず、当時の重みづけとして保存する。

残る実務上の仕事は、採用するならreader/writer・入口・配置・互換性・復旧手順を一緒に整えること。row schema 2を置いただけで旧readerが読めるようにはならず、UUIDだけで更新競合や意味重複は解決しない。少数データの模擬操作だけで運用の軽さや成長時の性能は確定しない。一方、それらが未観測だからというだけで、価値が明確な次の限定実利用試験まで不可能と結論しない。

今回の完了条件は、実在2件の候補、変更理由・契約・検査とこの見立てを保存し、2対象のRemote本文/SHAと対象外保持を確認すること。本番採用は今回の承認範囲外として残し、保存確認ごとにREADMEへ証拠追記のcommitを増やす循環を作らない。Root・HumanのCorrection/STOP/Final Sealと既存Guardを保持し、形式は協働を支えるKeliとして選び直せる。

EOF::DOTS_LESSONS_JSON_VS_JSONL::v002
