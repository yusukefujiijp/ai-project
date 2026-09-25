---
title: "STR-002 — 起動Queryと本体の統合・別Query作成方針の撤回"
version: "v001"
canonical_path: "control-center/changes/STR-002-single-prompt-consolidation.md"
class: "structural_change_record"
status: "six integrations and Plan Mode preparation remote-verified / independent and binding gates pending"
repository: "yusukefujiijp/ai-project"
branch: "main"
source_thread: "Ark27:06"
created: "2026-09-25"
updated: "2026-09-25"
base_commit: "36b8207d61b98562317b58ac65fb01eb7d04cc94"
base_tree: "939741fdbb46ed162a7ecefa245bdf6bb2b8272b"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_002::v001"
---

# STR-002 — 単一Promptへの統合

## 1. 判断と現在の状態

起動Queryと本体の分割について、Humanは「短期視点ではプラス」「長期視点では大きなマイナス」と評価した。起動・対象束縛・Guardの利益は残し、その利益を得るために別ファイルを同期維持する構造を撤回する。通常6組の統合と、Plan Mode・固定参照の移行を分ける。

これは当時の分割を無価値だったと書き換える判断ではない。評価範囲を使用中だけから、休止・再開・変更・別AIへの継承を含む運用へ広げた訂正である。旧版の短期的成功、今回の設計採用、文書保存、独立AIの理解、長期効果は別のEvidenceとする。

本記録は変更の由来・実体・検証・残点を所有する。Current Handoff、Thread Identity、Root司令塔、Human Authorityを置換せず、読むだけで次Taskや試験を開始しない。

## 2. Human Correctionと実行権限

以下はこのArk27:06の会話でHumanが述べた原文の短い抜粋である。長期メモリの転記ではない。

> 長期視点だとAI-PromptのQueryとの分割は大きなマイナスでした！

> 短期視点ではプラスだったのでこの非対称はとても面白いです！

Humanは、それ以前に別Queryの強い推奨とAI Learningの作成条件を「完全にカット」と明示した。Plan-onlyの調査・統合案・Graphによる意味整理を経て、2026-09-25の現在Messageで「Execute GitHub OK」「Human Seal OK」「実行して下さい」と対象計画の実行を承認した。「これで良ければ」はAIの内容点検を伴う継続意思として読み、方針・対象が前案と一致することを確認した。

承認は今回の単一Prompt化、必要な案内・方針修正、変更記録、検証・保存に適用する。無関係なArchive移動、過去Task再開、身体Trial、Token Reset、別研究、他AI起動、Canonical昇格を包括承認したとは扱わない。

## 3. 5W1H

- **Who:** 意味・方向・Correction・実行承認はYusukeJP。調査・統合・点検はArk27:06のAI協働者（Codex実行環境）。実装CommitのGitHub author／committerは実取得値で`yusukefujiijp`。GitHubの名義とAIによる執筆・検証の担当を区別する。
- **When:** 当該実行日は2026-09-25。基点Commitの記録時刻は`2026-09-25T02:07:42Z`（11:07:42 JST）。通常6組の保存は04:17:46 UTC、Remote検証は04:18:10 UTC。候補保存は別の段階として§8へ記録する。
- **Where:** `yusukefujiijp/ai-project`の`main`。通常6組の`prompts/`本体とQuery、Shelf README、AI Learningの方針・CLI metadata、BBPのQuery作成予約、control-centerの案内・本記録。後続準備は`ai-plan-mode/candidates/ai-plan-mode-v005.md`、`ai-plan-mode/tests/single-prompt-v005.md`、Subsystem READMEの候補案内。
- **What:** 本体へ固有機能を統合して別Queryを通常配置から削除する。別Queryの推奨・任意作成条件・将来予約を撤回し、意味と復元経路を残す。
- **Why:** 休止後の再開・修正・Future AIへの継承で、二つのファイルの役割・Version・更新を照合する負担を減らすため。短期の利益を否定せず、長期の運用評価を反映する。
- **How:** Current mainの対象Blob確認 → 本体とQueryの機能対応確認 → 本体内へ集約・重複除去 → 現用参照の修正 → 文書・Guard・変更範囲の点検 → 一貫したCommit → Remote全文・Blob・Tree再取得。別名のLauncherや新しい現役コピーは作らない。

## 4. 統合対応と削除対象

下表の削除対象はすべて`prompts/`配下。復元元は[変更前の固定Snapshot](https://github.com/yusukefujiijp/ai-project/tree/36b8207d61b98562317b58ac65fb01eb7d04cc94/prompts)であり、六つの旧Queryの内容と旧本体をそのまま辿れる。これは履歴・復元用で、旧Pairの現役維持ではない。

| 本体 | 本体へ移した固有機能・統合先 | 削除したQuery / 変更前Blob |
|---|---|---|
| [AI File DAME-DASHI](../../prompts/ai-file-damedashi.md) | §1へ一度だけの対象束縛、実名Report、指示／Data境界。§14を同じ本体を使う入力例へ集約。評価・Human Severity判断・Minimal Patch・Exit-to-Realityは保持 | `ai-file-damedashi_query.md` / `47b165496c337bfee771c5c1f9a78c228cadd6c8` |
| [AI Output Polish](../../prompts/ai-output-polish.md) | §9へInput Mode、複数Inputの役割、Output Type、Target Section、局所Patch、Missing／Ambiguity Gate。§2.6・§5.1で既存Markdownと現行InlineのEvidence受渡しを区別 | `ai-output-polish_query.md` / `d68251cdc9b99dab67bbf848a2f9c0cf843c4491` |
| [AI Metaphor Mode](../../prompts/ai-metaphor-mode.md) | §1へIdentity、Reality、Depth、Lens、Output Focus、Field Test OFF初期値とON時のBudget・STOP。内部Layer／Mapping／再投入を保持 | `ai-metaphor-mode_query.md` / `cf1e97a1b71d19300102f6d8aa7e1942faa51fd0` |
| [Keyword Tree](../../prompts/keyword-tree.md) | §1へKeyword・Reality・Depth・Optional Lens・Output Focus。明示DEEP／GAME_SEARCHのPositive GateとNon-Activation／Reality Guardを両立 | `keyword-tree_query.md` / `88f3ff5248dba0ae00510e5c317f8eb1d65c6425` |
| [AI-to-AI Communication](../../prompts/ai-to-ai-communication.md) | §10へArrivalとSemantic Binding、§8.5へWitnessを含むOutput、§16へ現在入力。Role Mismatch・Human Re-Binding・独立性と過去回答可視性を保持 | `ai-to-ai-communication_query.md` / `6821d801c71e068a8f2c777972c48249a6ad43f3` |
| [Ark-OKF](../../prompts/ark-open-knowledge-format.md) | §12へ起動・Context・回答前点検・Producer／Consumer、§15へ再利用。理論語の実益、Original OKFとの層差、Source・Living Review・言語方針を保持 | `ark-open-knowledge-format_query.md` / `29932c4796a6742c47aa281eee60b392b01897d5` |

削除はGit履歴から回復可能。旧Queryを別フォルダの現役文書へ移して二重管理を継続しない。必要なRollbackは固定Snapshotと変更差分から対象範囲だけ戻し、別作業の更新を広いRevertで消さない。

## 5. 作成方針と参照の扱い

- [Prompts README](../../prompts/README.md) §2を単一Prompt方針へ変更。Query作成条件を「任意」に弱めて残すのではなく撤回した。長さ・入力束縛・起動差は本体改善の理由として扱う。
- [AI Learning README](../../prompts/ai-learning/README.md)のQuery命名Pattern、任意Query項目、条件付き作成、後日作成予約を除去。[CLI](../../prompts/ai-learning/ai-learning-cli.md) metadataの後日再考も撤回。学習Kernel・Human実践の本文は変更しない。
- [BBP](../../prompts/ai-benefit-branch-pruning.md)はQuery作成予約のみを撤回し、Origin・適用条件・Benefit保存・Guard等の本文はByte-identicalに保持する。Versionはv002-candidateのまま、metadataの`policy_revision`とGit Blobでこの限定改訂を区別する。
- AI-to-AI §24の旧Query作成記録、STR-001の旧OKF Pair検証、過去Review・Ark07 Handoff内の成果記録はHistoricalとして保持。変更前の固定Snapshotから当時の内容を再現できる。歴史を現在の起動案内にしない。
- `control-center/PLAN.md`のD05は当時の診断・修復を保持し、§1.3から今回の方針変更へ接続する。STR-001の事実を失敗・未実施へ書き換えない。
- `ai-ark-seed/`など別Domain、古いThread開始文、専用試験Driver、DB等の一般的Query、Input Data、異なる機能のPromptは、名前だけで今回の削除対象にしない。

## 6. 別扱いの移行Gate

### 6.1 Plan Mode — 通常6組へ混ぜない

`prompts/ai-plan-mode.md`と同Queryはv003 Rollback Baseline。現在のActive Routeは`ai-plan-mode/`のv004であり、旧Pairだけを現役と誤認して統合しない。

単一Prompt化の方向と必要な移行準備はHuman承認済み。一方、[現在のSubsystem README](../../ai-plan-mode/README.md) §9–11と[試験契約](../../ai-plan-mode/tests/cold-start-test.md)には、独立したE1 Cold-Start、E5 Baseline比較、挙動同等性、Human Reality Verdict、Fresh Human Cutover Sealがある。作成・保存承認を未観測の検証結果へ変換しない。通常6組をこれらの通過待ちにしない。

現行Pair・旧Baseline・過去試験Driverは、必要Gateを通過するまで互換実体として保持する。これは別Queryの恒久推奨例外ではなく、切替途中の状態。

候補準備では、[v005単一Prompt](../../ai-plan-mode/candidates/ai-plan-mode-v005.md)と[評価者用の比較・試験資料](../../ai-plan-mode/tests/single-prompt-v005.md)を作成した。旧v004の§1–2と§4–19はByte-identical。旧QueryのLocator、Full Read、Identity、Portable Recovery、Arrival、Current Request Bindingを本体§3へ統合し、旧Pair照合を単一Document Identity照合へ置換した。身分・Version・用途Status・EOFの不一致停止は削除しない。

候補は30,694 bytes、旧Runtime＋Queryは37,402 bytes。一File化と内容保持の記述上の事実であり、文字数削減自体を品質・長期効果の証明にしない。候補の起動はこの一Fileだけで完結し、README／Testsを通常起動の必読Promptへしない。

現行v004と旧v003の本文、過去の試験Driver／Fixtureは変更しない。Subsystem READMEには候補の身分と未実施Gateを案内する。E1独立Cold-Start、E5挙動比較、Human Reality Verdict、Fresh Cutover Sealは未実施／未受領。執筆AIの全文読解・文面比較をE1／E5 PASSへ変換しない。候補保存とRemote検証の状態は§8が所有する。

### 6.2 Living Graph / One-Table — 固定参照

現在の`prompts/ai-living-graph-mode.md`と`prompts/ai-one-table-interface.md`には旧方針の将来Query作成条件が残る。Humanの現在方針とShelf §2では撤回済みだが、本文metadataからの物理除去を完了したとはしない。

- Living Graph: `45b0d379990f5807d9eecb3a0b7a6ee2d0b342d1`
- One-Table: `06be18a426b4611a324fea85f1161176c3e130d0`

これらを指定するArk23:14／15の固定Bindingが存在する。初期Ark23:15 Handoffは後続StateでHistoricalと明示されているため、それを現在のArk27 Bootとして再実行しない。一方、State内のReusable Source固定参照まで単なる言及と決めつけず、実際のBinding消費先と移行先を分けて扱う。今回はこの二Blobと旧Triadを変更しない。条件の残存を、今後の新設許可として使わない。

追加確認では、Ark23:15のCurrent入口は`runtime-upgrade-handoff.md`（Blob `9c36ee3ccdaeaceda02b740b7bf27a691f46c497`）。その全文を確認し、Reusable Runtimeは再接続Bootの追加必読ではなく、選択利用時のFull Read対象であることを確認した。READMEの§7・§12、Core INSTRUCTIONSの§4・§10、およびCurrent Stateの固定Source記録を区別した。これはArk23へのBoot、移行実行、全旧Handoffの再検証ではない。

固定Sourceの切替は、現在の入口・歴史再現・選択利用時のBinding消費を具体化してから行う。文字だけを消して旧SHA契約を黙って壊さず、古いHandoffの存在だけを無期限の変更禁止にも使わない。現在方針の再承認は不要だが、他ThreadのState／必要な入口移行まで含む影響範囲を明示する作業が残る。

## 7. 文書点検とEvidence境界

変更前の30読取対象は取得したGit Blobと一致。通常6組のQuery参照検索は結果切れなしで取得し、現用案内とHistorical言及を区別した。検索は外部利用者が存在しない証明ではない。

通常6組の実装点検では、次を機械照合とAI意味読解で確認した。

1. DAME-DASHIの評価・Severity・Human Seal・Exit Kernel、MetaphorのLayer 1–4、Keyword Treeの戦略層、AI-to-AIのOrigin・Convergence・Witness Guard、Ark-OKFの定義・Source境界を保持。
2. 各Query固有の入力・不在／曖昧さ停止・局所条件・出力が対応する本体へ到達する。
3. 現用の六本体に別Query依存がなく、方針資料に作成条件・予約がない。
4. Root・Teshuvah・Human Foreground One・Correction／STOP／Sealと適用Guardを保持。Human I/Oの簡潔化をAI品質低下にしない。
5. 必要なEOF、Code Fence、Path、Metadata、削除対象と対象外保持を確認する。

これは文書整合と執筆AIによる点検であり、独立した他AIのCold-Start、HumanのUI操作、長期の保守負担軽減を実証するものではない。旧版のField PASSを新Versionの実測へ移さない。通常Unknownの全解消を、今回の通常6組の保存条件に追加しない。

## 8. 保存・Remote検証

### 8.1 通常6組・方針・記録

- 実装Commit：[254f5294ddc327fbc0f5f28b73cc5d72a77cc486](https://github.com/yusukefujiijp/ai-project/commit/254f5294ddc327fbc0f5f28b73cc5d72a77cc486)。Parentは冒頭のbase_commit、Treeは`9efac854b90620034dbb7cca26450666998da71d`。
- 保存時刻：`2026-09-25T04:17:46Z`（13:17:46 JST）。Author／Committerはともに`yusukefujiijp`。
- Remote検証時刻：`2026-09-25T04:18:10Z`（13:18:10 JST）。変更した13 FileをCommit指定で全文再取得し、予定本文とBlob SHAが一致。mainの参照先も確認した。
- 12既存Fileの改訂＋本記録1 Fileの追加＋旧Query6 Fileの削除。Treeは329→324 File。対象外311 FileのBlobは基点と同一。六つの削除PathはTreeに存在しないことを確認した。
- 文書整合の13点検群を通過。Kernelの範囲一致、入力・Failure／Guard、方針条件除去、別Query参照、Fence／EOFを確認。独立実行試験ではない。

Tool成功応答だけではなく、Commit、Tree、main、全文、Blobを再取得して確認した。本記録自身の自己SHAは本文へ埋めない。

### 8.2 Plan Mode候補準備

- 準備Commit：[3ceb77d69b2b1ae261f379139c994710ef14e573](https://github.com/yusukefujiijp/ai-project/commit/3ceb77d69b2b1ae261f379139c994710ef14e573)。Parentは通常6組の実装Commit。Treeは`e6e99f9858c1d5e97f5445e1d1a75b196484f1a0`。
- 保存時刻：`2026-09-25T04:32:50Z`（13:32:50 JST）。Author／Committerはともに`yusukefujiijp`。
- Remote検証時刻：`2026-09-25T04:33:08Z`（13:33:08 JST）。下記三Fileと本記録の計四FileをCommit指定で全文再取得し、予定本文・Blob SHAと一致。mainの参照先も確認した。
  - 候補：`ai-plan-mode/candidates/ai-plan-mode-v005.md` / `6685c44a33ae7826fbd1437efacdb7ed043e327b`
  - 評価資料：`ai-plan-mode/tests/single-prompt-v005.md` / `af563d1c1adeb68672380ea100a2589a0fd08d79`
  - Subsystem案内：`ai-plan-mode/README.md` / `1e6d76b7b347469810962b99ba603cfdda9ed0c2`
- 2 File追加、READMEと本記録の2 File改訂。削除なし。Treeは324→326 File、対象外322 FileのBlobは直前Commitと同一。v004／v003 Pair、旧Test、固定Graph／One-Table、Current Ark27 Triad、AGENTSは保持。
- 通常6組の再点検を含む18の文書整合点検群を通過。候補のCore一致、単一Identity／EOF、Failure、validation-only、TestのNOT RUN表示、対象外非改訂を確認した。

これは候補準備とRemote保存の完了。独立E1／E5、Human Verdict、切替・退役・Canonical化は完了していない。本節の追記Commitは検証Receiptを残す記録更新で、Prompt本文の再改訂や試験実施ではない。

## 9. 次の接続と再開条件

通常6組とPlan Mode候補・比較・試験準備は保存・Remote確認済み。独立Cold-Startを必要とするGateでHuman Reviewへ戻る。次のHuman-facing Oneは、準備済み候補一FileによるE1 Cold-Startの最初の返答を観測すること。到達／全読解／現在依頼の束縛／Plan-only停止を確かめ、Failureまたは最初の返答後にHuman Reviewへ戻す。E1一件だけでE5やCutoverが済んだことにはしない。

固定Binding移行は別の未完了Branchとして保持し、上記試験との同時Human Taskに増やさない。旧Handoffの再Boot、次Trial、別DomainのQuery全削除を自動開始しない。

Human Correction、STOP、必須Source欠落、実質的なScope／権限拡張、Remote競合、固定Binding不一致は影響する操作を止める。入力や長期効果の通常Unknownは、そのまま表示する。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_002::v001
