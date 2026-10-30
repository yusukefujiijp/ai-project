---
id: STR-024
title: Harness初版 — 読み取り専用Repositoryレビューの実行補助
version: 0.2.1
created: 2026-10-29
updated: 2026-10-31
status: initial-implementation-and-focused-trial-recorded
scope: root harness 17 files; initial adoption and trial history; subsequent five-file documentation and regression revision
---

# STR-024 — Harness初版

初版の検査・実地試験・H1発見は当時の記録として保持する。公開request例の修正と接続・状態説明の局所改訂は、[2026-10-31の後続記録](#local-revision-2026-10-31)を参照する。過去の試験結果を改訂後の現行版の試験結果へ読み替えない。

## Humanの採用と境界

Humanは今回の設計を採用し、`yusukefujiijp/ai-project`直下の`harness/`へ17ファイルの初版、必要なテスト、一件の重点Repositoryレビュー、成果と最小証跡の保存、GitHubへの導入記録とRemote確認を依頼した。入口掲載は通し試験後の限定差分とする。試験で発見した改善の実装、既存ファイルの移動・削除、Root文書統合、製品設定変更、自動実行の設定は対象外。

実装開始のmainは`79770085364871cd026cb12ff669593fbf6cf6f4`。適用原本はAGENTS v004.12-candidate、artifact-to-github v001-human-authorized、ARK v003-candidate、現行keybindings、Rootと各所有入口。公開準備中にmainが`1e8399449a09f83e34d255bdc246060c33f96e9c`へ進み、Ark-OKF等の他担当成果を確認した。公開は最新headのtreeを基礎にし、期待head一致を条件にする。

Home Bは既存Mainの根本再設計に属し、その比較・本文案の進展と統合実装の権限を分ける。Main27、Support28、Ark29、Ark30の現在と受入れは[Domain入口](../../ark-project/README.md)と各Stateが所有する。本件はそれらを再定義・巻戻ししない。Report／Feedback・共有References・他担当の成果も既存所有先へ残す。

## 構成と理由

実装の所有は[`harness/README.md`](../../harness/README.md)。Actorから独立した仕事の接続なのでRoot直下に置き、`agents/harness/`へ所属させない。方法は[`repository-reviews/review-prompt.md`](../../repository-reviews/review-prompt.md) v002を固定commitから読む。本文をHarnessへコピー・移設しない。

17ファイルはREADME、pyproject、uv.lock、Profile、Work Adapter、六つのPython原本、三つのtest、合成fixture、eval READMEと合成JSONL。個別の配置・所有内容・読む相手・更新条件はHarness入口に記載した。run状態・原本cache・Report・証跡はソースRepository外へ置き、これらを17原本と混ぜない。

利用環境から、ChatGPT Work上のGitHub読取ConnectorとPythonを選んだ。PythonからConnectorを直接呼び出せるとは仮定せず、HostがToolの返却を正規化して渡す。Python 3.12.14、uv 0.13.4を観測。既存Pydanticを使う案は、オフライン解決用の依存cache不足を確認したため、外部依存ゼロの標準ライブラリ実装へ調整した。`uv.lock`は実生成済み。新しいAPI Key・製品設定・daemon・予定を要求しない。

取得byteのGit blob照合、固定Snapshot、読解範囲の申告、根拠行と出力hashの検証、中断・別process再開、POSIX単一Writer、結果のcomplete/partial、証跡ZIPの読み戻しを実装した。Human向けReportはmedia typeを持つ自由形式で、Markdownだけに固定しない。

## 公開前の機械検査

`PYTHONPATH=src uv run --frozen --offline python -m unittest discover -s tests -v`で**30件pass**。`uv lock --check --offline`も成功した。主要な反例は、EOFだけを残した中間欠落、別commit混入、未知版・型・重複キー、symlink・パス逸脱、読解範囲外の根拠、必読未完、再開時のcache・コード・入力改変、同時Writer、既存run上書き、HTML成果物の改変、歴史リンクをmainで評価する誤り。

これらは合成入力による機械検査。意味的な理解、独立した別AI、Humanの利用効果の実証ではない。evalsの六つの合成事例も、保存しただけで評価成功とは扱わない。

## 段階切替と観測記録

1. 初版17ファイル・この記録・生成物の限定ignoreを保存する。入口掲載はまだ行わない。
2. 全保存ファイルをRemoteから再取得し、意図したbyteと照合する。
3. 公開した固定コードを使い、Root・入口・文書役割、Main／Support／29／30との責務、Report／Feedback、Harnessの原本と成果の境界を重点として、一件の読み取り専用レビューを行う。
4. Reportと最小証跡を保存・確認した結果に応じ、Root README・Repository Review入口・変更記録索引を限定更新する。改善提案は記録に留める。

初版公開commit時点では、2–4は未確認だった。後続の実際の到達点を以下へ追記する。初版時点の予定を遡及して成功へ書き換えない。

## 能力の境界と復元

初版のread-onlyはReview操作の契約であり、Hostから書込Toolを除去する強制sandboxではない。PythonにはGitHub書込APIも対象コード実行もないが、Host全体の権限分離、Windows、外部URL・anchorの自動網羅、別AIによるcold start、反復利用効果は未確認。

原本取得と読解申告、機械合格と意味判断、ローカルZIPと永続保存、ReportとHuman Feedbackを別に扱う。証跡ZIPは原本cacheを含まないため、完全なRepository backupや単独で再開できるrun backupとは呼ばない。

復元は、利用案内の限定差分を外して従来のReview Prompt直接利用へ戻せる。コードとrunは固定版の証拠として保持できる。既存ファイルの移動・削除がないため転送Stubや原本移設の逆操作は不要。後続mainに他担当変更がある場合は本件の差分だけを戻し、main全体を過去へresetしない。固定履歴リンクは書き換えない。

<a id="live-trial"></a>

## 2026-10-29 — 公開した固定版による実地試験

初版commitは `a038ab0676cbe307d75f9866b1e838397608b404`、treeは `496c82db02b66bbe724e9da7d2d5179a5af99997`。17ファイル・本記録・限定ignoreの**19対象**をRemoteから全文再取得し、意図した内容との一致を確認した。対象以外のblobは公開基点から保持し、削除は0。取得し直した固定コードを別の作業コピーへ置いて利用した。

- run ID：`9e01bae3-93ac-4439-9357-d5f0fcd5439a`
- 対象とtool commit：上記初版commit
- tool code SHA256：`b84993146512b8db5ecb546ed83a8f854c19075777b95b4ae1a8ca0fafaff45c`
- 方法：`repository-reviews/review-prompt.md` v002、blob `913814722c8eccbbda2b579b3ddab4f126fa081d`
- 重点範囲：Root・入口・文書役割、Home Bの到達点、Main27／Support28／Ark29／Ark30の所有、Report／Feedback、Harnessの原本・実行状態・成果の境界。
- 原本39資料を固定版でbyte照合。全文読解申告22、関連範囲8、取得のみ9。同一作業で全文を読んだ契約はblob同一性で再利用し、Root READMEの並行Ark-OKF差分を確認した。全文取得と全文読解を混同していない。
- 比較資料：`repository-reviews/reports/2026-09-19-02.md`。当時の全体レビュー七論点を全面再検査したわけではなく、全体基点と重点観測、現用経路と固定Bindingの分離を比較した。

### 実際に成立した経路

WorkのGitHub読取Connector → HostによるJSON受渡し → Pythonのtree/blob/byte照合 → 実読解範囲の記録 → 意味と所有関係の比較 → 計画pause → 別processでresume → HTML Reportとresult → 結果検証 → 最小証跡ZIP → 成果物保存、を一件として実施した。レビュー中のGitHub操作はGETのみ。実装公開と後続の入口掲載は観測期間の外で扱う。

大きなtreeの受渡しはShell引数長の上限に当たり、内容を分割保存して回復した。取得処理中に別CLI読取がWriterと競合した際は後続ingestが拒否され、既に照合済みの26資料を確認して残10件を逐次取得した。追加依存3資料も照合した。これらを無かったことにせず最小eventへ残した。

計画pauseはHuman STOPではない。別processのresumeは、有効な依頼・同じコード・固定入力・原本cacheを再確認して成立した。その後のHumanの「続きから実行」では、runがactiveで結果未保存であることを実体確認し、未完だったReportと保存から継続した。

終了時mainは `6a3724475ac9e2f48ccff9463818110680b57a71` へ進んだ。差分は他担当による共有 `references/feedback/feedback.jsonl` と `references/lessons/lessons.jsonl` の二ファイル。取得済み39原本のblobは変わっていない。追加データ本文を開始Snapshotへ混ぜず、固定時点の重点報告とした。入口公開はこの並行成果を含む最新treeへ重ねる。

### 意味の確認と保持する所有

1. **H1 — 入力例の不整合を発見。** [固定Adapterの例](https://github.com/yusukefujiijp/ai-project/blob/a038ab0676cbe307d75f9866b1e838397608b404/harness/adapters/chatgpt-work/README.md#L13-L28)の `harness/`・`repository-reviews/` は、[入力規則](https://github.com/yusukefujiijp/ai-project/blob/a038ab0676cbe307d75f9866b1e838397608b404/harness/src/ark_harness/contracts.py#L21-L26)と一致せずstart前に拒否された。run未作成を確認し、試験用入力だけを `harness`・`repository-reviews` へ正規化して続行した。公開例・コード・テストの修正は、試験で見つけた改善を実装しないという今回の境界に従い行っていない。再利用時に注意する既知の制約であり、改訂するなら例と規則の整合が優先候補となる。
2. **H2／H3 — 原本と担当を保持。** 現行のARK／AGENTS／Root README／Domain READMEの分担と、Home Bの検討進展・統合実装未承認を分けた。Main27の全体判断、Support28のReport／Feedback、29のHome B補助、30の既存Report補助比較という公開記録の担当をHarnessへ移管しない。これらは観測Snapshotの記録であり、後の各Threadの新しい依頼や役割を凍結しない。
3. **H4 — 準備時Stateを現在の失敗にしない。** 12／08の初期Stateには当時の未観測表記が残る一方、Current11／07の `progress.next_transition` に後続の受入れ完了記録がある。今回直接読んだのは公開記録で、当時の観察者への帰属を保持した。現在のWork UIや受け手の内部理解を再検査したとは報告しない。
4. **H5 — ReportとFeedbackの所有を保持。** Human向けHTMLをprimaryとし、機械交換用resultを分けた。ReportはCurrentや方法の第二原本ではない。Report固有の二件のFeedback、共有Referencesの契約と専門側データを同期コピーせず、期待・批評・初回実験の合格評価・実利用効果を分けた。
5. **H6／H7 — 機械的な成立と意味・権限を分ける。** 原本byte、読解申告、根拠行、出力hash、状態遷移を検証した。Host全体から書込能力を除去する強制sandbox、別AIの独立利用、Humanの利益は別の未確認能力として残した。

### 結果検証と保存

結果検証は**43 pass・1 warning・3 not-checked**で受理され、runは `complete`。warningは上記main更新、not-checkedは意味の機械的証明、Host全体のread-only強制、外部リンク等の自動網羅である。completeは依頼された重点レビューを閉じたという意味で、H1の修正や全Unknownの解消ではない。

指定した7経路のPath存在を確認した。過去報告の固定リンクは `47509f5c3e37f6307ff518edd499ede860b90843` のtreeで評価し、anchorの意味は未検査のまま保持した。Root→Harnessは掲載候補のPath存在検査であり、この観測時点で既にRootへ掲載済みとは記録していない。

Humanへ提供する成果は次の二つ。成果物保存先から各ファイルの成功と識別情報が返り、ローカルファイルとの対応も保存された。これらのHuman向け保存を、GitHubから全AIが自動取得できる原本へ昇格したとは扱わない。本STRは公開可能な導入・観測・制約を所有し、原本cacheや私的会話全体を複製しない。

- `ark-harness-review-2026-10-29.html`：28,240 bytes。SHA256 `5a4385ec27d9fe04f194bbfc067d7825647e8a3e517fd2af4291642ff5d43961`。
- `ark-harness-review-evidence-2026-10-29.zip`：86,953 bytes。SHA256 `ebc34503557327f4607ea7a2ba47bdbab08edff0535d560b4904e51a028665e9`。14 memberを読み戻して実体一致。request・Profile・二時点のtree・run・sources・最小events・result・validation・HTML・機械テスト記録・参照検査・HTML構造検査・main差分を含む。原本cacheは含まない。

HTMLは構造・内部リンクを検査した。描画用ブラウザ実体がなく、ブラウザ画像renderとHuman端末での実表示は未確認。Markdownだけを許す出力制約は設けていない。

### 限定入口と切戻し

通し試験と保存の成立を受け、Root READMEにHarnessの一行、Repository Review入口に実行補助と試験への案内、GitHub整理入口に本STRの索引を加える。既存Review Prompt・全体比較基点を保ち、原本の移動・削除、Root文書統合、Actor State更新、製品設定、予定実行、発見した改善の実装はしない。

この入口commitは初版コードとは別に保存し、公開後に三入口と本記録をRemote全文再取得して差分一致を確認する。commit自身のSHAや保存後検査を本文内で先取りせず、実際の確認Receiptは最終応答へ示す。切戻しは本件の案内差分だけを対象にし、Home Bや他担当の並行成果を巻き戻さない。

<a id="local-revision-2026-10-31"></a>

## 2026-10-31 — 公開例・Work接続・状態別案内の局所改訂

### 採用範囲と基点

Humanは五ファイルの改訂案を採用し、その実装、必要な検査、GitHub反映とRemote再取得に限ってPlan-onlyを解除した。設計基点と実行開始時のmainは、ともに`158fed602a7c21c1316e32033087a4514dfecc7c`。AGENTS v004.14-candidate、artifact-to-github v001-human-authorized、現行の依頼・適用原本を確認した。同一性と適用条件を確認できる自身の全文読解を再利用した。

公開準備中のmainは`4d641377aa3688c6d4ea4882e56af1d3b43fbbc9`へ進んだ。差分は他担当による人物Wikiの三ファイルで、本件の五対象・AGENTS・Root README・方法原本は変わっていない。公開は最新headのtreeへ五対象だけを重ね、期待head一致を条件にする。他担当の人物Wiki、Home Bの最新反映、Root・AGENTS・各Actor・Report／Feedbackの所有を保持する。

変更対象は次の五ファイル。17ファイルの配置・原本所有は変更しない。

- `harness/adapters/chatgpt-work/README.md`：公開request例、Hostからのデータ受渡し、状態・整合性・現在の委任、応答欠落時の判断、結果と保存の境界。
- `harness/README.md`：入口の能力説明とWork Adapterへの案内。Home BのmetadataとHome／AGENTSの所有案内を保持。
- `harness/tests/test_sources.py`：公開例そのものを抽出し、現行Request parserへ通す回帰検査。
- `harness/tests/test_review.py`：CLI入出力、状態別の操作、欠損cache、応答失敗、既存のlock検査の拡張。
- `control-center/changes/STR-024-harness-repository-review.md`：本追記。初版の履歴を保持し、今回の観測を区別。

文書版は**v0.1.1**、実行実装は**v0.1.0**、交換schemaは**1**。実行用の六つのPython原本、Profile、依存設定、evals、レビュー方法原本は変更していない。方法は引き続き`repository-reviews/review-prompt.md`が所有し、複製・移動していない。新Skill、完全run復元、状態表示の作り直し、自動実行、製品設定、外部へのメッセージ送信、既存ファイルの移動・削除も本件に含めない。

### 改訂した説明と能力の境界

1. **H1の現用例を修正。** `harness/`・`repository-reviews/`を`harness`・`repository-reviews`へ修正した。Pathの許容範囲は広げていない。公開Markdownの指定区間をtestが直接読み、再び末尾slashへ戻した反例がparserで拒否されることも確認した。上のH1発見記録と初版への固定リンクは当時のまま保持する。
2. **HostからPythonへの受渡しを明記。** contentをJSON encoderへ渡し、Repository外・新run外の入力ファイルに保存する。`start`のrequestとtreeは別ファイル、profileはTOMLとする。対応する`--input -`には一つの完全なJSONを渡す。原文をShell codeや巨大な引数へ埋め込まず、CRLF・空白・末尾改行を保持する。ConnectorをPythonから自動呼出しする能力を追加したわけではない。
3. **active・paused・complete・partialを区別。** activeは現物確認後に続行、pausedだけがresume対象、completeとpartialは終了状態。終了後の証跡化・Host保存が未完であることと、レビューを再開できることを分ける。現在の有効な委任がある時に形式的な再承認を繰り返さない。
4. **cache欠損・破損を状態名へ混ぜない。** status等も失敗し得る。通常のingestは既存source照合を先に行うため、登録済みcacheを修復する操作にはならない。partialは破損を迂回しない。原本の再取得と旧runの復元を区別し、旧記録を保持して、必要なら現在の委任内で関係を記録した新runへつなぐ。専用修復・archive import・完全復元は未実装のままである。
5. **応答と実行結果を区別。** finishのcode 0はcompleteまたはpartialの受理、code 1はresult・validationが保存された検査不合格でactiveのまま。code 2や応答欠落だけでは未実行を証明しない。status成功は出力hashや永続保存の一括検証ではない。終了済みの結果を再検証するbundleと、Hostの保存先確認を分ける。

この局所改訂を成立させるための実行コード変更は不要だった。cache修復や完全復元など、現行実装にない能力を文書の説明で補ったとは扱わない。

### 今回実行した機械検査

Python **3.12.14**、uv **0.13.4**、POSIX環境で、次を実行した。

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=harness/src python3 -B -m unittest discover -s harness/tests -v
# harnessディレクトリで実行
uv lock --check --offline
```

最終の全testは**42件pass**（既存30件を保持、12件追加。既存のPath・lock検査も拡張）。lock整合確認も成功した。初版の30件passや43 pass・1 warning・3 not-checkedを今回の結果として流用していない。

追加・拡張検査では、公開例と境界目印、末尾slash拒否、1 MiBを超える合成sourceのファイル／stdin入力、別ファイルによるstart、二つのJSONを同じstdinから読む誤用の拒否、不正JSON、activeへのresume拒否、終了runの再開・更新拒否、partialのbundle、active／pausedのbundle拒否、欠損cacheによるstatus・show・resume・ingest・finishの失敗、code 0／1／2と保存結果、status／showのlock競合を確認した。cache改変検出、別process再開、改変出力のbundle拒否等の既存検査も通った。

応答欠落の回帰検査は、実際のfinishによる保存後、CLI応答の境界へ`BrokenPipeError`を注入した合成検査である。code 2でもrunはpartial、result・validationは保存済みであり、現物を確認してbundleを作れることを確認した。製品やネットワークのあらゆる切断、全書込段階での強制終了、完全transaction rollbackを検証したとは扱わない。

### Hostのファイル書込経路からCLIへの合成受渡し

unit testとは別に、このWork Hostで小さな合成contentを作り、JSON encoder → ファイル書込Tool → request／tree／source入力ファイル → `start` → `ingest --input -`へのファイルredirectを実行した。対象は架空の`example/repository`の`synthetic/transport.txt`。Repositoryの実原本をレビューした試験ではない。

Host側の元文字列から独立に得たUTF-8 byte列と、書込後のJSONを復号したcontent、CLIが保存したcacheを照合した。日本語、引用符、バックスラッシュ、CRLF、Shellで意味を持つ文字のliteral、末尾改行なしを含む**82 bytes・3行**が一致した。

- run ID：`ee0b2d7d-bef0-4baa-8763-910ac09dfcb0`
- 開始時刻：`2026-10-30T22:01:11Z`（2026-10-31 07:01:11 JST）
- 合成contentのGit blob SHA：`4d2494da4c8554af2546163c4df2ee806b3030f3`
- 合成contentのSHA256：`bbae3700c6fc991c244b21de3a9c8bd2833b39e8210292d58e40c2772b6d9d53`
- 実行コードSHA256：`b84993146512b8db5ecb546ed83a8f854c19075777b95b4ae1a8ca0fafaff45c`。初版と同一。

このrunは受渡し検査だけを行ったactiveの記録で、読解申告は0、review resultは作成していない。合成入力・一時Profile・cacheはRepository外の検査作業用で、五ファイルの公開対象へ混ぜない。入力の正確な受渡しが、このHostのこの経路で成立したことを示す。任意の容量や全Toolの自動接続、意味理解の証明ではない。

### 保存・参照・切戻しと未確認

公開前の検査結果を本追記へ記録し、GitHubへは五ファイルの局所差分だけを保存する。公開後は対象五ファイルを固定commitからRemote全文再取得して候補内容と照合し、最新mainとの関係を確認する。commit自身のSHAと実際のRemote確認Receiptは最終応答へ示し、この本文で保存後の成功を先取りしない。

現用のAdapter例とREADMEの利用説明は更新される。方法原本、Home Bの所有案内、過去のH1・初版試験・固定履歴リンクは保持する。切戻す必要が生じた場合は、本件の五ファイル内の差分だけを最新mainへ逆適用し、他担当の変更を保持する。main全体を過去へresetせず、運用runの状態やhashを書き換えない。

**今回の実地Repositoryレビューは未実施。** evalsの実行、独立した別AIの利用、Humanの実利用効果、Windows、Host全体へのread-only強制、完全run復元は今回確認していない。文書改訂、合成機械検査、このHostの合成受渡し、GitHub保存・Remote再取得、実地レビューの有無を分けて報告する。
