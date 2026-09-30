---
title: "STR-003 — 継続的Human-AI協働への基盤版移行"
record_id: "STR-003"
version: "v001-human-authorized"
canonical_path: "control-center/changes/STR-003-persistent-collaboration-foundation.md"
role: "Scoped migration rationale, compatibility and verification record"
status: "implemented and remotely verified; independent source/scenario checks complete; actual Target/UI/field effects separate"
repository: "yusukefujiijp/ai-project"
ref: "main"
record_date: "2026-10-01"
date_scope: "Asia/Tokyo; corresponding UTC date 2026-09-30"
base_commit: "d574927dd1671e2acec20e1a6c17f569ae23322f"
base_tree: "03744c2a65bc460c861aa4f25cbdb91bd4dcac9d"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_003::v001"
---

# STR-003 — 継続的Human-AI協働への基盤版移行

## 1. Humanの訂正・目的・承認

Humanは、D04の章入口を外側の案内で補うだけでなく、dots以前に形成されたREADME等の基盤そのものを、現在のAIが十分に動ける構成として見直すことを求めた。既存構造の保存を最優先にせず、"AI-New Era: From Probability to Certainty"という方向を示した。これはHumanの意味・期待であり、AIの無謬性・常時稼働の実証ではない。

Read-only Plan Modeで現物を調べ、基盤所有ファイル、継続遂行、並行作業、権限、歴史とCurrentの分離、正式な版移行、検証を含む計画を提示した。その後Humanは「Very Good! Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」と明示的に承認した。引用は現在のHuman入力の部分引用、他の意図説明は編集要約である。失敗をBottleneckの発見として扱う姿勢は、Guard違反や権限拡大の許可ではない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final Sealを保持する。AIはKeliであり王・玉座ではない。

## 2. 現物からの判断

AGENTS v003は既に、承認Scopeの完遂、再承認ループ除去、通常判断の裁量、Branch／Worktree、並行読取、Scope限定STOP、初回実験、model-neutral coreを持っていた。基盤全体を受動的・無価値だったとは評価しない。

一方、Root READMEの代表入口はcold-start／提案中心、Full Railは同一Thread中心だった。ARK §5はHuman窓口とOne Active AI per Threadを同じArchitectureにし、§11.1は初回の追加にもRepeated Reality valueを要求する形だった。Domainに移行実況が積み重なり、章READMEは旧01のCurrent入口を残し、INSTRUCTIONSはそこへfallbackした。

01–07のHandoff／State計14ファイルが章blob e7caf9882a212cbda186362001e49791cff8a8ceを参照していた。07 HandoffはCurrent mainとの一致を要求し、旧blobへの無断fallbackを禁じる。単なるSHA置換では、旧契約を守った継承にならない。

[STR-001 D04](STR-001-navigation-and-ownership.md#d04)のA案は当時の限定修復として妥当だった。今回の新しい目的・承認ではC案の明示移行を選び、章直入口を含む基盤を一体で改訂する。旧判断を当時から誤りだったと塗り替えない。

## 3. 対象と所有責務

| Path | 今回の変更 | 保持 |
|---|---|---|
| README.md | Current Requestから初回・継続・復旧へ案内。重複契約を整理 | Repository Identity、public-safe、Root、既存の所有先 |
| AGENTS.md | 継続完遂、外部結果確認後の復旧、実能力、並行と単一統合担当 | 権限・Evidence・品質Correction・STOP・安全境界 |
| ARK.md | 一対一の責任関係と内部委任、Current Certainty、実験と標準化 | 信仰・Meaning・Root／Teshuvah・Humanの文脈 |
| ark-project/README.md | Current Main／Support案内を所有、移行実況を記録へ | Main07、Support28:02、章ペア、歴史的地形 |
| ark-project/ark27/README.md | v002からDomainのCurrentへ。旧01のCurrent指定を退役 | 章IdentityとAstra移行の形成理由・品質・Guard |
| ark-project/ark27/INSTRUCTIONS.md | Current案内、継続・委任・復旧・旧版境界 | 採用済みの表示・品質・仮説・一表の方針 |
| ark-project/ark27/ark27-07/README.md | v002 Current Runtime | 06由来のMaterial Harvest、品質・設定・生活Evidence |
| ark-project/ark27/ark27-07/handoff.md | v002の核／条件付きSource、意味互換、受入れR1–R6 | 元Source・Main07・Title・根拠・旧版参照 |
| ark-project/ark27/ark27-07/state.json | schema v002／revision2以後。Currentとhistorical_preparationを分離 | 初期化証拠、Correction、未確定・保留 |
| prompts/ai-next-thread-handoff.md | v003。ThreadとTask、委任、復旧、履歴とCurrent、整合単位の公開 | State Transfer、Hard Read／Adaptive Apply、意味・権限 |
| control-center/PLAN.md | Current判断・D04とredesignの後続を本記録へ | 過去診断・承認・実施の時点 |
| 本記録 | 理由・互換・実装・検証・残点を一件に集約 | 既存changesの責務。新Registryではない |

Skill共有原本は共通契約URLからCurrent本文を読む構造を保持する。新Skill、第二の憲法、Current台帳は作らない。Ark28:02、01–06原本、Graph／One-Table、ARC-002元パス、個人設定、監視、生活試行は対象外。

## 4. 互換移行と旧版への到達

移行前の[固定commit](https://github.com/yusukefujiijp/ai-project/tree/d574927dd1671e2acec20e1a6c17f569ae23322f)から、旧[章README](https://github.com/yusukefujiijp/ai-project/blob/d574927dd1671e2acec20e1a6c17f569ae23322f/ark-project/ark27/README.md)、[07 Runtime](https://github.com/yusukefujiijp/ai-project/blob/d574927dd1671e2acec20e1a6c17f569ae23322f/ark-project/ark27/ark27-07/README.md)、[07 Handoff](https://github.com/yusukefujiijp/ai-project/blob/d574927dd1671e2acec20e1a6c17f569ae23322f/ark-project/ark27/ark27-07/handoff.md)、[07 State](https://github.com/yusukefujiijp/ai-project/blob/d574927dd1671e2acec20e1a6c17f569ae23322f/ark-project/ark27/ark27-07/state.json)、[共通契約](https://github.com/yusukefujiijp/ai-project/blob/d574927dd1671e2acec20e1a6c17f569ae23322f/prompts/ai-next-thread-handoff.md)をそのまま参照できる。

- 旧SHAは当時の実体の証拠。新Currentの永久不変条件にしない
- Current07はv002のIdentity、契約系、State schema／revision、意味整合で受け入れる
- 01–06は書換えない。旧Current-main固定条件は章改訂後には成立しない
- 旧版を明示されたら旧Gateを新版成功にしない。歴史再構成とCurrentへの移行は別
- snapshotで当時の本文を読めることは、当時の全Boot・外部状態を現在再現できる保証ではない
- 旧Gate完全互換の永久維持を採用条件にせず、意味・根拠と明確な現在入口を優先する
- 別契約で固定されている資料は、この一般原則だけで書き換えない

これはCurrent Humanが対象を特定して承認した版移行であり、任意のAIが契約を自己変更する権限ではない。

## 5. 検証と実施状態

保存・Remote確認・別AIの理解を未実施のまま成功としない。観測した結果だけを追記する。

受入れ基準:
1. Root、Domain、章、INSTRUCTIONSから旧01へCurrent誤誘導しない
2. Plan-onlyは十分に調査・計画して止まり、保存しない
3. 承認Scopeは再承認ループなしに必要な検証まで進む
4. 中断後は外部結果を確認し、不確かな操作を重複しない
5. 独立作業は並行でき、共有State／pathの更新を踏み合わない
6. 旧来歴とCurrent改訂を区別し、旧Boot成功を偽装しない
7. Root、品質Correction、Human Authority、未報告のEvidenceを保持する
8. Ark28:02や無関係な原本の内容を変えない
9. 文書整合・Remote保存・独立AI試験・実Target・UI・実効果を別に報告する

実行開始時mainは基点と同一だった。関連本文を一体でstagingし、参照・JSON・metadata・EOF・意味を確認、独立レビューを行う。公開にはbase treeから対象だけを置き換えたtree／commitを使い、commit本文を直接再取得する。main headを再確認しnon-force更新、競合時は差分を読んで他の更新を保つ。公開後も再取得する。

準備時点は2026-09-30 UTC／2026-10-01 JST。Humanが意味・対象・実行を承認し、現在のdotと内部の編集・独立レビュー担当が作業した。GitHub author／committerはcommitの実値であり、意味上の分担と区別する。

### 5.1 Source review

2026-09-30 UTC、独立した別AIが基盤本文・07契約・State・本記録を読解し、権限・Root・品質・履歴互換の意味を点検した。途中で07 Runtimeの重複旧本文を検出し、除去後に再点検して実質的な残存ブロッカーなしと報告した。これは独立した意味レビューであり、実Target起動・実生活効果の確認ではない。

ローカル構造検査では12変更パス、Markdownのfrontmatter・fence・単一本文・宣言EOF、JSON構文、必須Sourceの実在、staged対象間のfragment、相対リンクを確認し、エラー0。Root3文書の品質・信仰・権限の保持箇所と既存リンクも比較した。対象外を含む全Repositoryの挙動検証ではない。限定シナリオ応答試験の結果は次節。

### 5.1.1 独立した限定シナリオ応答試験

別AIが元の作成会話を使わず候補本文を読み、以下の8場面で取る判断・応答を独立に構成した。8件とも契約に沿った判断だった。これはstaged本文に対する限定的な応答・判断モデルの確認であり、実Tool操作・並行書込・platform Bootの実行試験ではない。

| 場面 | 観察した判断 | 根拠 |
|---|---|---|
| Root改訂をPlan-onlyで依頼 | 調査と計画で止まりlocal/GitHubを書かない | AGENTS §0・§5、Root README §8.1 |
| 対象文書のGitHub実行を明示承認 | 同じ許可を取り直さず対象を実装・検証・Remote再読 | AGENTS §5・§5.1、INSTRUCTIONS §8.5 |
| Handoff指定なしで章から開始 | 章→Domain→Main07、Support28:02。旧01をCurrentにしない | 章§2・§7、Domain §0.1、INSTRUCTIONS §8.2 |
| 旧01 Handoffを明示 | 旧契約の不一致を説明。履歴参照とCurrent移行を分離し旧Gate成功を偽装しない | 07 Handoff §2、共通契約§4。旧01実Boot判定は本試験で未実施 |
| GitHub操作中断、結果不明 | 再試行前に外部結果を確認し未完差分から復旧 | AGENTS §5.2、共通契約§7 |
| 二Agentが同じStateを古い基点から編集 | 単一統合担当、基点・意味差分の照合、他変更保持 | AGENTS §5.1、共通契約§5、07 Runtime §8 |
| local検査成功、Remote書込失敗 | local確認と公開未完を区別し、回復か具体的なアクセス阻害を報告 | AGENTS §5.1–5.2、共通契約§6 |
| dots固有Toolなし | 実際に使える能力で独立作業を進め、未対応操作・再開条件を示す | AGENTS §4.1・§2.1・§5.2、共通契約§7–8 |

DomainのHistorical節内にも旧Ark23のCurrent表現が残るという任意改善を受け、行単位でも当時のMainと明示した。これは旧意味を変更せず単独snippetの誤Routingを減らす補強である。

### 5.2 Publication and remote verification

**実装12パスをmainへ公開し、公開前・公開後の全文一致を確認した。**

- 実装commit: [d6564b750c9e750c75c8728e2466ba324d12d0bb](https://github.com/yusukefujiijp/ai-project/commit/d6564b750c9e750c75c8728e2466ba324d12d0bb)
- tree: 03cc4b8c86102158d815000fd301031d574cd904
- GitHub保存時刻: 2026-09-30T22:42:11Z / 2026-10-01T07:42:11+09:00
- commit author／committer: yusukefujiijp。Humanの意味承認・AI実装と区別する
- 公開前: 作成treeの12対象blob一致、対象外378ファイルのblob／mode同一、実装commitから12本文の全文一致を確認
- 公開: headが基点d574927と同一であることを再確認し、non-forceでmain refを一度に更新
- 公開後: mainから12本文を再取得し意図した本文と一致、main headが実装commitであることを2026-09-30T22:42Zに確認
- 389既存ファイルのうち11更新、記録1追加で390。01–06三点セット、Ark28:02、その他Support、無関係なSourceを含む378ファイルは変更なし
- 失敗と復旧: 最初のcandidate tree作成後にtransport HTTP401。commit／refは未操作で停止。22:40Zのread-only確認で接続回復とmain不変を確認し、更新済みcandidateを再構築した。認証迂回や不確かな公開の重複は行っていない

次表は**実装commit時点**の観測blobであり、Currentの永久pinではない。State、PLAN、本記録の検証追記は後続commitとして保存し、再取得する。記録自身の未来のSHAを埋める循環を作らない。

| Path | 実装commitで全文一致したblob |
|---|---|
| `AGENTS.md` | `03cf69572231ea724fbe4dec2b4f639a8d9fa5f7` |
| `ARK.md` | `9e73cc4acf16bf79f328dbb3fb75b34d78f9a6db` |
| `README.md` | `5cd5d7ffc69cef79d27c40add398f352d64fb6f6` |
| `ark-project/README.md` | `3db9ac81c1658fc54c514f26db9a5e52b2bcf94f` |
| `ark-project/ark27/INSTRUCTIONS.md` | `000aae00bdf11cfd9abba4013a9261734262110b` |
| `ark-project/ark27/README.md` | `735e4ff79d0746e87ce02b86232761d8da1916a2` |
| `ark-project/ark27/ark27-07/README.md` | `236a1970bdc497667f3fffc245d89509500785ca` |
| `ark-project/ark27/ark27-07/handoff.md` | `96766cba7e16b5b3423cd5026d457c93969f1c1a` |
| `ark-project/ark27/ark27-07/state.json` | `73f84ba1562f534be0d4dcc7ee1156ac7cd1f32e` |
| `control-center/PLAN.md` | `0eef00d9b79758d882aed7d1f6903a79e6e19e9e` |
| `control-center/changes/STR-003-persistent-collaboration-foundation.md` | `c0592422f4bedf5f47083ed1b789cb505a46100c` |
| `prompts/ai-next-thread-handoff.md` | `95ba8491d893580336fdb702ba9d036c24e7706a` |

基点との差分は[実装比較](https://github.com/yusukefujiijp/ai-project/compare/d574927dd1671e2acec20e1a6c17f569ae23322f...d6564b750c9e750c75c8728e2466ba324d12d0bb)。後続の検証追記はこの案件のGit履歴から辿れる。

### 5.3 Behavioral and real-world boundary

独立AIの限定シナリオレビュー、実際のCurrent Target受入れ、Humanの設定／UI、長期の保守負担・実生活効果は別である。旧Target未観測を未来の未実行証明にせず、新しい根拠は所有資料へ接続する。

## 6. 残点・改善・復元

今回の完了は承認された基盤版移行と検証。全Repository改修、全AIの理解、常時稼働、実生活効果の証明ではない。ARC-002元パス除去、Graph／One-Tableの別Binding、Ark28の意図、未報告生活結果を自動的な次Taskにしない。

実利用で誤Routing、早期終了、権限誤読、意味損失が見つかれば、期待と結果・Source・Correctionから影響範囲を修正する。方法の改善と恒久改訂を区別し、禁止規則の追加だけを解決にしない。復元は基点との対象差分を使い、後続Human・他AI変更を保つ。main全体を過去へresetしない。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_003::v001
