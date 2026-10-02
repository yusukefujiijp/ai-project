---
title: "アーカイブ案件 — 提案・判断・実施・記憶"
version: "0.8.0"
canonical_path: "control-center/ARCHIVE.md"
role: "Single record for archive proposals, Human decisions, execution and reconsideration"
status: "human-authorized record structure / per-case approval and execution below"
repository: "yusukefujiijp/ai-project"
primary_reader: "YusukeJP / Current AI / other AI / Future AI"
created: "2026-09-22"
updated: "2026-10-03"
expected_eof: "EOF::AI_PROJECT_CONTROL_CENTER_ARCHIVE::v0.8.0"
---

# アーカイブ案件 — 提案・判断・実施・記憶

**今後も使う資料を見通しやすくするため、役割を終えた現役配置を根拠から選び、YusukeJPの承認後に `__archives/` へ移す。提案から実施後の見直しまで、同じ案件で理由を辿れるようにする。**

最初の退役案件は[ARC-001](#arc-001)。続く三群は[ARC-002](#arc-002)・[ARC-003](#arc-003)・[ARC-004](#arc-004)、今回の実施経緯は[三群の記録](#archive-batch-2026-09-22)にある。chocoZAPの記録再設計と旧日別資料の保管は[ARC-005](#arc-005)、旧Plan Mode資料の退役と新Skillへの接続は[ARC-006](#arc-006)、旧Thread-End・Thread Craft三ディレクトリの退役と出典保持は[ARC-007](#arc-007)にある。初穂の形成史の保管と現役Actorログへの整理は[ARC-008](#arc-008)、旧Note六原本の保管と現役棚の退役は[ARC-009](#arc-009)にある。全体の目的と形成史は[README](README.md)、診断と優先順位は[PLAN](PLAN.md)、保存実体への入口は[__archives](../__archives/README.md)にある。本書は個別案件の判断・承認・結果を所有する。一般的な会話ログ、全ProjectのTask台帳、全作業の追加Boot条件にはしない。

## 1. なぜ記録するか

以下はYusukeJPとのこの構成を決めた対話の編集要約であり、逐語録ではない。

Player系三Repositoryのアーカイブから継承するSeedは、役割を終えることと知恵を渡すことを両立させる整理方法である。Humanはai-project全体のスパゲッティ構成を、整理整頓→レイヤー構造→関係の構造化→interface化へ進めたいと考え、不要になった現役配置のアーカイブを優先した。

さらに、既存の `__archives/` があることを重視し、AIが候補と理由を具体例付きで提案し、YusukeJPが承認した後に実体を移すことを明示した。その記録と記憶をMarkdownに残す理由は、他AI・Future AIが「何を移したか」に加え、「なぜ作られ、なぜ退役を選び、何を残したか」を理解するためである。

原文の要点は「archive候補とその理由を詳細明確に」「人間側YusukeJPが承認後__archivesに放り込む」「その記録と記憶を取るMarkdownが必要」。本書はこの意味を具体化する。GitHub上に元会話への検証可能なURLは記録していないため、上記対話の出典はこのThreadのHuman発言として区別する。

「不要」は現在の運用に置く必要がないという判断であり、知恵の無価値を意味しない。古さ、ファイル名、空ファイル、重複、検索結果がないことだけで退役を決めない。現在の役割と依存、維持・修正・移動それぞれの利益を比較する。初回調査時のPlan Modeとrollback用の旧版には異なる役割があり、当時は重複の外見だけで退役を決めなかった。その後のHumanによる用途・維持方針の変更を[ARC-006](#arc-006)へ記録し、初回の保持判断を恒久化しない。

## 2. HumanとAIの役割

AIは読取、根拠確認、候補選定、代案比較、影響範囲・保存先・復元方法の具体化を担う。Humanへ「どれが不要か」を説明なしに返さず、推奨と理由を判断可能な形にする。

このアーカイブ方針では、YusukeJPが具体的な対象と変更範囲を承認した後に、その範囲を移動する。関連ファイルを一案件にまとめて承認することもできる。承認済み範囲では、必要な参照整理・保存先照合・記録まで続け、同じ許可を反復して求めない。文書への掲載、方向性への賛同、歴史的な削除予定を、別の対象への移動承認に拡張しない。

通常の権限はCurrent Human Requestと[AGENTS](../AGENTS.md)に従う。これはHumanが今回指定したアーカイブの運用であり、無関係な修正・読取・作業へ新しい承認工程を課す意味ではない。新しいHumanの訂正・STOP・承認範囲の変更があれば、その差を案件へ記録する。

実行担当は依頼に応じてAIまたはHumanとなる。Humanが手動移動した場合は報告とRemote確認を分けて残す。保存されたMarkdownが、他AIの読解やアカウント設定へ自動反映されたとは扱わない。

## 3. 一案件に残す意味

案件IDは、提案・保留・承認・実施・復元を同じ経緯へ結ぶために用いる。パス名を後で変えても、以前のIDから到達できるようにする。

- 対象、元の役割、確認時点、根拠のパス・節・版。
- 何が現在の判断を難しくし、なぜ維持や局所修正よりアーカイブを勧めるか。
- 保存する内容・Seed・由来、移動先、影響する参照、対象外として残す資料。
- Humanの判断、対象範囲、条件、記録できる原文または編集要約。未確認の日時・承認・会話URLは補完しない。
- 実施前後の差、変更commit、保存内容・参照の確認結果、未実施・未観測の範囲。
- 期待した効果と実際の結果、失敗・訂正・保留理由、再検討や復元の条件。

状態は、例えば「候補→提案済み→承認済み→移動済み→確認済み」と区別できる。保留・見送り・一部実施・復元等も、実際の出来事に合う語で記録する。この語彙や項目数を全案件の固定Schemaにはしない。特に、承認と実施、保存と別AIの理解を一つの完了表示へまとめない。

案件冒頭に現在の判断を置き、後段に重要な形成・訂正の順序を残す。新しい事実で判断が変わっても、以前の理由を無言で消さない。案件を分割する必要が育った場合は本書を索引にできるが、同じ内容の独立原本を増やさない。

```mermaid
flowchart TD
    A["AIの候補提案"] --> H["YusukeJPの判断"]
    A -->|"根拠と変更案"| R["同じ案件の記録"]
    H -->|"承認"| M["移動と参照整理"]
    H -->|"保留・見送りの理由"| R
    M --> S["__archivesの保存実体"]
    M --> V["内容と参照の確認"]
    S -->|"由来をたどる"| R
    V -->|"結果と残った問題"| R
    R -->|"新しい事実で再検討"| A
```

アーカイブでは、現役として使う案内を外し、判断の由来へつなぎ直す。保存原本の古い `current`・承認・起動指示は当時の記述として読む。フォルダ名だけでは実行・書込みを技術的に禁止できず、実効的な呼出し元や通常案内が残る場合は案件の対策に含める。

## ARC-001

**完了：Human承認に基づき、撤回済み実験のchecker一つを通常のtoolsから__archivesへ移した。保存先の全文・blob一致、元配置の消失、関連記録と対象外ファイルの保持をRemote再取得で確認した。**

- **現在の状態**：個別承認済み・移動済み・Remote確認済み。Ark27:06のLiving Reviewで具体案を提示した後、新たなHuman実行承認により一ファイルの移動と関連三文書の更新を完了した。05の補足受入れ・ランキング希望・05→06準備の承認とは別の、今回の個別実行承認である。他の候補の移動や順位固定へ拡張しない。実行と確認の根拠はG節。
- **提案日・実行前確認日・実施確認日**：2026-09-22。確認時刻の基準はUTC。Human発言の未提示時刻は補完しない。
- **今回の承認範囲**：下記の一ファイル移動と、それに必要な索引・案件記録・診断の更新、保存後の確認。
- **全体診断との関係**：[PLANのD06](PLAN.md#d06)。
- **調査基点**：[commit d8c744d](https://github.com/yusukefujiijp/ai-project/commit/d8c744dd68d5a366855bb33e3167147adfc213cd)、Tree `aa85ce2f0a286c5c1891437a145c2301c6c99614`。再帰Treeは309ファイル、`truncated: false`。

### A. 対象と移動先

元の配置は `tools/check_repo_reality.py` の一つ。保存先は [__archives/ARC-001/tools/check_repo_reality.py](../__archives/ARC-001/tools/check_repo_reality.py)。提案・実行前確認時には移動先は存在しなかった。G節の実行commitで元パスの除去と保存先の追加を同じTreeへ反映し、main上の保存先と元配置を確認した。

対象blobは `9ae7c177a78f081d816a25da4d92021c5c582fec`、7,346 bytes。同じblobは[既存sandbox保存版][sandbox-checker]にもある。現役側の実体を内容変更なしで移し、既存sandboxはそのまま保持した。

移動後も元の相対パス `tools/check_repo_reality.py` を案件フォルダ内に保ち、由来の対応を見通せるようにした。原本のコードは内容を変更せず保存し、退役の意味と扱いは本案件・__archives入口で説明する。現役側に別コピーは残していない。

### B. なぜ存在し、なぜ退役を勧めるか

[実験の記録][sandbox]によると、2026-08-20にCURRENT_BOARD、checker、GitHub ActionsをRepositoryの通常配置へ接続した後、Human訂正でRoot READMEを復元し、実験資料をsandboxへ隔離した。当時の手動削除予定にはcheckerも含まれる。この予定は歴史的な根拠であり、今回の操作権限ではない。

今回確認した[checkerのコード][checker]は、`REQUIRED_FILES`で `CURRENT_BOARD.md` と `.github/workflows/reality-check.yml` を必須にする。しかし両方とも調査基点Treeにない。またRoot READMEがCURRENT_BOARDを案内しなければ警告を出す。

そのため、通常の `tools/` にあるcheckerを現在の正常判定と受け取ったAIが、撤回済みの仕組みを再作成することを「修復」と誤認する可能性がある。これは誤用経路の推論であり、今回実際に別AIが復活させたという観測ではない。

今回の推奨は、通常配置からの退役と理由の保存である。古い判定を現在の仕様へ書き直すには、新たな正常条件と用途の設計が必要になる。いまの目的は撤回済み実験の現役配置を整理することであり、そのツールの再開発を同時に始める必要はない。

### C. 参照関係の調査

GitHubの既定branchコード検索で `check_repo_reality` を検索し、9ファイルを取得した。結果URLはすべて上記基点commitを指していた。関連語 `reality-check` も検索し、7ファイルを取得した。下表は前者の9ファイルを意味別に整理したもの。検索断片だけで判断せず、必要なIdentity・該当節・コードと、既読資料の同一blobを確認した。

| Node | Edge | 確認した意味と移動時の扱い |
|---|---|---|
| [toolsのchecker][checker] | 自分自身と旧Board・Workflowを必須とする | 対象本体。通常配置から退役させる |
| [sandboxのchecker][sandbox-checker] | 同じ必須条件を保持する | 同一blobの歴史保存版。そのまま保持する |
| [sandbox README][sandbox] | 当時の配置・撤回理由・原型を記録する | 非現役の実験記録。歴史的なパスを一括置換しない |
| [sandboxのBoard][sandbox-board] | 実験当時の起動コマンドと配置を案内する | 親sandboxの隔離記録と組で読む歴史資料 |
| [sandboxの旧Root README][sandbox-root] | 実験当時の通常入口からcheckerへ案内する | 保存された旧Rootであり、現在のRoot READMEではない |
| [sandboxのWorkflow][sandbox-workflow] | Pythonコマンドでcheckerを呼ぶ | 保存資料内の実行定義。現行.github/workflows配下の定義ではない |
| [Ark21:06 Session記録][session] | 当時の未実施・Scope外候補として言及する | 経緯の原本として保持。実パスは小文字のark21-06 |
| [2026-09-19レビュー][review] | 当時の残存checkerを固定Evidenceで説明する | 日付付き観測。現在の状態へ書き換えない |
| [PLANのD06](PLAN.md#d06) | 残存配置の問題を診断し本案件へ案内する | 実施後に診断結果と残存範囲を更新する。固定Evidenceは保持 |

調査基点の `tools/` は対象一ファイルだけ。`.github/workflows/` には改行のみのREADMEだけがあり、同配下にYAMLのWorkflow定義はない。検索で見つかった実行コマンドはsandboxの歴史資料に属する。

**調査の限界**：これはTreeの全配置確認と、指定語による参照検索・対象箇所の意味確認である。全309ファイルの全文意味読解、全Git履歴、外部サービス・別Repository・個人端末の呼出し調査ではない。検索で一致しない動的呼出しや外部利用は未確認。検索結果だけから「どこからも絶対に使われていない」とは断定しない。

checkerは今回実行していない。レビューにある過去の実行結果を今回の検証結果として転記しない。

### D. 比較した案と保存するSeed

- **採用した案**：現役コピーを__archivesへ移し、既存sandboxと本案件へ由来をつなぐ。現役側の見通しと歴史保存を両立させる。
- **維持して注意書きだけ追加**：通常配置のまま誤用可能性が残り、不要な現役配置を減らすHumanの目的への効果が弱い。
- **現役コピーを除きsandboxへの索引だけ残す**：内容保存は可能だが、Humanが今回指定した__archivesへの実体移動とは異なる。前段のAI案から今回の推奨を改めた理由として残す。
- **checkerを再設計**：将来の選択肢として残るが、退役の完了に必要な作業ではない。

保存するSeedは、検査の着眼点、当時のコード、仮説を正常条件にした経緯、早い通常運用への接続を撤回した理由である。「失敗したから消す」「現在のcheckerが要求するから旧仕組みを復活させる」のどちらにも単純化しない。Future AIは新しい目的と根拠で再利用・再設計を提案できる。

移動自体でRepository全体のファイル数は減らない。現役側の `tools/` を退役させ、対象の実体と理由へ到達できることが、この案件の具体的な整理成果である。誤認頻度の低下や別AIの実理解は、配置の変更とは別の観測として扱う。

### E. 今回承認された作業範囲

1. `tools/check_repo_reality.py` を `__archives/ARC-001/tools/check_repo_reality.py` へ、内容を変えずに移す。
2. `__archives/README.md` に保存実体と本案件への索引を追加する。
3. 本案件へHuman判断・移動前後の対応・実行commit・保存確認・残点を追記する。
4. `control-center/PLAN.md` のD06を実施結果に合わせて更新する。提案段階で解消済みにしない。

この具体案では、歴史資料のパス記述はそのまま残す。PLAN・本案件が使う固定commitへのEvidenceリンクは、元のパスがmainからなくなっても当時の内容を参照できる。現行の新しい案内は実際の保存先へ向ける。

対象外はsandbox全体、Root README、他のtools、他のProject・Runtime、Workflowの新設・起動である。移動直前に対象や参照関係が実質的に変わっていた場合は影響を再評価し、承認範囲を広げる変更が必要ならその差分を示す。

### F. 承認後の実施・確認・復元

まずmain・対象blob・移動先の空き・関連する参照を再確認する。Contents APIで段階的に移す場合は、移動先の作成とRemote全文照合を先に完了し、その後に元ファイルを取り除く。途中で止まったら、保存先だけ存在する等の実状態を記録し、完了と扱わない。使用可能な手段と依存関係に合う実施方法を選べる。

完了時は、保存先の内容が承認対象と一致すること、元のパスが通常配置に残らないこと、索引から実体・由来・本案件へ届くこと、対象外に意図しない変更がないことを確認する。保存内容、参照整理、別AIの実理解は別の観測として報告する。

外部利用等の予想外の依存が見つかれば、その呼出し目的と現在の必要性を確認し、案内の修正、移動の見直し、復元を比較する。復元時は、保存実体または移動前の固定commitから同じ内容を元のパスへ戻し、関連案内と本案件へ理由を追記する。復元可能性と、古い判定基準を現役へ再採用してよいかは別に判断する。履歴の書換えを復元の前提にしない。

### G. 判断と実施の履歴

- **2026-08-20のHistorical Source**：sandboxに撤回・隔離と手動削除予定が記録された。今回の承認ではない。
- **2026-09-22・Human訂正**：現役配置のアーカイブを優先し、AI提案→YusukeJP承認→__archivesへの移動→理由と経緯の記録を指定。
- **同日・AI案の修正**：既存sandboxへの索引中心の案から、現役コピーを__archivesへ移しsandboxの文脈を保持する案へ変更。
- **同日・文書整備の実行依頼**：構成案提示後のHuman「OK！Very Good! 早速、やってみましょう！」を受領。README・PLAN・本書・__archives入口の整備と、候補の参照調査を実施する範囲として扱った。
- **同日・具体案の作成**：本案件に対象・理由・参照調査・保存先・実施と復元の方法を記録。個別移動の承認・実施・移動後の確認はまだ記録されていない。

- **同日・移動前の本流合流を指定**：四文書の保存・具体案の提示後、YusukeJPが「ここまでで一旦、Ark27：05の最新ark-projectに合流させよう！」と指示。移動後では接続が複雑になるという理由を説明した。これを[SUPPORT_RECONNECTの補足](PLAN.md#reconnect-ark27-05)へ反映し、移動を先行させず、成果・理由・未承認の範囲を既存05へ渡す。
- **Source準備と実体の区別**：今回の補足保存はPLANと本書に限定する。checkerの現役パス、既存sandbox、__archivesの保存実体を変更しない。Target受入れはPLANの補足接続で観測を区別し、そこから移動承認を自動推定しない。

- **2026-09-22・05での受入れを後続記録**：既存Ark27:05が四文書と六条件を根拠付きで理解し補足接続した。次Threadで候補をランキングとして比較したいというHuman希望を受領した。05→06の準備実行が承認されたが、本件の個別移動承認は含まれない。詳細な受入れ観測の所有先はPLAN補足§8、05の発言・判断の出典は同節が案内するR05。

- **2026-09-22・Ark27:06での個別実行承認**：06のLiving Reviewは本件について、現役維持と理由・復元経路を保つ退役を比較し、後者を推奨した。対象一ファイル、保存先、索引・案件履歴・PLANの更新、実行前の現物確認を提示した後、Humanが「良いですね！」「Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」と明示した。この応答を上記具体案の実行承認として受領し、同じ許可を再要求せず、必要な確認・保存・記録を継続する。出典はこのArk27:06のHuman発言。会話URLは未提示。他案件の移動・全診断の修正・新Trialの承認ではない。
- **同日・実行前のRemote確認**：[commit e3acc6f](https://github.com/yusukefujiijp/ai-project/commit/e3acc6f2c5e5f24f40a8e35aa3b9dea5801a9c0f)、Tree `12f003ce6d22a66fac1280c7b9defbe5255de0d7`。再帰Treeは316ファイル、`truncated: false`。元ファイルとsandbox保存版は同じblob `9ae7c177a78f081d816a25da4d92021c5c582fec`、7,346 bytes。移動先は未作成。`CURRENT_BOARD.md` と `.github/workflows/reality-check.yml` はなく、通常の `.github/workflows/` は改行のみのREADME一つだった。
- **同日・参照関係の更新確認**：同じ基点を指すGitHubコード検索で `check_repo_reality` は16ファイル、`reality-check` は8ファイル、いずれも `incomplete_results: false`。前回の9ファイルから増えた7件は、本案件、__archives入口、06のREADME・Handoff・State、05のState・Task Records。05・06の資料は確認済みのSource準備版と同じblobであり、当時の配置・未承認状態を継承する根拠として保持する。現役checkerの呼出し追加とは扱わない。sandboxの撤回理由、旧Board・旧Root・Workflowの呼出し箇所、Session記録と過去レビューの対象節を確認した。現在のRoot READMEには検索語の参照がなく、現役Workflowの呼出しも見つからなかった。全316ファイルの全文意味読解、動的呼出し、外部利用の不存在証明ではない。
- **同日・実装方法**：Git Data APIで現行Treeを基礎にし、元blob・mode `100644` をそのまま保存先へ設定する。元パスの除去、保存先の追加、__archives索引・本案件・PLANの更新を一つのコミットへまとめ、mainを非forceで更新する。親commitが変わった場合は差分を再確認する。checkerの実行や旧Board・Workflowの復活は行わない。
- **同日・移動実行とRemote確認**：[commit 2b8d06c](https://github.com/yusukefujiijp/ai-project/commit/2b8d06c6ba008c9b3044f851455d332067851e4c)、Tree `1c2f9f4861f269baca9d11faca5bcb3823862ac2`。mainのrefがこのcommitを指すことを確認した後、保存先コードと関連三文書をmainから直接再取得し、意図した全文・blobとの一致を確認した。保存先は元と同じ7,346 bytes・blob `9ae7c177a78f081d816a25da4d92021c5c582fec`・mode `100644`。Remote Treeで元ファイルとrootの `tools/` が存在しないことを確認した。
- **同日・変更範囲と案内の照合**：移動一件と関連三文書以外の既存312ファイルは同じblob・mode。総ファイル数は316で不変、Treeは `truncated: false`。Root README、既存sandbox、各ThreadのTriad、固定Binding、既存Workflow配置を保持した。関連三文書のYAML・canonical_path・版とEOF、42件の相対リンク先と取得済み対象の参照見出しを確認した。保存先・案件・由来の経路を接続し、履歴内の旧パスは当時の根拠として残した。
- **確認結果の保存と限界**：移動反映版はARCHIVE `0.2.0`、PLAN `0.4.0`、__archives入口 `0.2.0`。本改訂はその保存後観測を受けて案件とD06／E09を確認済みへ更新する。確認済みなのは配置・内容保持・関連記録の整合であり、別AIの実理解、誤用頻度の減少、動的・外部呼出しの不存在は認定しない。本書自身の最終blobを自己参照で埋め込まず、追記後の版はGit履歴とRemote再取得で照合する。

後続のHuman判断とActual Resultはこの履歴へ追記し、冒頭の状態を更新する。実施前の期待を成功実績へ置き換えない。


## ARC-002

**廃止済みWorkout Bridgeの原本を保存し、通常利用への案内を退役扱いへ更新する。旧Bootの固定参照を守るため、元パスの同一内容は互換用に保持する。元パス除去は未実施であり、完全な物理移動とは数えない。**

- **現在の状態**：Human承認済み・原本保存済み・退役案内更新済み・Remote確認済み。元パスは固定参照の互換用に保持し、その除去は保留。確認根拠は[今回の実施記録](#archive-batch-2026-09-22)。
- **対象**：`ai-ark-seed/ai-ark-seed-cards/next-cycle-workout-bridge.md`。
- **保存先**：[ARC-002の原本](../__archives/ARC-002/ai-ark-seed/ai-ark-seed-cards/next-cycle-workout-bridge.md)。元と同じblob `857e03089bd28063fa59d773782468b3a5aa54cb`、9,915 bytesを保持する。
- **退役理由**：[現行Ark27指示§8.9](https://github.com/yusukefujiijp/ai-project/blob/802b71f47411661457bd155dc07d63d2656158f6/ark-project/ark27/INSTRUCTIONS.md)は廃止済み・Closingとして復活させないと明示する。カードはArk23:07限定の非Canonical・E0・実地未検証候補であり、廃止前の設計と後続Correctionを区別して保存する。

### A. 依存と採用した方法

実行前のパス名検索は参照11ファイル。特に[Ark23:08 QueryのRequired Sources](https://github.com/yusukefujiijp/ai-project/blob/802b71f47411661457bd155dc07d63d2656158f6/ark-project/ark23/ark23-08/lords-complete-victory-tradeoff-resolution-best-practice_query.md)は元パス・blob SHA・Exact EOFを固定する。短い移動案内への置換ではこの一致を保てず、単純な削除は旧main指定の読取契約を変えてしまう。今回はカードのアーカイブ原本を追加し、元パスの同一blobも保持する方法をAIが選んだ。これは参照保全を含む承認済み整理の実装判断であり、Humanが特定の互換方式を逐語指定したという記録ではない。

[Card Shelfの入口](../ai-ark-seed/ai-ark-seed-cards/README.md)に、廃止、保存先、元パスの互換目的を表示する。[Living Fruitの原本](https://github.com/yusukefujiijp/ai-project/blob/802b71f47411661457bd155dc07d63d2656158f6/ai-ark-seed/ai-ark-seed-cards/living-fruit.md)にもBridgeを含む二段Closingと設定コピー文があるため、同入口で当時の記録として読む境界を説明する。Living Fruit自体の廃止や本文改稿は行わず、その固定blob `2f188ce6b04042fbd5f3575341c23aa0f5d7db49`と旧ThreadのBindingを維持する。

保存する価値は、現在回答の完了と次Query送信後の待機を区別した設計、任意性、身体Guard、Human Correctionの軌跡である。保存原本の承認・起動文はHistoricalであり、現在のClosingや身体Taskの発火権限ではない。

### B. 残点・再検討・復元

元パスへの直接アクセスは残る。入口の注記は技術的な実行停止機能ではなく、誤読減少・他AIの理解も未観測。原本を今後改訂する場合は独立二原本として同期を続けず、この案件で変更目的と固定参照への影響を先に解決する。現行の廃止決定はCard ShelfとArk27指示が案内する。

元パスを除去するには、旧契約を実行可能な状態で残す範囲と、固定commitによる歴史閲覧へ移す範囲を具体化する。今回の承認を旧Handoff・Query群の一括改訂へ広げない。今回の保存・案内を戻す場合は基点commitまたはGit履歴から対象の案内を復元できるが、Bridgeの再採用は別のHuman判断である。

## ARC-003

**X DeepQuoteの旧Stage 02と、そのファイル受け渡し方式を前提とする監査Packetの二資料を移動する。後続Stage 02と現在のStage 01・02Rは維持する。**

- **現在の状態**：Human承認済み・二原本の移動済み・Remote確認済み。元二パスと通常配置の`prompts/fable5/`は消失。確認根拠は[今回の実施記録](#archive-batch-2026-09-22)。
- **元の役割**：Stage 02は最終引用投稿・候補選択・Lite実行、PacketはX DeepQuoteとAI Output Polishを対象とした特定方式の監査依頼。

| Node | Edge | 原本の同一性 |
|---|---|---|
| `prompts/x-deepquote/x-deepquote_02-quote-completion-gate_v001-8.md` | [保存先](../__archives/ARC-003/prompts/x-deepquote/x-deepquote_02-quote-completion-gate_v001-8.md)へ移動 | blob `b9cf4e1c44bb1ec03b03502d08413f39ecb6a1ce`、14,169 bytes |
| `prompts/fable5/fable5-x-deepquote-markdown-handoff-ai-output-polish-audit_packet_v001.md` | [保存先](../__archives/ARC-003/prompts/fable5/fable5-x-deepquote-markdown-handoff-ai-output-polish-audit_packet_v001.md)へ移動 | blob `d90566ea95663c4ffa98ab0a8916036fbfabe01b`、7,093 bytes |

### A. 理由・代替先・参照

旧Stage 02 §16は`downloadable_markdown_file`、[後続v001-9 §16](https://github.com/yusukefujiijp/ai-project/blob/802b71f47411661457bd155dc07d63d2656158f6/prompts/x-deepquote/x-deepquote_02-quote-completion-gate_v001-9.md)は`chat_inline_markdown_block`を指定する。[現在のStage 01 §7](https://github.com/yusukefujiijp/ai-project/blob/802b71f47411661457bd155dc07d63d2656158f6/prompts/x-deepquote/x-deepquote_01-depth-builder.md)もChat Inlineを採用している。一方、旧Packetはダウンロード方式への移行を前提とし、現在のTreeにないStage 01 `v001-5`と旧Stage 02 `v001-8`を監査対象にする。

旧版の番号だけで退役とせず、この役割・出力差とHumanの今回の承認から、旧方式の通常配置を退役する。監査が実施・完了したという証拠は追加しない。既知の旧Stage 02パス検索は自身とPacketの2ファイル、Packet名検索は自身1ファイルであり、二原本を同じ案件に保存する。[Prompts入口](../prompts/README.md)から現在の三段階とこの履歴へ案内する。

`prompts/fable5/`は実行前に当該Packet一ファイルだけだったため、その通常配置がなくなる。`claude/`のFable5資料、AI Output Polish、Stage 02Rは対象外。Stage 02RはSourceへ立ち戻る修正という別の役割を持ち、現在もダウンロード方式を記述する。この案件はその仕様を変更せず、全Stageの出力方式が統一済みとも主張しない。

### B. 保存する価値・Unknown・復元

SourceとPublication Voiceの分離、未根拠情報を除く判断、公開可能時の停止、監査の観点を原本に保持する。旧Packet内の元パスはHistoricalとして残し、現在の監査依頼へ自動復帰させない。旧方式の外部利用・外部に保存されたQueryは未調査であり、検索件数を不存在証明にしない。

必要な外部利用が判明した場合は、その目的と現在の方式を比較する。復元は保存先から元の二パスへ同じ内容を戻し、Prompts入口と本案件へ理由を追記する。旧版を別方式として再採用する判断と、原本が復元可能であることを分ける。

## ARC-004

**旧Compile／Pickup四ファイルを移動する。文脈付きSeedを別Threadへ渡して成熟させる価値を保持し、新しい軽量Seed／Card化方式との完全同等を主張しない。**

- **現在の状態**：Human承認済み・四原本の移動済み・入口更新済み・Remote確認済み。現行Seed入口から役割差・保存価値・四原本へ到達できる。確認根拠は[今回の実施記録](#archive-batch-2026-09-22)。

| Node | Edge | 元blob |
|---|---|---|
| `prompts/ai-compile-ark-seed.md` | [保存先](../__archives/ARC-004/prompts/ai-compile-ark-seed.md)へ移動 | `c1684cfd34117eaf3208fbd6e8b2f732077de056` |
| `prompts/ai-compile-ark-seed_query.md` | [保存先](../__archives/ARC-004/prompts/ai-compile-ark-seed_query.md)へ移動 | `fe72a415643b4e403bb2fa8ac86e58c2a8b44c47` |
| `prompts/ai-pickup-ark-seed.md` | [保存先](../__archives/ARC-004/prompts/ai-pickup-ark-seed.md)へ移動 | `91a3727467262606e111d0307b85021885e22f81` |
| `prompts/ai-pickup-ark-seed_query.md` | [保存先](../__archives/ARC-004/prompts/ai-pickup-ark-seed_query.md)へ移動 | `0774ebcb5f4d24c5af0470774ef18d8bb4ad19d5` |

### A. 退役理由と、保持を必要とした違い

現存する[AI Ark Seed](../ai-ark-seed/README.md)は単一QueryでCOMPILE／PICKUPを解決する。旧四ファイルは別々のPairであり、本文の起動先にも不存在の`ark-project/prompts/`を保持していた。[既存レビュー§3.6](https://github.com/yusukefujiijp/ai-project/blob/802b71f47411661457bd155dc07d63d2656158f6/repository-reviews/reports/2026-09-19.md)もこの不一致を指摘する。ただしパス不良だけなら局所修正も可能であり、それだけを退役理由としない。

旧CompileはOrigin Context・Human Original Wording・因果・Unknown・First Legal Moveを伴うSeedとPickup-Ready Packetを作り、旧Pickupは専用ThreadでConcept Maturationを開始する。新Compileは軽量の`"Name(Definition)"`、新Pickupは選択したSeedのCard化判断を中心にする。この違いを[現行Seed入口の文脈継承案内](../ai-ark-seed/README.md#10-context-preservation)に残し、必要時に保存原本へ戻れるようにした。

例えば複雑なCorrectionを別Threadが深掘りする依頼では、一文Seedだけで文脈が足りると仮定しない。発見前の状況、Trigger、Humanの意味、変化、未確定、次の合法手を必要な深さで保持する。軽量Seed、文脈付き移植、永続Card化は異なる成果物であり、回答品質や説明を縮める理由にしない。保存原本は設計知識として参照し、旧Queryの不存在パスをそのまま起動しない。

### B. 依存・境界・復元

実行前の文字列検索では旧Compileは自身の二ファイルと固定commitへリンクする過去レビュー、旧Pickupは旧四ファイル内の参照だった。原本同士の関係はこの一群で保持する。過去レビューは観測時点の根拠として変更しない。

変更は入口の整理と四原本の移動であり、現行Query・Compile・Pickup Runtimeの契約、Seed Cardの内容、Field Test状態、Canonical Statusを変更しない。新方式が旧方式の全用途を代替すると実証したものでもない。文脈付き移植の依頼はCurrent Human Requestと適用される移行契約から扱い、旧Pairを自動Fallbackにしない。

旧方式固有の実利用が必要と判明した場合は、保存原本から四パスを復元する案と、その意味に合う現在の接続を比較する。復元時も原本内の旧パス不一致は自動的に解消しないため、利用可能と報告する前に経路を再確認する。

## archive-batch-2026-09-22

### 三群の承認・実装・確認を区別する

1. **提案**：Ark27:06で、第1位Bridge一ファイル、第2位X旧二資料、第3位旧Seed四ファイルを理由・依存・保存価値とともに提示した。第1位の固定参照と第3位の役割差を明示し、旧Plan Mode・thread-end・旧Thread群等は除外した。
2. **今回のHuman承認**：その直後のYusukeJPの「全てOK！」「Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」を、三群と必要な参照整理・保存確認への実行承認として受領した。出典は本Ark27:06会話。未提示の会話URLや発言時刻は補完しない。05の受入れ・次Thread希望やARC-001の承認の流用ではない。
3. **実行前のRepository確認**：2026-09-22 UTC、main [`802b71f`](https://github.com/yusukefujiijp/ai-project/commit/802b71f47411661457bd155dc07d63d2656158f6)、Tree `564e3645fd531a8f96e89722134ba2feefc2d291`、316ファイル、`truncated: false`。対象七原本はランキング調査と同じblob。新しい保存先は未作成。現行AGENTSと局所ガイドを照合し、確認済み06 Bootは再実施していない。
4. **AIの実装判断**：ARC-002は固定参照を保つ互換原本を元パスへ残し、アーカイブ保存と退役案内を実施する。元パスの除去は保留。ARC-003・004は六原本を移し、通常配置から除く。旧Seedの価値を現行入口から辿れるようにし、未承認のRuntime再設計や旧Thread一括改訂は行わない。
5. **変更範囲**：七原本の保存、六元パスの除去、ARCHIVE・PLAN・__archives入口・Prompts入口・AI Ark Seed入口・Card Shelf入口の更新。保存原本、Living Fruit、旧Boot資料、現行専門Runtime、Root指示、他のProjectは内容を保持する。
6. **移動・保存の実行**：mainを非forceで[commit `012323c`](https://github.com/yusukefujiijp/ai-project/commit/012323c58568a0fa1435be2c3e0399b66cab5f96)へ更新した。Tree `8e6c18b5ce613d91218a19908dfb97dbf8812b92`。七原本は既存blobとmode `100644`をそのまま保存先へ使用し、六元パスの除去と六案内文書の更新を同じcommitへまとめた。
7. **Remote再取得**：更新後のmain refを確認し、七保存先・六更新文書・Bridgeの互換元パスの計14パスをmainから直接再取得した。全文とblobが意図した内容に一致した。Bridgeの元パスと保存先はともにblob `857e03089bd28063fa59d773782468b3a5aa54cb`、旧Living Fruitも元blobを保持する。
8. **Treeと案内の確認**：再帰Treeは317ファイル、`truncated: false`。元六パスと`prompts/fable5/`はなく、対象外の既存304ファイルは同じblob・mode。現行専門Runtime、旧Plan Mode、旧Threadの固定資料、06 Triad、Root指示等を保持した。六更新文書のmetadata・必要なExact EOF・code fenceと、95件の相対リンク先、更新対象間の見出し参照を照合した。過去資料の旧パス記述を一括変更せず、固定commitの根拠を維持する。
9. **今回完了した範囲と残点**：ARC-003・004の六原本の物理移動、ARC-002の原本保存・退役案内・互換保持を確認した。ARC-002の元パス除去は未実施。旧Bootの再実行、別AIの理解、外部利用の不存在、誤読減少、実生活効果は未確認。本確認記録自体は後続の記録commitへ保存し、その最終blobを本文へ自己参照で埋め込まずGit履歴とRemote再取得で照合する。

調査は全Treeの配置確認、候補と関係する本文の照合、指定語による参照検索である。全316ファイルの全文意味読解、全Git履歴、動的・外部利用の不存在証明ではない。ChatGPT長期メモリは本件の保存Sourceに使わず、今回の会話と確認済みRepository本文を根拠とする。Root・Teshuvah・Human Foreground One・Guard、HumanのCorrection・STOP・Final Sealを保持する。新候補、次Trial、他Projectの整理を自動開始しない。

[checker]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/tools/check_repo_reality.py
[sandbox]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/ark-project/ark21/Ark21-06/sandbox/README.md
[sandbox-checker]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/ark-project/ark21/Ark21-06/sandbox/check-repo-reality-v001-experimental.py
[sandbox-board]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/ark-project/ark21/Ark21-06/sandbox/current-board-v001-experimental.md
[sandbox-root]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/ark-project/ark21/Ark21-06/sandbox/root-readme-v002-experimental-mistake.md
[sandbox-workflow]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/ark-project/ark21/Ark21-06/sandbox/reality-check-v001-experimental.yml
[session]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/ark-project/ark21/ark21-06/README.md
[review]: https://github.com/yusukefujiijp/ai-project/blob/d8c744dd68d5a366855bb33e3167147adfc213cd/repository-reviews/reports/2026-09-19.md

## ARC-005

**chocoZAPの現役記録をREADMEとJSONへ集約し、旧日別Markdown一式を、日付ごとの文脈記録を再利用するための資料として保管する。**

- **判断と実装**：YusukeJPが本会話の修正版計画へ実行・GitHub保存を承認し、AI assistantがこの版で新構成への切替と三資料の保管を行った。確認日：2026-09-24。正確な保存時刻・GitHub上の記録者・変更差分は本案件を追加したコミットで辿る。
- **調査・原本の基点**：main `4efbf44eb31c22c660d9c75f4be1917e3d3b716f`。GitHub接続はCONNECTOR_ONLY_MODE。確認済みの共通指示・Skillを再利用し、対象外の構成・他案件は保持する。

### A. 何をどこへ保存したか

| Node | Edge | 移行前のblob |
|---|---|---|
| `chocozap/README.md` | [注記付き保管版](../__archives/ARC-005/chocozap/README.md)へ接続 | `2c3becb892edbd9502c63215bdfec15057aa144c` |
| `chocozap/records/2026/2026-09-24.md` | [注記付き保管版](../__archives/ARC-005/chocozap/records/2026/2026-09-24.md)へ接続 | `79f0d020d90dbe624076da201c4faa8226974a2d` |
| `chocozap/records/undated/cz-visit-0001.md` | [注記付き保管版](../__archives/ARC-005/chocozap/records/undated/cz-visit-0001.md)へ接続 | `e27f1b6e545b4b5a6bdda5cdc8ff87825f338306` |

[現行のREADME](../chocozap/README.md)は案内を簡素化して同じ入口に残し、実データの正本を [sweet-spots.json](../chocozap/sweet-spots.json) とした。旧日別ファイルとundatedの移動案内は元パスから撤去した。旧mainの二つのファイルURLは存続しない。過去版は上記基点の同じパスから参照できる。

保管版にはfrontmatterの `archive_*` 項目と冒頭注記を追加した。注記を除いた原文は移行前の内容と一致する。保存版のblobは注記追加により原blobと異なる。日別記録の数値・引用・来歴、旧案内の設計と限定検証記録を保持した。旧相対リンクは当時の元パスを基準とするため、保存版の冒頭から固定commitの原本へ戻って辿る。

### B. Humanの訂正から残した価値

以下は本会話のHuman発言を編集した要約であり、逐語録やB-Gate実践の結果報告ではない。

1. 数値の記録・訂正に対して処理が重いというFeedbackから、Humanは日別Markdownの継続更新をやめ、READMEと一つのJSONを中心に作り直す方針を選んだ。月別等の分割はデータ量と実運用を見て再検討する。
2. 当初は旧記録を現行配置から撤去しGit履歴へ残す計画だった。その後Humanは日毎の詳しい記録を「ドラッカー的『予期せぬ成功』」と評価した。忘れやすい休日やB-Gate検出の情報を、日付と文脈を持つ記録から詳しく振り返る用途へ応用できる可能性を挙げた。
3. Humanは今回のchocoZAP運用ではカットする判断を維持しつつ、復帰や他分野への応用に備えてファイルを残す案を提示した。条件は、他AI・Future AIが現役と誤認して追記しないことだった。
4. AIが現役の入口・正本と保管資料を分け、状態表示と復帰条件を付ける計画を提示した後、Humanは「Execute GitHub OK」「実行して下さい！」と承認した。承認範囲は本移行・保管・必要な案内と確認である。

保存するSeedは、頻繁に更新する数値の扱いやすさと、一日の状況・本人の言葉・訂正・前後関係を後から辿れる価値を、それぞれの用途に合わせて残すこと。日別Markdownが無価値・不適切一般という判断ではない。Humanの好評価は保持し、B-Gateでの実利用や精密な想起の改善が実証されたとは扱わない。記録にない出来事や本人の心中を補完しない。

### C. 通常運用・再利用・復帰の境界

通常の読み書きと集計は現行READMEとJSONを使う。保管資料は二つ目の可変台帳や自動Fallbackではない。JSONが読めない時も、旧記録へ追記したり旧値を現在の値として代用したりしない。フォルダ名・注記は運用上の区別であり、技術的な書込み禁止権限を設定したものではない。

復帰や転用を検討する時は、この案件と原資料を読み、現在のHumanの目的・判断に照らして必要な要素を選ぶ。chocoZAPへ戻す場合はその時点のJSONとの責務を決め、現在の訂正を保持する。別分野では新しい目的へ合わせ、旧chocoZAP運用を自動再開しない。実際に復帰・転用したら、その根拠と実施結果を本案件へ接続する。

今回、B-Gateのデータ収集・新しい記録システム・別Skill・成功事例ファイル・定刻処理は作成していない。長期メモリは転記していない。Skillは保存詳細を現行READMEへ委ねる既存の接続を維持し、本文や登録設定の変更を必要としなかった。

### D. 確認の範囲

公開前の内容照合では、2026-09-24・来館cz-visit-0001・四機械六条件・O001〜O006・S01〜S06・C01の対応を確認した。O006の現在値は10kg、5kgは訂正前の申告であり、新しい来館や運動上の成長として数えない。日付確認、本人の訂正と実地Sampleへの評価を保持し、未報告の周回・運動量・時刻を追加していない。

JSONの構文とID・出所参照、保管注記を除いた本文の一致、現役側がREADMEとJSONだけになる構成と参照先を照合する。保存後は実行AIが当該版を再取得し、保存内容・撤去対象・参照先を確認して実際の保存版を完了報告に示す。この記録は内容照合とRemote確認を混同せず、保存後の結果を先取りしない。

今回の確認は構造とデータ移行の範囲である。通常の更新速度、他AIの実理解、誤追記防止の実績、B-Gate等での生活上の効果は別に観測する。将来の容量・読書き時間・競合・比較範囲に問題が現れた場合は、分割や運用を再検討する。

### E. 保存後の再取得確認

2026-09-24、AI assistantが移行コミット [`8121cad`](https://github.com/yusukefujiijp/ai-project/commit/8121cadd25fdf04431b93d81b4af865a771e0923) の公開後にmainを再取得した。更新・追加した七ファイルは保存予定の全文と一致し、ツリーの変更は計画した九パス（七ファイルの作成・更新と旧二ファイルの撤去）だけだった。現役のchocozap配下はREADMEとsweet-spots.jsonの二つ。六条件・訂正・出所を保持し、ショルダープレス片手の現在値10kgを再確認した。

JSONはUTF-8で1,996バイト。今回の再取得呼出しは約0.33秒だった。これは移行直後の一回の取得観測であり、通常の追加・訂正の総所要時間や速度向上の実証ではない。確認済み状態はこの保存版に対するもので、以後の更新は現行正本を読む。

## ARC-006

**旧Plan Modeの専用Subsystem八資料と旧v003 Pair二資料を退役し、一つのQueryから柔軟なPlan Mode Skillへ接続する。** 旧方式の機能同等な更新ではなく、Humanによる目的・維持方針の変更として扱う。

### A. 判断の形成と今回の権限

HumanはQuery分割を「短期視点ではプラス」「長期視点では大きなマイナス」と評価し、専用性の強いPlan Mode資料も時間経過後の使いづらさを理由に退役対象へ追加した。Plan Mode自体の重要性は維持し、一つの長過ぎず短過ぎないQueryから、案件に合わせて十分に考えるSkillへ接続する方針を選んだ。

移行Skillから横展開するのは、定型の責務を一つの入口の奥へ委ねる上層の設計であり、移行固有の本文や固定Gateのコピーではない。HumanはAIの自由度・創発性とFuture AIの深化・進化に応じた改善余地を求め、旧資料からの吸収を任意とした。採用の中心は現在の計画の品質であり、全旧機能の保存・旧v005との挙動同等性を条件にしない。

複数回のPlan-onlyによる調査・検討の後、2026-09-26の現在入力でYusukeJPは統一Queryの同時作成を明示し、「Execute GitHub OK」「Human Seal OK」「実行して下さい」と承認した。対象は新Skillの作成・導入・GitHub共有、旧十資料の退役、必要な九文書の案内・5W1H更新、検証・Remote確認である。以前の包括的なGoだけを根拠にせず、この具体化された計画への現在の承認を使った。

旧v005候補の採用Branchは**目的変更で終了**した。独立E1／E5はNOT RUN、旧方式採用のHuman Reality Verdict／Fresh Cutover Sealは未受領だった履歴を保持する。今回の実行承認を旧試験のPASSやFAILへ変換しない。[STR-002 §6.1](changes/STR-002-single-prompt-consolidation.md#61-plan-mode--目的変更による旧採用branchの終了)が過去の準備との関係を示す。

### B. 5W1Hと変更範囲

- **Who:** 意味・訂正・方向・実行承認はYusukeJP。設計・実装・確認はArk27:06のAI協働者（Codex実行環境）。GitHub author／committerと正確な保存時刻は、保存後の取得値を§Fへ記録した。AI担当とGitHub名義は区別する。
- **When:** 2026-09-26の承認・実装。会話の順序は上記の編集要約で残し、未確認の個別発言時刻や会話URLは補完しない。
- **Where:** `yusukefujiijp/ai-project` / `main`。原本基点は[commit 57d3d7f](https://github.com/yusukefujiijp/ai-project/commit/57d3d7f1f5d46cbcaefdc752608acb7021c06bae)、Tree `109b9d296c33e6a86b1e60f4220dbe01281fec15`。GitHub接続はCONNECTOR_ONLY_MODE。
- **What:** 下表の十原本を`__archives/ARC-006/<元パス>`へ移し、旧配置から除去する。共有Skillは`skills/plan-mode/SKILL.md`と`agents/openai.yaml`の二ファイルを追加する。
- **Why:** 休止・再開・維持・別AIへの継承を含めた負担を減らし、Plan Modeの高い可能性を特定時期の手順・固定出力へ閉じ込めないため。短期の成功を無価値にせず、長期の再評価を反映する。
- **How:** 元blobをそのまま保管先へ使用し、現役の案内を新Skillへ変更する。Skill形式・限定挙動・導入を確認し、GitHub保存後にCommit・Tree・本文・対象外保持を直接再取得して照合する。

更新九文書はroot `README.md`、`prompts/README.md`、`prompts/ai-full-rail-next-gate.md`、`control-center/README.md`、`control-center/PLAN.md`、本書、`control-center/changes/STR-002-single-prompt-consolidation.md`、`__archives/README.md`、`skills/README.md`。Full Railは§10・§14の旧Plan Mode参照と関連metadataのみを修正し、権限の所有先を現在のHuman入力・AGENTS・適用契約へ戻す。新Skillを全体の状態管理者にしない。

### C. 十原本の保存先

| Node | Edge | 保持するGit blob |
|---|---|---|
| `ai-plan-mode/ai-plan-mode_query.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/ai-plan-mode_query.md)へ移動 | `5efcb1ef0cc3288df577b28ec78e351aa9e48987` |
| `ai-plan-mode/ai-plan-mode.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/ai-plan-mode.md)へ移動 | `aa3c420bbfee56c94e12b7417ca567151139967e` |
| `ai-plan-mode/candidates/ai-plan-mode-v005.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/candidates/ai-plan-mode-v005.md)へ移動 | `6685c44a33ae7826fbd1437efacdb7ed043e327b` |
| `ai-plan-mode/README.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/README.md)へ移動 | `1e6d76b7b347469810962b99ba603cfdda9ed0c2` |
| `ai-plan-mode/tests/cold-start-test.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/tests/cold-start-test.md)へ移動 | `220339b3da56495d9c5395db0e232ddf772f1e32` |
| `ai-plan-mode/tests/fixtures/truncated-runtime-without-eof.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/tests/fixtures/truncated-runtime-without-eof.md)へ移動 | `2bea9dd426a8ef2c2843c892c5f0ab2f1597c950` |
| `ai-plan-mode/tests/partial-read-test_query.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/tests/partial-read-test_query.md)へ移動 | `d8e9ed357f0f7c895de24a00fa1a90b2bc89185d` |
| `ai-plan-mode/tests/single-prompt-v005.md` | [同一原本](../__archives/ARC-006/ai-plan-mode/tests/single-prompt-v005.md)へ移動 | `af563d1c1adeb68672380ea100a2589a0fd08d79` |
| `prompts/ai-plan-mode_query.md` | [同一原本](../__archives/ARC-006/prompts/ai-plan-mode_query.md)へ移動 | `f87f14605bc9cd63043be282dca9d3053fd8f525` |
| `prompts/ai-plan-mode.md` | [同一原本](../__archives/ARC-006/prompts/ai-plan-mode.md)へ移動 | `c895fa27ae5e13b4b3343f22e76cf46b845bfa0b` |

保管版は原文・改行・metadata・EOFを含めて同一blobとする。意図的にEOFを欠く`truncated-runtime-without-eof.md`もFixtureとして保存し、完全なRuntimeへ修復しない。原文への注記追加は行わず、本案件と`__archives/README.md`で歴史資料の境界を示す。

元十パスに互換原本・Stubは置かない。旧資料の`active`、`current`、起動命令、試験Gate、`canonical_path`は当時の記述であり、現在の作業を拘束する入口や自動Fallbackではない。保管は旧仕様の全利益を新Skillへ移植したという意味ではない。

### D. 参照影響と復元

実体と現用参照の調査では、旧パス群への言及を退役十資料、現役六文書、歴史的五文書に分けた。Current mainの全Treeと指定語の検索を用いた確認であり、全Git履歴・全外部利用の不存在証明ではない。

歴史的な`thread-end/ark/ark0707_20260726_start-query.md`、`ark0705_20260722_handoff_v002.md`、`ark0705_to_ark0707_20260726_reboot-map.md`には旧v003への参照が残る。これらのmain上の旧資料URLは今回の除去後には解決しない。旧Ark07のBootを現在のmainで互換実行できるとは主張せず、当時の文脈は[移動前の固定snapshot](https://github.com/yusukefujiijp/ai-project/tree/57d3d7f1f5d46cbcaefdc752608acb7021c06bae)の元パスから辿る。履歴本文の一括書換えや旧Bootの再実行は行わない。

`repository-reviews/reports/2026-09-19.md`の固定観測とArk21 sandboxの歴史的記述も保持する。保管版の相対リンクは元配置を基準とするものがあるため、元の参照関係を再現する時は上記固定snapshotを使う。現在のArk27:06 Required SourcesのBindingは旧Plan Mode十原本を指しておらず、Current Triad・固定Runtime・共通移行契約は変更しない。

復元する場合は、現在のHumanの目的・対象・権限を確認し、必要な原本を保管先の同一blobまたは基点commitから取得する。原パスへ戻すことと現役へ再採用することは別であり、再採用時には現在の依存・案内・Guardを再検討して本案件へ理由と結果を追記する。過去の承認を現在の自動復帰許可にしない。

### E. 新Skillと確認境界

新Skillの原本・統一Query・限定応答確認は[Skills Hub §3.3](../skills/README.md#33-plan-modeの統一入口)が所有する。設計は一つの入口、柔軟な方法選択、必要な深さ、訂正可能な仮説、現在の権限と停止を中心にする。通常利用時の方法適応、改善案、永続改訂を区別し、毎回の自己監査や自動書換えを義務化しない。

導入・形式・限定挙動・Remote保存は別の観測であり、全AI互換性、自然な自動選択の安定性、Human UI操作、長期の保守負担軽減は未実証のまま残す。旧資料と新Skillの機能差はHumanが許容した設計変更であり、旧v005の試験通過へ置換しない。

「一時期の成功が、時間経過後の保守負担として現れる」ことを整理整頓の診断へ使い、他分野へ横展開できる可能性はSeedとして保持する。今回はHumanの運用評価と設計仮説であり、一般理論・生活上の効果・独立した新Projectとして確定しない。

ChatGPT長期メモリを保存Sourceに使わず、現在の会話と確認済みRepository本文だけを根拠にする。Root・Teshuvah・Human Foreground One・Guard、Correction・STOP・Final Sealを保持する。固定Graph／One-TableのBinding移行、ARC-002の元パス除去、D04、次Trial、実Thread移行、別の整理案件は開始しない。

### F. 保存後確認

1. **Skillの導入と同一性。** 2026-09-26、形式検証後にPlan Modeを導入し、保存先を再取得して本体・表示名・統一Queryを確認した。共有するSKILL.mdはUTF-8で5,823 bytes、SHA-256は`dec1a4b1d4f6d5df0cfc34aa1d443b1c07869592481cd93cf9ff965832c45a4e`。導入済み本文とGitHub共有本文は一致した。表示設定には同じQueryを保持し、導入環境が付加するアイコン・内部設定はGitHubへ輸出していない。このhashは初回版の証拠で、Future AIの改訂を禁止する固定条件ではない。
2. **公開直前のmain進行。** 調査基点の後に別作業が進み、公開直前のmainは`197281bbb7d7765bf4cb75a6228667db070cd00e`、Treeは`a79e3db227ee1c1c500efd9e8c763eaca7fa11ae`だった。既存326ファイルのblob・modeは調査基点と同一で、別作業の二追加を確認した。その最新Treeを親として使い、追加内容を保持した。別作業の内容を今回の成果や追加整理対象にしていない。
3. **実装Commit。** [`2827352`](https://github.com/yusukefujiijp/ai-project/commit/2827352cc7bbc8c22a3f1e89906565300cfd1860)。Parentは上記`197281b`、実装Treeは`0d5390a36239b7592d63e4f548844a8990ea43be`。GitHubから取得したauthor／committerはともに`yusukefujiijp`。保存時刻は`2026-09-26T08:28:14Z`（17:28:14 JST）。意味の承認とAIの執筆・検証担当は§Bの区別を保持する。
4. **Remote直接再取得。** `2026-09-26T08:29:12.861Z`（17:29:12.861 JST）に検証を完了した。上記Commitを指定して新規・更新11ファイルと保管10ファイルの計21本文を再取得した。11本文は保存予定の全文と一致し、10保管原本のblobは§Cの移動前blobと一致した。旧十パスはTreeに存在しない。
5. **変更範囲。** 追加12パス（保管10＋Skill2）、削除10パス、既存更新9パスの計31パス。公開直前の328ファイルから330ファイルへ変わった。対象外309ファイルのblob・modeは親Commitと同一で、Current Ark27:06 Triad、固定Runtime、共通移行契約、AGENTS、既存export-manifestを保持した。Commit・非省略の再帰Tree・mainの参照先も再取得して一致を確認した。
6. **構造と挙動の検証範囲。** 更新文書のIdentity・YAML・必要なExact EOF・Code Fence、243件の相対参照と更新対象内の57件の見出し参照を照合した。保管資料の旧相対リンクを現在の有効リンクと誤認せず、§Dの固定snapshotへ接続する。限定した三AI文脈・五応答の挙動はSkills Hub §3.3に記録した。旧試験E1／E5、全外部リンク、全AIでの再現、自然な自動選択の安定性、Human UI操作、長期効果の検証ではない。

Skill作成・導入、GitHub共有、旧十資料の退役、現用案内・5W1H更新、Remote確認は上記の範囲で完了した。この確認追記は同じ案件への記録更新であり、Skill再改訂や新試験ではない。追記自身の自己SHAは埋め込まず、保存後の再取得で照合する。次の接続はHuman Reviewとし、通常Unknownや残る別Branchを自動実行の理由にしない。


## ARC-007

**旧Thread-EndとThread Index／Mission Craftの常設入口を退役させ、27原本・成果・出典への接続を保持する。**

状態：**27原本の保管・通常入口の退役・出典整合・Remote確認完了**。Thread-End系21原本と蒸留・Mission Craft系6原本を、一つの案件の中で役割を分けて扱う。

### A. Humanの選択と今回の権限

2026-09-29 JST、Ark27:07のHumanは、GitHub整理整頓への集中を継続し、`thread-end/`・`_thread-index/`・`_thread-mission/`の三つを「取り敢えず、archive化したい」と提示した。最初は実装を止めたLiving Reviewを求め、AIは役割・保存価値・参照影響を調べた。

AIは「三ディレクトリ27原本の保管＋現役案内と出典接続の限定整合」を推奨し、旧方式を常設の実行入口から外し、必要時に参照・再採用する歴史資料へ移す意味を提示した。その直後、Humanは「Execute GitHub OK」「Human Seal OK」「実行して下さい」と、提示済み範囲の継続実行を承認した。本案件の権限はこのCurrent Human入力に基づき、Source06や別Threadの過去承認から借りない。

以上は現在の会話に基づく編集要約で、引用符内のみ短い原文抜粋。検証可能な会話URLは提供されていない。Humanの意味・選択・承認、Ark27:07 AIの調査・執筆・操作・検証、GitHubのauthor／committerと保存時刻を区別する。ChatGPT長期メモリは保存Sourceに使わない。

### B. 何を退役させ、何を残すか

| Node | Edge | 保存する価値と現在の位置づけ |
|---|---|---|
| `thread-end/`：21原本 | Threadの状態 → Handoff／Reboot Map／Start QueryとOne-Query Reboot | 方式・案内5文書と過去Thread資料16件。移行の意味、Human Seal、SourceとTargetの成功判定の区別、当時のCorrectionを同一原本で保持 |
| `_thread-index/`：3原本 | Raw Thread → Distilled Thread Source | Missionに直結する材料だけへ過適合せず、場面・Humanの願い・AIの誤りと回復・未消化の価値を残すCraftを歴史資料として保持 |
| `_thread-mission/`：3原本 | Distilled Source → Thread固有のMission Card | Sourceの深さとMissionの結晶化は別工程。Root Guard・誤読防止・Living Review等の設計価値を保持し、当時の固定制作手順を通常義務から外す |
| [Ark01 Thread Index](../ark-project/ark01/thread-index/README.md)と[Mission Card棚](../ark-project/ark01/mission-card/README.md) | 過去の制作方式 → 保存済みの成果 | 26分析原本・manifest・既存Cardをその場所に保持。二READMEのみ、旧Craftの現在の推奨と当時の制作根拠を分ける |
| 現在の[共通移行契約](../prompts/ai-next-thread-handoff.md) | 現在の依頼・Handoff → 移行準備とTarget再構成 | Current契約を保持する。旧三系統の全機能がこの契約や新Skillへ移植済みという意味ではない |

旧入口はRoot README・ARK・System・Note・Ark Domainに残り、Ark01 Mission Card側にも旧制作Workflowの推奨があった。物理移動だけでは旧手順を通常利用する案内が残るため、移動と現用案内の整合を同じ実装範囲にした。古い・未使用と推定した・似た名前という理由だけではなく、Humanの現在の選択と具体的な役割・依存を根拠とする。

現状維持は旧方式を常設の選択肢として残す。原本を除去してGit履歴だけへ委ねる案は、由来の発見を難しくする。全面的な後継Skillの制作を先行条件にする案は、今回の整理目的を拡張する。このため、既存アーカイブ方式を使う限定退役を採用した。

期待する効果は、現在の入口選択と過去の知恵の参照を区別しやすくすること。実際の利用負担軽減・長期効果・全AIでの理解は未観測。簡潔なHuman I/Oや入口整理を、AIの必要な検討・読解・説明の省略へ変換しない。

### C. 調査基点・変更単位・5W1H

- **いつ／基点**：2026-09-29 JSTの調査・承認。実装直前のmainは[commit 04055cb](https://github.com/yusukefujiijp/ai-project/commit/04055cba7279a6da95e0105c819729624c23b3aa)、Treeは`f4e501555e0558a0d40a5dc143f42fa5c00b4fc1`。再帰Treeは非省略、385ファイル。保存の正確な時刻は§GのGitHub結果で区別する。
- **誰**：YusukeJPが対象・意味・実行を承認。Ark27:07 AIが調査、原本保管と案内の設計・執筆、GitHub操作、Remote照合を担う。MainはArk27:07、control-centerはai-project全体の司令塔。Ark28の役割・支援入口は変更しない。
- **どこ／何を**：三ディレクトリ27原本を`__archives/ARC-007/<元の相対パス>`へ移し、元27パスを除去する。互換原本・Stubは残さない。現在の案内5文書、成果物のREADME2文書、出典3文書、台帳・索引3文書の計13既存文書を限定更新する。
- **なぜ**：旧方式の常設推奨を退役させながら、当時の知恵・未確定状態・成果・出典を辿れるようにする。ファイル総数の削減自体を成功条件にしない。
- **どう**：元のGit blobを新住所へ直接参照し、原文・改行・metadata・EOFを含め内容を保持する。移動と現用接続を同じTreeへまとめ、mainの進行を公開直前に確認する。Remote再取得・対象外保持・Binding確認後に実施結果を追記する。

調査では、三方式のREADME・Runtime／Craft・Queryの9文書と二Routerを全文読解した。過去16資料は状態・依存・参照箇所を重点確認し、27実体の取得を確認した。全385テキストファイルの参照文字列照合では、対象の元パス・ファイル名・現在のblob SHAを調べた。27原本のSHAを直接固定参照する記述は見つからなかった。これは全385本文の全面意味監査、全Git履歴・全外部利用・暗黙の依存の不存在証明ではない。

### D. 二十七原本の対応

| 元のNode | Edge：同一内容の保存先 | 保持するGit blob |
|---|---|---|
| `_thread-index/README.md` | [保管原本](../__archives/ARC-007/_thread-index/README.md) | `c2c00243833e30994206c96aeb0f42888745d119` |
| `_thread-index/thread-index_card-craft.md` | [保管原本](../__archives/ARC-007/_thread-index/thread-index_card-craft.md) | `fb9e5f3b28e703f4d6f0f0f0acf6db3f4fa11965` |
| `_thread-index/thread-index_card-craft_query.md` | [保管原本](../__archives/ARC-007/_thread-index/thread-index_card-craft_query.md) | `3f00c261b8f7bc26ab5182fed424ba53d2b245ea` |
| `_thread-mission/README.md` | [保管原本](../__archives/ARC-007/_thread-mission/README.md) | `8f4a890685e316e1ab8174dfc58419166e7ca882` |
| `_thread-mission/thread-mission_card-craft.md` | [保管原本](../__archives/ARC-007/_thread-mission/thread-mission_card-craft.md) | `cc189333ef32fd8a0557e7fe71ce61238ec7d347` |
| `_thread-mission/thread-mission_card-craft_query.md` | [保管原本](../__archives/ARC-007/_thread-mission/thread-mission_card-craft_query.md) | `32dca7822a982e64a42cd039796509b3313bd85b` |
| `thread-end/README.md` | [保管原本](../__archives/ARC-007/thread-end/README.md) | `b09019703e552993cc13f7b6a5231aba70a0d395` |
| `thread-end/ai-thread-end.md` | [保管原本](../__archives/ARC-007/thread-end/ai-thread-end.md) | `b00f6ce802590e9280320b70897eb0ebd12b49f1` |
| `thread-end/ai-thread-end_query.md` | [保管原本](../__archives/ARC-007/thread-end/ai-thread-end_query.md) | `4dd30988a4f2e7e41b61c2b77892615e9a483520` |
| `thread-end/ark/README.md` | [保管原本](../__archives/ARC-007/thread-end/ark/README.md) | `3f20ba3a490f7913a34a7ab3e8f4cdf0996e0707` |
| `thread-end/ark/ark07/README.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark07/README.md) | `5654e6a94038e1f0d4470c46f84d0f51dc8bc978` |
| `thread-end/ark/ark07/ark0705_20260722_handoff_v003.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark07/ark0705_20260722_handoff_v003.md) | `cf3afc5c1f1a9d6485b82bcf6774e701098afd5c` |
| `thread-end/ark/ark07/ark0705_to_ark0708_20260731_reboot-map.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark07/ark0705_to_ark0708_20260731_reboot-map.md) | `6d14ca80f52b20f10e508f3140b80727bfd8ec70` |
| `thread-end/ark/ark07/ark0708_20260731_start-query.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark07/ark0708_20260731_start-query.md) | `4ce6310c77efe4279dd72556663b0d293b0015f8` |
| `thread-end/ark/ark07/ark0711_20260806_start-query.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark07/ark0711_20260806_start-query.md) | `6d2a0bb998e195f1284137fa5d2f43af1c558b6f` |
| `thread-end/ark/ark0705_20260722_handoff.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark0705_20260722_handoff.md) | `0ccff2b94bfe43aaadddb3eb33aa2227f92de862` |
| `thread-end/ark/ark0705_20260722_handoff_v002.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark0705_20260722_handoff_v002.md) | `215e0f0405ac5278c41a9478237135df9764945a` |
| `thread-end/ark/ark0705_to_ark0706_20260724_reboot-map.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark0705_to_ark0706_20260724_reboot-map.md) | `5850b84f661f4497cdb2e2c239ca13144b36ebed` |
| `thread-end/ark/ark0705_to_ark0707_20260726_reboot-map.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark0705_to_ark0707_20260726_reboot-map.md) | `f4b3f7750763ff462cf1081383cb36b93ee0786d` |
| `thread-end/ark/ark0706_20260724_start-query.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark0706_20260724_start-query.md) | `2a85e61f9b759d09d0926e336c90566cef92d0e1` |
| `thread-end/ark/ark0707_20260726_start-query.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark0707_20260726_start-query.md) | `5aa64a4746d17e6c7269d5df10698def4cbdf294` |
| `thread-end/ark/ark08/ark0707_20260726_handoff.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark08/ark0707_20260726_handoff.md) | `40cb603e57570f9541c608b4ced59c3ca9d93426` |
| `thread-end/ark/ark08/ark0707_to_ark0801_20260729_reboot-map.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark08/ark0707_to_ark0801_20260729_reboot-map.md) | `02dd825dffb27ab59965189bfda85493ca15705a` |
| `thread-end/ark/ark08/ark0801_20260729_start-query.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark08/ark0801_20260729_start-query.md) | `feeb9c2b3b0d0a55f6ae8aa18ffb9e1c7939009c` |
| `thread-end/ark/ark17/ark1701_20260802_handoff.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark17/ark1701_20260802_handoff.md) | `b434483a8081d9213a9d3442971a7f310cbfa02b` |
| `thread-end/ark/ark17/ark1701_to_ark1702_20260802_reboot-map.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark17/ark1701_to_ark1702_20260802_reboot-map.md) | `342c915f069b298fb14e943179207c4d4ddd9c35` |
| `thread-end/ark/ark17/ark1702_20260802_start-query.md` | [保管原本](../__archives/ARC-007/thread-end/ark/ark17/ark1702_20260802_start-query.md) | `97877bd35f250bd50886d85636822b87bd70116a` |

保管原本には注記を挿入せず、旧`canonical_path`も改変しない。当時の住所・命令・`active`・`pending`・`NOT_RUN`等は歴史記述であり、現在の実行権限や再開指示ではない。アーカイブしたことから、当時のMissionを完了・失敗・中止のいずれにも再分類しない。旧Routerの自動移動禁止と明示Human移行Missionによる再検討条件を踏まえ、今回は§Aの具体的な承認に基づいて移す。

### E. 現用接続と保持した歴史

| 対象 | 今回の変更 | 変更しない意味 |
|---|---|---|
| Root README・ARK・System・Note・Ark Domain | 旧方式の通常実行案内をARC-007の歴史資料案内へ変更 | Current共通移行契約、Main／Support、憲章、成長履歴、既存Runtimeの版 |
| Ark01 Thread Index／Mission CardのREADME | 保持する成果を明記し、旧Craft・追加候補・制作Workflowを歴史的説明へ区分 | 26分析原本・manifest・既存Cardの本文、制作時の出典、未確定評価 |
| [Ark11 Source Lineage](../ark-project/ark11/ark11.md#25-source-lineage)・[Waiting Trap Seed](../ai-ark-seed/ai-ark-seed-cards/foresight-waiting-trap.md) | Ark07:11原本の保管先と移動前snapshotを接続し、当時の住所を保持 | Field・Evidence・Boot・実施状態。原本保存を新しい実証として数えない |
| [AI-to-AI Communication §23.2](../prompts/ai-to-ai-communication.md#232-ark-sources) | Ark07:05 Handoffの保管先・元住所・固定snapshotを接続 | 当時のField Test結果、Protocolの実行契約、単一Prompt化の成果 |
| 本書・PLAN・__archives索引 | 理由・範囲・保存実体・確認結果を同じ案件へ接続 | 過去案件の証拠、日付付きRepository Review、Ark21 sandbox、当時の承認 |

調査で見つかった旧`_thread-end/`（先頭underscore付き）の歴史記述を、今回の`thread-end/`へ機械置換しない。既存CardのCraft名も当時の制作根拠として残す。STR-001の修復履歴やARC-006で説明した古い参照を、今回の所在地へ遡及的に塗り替えない。

### F. 復元・互換性・今回の境界

[今回の移動前snapshot](https://github.com/yusukefujiijp/ai-project/tree/04055cba7279a6da95e0105c819729624c23b3aa)は、今回移した原本・元配置と変更前の案内を回復する根拠である。一方、旧Plan Modeへ依存するArk07資料については、ARC-006が指定した[さらに前のsnapshot](https://github.com/yusukefujiijp/ai-project/tree/57d3d7f1f5d46cbcaefdc752608acb7021c06bae)も保持する。今回の移動前snapshotだけで、既に退役した依存まで復活するとは扱わない。

原本の同一性、出典へ到達できること、当時の文脈を調べられること、旧Bootが現在のmainで動作することは別である。保管内の相対リンク・main指定・起動命令を現在の実行互換性として保証せず、旧Bootや未実施試験を再実行しない。具体的な現用consumerや外部参照の必要性が後から判明した場合は、影響する枝の接続・復元・再採用を現在のHumanの目的と権限から検討し、本案件へ理由と結果を追記する。

Scope外は、Graph／One-Tableの固定Binding移行、ARC-002の元パス除去、D04、Ark01成果の一括変換、旧試験再開、新Skill制作、別のアーカイブ、実Thread移行。旧Plan Mode v005の未実施試験は目的変更で終了した履歴として保持し、今回のNext Gateにしない。新Plan Modeの導入・共有・限定確認と、長期効果・全AI互換性は区別する。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのCorrection・STOP・Final Sealと適用Guardを保持する。器の退役を信仰・Mission・Humanの経験の処分へ変換しない。

### G. 保存後確認

1. **実装commitと担当。** [`8f013f3`](https://github.com/yusukefujiijp/ai-project/commit/8f013f3480f6026008e1505c72739127a0a5cd3c)。Parentは`04055cba7279a6da95e0105c819729624c23b3aa`、Treeは`6e9ff8e2b6fbac9d812debf515ee926b0f8e1c97`。GitHubのauthor／committerはともに`yusukefujiijp`、保存時刻は`2026-09-29T11:59:49Z`（2026-09-29 20:59:49.000 JST）。Humanの意味・承認と、AIの執筆・検証担当は§A・Cの区別を保持する。
2. **Remote直接再取得。** `2026-09-29T12:00:52.446Z`（2026-09-29 21:00:52.446 JST）に、上記commitを指定して40本文（保管27＋更新13）を直接再取得した。27保管原本は§Dの元blob・byte数と一致し、13更新本文は保存予定の全文・blobと一致した。Toolの保存成功応答だけで完了としなかった。
3. **配置と対象外保持。** 非省略の再帰Treeで、元27パスと旧三ディレクトリが存在せず、保管27パスが存在することを確認した。追加27・除去27・既存更新13の計67パス差分で、ファイル総数は385のまま。対象外345ファイルのblob・modeはParentと同一。Ark01の26分析原本・manifest・既存Card、旧Review・sandbox・過去案件原本を保持した。
4. **MainとBinding。** commit・Tree・main参照を再取得し、mainが上記実装commitを指すことを確認した。Ark27:07 Stateは変更せず、そこから参照するRuntime `b24c29e59d291fa58c3bf2c4c1fe4770fe468d70`、Handoff `1546f634ed0191b7b6ad22e73307885d9603a0d5`、章Runtime `e7caf9882a212cbda186362001e49791cff8a8ce`の固定Bindingを照合した。共通移行契約・AGENTS・Ark28資料も保持。既に確認済みのBootは再実行していない。
5. **構造と意味の確認。** 更新13文書のFrontmatter YAML、必要なExact EOF、Code Fence、251件の相対リンクと更新対象内の52件の見出し参照を照合した。通常の入口は歴史資料案内へ変更し、Ark01の制作手順は当時の説明へ区分した。Ark11・Seed・AI間通信の出典は保管先と固定snapshotへ接続し、元住所と当時のEvidenceを保持した。保管原本内の旧相対リンクは現行互換性の検査対象にせず、§Fの境界を適用する。
6. **確認の限界。** 以上は原本保存・現用案内・出典・構造・Remote実体の確認である。旧Bootの動作、全外部consumerの不存在、他AIの実読解、Human UI操作、生活上の効果、長期の負担軽減は実証していない。

三ディレクトリの退役と限定した接続整合は、上記の範囲で完了した。この完了追記は同じ案件の検証記録であり、別の整理・Skill改訂・次Trialの開始ではない。追記自身の自己SHAは埋め込まず、保存後に再取得して本文・EOF・Treeを照合する。次の接続はHuman Reviewとする。

## ARC-008

**新規Actor記録をdots/logsへ一本化し、固有な初穂の形成史は原文を変更せず保管する。** 現役領域の整理と、歴史を失わないことを両立させる案件。

### A. 判断・承認・対象

2026-10-02のDots対話で、Humanはlogsとrecordsを両方現役にする冗長性と、残すことで得られる耐性の釣り合いを問い直した。AIは一つの現役logsと、固有の形成史をrootの既存__archivesへ保管する構成を推奨した。重複する更新先は減らし、命名・初穂の意味・数え違いの訂正まで機械的な短いイベントへ置換しない判断である。[成功事例](../success-cases/decisive-choice-single-log-preserved-history.md)は、この決断へのHuman評価を所有する。

Plan-onlyで調査・計画提示した後、Humanは「Very Good! Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」と統合計画を承認した。これは当該Dots対話の編集要約と短い引用であり、会話URLや個別発言時刻は補わない。承認範囲は一原本の保管、必要な現用リンク・索引、Actorログ、STR、成功事例と検証。別の整理やlessons移設、Save Skill導入へ拡張しない。

### B. 対応・同一性・元の参照関係

| 元の配置 | 保存先 | 保持するblob |
|---|---|---|
| `dots/records/2026/20261001-first-fruit.md` | [同一原本](../__archives/ARC-008/dots/records/2026/20261001-first-fruit.md) | `7daa0946a812dcff15ded93b422c64f9f989e63f`、12,158 bytes、mode 100644 |

調査基点は[main snapshot 1eab746](https://github.com/yusukefujiijp/ai-project/tree/1eab74651f254ec32099c107e0ad90fef9a5de16)。[移動前の元パス全文](https://github.com/yusukefujiijp/ai-project/blob/1eab74651f254ec32099c107e0ad90fef9a5de16/dots/records/2026/20261001-first-fruit.md)から当時の相対リンクを辿れる。原文・改行・旧canonical_path・Exact EOF・相対リンクを含めて同じblobを新住所へ参照する。本文内に保管注記を挿入せず、元パスには互換原本・Stubを残さない。

保管した本文中の `../../actors/dot-0000/README.md`、`../../README.md`、`../../../control-center/...` は元配置基準であり、**保管先からはそのまま解決しない**。これらを現在も有効なリンクとは報告しない。元の関係を調べる時は上記固定snapshotの元パスを使う。現在のActor・Dots・STRへ進む時は[dots入口](../dots/README.md)と本案件を使う。

[STR-005](changes/STR-005-dots-collaboration-foundation.md)の元パス表と実装blob表は、当時の証拠として一切変更しない。保管を、STR-005が当時から新住所へ作成したという歴史に書き換えない。

### C. 現用接続・復元・境界

現用参照はdots README、Actor README（命名の§3 fragmentを含む）、Board Topic、STR-006の四文書から保管先へ接続する。Boardの通知・受信版、STR-006の他の責務や並行改訂は変更せず、リンク修復の理由だけをmetadataへ残す。ファイル名検索で確認した六文書のうち、形成原本は同一保存、STR-005は歴史証拠保持とした。全外部consumer・全Git履歴の調査ではない。

復元を検討する時は現在の目的・権限・依存を確認し、上表の保管先または固定snapshotから同じblobを元の `dots/records/2026/20261001-first-fruit.md` へ戻せる。必要な案内を対応させ、理由をこの案件へ記す。原本の復元可能性はrecordsの並行運用への再採用承認ではなく、Repository全体のresetも行わない。

実装・技術検証・公開証拠は[STR-008](changes/STR-008-actor-logs-and-preserved-history.md)とそのGit履歴へ接続する。配置の切替と長期の負担軽減・Future AIの実利用は別の確認である。

## ARC-009

**旧 `_note/` の六原本を同一blobで保管し、現役の汎用Note棚を退役させる。知恵の保存・再利用と、現在の運用指示を分ける案件。** 六原本の同一保存・旧配置の退役・五文書の限定整合を実装し、Remote再取得で確認した。根拠は§G。

### A. 判断の形成・承認・今回の担当

Ark27:07で、Humanは `_note/` を「活用しようと思ったが上手くいかなかった」と報告し、アーカイブ案と、方法を改善して残す可能性の双方を検討するよう求めた。当初は「まだ実装せず」というPlan-onlyだった。ARC-007の三ディレクトリに対する承認を `_note` へ流用せず、提案段階として保持した。その状態は[当時のBoard受領記録](../board/topics/20261001-dots-work-reconnection/replies/20261001-ark27-07.md)にも残る。

2026-10-03 JST、Humanは `_note` 検討への再接続と残り利用枠の活用を求めた。Ark27:07は六本文・参照・現行AGENTS・Dotsの所有範囲を照合し、六原本の同一保存と五文書の限定整合を具体化した。その後、Humanは「OK！Very Good! 実行して下さい！」および「Execute GitHub OK!」「Human Seal OK!」と承認した。今回の変更はこの承認に基づく。上記は本会話の短い引用と編集要約であり、未確認の会話URLや発言の秒時刻は補わない。

- **意味・範囲の承認者**：YusukeJP。
- **実装・結果統合担当**：Ark27:07のCurrent AI。読取専用の独立レビュー担当は参照・保管境界を点検し、書込みは統合担当のみが行う。
- **対象**：下記六原本の移動と、Root README・本書・PLAN・__archives索引・STR-001の案内／証拠リンク。別の整理候補の実装は含まない。
- **併せて受けた別成果物の依頼**：実行後の盤面から、Token Reset後のGitHub整理整頓の指針を一つのMarkdownへ保存する。これは時点付きの再接続資料であり、Reset操作・新Thread移行・候補全件の実行承認ではない。
- **GitHubの名義・保存時刻・Remote観測**：実施後の§Gで、意味承認・AI担当とは別に記録する。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・整理・文書はKeliであり、HumanのCorrection・STOP・Final Sealと適用Guardを保持する。ChatGPT長期メモリを本案件のSourceや保存対象にしていない。

### B. なぜ現役配置を退役させるか

確認基点は[main snapshot 5badd3a](https://github.com/yusukefujiijp/ai-project/tree/5badd3ab3bbface75a4663c5d03116adae7b0323)。六ファイル、合計70,601 bytesが存在した。READMEのCurrent Notesは五本文のうち一件だけを案内する。本文には条件付きの観測・有用な方法と、特定モデルの固定分担、main一律優先、操作ごとの再承認等の古い運用指示が混在している。これらを現行AGENTSの委任・継続・復旧契約より上位に置かない。

Humanの「うまくいかなかった」という評価と、上記の文書上の不整合はConfirmedとして区別する。低い利用頻度や失敗原因の全体を測定したわけではない。「どの依頼で読み、何の判断に使い、どこで更新するかという接続が弱い」という原因解釈はAIのCandidateである。

維持するなら索引の補完、観測と現行指示の分離、読取条件・更新担当、AGENTS／Skill／Project原本との責務整理が必要になる。現時点では、その保守を必要とする独立した具体用途を確認していない。既存の所有先と並行する総合棚を再建するより、原本と再発見の入口を保存する判断を採用した。古さ、六件という数、検索結果の少なさだけを退役理由にはしない。

Dotsの[lessons契約](../dots/README.md#5-dotsの学びを次の判断へ戻す)はDots自身の仕事から得た条件付き学びを所有する。旧Noteを一括輸入すると、異なる経験の観測者や適用条件を混同し得るため、今回は移植しない。必要になった知恵を出典付きで使う余地は保持する。

### C. 保存する知恵と再利用の入口

| Node | Edge | 保存価値と現在への適用境界 |
|---|---|---|
| README | Noteの身分 → 現行所有先との区別 | 判断材料は自動権限ではない。旧汎用保存先の指定はHistorical |
| AI Multi Production | 工程分担 → Humanの集中・統合責任 | 工程を分ける知恵を保持。モデル名による固定の優劣・役割を現在へ流用しない |
| ChatGPT GitHub | 保存 → 再取得 → 内容欠落検出・回復 | 保存と検証をつなぐ。main一律規則・再承認の旧条件は現行AGENTSと区別 |
| Fable5 Mission | 野心＋制約 → 成果・限界・次Action | 終了済み目的の混入を防ぐ。過去の投稿本数・監査制限を今のGateにしない |
| Fable5 Review | 外部指摘 → 採用・不採用・保留 | レビューを機械的採用せず必要な修正を判断。特定モデルの恒久的必須工程にはしない |
| GitHub Bottleneck | 条件付き成功・失敗 → 次の操作判断 | 操作・観測・回復を分ける。当時のConnector挙動を現行環境の保証にしない |

この表は原文を置換する要約や、新しい共通運用規則ではない。読み直す際の問いを示す入口である。全知恵のSkill化・Canonical化をアーカイブの前提にせず、原本へ戻れるまま必要時に再検討する。

### D. 六原本の対応と同一性

| 元パス | 保存先 | 保存するblob | bytes |
|---|---|---|---:|
| `_note/README.md` | [保管原本](../__archives/ARC-009/_note/README.md) | `96999cba0c375d7115c10b7383bd2f2c235681f1` | 6,155 |
| `_note/ai-multi-production_note.md` | [保管原本](../__archives/ARC-009/_note/ai-multi-production_note.md) | `faf6ebd02d6db8074f626508992f4b40235a35b2` | 11,605 |
| `_note/chatgpt-github_note.md` | [保管原本](../__archives/ARC-009/_note/chatgpt-github_note.md) | `3853dec1bdd154c03aaf72fe3510ba5cdbdb73de` | 19,380 |
| `_note/fable5-mission_note.md` | [保管原本](../__archives/ARC-009/_note/fable5-mission_note.md) | `1bd89fc6991f3c35f6cdeae3a4614eac75b1e4a4` | 13,389 |
| `_note/fable5-review_note.md` | [保管原本](../__archives/ARC-009/_note/fable5-review_note.md) | `15de19cffc3b8365cd6aa6c06c6f78a55e3d75b7` | 11,259 |
| `_note/github-bottleneck_note.md` | [保管原本](../__archives/ARC-009/_note/github-bottleneck_note.md) | `a71464c1727966447d65bbc79d7bcad4cb24d520` | 8,813 |

全原本のmodeは100644。本文・改行・旧canonical_path・active等のmetadata・過去の命令を改変せず、同じblobを新住所へ参照する。元の `_note/` にStub・互換原本・新READMEを残さない。六原本の保管を、当時のMissionが完了・失敗・中止した証拠へ変換しない。

### E. 現役案内・歴史証拠・参照の区別

1. **Root README**：現役のNote棚への案内を本案件へ接続し、保存価値とHistorical身分を明示する。
2. **本書・PLAN・__archives索引**：判断・承認・保存実体を同じ案件へつなぐ。PLANと索引に独立した承認・通信状態台帳を作らない。
3. **STR-001**：file-manifestの `_note/README.md` リンクを[当時の実装commitの本文](https://github.com/yusukefujiijp/ai-project/blob/9dd82cc37d9e95e03505949c18f66ffd26914a99/_note/README.md)へ固定する。直接再取得したblob `bca4449a8a76c5099a24e5fa45495e0dedf7b9a9` は表の証拠と一致する。今回保存する最新版 `96999cba0c375d7115c10b7383bd2f2c235681f1` と同一視しない。元パス名・当時のblob・担当・結果を保持する。
4. **保持する歴史**：PLANの `cc560d1` 固定診断、日付付きRepository Review、Ark21 sandbox、Boardの当時の `_note` 提案段階の記録は塗り替えない。旧 `g_global/chatgpt-github.md` の歴史例など、この移動が新たに壊す参照ではない事項を一括修正しない。

調査は `_note/`・五実ファイル名・関係する入口を用いたRepository検索と原文照合である。Current07 Handoffの必須核に六Noteへの直接必須参照は検出されなかった。全Git履歴・全外部consumer・全AIの実行環境を網羅した監査ではなく、未知のconsumerの不存在は保証しない。独立レビューでも同じ限定範囲の参照・保存境界を点検した。任意のblob文字列補助検索の一件はrate limitで未確認だが、必須本文・実ファイル名・入口の確認不足ではない。

### F. 当時のリンク・復元・再検討

保管README内の `../prompts/`・`../control-center/`・`../__archives/` 等は元配置基準であり、保管先から同じようには解決しない。現行リンクとして成功と報告しない。[移動前の_noteフォルダ](https://github.com/yusukefujiijp/ai-project/tree/5badd3ab3bbface75a4663c5d03116adae7b0323/_note)と[README全文](https://github.com/yusukefujiijp/ai-project/blob/5badd3ab3bbface75a4663c5d03116adae7b0323/_note/README.md)から、その時点の参照関係を辿れる。現在の権限・協働方法はAGENTSや該当所有資料へ戻る。

復元を検討する条件は、具体的な現役consumer、保存した知恵を繰り返し使う独立用途、または今回の退役で生じた実害が確認された時。現在の目的・依存・Human判断に照らし、必要な原本を同じblobで元のパスへ戻し、案内を整合できる。main全体を過去commitへresetせず、後続のHuman・他AIの変更を保持する。復元可能性は旧方式の自動再採用承認ではない。

今回の完了条件は、六原本同一保存、元パス退役、五文書の限定整合、保存後のRemote確認と対象外保持である。旧Bootの互換動作、他AIの実読解、UI変更、長期の探索負担軽減、生活効果の実証は別である。

### G. 保存後確認

1. **実装**：[commit 02e9779](https://github.com/yusukefujiijp/ai-project/commit/02e9779fc628dbfe7ee9ed08275c6b839407ef0e)。Parentは `5badd3ab3bbface75a4663c5d03116adae7b0323`、Treeは `7b70f4bc4401238b41f0fd0039a393393378fa28`。GitHubのauthor／committerはともに `yusukefujiijp`、保存時刻は `2026-10-02T16:42:58Z`（2026-10-03 01:42:58 JST）。意味承認とAIの担当は§Aと区別する。
2. **Remote本文**：公開前に実装commitから11本文（保管6＋更新5）を再取得し、予定全文とblobが一致した。non-forceでmainを更新した後、`2026-10-02T16:43:45.893Z`（2026-10-03 01:43:45.893 JST）にmainから11本文を再取得し、全文・blob一致とheadが実装commitを指すことを確認した。
3. **配置と対象外保持**：非切断の再帰Treeで、元六パスがなく保管六パスが存在することを確認した。6追加・6除去・5更新、計17パス差分。ファイル総数は418のまま、対象外407ファイルのblob・modeはParentと同一。六原本は合計70,601 bytesを保持した。
4. **構造と意味**：五更新本文のFrontmatter YAML、宣言EOF、Code Fence、追加された相対リンク13出現とARC-009見出しを照合した。STR-001の証拠リンクは当時の実装blobと一致。読取専用の独立レビューで対象・歴史証拠・保管境界と五文書差分を点検し、重大な不足は検出されなかった。これは別AIの実運用や旧Boot再現の試験ではない。
5. **実行前提と保持**：Current07のv002核について、同じContextでの確認済み同一本文を再利用し、未確認範囲は統合担当自身が全文読解してR1–R6を照合した。Source準備・STR-003 Remote検証をTarget自身の再構成成功へ借用していない。07三点セット・章・Domain・AGENTS・ARK・Ark28・Dots／Board本文は変更していない。
6. **確認の限界と終了**：本件は保管・案内・証拠・Remote実体の確認まで完了。外部consumerの全不存在、全AIの理解、UI操作、長期の負担軽減や生活効果は未観測。原本中の旧相対リンクは§Fの固定snapshotから辿る。今回の完了を別のアーカイブ、固定Binding移行、次Trialの開始にしない。

この追記は確認済み結果の保存であり、記録自身の自己SHAは埋め込まない。追記を含む最終本文も保存後に直接再取得する。同じHuman依頼による実行後の再接続指針は[2026-10-03 GitHub整理整頓の指針](20261003-cleanup-direction.md)へ接続する。


EOF::AI_PROJECT_CONTROL_CENTER_ARCHIVE::v0.8.0
