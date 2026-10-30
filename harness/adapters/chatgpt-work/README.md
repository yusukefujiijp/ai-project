# ChatGPT Work Adapter — 文書 v0.1.1

対象実行実装は`ark-harness` v0.1.0、交換schemaは1。今回の文書・回帰検査の改訂は、実行コードの版や能力を変更しない。

このAdapterは**Hostが実行する接続手順**。PythonからWorkのTool registryを呼ぶプラグインではない。[Harness入口](../../README.md)・現行AGENTS・現在の依頼を適用し、レビュー方法は`repository-reviews/review-prompt.md`の原本から読む。ここへ方法本文を写さない。

## 1. 実行環境と依頼を確定する

利用可能なGitHub Connectorの読取Tool、Python 3.12以降、POSIX、ローカル書込先、成果物保存先を実際に確認する。宣言されたToolと成功した操作は分ける。製品設定・認証を勝手に変更しない。GitHubの操作はレビュー中GETだけとし、対象コード・Hook・依存install scriptは実行しない。

公開済みのHarnessを固定commitから取得して利用する。最低限、六つの`src/ark_harness/*.py`とProfileを元の構成で保存し、固定treeのblobと照合する。`tool_commit`はその取得版。ローカルコードhashだけではcommitとの対応を証明できないため、HostのRemote照合が必要である。

`request.json`を現在の依頼から作る。必読原本は適用契約から解決し、実行ProfileのReview入口・方法はPythonも全文読解を必須とする。フォーカスレビューをRepository全体のレビューと表示しない。

<!-- ark-harness:request-example:start -->
```json
{
  "schema_version": 1,
  "repository": "yusukefujiijp/ai-project",
  "ref": "main",
  "purpose": "Root・入口・文書役割とHarness接続の重点レビュー",
  "scope": "focused",
  "paths": ["README.md", "harness", "repository-reviews"],
  "required_sources": [{"path": "AGENTS.md", "read": "full"}],
  "repository_writes": false,
  "execute_target_code": false,
  "output_intent": "Humanが読めるReportと最小証跡。形式は内容から選ぶ"
}
```
<!-- ark-harness:request-example:end -->

これは入力形の例であり、今回の依頼・必読・読解範囲はHostが現在の適用契約から解決する。Repository相対Pathは正規形で指定し、ディレクトリでも`harness`のように末尾の`/`を付けない。絶対Path、空の要素、`.`、`..`、バックスラッシュ等は現行parserが拒否する。不正なPathを自動修正する仕様にはしない。

`paths`は重点範囲の指定であり、配下の全資料の自動取得・全文読解・意味的な調査完了を保証する欄ではない。`required_sources`もこの例だけで今回の必読を尽くしたとは扱わない。`schema request`で交換形式を確認できるが、Pathや相互条件は実際のRequest parserでも検査する。回帰testは上の目印で囲んだ公開例自体を読む。

## 2. 原本を固定して取得する

利用できるTool名・引数をその環境で解決する。初版で利用したのはGitHub Connectorの`fetch`と`fetch_file`。WorkのToolを呼ぶHost側で次を行う。

1. `GET /repos/yusukefujiijp/ai-project/git/ref/heads/main`で開始commitを得る。
2. `GET /repos/.../git/commits/<commit>`で実際のroot tree SHAを得る。
3. `GET /repos/.../git/trees/<tree-sha>?recursive=1`でtreeを得る。`truncated=true`は初版では拒否する。部分treeを完全なtreeと宣言しない。
4. 下記のSnapshot形式へ変換し、`snapshot.json`へ保存する。返却にある`url`等のAPI固有欄は入れず、path/mode/type/sha/sizeだけに正規化する。treeレスポンスの`sha`が要求refを表示する実装もあるため、root treeは手順2の値を使う。
5. `fetch_file(repository_full_name=..., path=..., ref=<固定commit>, encoding="utf-8")`で原本全文を取得する。部分表示やTool wrapper全体ではなく、実際のcontent文字列と返却blob SHAを受け渡す。

Snapshotの形（`schema snapshot`で完全な型を取得できる）:

```text
schema_version: 1
repository: owner/name
commit: 40桁の固定commit
tree_sha: 40桁の実root tree SHA
truncated: false
entries: [{path, mode, type, sha, size（任意）}, ...]
```

GitHub treeとcommitの真正性はConnectorからの取得に依存する。Pythonは取得元サービスを認証し直すものではなく、渡されたSnapshot内のblobと原本byteの対応を検査する。

```sh
PYTHONPATH=harness/src python3 -m ark_harness start \
  --run /absolute/path/outside-repository/review-run \
  --profile harness/profiles/repository-review.toml \
  --request /absolute/path/inputs/request.json \
  --tree /absolute/path/inputs/snapshot.json \
  --tool-commit ACTUAL_40_CHARACTER_COMMIT
```

### 2.1 原本をデータとして受け渡す

Toolの返却はHostの実行層でデータとして扱う。実際のcontent文字列、返却blob SHA、取得時に束縛したrepository・commit・pathをSourceInputの各欄へ渡し、JSON encoderで入力JSONを作る。表示用の抜粋やTool wrapper全体をcontentへ入れない。**原文の手入力・要約・改行正規化・文字列stripは行わない。**

入力JSONはソースRepository外、かつ新しく開始するrunの外にある入力作業ディレクトリへ保存する。Hostが利用できるファイル書込Tool等へJSONをデータとして渡す。実行時に実在するPathへ束縛し、`start`の前にrunディレクトリを作らない。`start`自身が新しいrunを作成し、request・profile・treeを固定する。

JSONのインデントやUnicodeエスケープ表現は、復号後のcontentを変えなければ選べる。原本のCRLF・空白・末尾改行はcontent内に保持する。JSON化はShell用のエスケープではない。原本文字列や巨大JSONをShellコマンド本文・巨大な引数・環境変数へ埋め込まない。base64化だけでもShellの解釈や引数長の問題が解消するとは考えない。

このAdapterでは`start`のrequestとtreeを別々のJSONファイル、profileをTOMLファイルとして渡す経路を標準にする。`--request - --tree -`を同時指定して標準入力から二つのJSONを読む使い方はしない。

```text
schema_version: 1
repository: yusukefujiijp/ai-project
commit: snapshotのcommit
path: 元のRepository相対Path
blob_sha: Connector返却のblob SHA
content: 取得した原文文字列
role: instruction | method | subject | dependency | history
purpose: 今回この原本を必要とする理由
```

`ingest`・`mark-read`・`add-tree`・`finish`の`--input`にはJSONファイル名、または標準入力を表す`-`を指定できる。標準入力には一つの完全なJSONを渡し、入力を終了する。例えば、上で用意したファイルから渡す場合は次の形になる。

```sh
PYTHONPATH=harness/src python3 -m ark_harness ingest \
  --run /absolute/path/outside-repository/review-run \
  --input - < /absolute/path/inputs/source.json
```

`--input /absolute/path/inputs/source.json`によるファイル入力も使える。この二つは代替経路であり、同じ操作を二重実行する指示ではない。標準入力対応だけでConnectorとの自動接続が成立するわけではなく、入力を正確に渡す工程はHostが担当する。受け渡し不能なら、取得できた範囲とPythonへの受け渡しが成立した範囲を分ける。

`ingest`でbyte照合する対象は通常のUTF-8 Git blob。symlink、submodule、binaryを暗黙に追わない。登録済みcacheが健全な場合、同じsourceの再取得は既存の読解申告を保持する。失敗は、その状態で実行できる`note --kind fetch-failed --detail ...`等、またはHost側の受領記録へURL・Path・原因・未確認範囲を最小限残し、秘密やTool応答全体を混ぜない。cache欠損時は§4.2へ進む。

## 3. 実際に読み、読んだ範囲を記録する

`show --run ... --source-id '<commit>:<path>' --start 1 --end 100`等で照合済み本文を読み、Hostの表示上限に応じて未読部分を回収する。全文取得とHostへの全文表示は異なる。EOFが表示されたことだけで中間の読解を宣言しない。

実際に読んだ後で、`mark-read --input read.json`を使う。

```json
{
  "source_id": "固定commit:Repository相対Path",
  "ranges": [{"start": 1, "end": 100}],
  "reviewer": "今回の実行AIの識別",
  "note": "この範囲を読んだ目的・確認事項"
}
```

空ファイルは空のrangesで明示申告できる。同じblobを同じ作業文脈で全文読解済みなら、commit/path/blobの一致を確認して読解記録を再利用できるが、別AIの記録を自身の理解の証明へ読み替えない。関連範囲だけ読んだ長い文書を全文既読にしない。

既存原本にある必読依存・Identity・STOPはHostが解決する。方法の参照一覧を無条件に全資料の新必読にはしない。必要な固定履歴は、そのcommitの完全treeを`add-tree`し、同じ方法で取得する。現用リンクと固定履歴を混ぜない。`check-link --href ...`は指定ファイル参照の存在を検査し、anchor・外部URL等の未検査は別に返す。

## 4. 中断・再開と読取専用の境界

### 4.1 状態・整合性・現在の権限を分ける

中断後は現在の依頼とSTOP、runの状態、必要ファイルの整合性を分けて確認する。同じrunへのCLI操作は逐次行う。`status`・`show`も排他的なlockを取るため、`ingest`等と重ねて実行しない。lock取得はローカルの`.writer-lock`を作成し得る。Repository読取専用という契約と、ローカルファイルへ一切書き込まない操作を混同しない。

- `active`：直前の操作結果と現物を確認し、未完の工程から続ける。`resume`は使わない。状態名だけで直前操作の成功を認定しない。
- `paused`：現在も有効な続行権限を確認して`resume`する。同じ実装コード、不変入力、登録済み原本cacheを再照合してから`active`へ戻る。
- `complete`：依頼された範囲を閉じた終了状態。レビューの再開はできないが、証跡化やHostによる永続保存が未完なら、現在の委任内でその工程を進められる。
- `partial`：残点を持つ部分結果としての終了状態。一時停止ではなく、`resume`の対象にもならない。残点を続ける場合は現在の委任と対象版を確認し、必要なら前回との関係を持つ新runを開始する。有効な委任がある場合に形式的な再承認を毎回要求しない。

終了したrunのstateを手で`active`へ変えない。次は、健全なactive runを計画中断し、状態確認後に同じ仕事へ戻る操作例である。実際の権限と中断理由をHostが確認して使う。

```sh
PYTHONPATH=harness/src python3 -m ark_harness pause --run /absolute/path/review-run --reason '根拠取得まで完了。残る比較とReport作成を次のprocessで続ける'
PYTHONPATH=harness/src python3 -m ark_harness status --run /absolute/path/review-run
PYTHONPATH=harness/src python3 -m ark_harness resume --run /absolute/path/review-run --authority '現在も有効な依頼とScopeを確認。新しいSTOPはなく、同じ読取専用レビューを再開する'
```

別processでも同じ版・不変入力・原本cacheを照合する。`--authority`は理由の記録であり、文字列を入れるだけで許可が発生する機能ではない。Human STOP後は実際の再開権限が得られるまでresumeしない。Target mainが進んだ場合も、同じrunへ新しいmain本文を混ぜない。新Snapshotが必要なら新runを作る。

### 4.2 cache欠損・破損と結果不明

cache欠損・破損は第五のrun状態ではなく、どの状態にも重なり得る整合性問題である。登録済みcacheが欠けると、`status`・`show`・`resume`・`ingest`・`finish`等は、それぞれの状態条件や整合性検査で失敗し得る。`status`成功をあらゆる回復の前提にしない。

通常の`ingest`は新しい原本を書き込む前に既存sourceを照合するため、登録済みcacheが失われた場合、同じ原本の再投入だけでは修復できない。元commitから原本を再取得できることと、旧runを復元できることは別である。現行CLIにcache修復・archive import・完全run復元の専用操作はない。未取得の必読資料を残す部分成果と、登録済みcacheの破損を区別し、後者を`partial`の指定だけで保存できると考えない。

旧runを削除したり、state・hash・読解申告を手で書き換えたりせず、残る記録と確認できない範囲を保持する。CLIで読めない記録を直接参照しても、それだけで整合性確認済みとはしない。現在の依頼が続行を含む場合は、新runの対象版と必要Sourceを解決し、前runのID・対象commit・中断理由・未確認範囲を必要な範囲で参照する。新runの既存`note --kind scope-note`等で関係を記録できる。新しい状態Schemaや台帳を前提にせず、旧`sources.json`のコピーを新runの検証・自身の読解の証明へ置き換えない。確認済みの自身の読解の再利用は適用契約に従う。

応答欠落や処理中断は未実行の証明ではない。再実行前に対象操作の現物を確認する。ファイル単位のatomic replaceは、全操作を一括して戻せるtransactionではない。開始途中で`run.json`等が不足した場合も旧状態を保持し、新runの必要性を判断する。完全復元を本Adapterの説明だけで実装済みにしない。

HarnessはWorkからGitHub書込Toolを取り除かない。レビュー中のConnector操作をGETに限定し、改善実装・コメント投稿・設定変更・予定登録を行わない。導入作業の公開と、その後の読取専用試験の期間・操作を記録上分ける。

## 5. 結果を検証し保存する

終了時にmainを再取得し、`end_ref_commit`と差分の影響を記録する。HostはReview Promptに沿って意味を判断し、Humanに適したReportを`deliverables/`へ作る。HTML、Markdown、PDF等のmedia typeとbyte SHA256を`outputs`に記す。相対Pathは`deliverables/`内に限り、primaryは一つ。形式の違いを誤検知しない。

`schema result`で結果の交換形式を取得する。必要なのはrun ID、対象commit、終了refとその評価、complete/partial、結論、findingごとの確度と時点、source IDと根拠行、限界・残点、出力Path/media type/hash、Hostの意味的確認である。`current-human`の主張を古い文書だけから断定しない。未確定の意味を機械のpassへ隠さない。

`finish --run ... --input result.json`後、応答・`validation.json`・run状態を対応させる。機械合格・Hostの意味確認・未検査能力を分ける。

- 終了code 0：検査に受理され、runはresultのoutcomeに従って`complete`または`partial`となる。code 0だけで全面完了・永続保存完了・Humanの利用効果を認定しない。
- 終了code 1：結果検査が不合格。`result.json`と`validation.json`は保存され、runは`active`に残る。現在の依頼内で不整合を修正し、再検証する。
- 終了code 2、処理中断、応答欠落：操作が一切行われなかった保証ではない。再実行前に対象操作の現物を確認する。`status`成功もresult・成果物のhash・永続保存先までの一括検証ではない。

受理済みの`complete`／`partial`を結果修正のために手で`active`へ戻さない。依頼範囲が未完なら残点を持つ部分結果として扱い、続行は§4の条件から判断する。今回の依頼に含まれない改善の実装は始めない。

`bundle --run ... --out /absolute/path/outside-repository/review-evidence.zip`で終了状態の結果と成果物を再検査して証跡を作り、読み戻し成功を確認する。ZIPは既存ファイルを上書きせず、原本cacheを含まない。展開だけで再開できるrun backupではない。Hostは利用可能な保存Toolの契約を読み、ReportとZIPを永続保存して返却ID・状態・必要なhashを確認する。保存失敗ならローカル検証済みと永続保存未完を分け、結果不明なら保存先IDや実体を確認してから次を決める。保存先IDはHostの受領記録・回答へ残し、完成ZIP内へ自分自身の保存IDを埋め込む循環を作らない。固定commitから将来も原本を再取得できるとは保証しない。

GitHubへReportを保存する場合は、その時点の明示権限と`repository-reviews/README.md`の記録契約に従う。初版のレビュー操作からGitHubへの結果Writeを自動化しない。Reportの保存とHumanからのFeedback受領、他AIによる再利用、実生活での効果は別の観測である。
