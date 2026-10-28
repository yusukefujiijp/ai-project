# ChatGPT Work Adapter — v0.1.0

このAdapterは**Hostが実行する接続手順**。PythonからWorkのTool registryを呼ぶプラグインではない。[Harness入口](../../README.md)・現行AGENTS・現在の依頼を適用し、レビュー方法は`repository-reviews/review-prompt.md`の原本から読む。ここへ方法本文を写さない。

## 1. 実行環境と依頼を確定する

利用可能なGitHub Connectorの読取Tool、Python 3.12以降、POSIX、ローカル書込先、成果物保存先を実際に確認する。宣言されたToolと成功した操作は分ける。製品設定・認証を勝手に変更しない。GitHubの操作はレビュー中GETだけとし、対象コード・Hook・依存install scriptは実行しない。

公開済みのHarnessを固定commitから取得して利用する。最低限、六つの`src/ark_harness/*.py`とProfileを元の構成で保存し、固定treeのblobと照合する。`tool_commit`はその取得版。ローカルコードhashだけではcommitとの対応を証明できないため、HostのRemote照合が必要である。

`request.json`を現在の依頼から作る。必読原本は適用契約から解決し、実行ProfileのReview入口・方法はPythonも全文読解を必須とする。フォーカスレビューをRepository全体のレビューと表示しない。

```json
{
  "schema_version": 1,
  "repository": "yusukefujiijp/ai-project",
  "ref": "main",
  "purpose": "Root・入口・文書役割とHarness接続の重点レビュー",
  "scope": "focused",
  "paths": ["README.md", "harness/", "repository-reviews/"],
  "required_sources": [{"path": "AGENTS.md", "read": "full"}],
  "repository_writes": false,
  "execute_target_code": false,
  "output_intent": "Humanが読めるReportと最小証跡。形式は内容から選ぶ"
}
```

これは入力形の例。実際の依頼・必読・読解範囲を省略する権限にはならない。`schema request`も参照できる。

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

Toolの返却contentをJSON encoderに渡して`source.json`を作る。**手で再入力・要約・改行正規化・文字列stripしない。**Shellへ渡す場合はquoted heredocや安全な引数渡しを使い、原本文字列をShell codeへ埋め込まない。

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

`ingest --run ... --input source.json`でbyte照合する。対象は通常のUTF-8 Git blob。symlink、submodule、binaryを暗黙に追わない。同じsourceの再取得は既存の読解申告を保持する。失敗は`note --kind fetch-failed --detail ...`等でURL・Path・原因・未確認範囲を最小限記録し、秘密やTool応答全体を混ぜない。

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

```sh
PYTHONPATH=harness/src python3 -m ark_harness pause --run /absolute/path/review-run --reason '根拠取得まで完了。残る比較とReport作成を次のprocessで続ける'
PYTHONPATH=harness/src python3 -m ark_harness status --run /absolute/path/review-run
PYTHONPATH=harness/src python3 -m ark_harness resume --run /absolute/path/review-run --authority '現在も有効な依頼とScopeを確認。新しいSTOPはなく、同じ読取専用レビューを再開する'
```

別processでも同じ版・不変入力・原本cacheを照合する。`--authority`は理由の記録であり、文字列を入れるだけで許可が発生する機能ではない。Human STOP後は実際の再開権限が得られるまでresumeしない。Target mainが進んだ場合も、同じrunへ新しいmain本文を混ぜない。新Snapshotが必要なら新runを作る。

HarnessはWorkからGitHub書込Toolを取り除かない。レビュー中のConnector操作をGETに限定し、改善実装・コメント投稿・設定変更・予定登録を行わない。導入作業の公開と、その後の読取専用試験の期間・操作を記録上分ける。

## 5. 結果を検証し保存する

終了時にmainを再取得し、`end_ref_commit`と差分の影響を記録する。HostはReview Promptに沿って意味を判断し、Humanに適したReportを`deliverables/`へ作る。HTML、Markdown、PDF等のmedia typeとbyte SHA256を`outputs`に記す。相対Pathは`deliverables/`内に限り、primaryは一つ。形式の違いを誤検知しない。

`schema result`で結果の交換形式を取得する。必要なのはrun ID、対象commit、終了refとその評価、complete/partial、結論、findingごとの確度と時点、source IDと根拠行、限界・残点、出力Path/media type/hash、Hostの意味的確認である。`current-human`の主張を古い文書だけから断定しない。未確定の意味を機械のpassへ隠さない。

`finish --input result.json`後、`validation.json`を読む。機械合格・Hostの意味確認・未検査能力を分ける。修正が必要ならactiveのまま直して再検証し、依頼範囲が未完ならpartialと残点を保存する。今回の依頼に含まれない改善の実装は始めない。

`bundle --out /absolute/path/outside-repository/review-evidence.zip`で証跡を作り、読み戻し成功を確認する。ZIPは既存ファイルを上書きしない。Hostは利用可能な保存Toolの契約を読み、ReportとZIPを永続保存して返却ID・状態・必要なhashを確認する。保存失敗ならローカル検証済みと永続保存未完を分け、同じ内容の二重保存前に既存結果を確認する。保存先IDはHostの受領記録・回答へ残し、完成ZIP内へ自分自身の保存IDを埋め込む循環を作らない。

GitHubへReportを保存する場合は、その時点の明示権限と`repository-reviews/README.md`の記録契約に従う。初版のレビュー操作からGitHubへの結果Writeを自動化しない。Reportの保存とHumanからのFeedback受領、他AIによる再利用、実生活での効果は別の観測である。
