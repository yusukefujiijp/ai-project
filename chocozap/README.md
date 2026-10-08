---
title: chocoZAP Sweet Spot — 記録・推移・分析
version: v0.3.0
updated: 2026-10-08
updated_reason: 実施日と報告日の分離、根拠付き分析、検証・CSV出力を追加
canonical_path: chocozap/README.md
status: active
---

# chocoZAP Sweet Spot

YusukeJPの短い報告から、条件ごとのSweet Spotの移行と、その意味を読み直せるようにする。Humanは自然な言葉で伝え、AIが出所・未知・訂正を保って整理する。入力書式や補助スクリプトの実行をHumanへ要求しない。

| 役割 | 正本・入口 |
| --- | --- |
| 本人の報告・重量・系列・訂正 | [sweet-spots.json](sweet-spots.json) |
| 根拠につながるAI分析・再検討条件 | [analyses.json](analyses.json) |
| 検証・最新参照・履歴・CSVの再生成 | [tools/sweet_spots.py](tools/sweet_spots.py) |
| 継続する基本方法と会話支援 | [chocozap-sweet-spot](../skills/chocozap-sweet-spot/SKILL.md) |
| 学習記録と実用チェックリスト | [artifacts/README.md](artifacts/README.md) |

JSONが正本。表・グラフ・最新一覧は必要時に生成し、別の手入力台帳を増やさない。AI分析を本人の観察へ逆流させない。

## 1. 二つの日付と保存時刻

| 項目 | 意味 | 不明なとき |
| --- | --- | --- |
| `observed_date` | 実際に観察・実施した日 | `null`。報告日で代用しない |
| `reported_date` | 当初の本人報告の日 | `null`。保存時刻で代用しない |
| `created_at` | この記録が最初に作られた時刻 | 実施・発言・最終更新の時刻ではない |
| `legacy_day` | v1の日付キーを移行時に保存したもの | 新規記録には不要。集計軸にしない |

日付基準は `Asia/Tokyo`。「今日／昨日」は発言時点で解決し、読出日で解釈し直さない。後日届いた訂正の発言日は訂正または出所の `reported_date` へ添え、当初の記録日を変更しない。出所の発言日と、その出所が説明する運動の日も別である。

2026-09-24と09-27には実施日の根拠がある。09-27は実施日を明記した原文を保持する一方、当初の発言日は独立に確認できないため未確認とした。以降の更新は保存済みcontextにある報告日を使用し、運動日を補っていない。

**日付軸を混ぜない。** 「報告日別」は報告状態の変化、「実施日別」は実施日を確認できた観察の変化。選んだ日付がない点を別の日付で穴埋めせず、日付未確認として残す。欠測区間の補間や、未報告日の横ばいを実測と扱わない。

## 2. 実データの構造（schema_version: 2）

全体は `schema_version`、`timezone`、`records`。v1からの移行情報は `migration` に残す。

### 記録と条件

- 記録は `id`、`reporter`、`observed_date`、`reported_date`、`reference_scope`、`spots`、`sources` を持つ。日付の根拠は `date_basis`、特定の出所は `date_source` で示せる。未知の追加項目を更新時に消さない。
- `records` は報告を整理する単位であり、来館・周回・独立した試行の数ではない。既存の `cz-visit-*` IDは不透明な識別子として保持した。新規には `cz-record-*` 等の一意なIDを使える。同日だけを理由に同じ来館へまとめない。実際の来館が本人報告で特定された場合だけ任意の `session_id` を添える。
- `reference_scope` は `current`（その報告時点の現在の基準）、`historical`（過去の観察のみ）、`unspecified`。後日届いた昔の記録を現在値に上書きしない。観察単位の同名項目で上書きできる。
- 条件は `machine` と報告どおりの `mode`（両手・片手・片足・縦／横等）。任意の `round` と `condition` オブジェクトに、実際に報告された周回・器具や設定の区別を添えられる。比較はこれらの完全一致が基本。片手の縦／横と未指定、使い方不明と両手を合流させない。未知は未知の条件群として残す。

### 観察・系列・切替

- `spots`：単一重量のSweet Spot申告。`id`、`machine`、数値の `kg`、`source` と、報告された条件を持つ。
- `sequences`：任意の順序付き重量申告。`id`、`source`、空でない数値配列 `kg_sequence`、特定できる `machine` または元の `label`。順序と同値の反復を保つ。配列の長さをセット数・反復回数にしない。
- 開始重量を本人がSweet Spotと確認した系列だけ `sweet_spot_source` を持つ。履歴・CSVでは `spots` と、この系列の先頭を一観察ずつ抽出する。下降途中の重量を独立したSweet Spotにせず、同じ観察をspotsへ重複登録しない。
- `report_kind` は `observation`（申告）、`update`（新しい基準への更新）、`reaffirmation`（同値の継続確認）、`unspecified`。本人が述べた意味に基づく区分で、初回の運動や新たな実施の証明ではない。v1系列の継続確認は `sweet_spot_source`、その他は `source` を読む。
- 同じ重量の新しい本人報告も別の観察として残す。新報告とAIの再掲・保存の再試行は別。`previous_ref: "記録ID/観察ID"` は同条件の以前の記録との関係を示し、それ自体で因果・来館を認定しない。
- 観察にも必要なら `observed_date`、`reported_date` を添え、記録の既定値を上書きできる。明示した `null` は既定値へ戻さず未確認とする。
- `transitions` の `from`・`to` は同じ記録内の系列ID。`at: "to_sweet_spot"` と `source` は、切替先のSweet Spot重量を境に使い方を切り替えたという報告の関係。切替前の系列へ境界重量や途中段階を追加しない。
- `start_time` は分かる場合のみ、`time: "HH:MM"`、`source`、必要なら `approximate: true`。開始時刻から各機械の時刻・終了・所要時間を推定しない。

継続する基本方法は共通スキルが所有する。第一周で見つけたSweet Spotと条件を休憩後の集中した第二周へつなぐ。両手・片手で扱う種目では、両手のSweet Spotから下げ、片手のSweet Spot重量で片手へ切り替えてさらに下げる。日別に `transitions` がないことは方法の失効ではなく、その日の切替実施が未報告という意味。現在の基準を案内できても、未報告の実施・周回・中間重量を生成しない。

### 原文・訂正・Feedback

- `sources` は記録内の出所IDをキーに、本人の原文 `text` を一度保存する。AI側の問い・日付根拠等は `context` に分ける。出所の `reported_date` は、その発言日が分かる場合の情報であり、全観察の日付を変更しない。
- `corrections` は `id`、観察IDの `target`、`field`、`from`、`to`、`previous_source`、`source`。対象の現在値と対応する出所も更新し、訂正履歴は追記する。重量訂正なら `source`、機械名訂正なら `machine_source` 等を更新する。訂正を新しい運動観察にしない。
- `feedback` は `source` と、必要なら観察・訂正IDの `about`。本文は出所に置く。
- 記録IDは全体で一意、観察IDはspotsとsequencesを通じて記録内で一意。出所・訂正と合わせて `記録ID/項目ID` で分析から参照する。
- 未報告・省略・`null` は、未実施・ゼロ・変化なしを意味しない。必須でない情報をHumanの入力負担にしない。

## 3. AI分析とGraphのつながり

[analyses.json](analyses.json) は重量台帳を複製せず、`findings` に以下を保存する。

- `id`、`as_of`（分析対象の時点）、`status`（active / superseded / withdrawn）、`kind`、`claim`。
- `evidence`：観察・出所・訂正への参照配列。`reasoning`：計算・関係・解釈。`limits`：不明点・代替説明・断定できないこと。
- `review_when`：どんな報告や訂正で判断を見直すか。`revisions`：変更理由と以前の判断。判断を変える際は旧claim・reasoning・evidence・指紋等も履歴へ残す。
- `evidence_fingerprint`：参照項目、その関連出所・訂正・日付のSHA-256。補助スクリプトが根拠の変化を検出する。新しい無関係な記録の追加だけでは失効させない。指紋一致は分析の正しさや最新性の保証ではない。

`active` はそのas_ofにおける現行解釈であり、「常に最新」の印ではない。新報告がreview_whenに当たるか、AIが更新時に確認する。指紋を機械的に付け直して分析済みと扱わない。分析の誤りは実データを変更せず、分析側を訂正する。

```mermaid
flowchart TD
  R["本人の原文"] --> O["日付・条件付き観察"]
  C["訂正・継続確認"] --> O
  O --> V["条件別推移・最新参照"]
  O --> A["根拠付きAI分析"]
  M["継続する方法"] --> A
  V --> A
  A --> Q["次に確かめる点"]
  Q --> R
  C --> J["関連分析を再検討"]
  J --> A
```

Graphは項目数を増やすためではなく、数値・出所・解釈・再検討条件の依存関係を追うために使う。重量の伸び率や両手／片手の比率は記録上の関係であり、筋力・筋肥大・神経適応・左右差の診断ではない。反復回数、可動域、機械条件、感覚などが未確認なら原因や運動量を確定しない。

## 4. 読み出しと補助コマンド

Python 3.9以降の標準ライブラリのみ。以下はリポジトリのルートから実行する。JSONを直接読めるAIにはスクリプト実行を必須にしない。

```bash
python3 chocozap/tools/sweet_spots.py validate
python3 chocozap/tools/sweet_spots.py latest
python3 chocozap/tools/sweet_spots.py history --machine チェストプレス
python3 chocozap/tools/sweet_spots.py csv --date-basis reported --output /tmp/chocozap-reported.csv
python3 chocozap/tools/sweet_spots.py csv --date-basis observed --dated-only --output /tmp/chocozap-observed.csv
python3 chocozap/tools/sweet_spots.py self-test
```

`latest` はcurrent指定の報告を条件別に取り出す。報告日があればその日、なければ確認済み実施日を「参照順序」の基準にする。これは最新の**報告上の基準**を探す規則であり、実施日の混合グラフを作る規則ではない。日付が同じ候補を配列順で決着させず、日付不明の候補も捨てず、曖昧さを返す。後日訂正された古い観察を保存時刻で最新にしない。

`history` と `csv` は条件を自動合流せず、選んだ日付軸で並べる。日付未確認は末尾に残し、`--dated-only` のときだけ除く。`--machine`・`--mode` で完全一致の条件を選べる。CSVの `graph_date` と `date_basis` は軸を明示し、観察日・報告日・原文参照・訂正参照も各行に残す。空欄は未確認。表計算ソフトで数式になり得る文字列は先頭にアポストロフィを添える。

CSVは再生成可能な中間形式。無指定なら標準出力、`--output` は既存ファイルを上書きしない。既定データはスクリプト位置から解決し、`--data PATH`・`--analyses PATH` で読み出すファイルを明示できる。

分析作成時の指紋確認：

```bash
python3 chocozap/tools/sweet_spots.py fingerprint --ref cz-visit-0007/O001 --ref cz-visit-0002/O004
```

検証はJSON形式、ID、数値、日付、出所、訂正、系列間の切替、同条件のprevious_ref、分析の参照と指紋を確認する。グラフでは点の意味・日付軸・条件を明示し、欠測を線の実測として見せない。現在のデータ量では回帰・予測・因果の断定を優先しない。

## 5. 通常の更新

本人報告・訂正・Feedbackを、現在の権限の範囲で継続保存する。同じ範囲の許可を聞き直さず、現在のSTOP・Plan-only・保存しない指定を優先する。設計相談、仮例、AIの推奨、長期メモリを実記録へ転記しない。

1. 最新のJSONとSHAを取得。対象の報告・観察・条件を解決し、確認済みで変更のない本案内を再利用する。通常の数値更新でアーカイブ全読込を要求しない。
2. 新報告か、同値の継続確認か、訂正かを判断する。AIの再掲は観察を増やさない。同じ保存操作の再試行は出所・対象・保存結果で既反映を判定し、差分がなければ `NO_CHANGE`。
3. 関係する分析を読み、必要なものだけ改訂または再検討対象とする。旧履歴・原文・未知の追加項目を保持する。
4. 構文・意味・参照・差分を検証。現在のSHAを使って保存し、競合時は再取得・整合する。同じファイルへ並行書込みせず、古い全文を強制上書きしない。形式変更と対応する案内は一つの整合した変更として保存する。
5. 保存先を再取得し、対象の値・出所・差分を照合して完了を伝える。取得失敗や未保存はその範囲を明示する。

取得失敗を「記録が存在しない」と解釈しない。正本が読めないことを理由に旧資料へ書いたり、旧資料を現在値の代用にしない。JSONにはEOF文字列を足さない。

## 6. 履歴と配置

2026-09-24に旧日別Markdown方式からJSONへ移行した。旧資料・保存価値・本人の「予期せぬ成功」という評価・復帰条件は [ARC-005](../control-center/github/ARCHIVE.md#arc-005) が所有する。旧資料は参照用で、現行の集計・追記先ではない。

2026-10-08にv2へ移行。元の24観察（単一申告16件と確認済み系列起点8件）、全ID・出所原文・訂正・系列を保持した。これは来館24回の意味ではない。報告日・実施日・保存時刻を分離し、分析と再生成用の補助スクリプトを追加した。変更の記録はGit履歴から確認できる。

日別Markdown、手編集CSV、常設の静的グラフ、バックアップ用コピーを定期生成しない。容量・読書き時間・競合・比較範囲に問題が現れたら分割を検討する。将来の自動週次分析や他の運用への応用は候補であり、今ある自動実行機能ではない。

足部・足関節の学習記録は2026-10-06に追加し、10-08に現行パスへ参照を整えた。本移行では学習記録と実用チェックリストの内容・パスを変えていない。

EOF::CHOCOZAP_RECORDS_GUIDE::v0.3.0
