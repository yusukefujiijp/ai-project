---
title: "STR-013 — GitHubの計画・アーカイブ案件を専門領域へ置く"
version: "v001-human-authorized"
canonical_path: "control-center/changes/STR-013-github-plan-and-archive-relocation.md"
status: "scoped implementation published and remotely verified; independent reader and field effects unobserved"
created: "2026-10-06"
updated: "2026-10-06"
latest_followup_status: "house rename prepared; remote verification pending"
owner: "Ark27:08"
repository: "yusukefujiijp/ai-project"
branch: "main"
research_base_commit: "7516f4c029b43df99633fbe1b38d4469f79a5a36"
expected_eof: "EOF::STR_013_GITHUB_PLAN_ARCHIVE_RELOCATION::v001"
---

# STR-013 — GitHubの計画・アーカイブ案件を専門領域へ置く

## 1. Humanの意図と、今回変わった判断

YusukeJPは、共通親`control-center/`とGitHub専門入口を分けた[STR-012](STR-012-control-center-domain-entries.md)の成果を評価した後、自身で`home/README.md`を改行のみで作った。これは家の中の整理へ横展開する方向を示すSeedであり、家の整理計画や生活上の成果を完成した報告ではない。

同じ入力で「完全にあなた(AI)が自由にして良いフォルダ・ファイル構図構成」「内容もそれに基づいて変更修正改善してOK！」と述べ、PLAN・ARCHIVEを`control-center/github/`へ入れる案とGraph Modeによる整理を求めた。このCurrent入力を、二原本の配置と内容・必要な案内の改善を行う権限として受け取った。以前の広いGoの転用や、未承認の別作業の自己承認ではない。上記は確認できる短い原文で、それ以外の説明は編集要約。元会話の検証可能なURLは未提示であり、作らない。

Humanの意図は、共通の整理目的と知恵への接続を保ちながら、GitHubと家の整理を対象ごとの兄弟領域として育てること。GitHubに保存する家の記録も、整理対象は家である。記録媒体が同じことと、目的・現実・制約が同じことを混同しない。AIはScope内の設計・通常判断・実装・検証を引き受け、HumanはMeaning・Correction・STOP・Final Sealを保持する。

前段では、既存住所を保持した入口分離を完了した。今回はHumanが次の領域のSeedを作り、専門側への物理配置を明示したため、PLAN・ARCHIVEを親から専門領域へ置く判断に進んだ。前段の完了を未完了へ戻す変更ではない。

## 2. 関係から選んだ構成

共通親にGitHubの二台帳の本文を残すと、家の整理を始める読み手が、それらを全領域共通の計画や廃棄手順と受け取る余地がある。これは構造からのAI推論であり、実際にその誤読が発生したという観測ではない。専門領域へ本文を置くことで、目的・所有先・配置を合わせる。

一方、旧住所はHandoff、Skill、経験、履歴等から参照されている。全参照元の契約変更を一度に行う利益は今回のScopeでは示されていない。本文を一元移設し、旧住所に案内だけを残す構成を採用した。独立して更新される計画・案件のコピーは作らない。旧住所は自動転送機能ではなく、明示的にリンクを辿るための文書である。

| Node | Edge | 担当する意味 |
|---|---|---|
| [共通入口](../README.md) | 整理対象 → 適切な専門領域 | 共通目的・分類・横展開。各領域の進捗は持たない |
| [GitHub入口](../github/README.md) | GitHubの依頼 → 原本 | このRepository全体の構造整理。家の整理を包含しない |
| [PLAN](../github/PLAN.md) | 現在の問い → 判断・証拠・残点 | GitHub計画の単一原本 |
| [ARCHIVE](../github/ARCHIVE.md) | 退役案件 → 理由・承認・実施・復元 | GitHub案件の単一原本。保管実体は既存__archives |
| [旧PLAN](../PLAN.md)・[旧ARCHIVE](../ARCHIVE.md) | 既存参照 → 新原本・既存節 | 案内だけ。本文読解・旧Bindingの代替ではない |
| [houseのSeed（当初名home）](../house/README.md) | Humanの横展開意図 → 今後の具体化 | Human作成の改行一つを保持。今回、家の作業は開始しない |
| 既存changes・整理指針 | 専門入口 → 形成理由・時点付き根拠 | 現行Handoffの必須Sourceを含む住所を保持。本文を二重化しない |

## 3. 確認したRealityと調査境界

基点commitは`7516f4c029b43df99633fbe1b38d4469f79a5a36`。前回の検証済みmain `ab5255fd616a879ef94a84ab92a4d71607cdaa4c`との差は、Human作成の`control-center/home/README.md`一つ。内容は改行一つ・1 byte、blob `8b137891791fe96927ad78e64b0aad7bded08bdc`。実体は`home`という一ファイルではなく、`home/`内のREADMEである。

移設前PLANはv0.13.0・blob `3644a8743438de98dd96550e1c7c381c1c38c34a`、ARCHIVEはv0.9.0・blob `4dc9a6a0e6f07893c49e9b0ce83767177bf3083f`。旧版の本文は[PLAN固定版](https://github.com/yusukefujiijp/ai-project/blob/7516f4c029b43df99633fbe1b38d4469f79a5a36/control-center/PLAN.md)と[ARCHIVE固定版](https://github.com/yusukefujiijp/ai-project/blob/7516f4c029b43df99633fbe1b38d4469f79a5a36/control-center/ARCHIVE.md)に残る。

既定branchのコード検索で旧PLANパスは21ファイル、旧ARCHIVEパスは43ファイル、合計48の異なる参照元を得た。検索URLは直前commitを指していたため、48本文を今回の固定基点から取得しTreeのblobと照合して参照を抽出した。追加のファイル名検索では52の異なる参照元まで確認し、固定基点の本文から相対リンクも含めて抽出した。検索結果の存在と全文意味読解を同一視しない。今回、台帳の全案件を再監査・再Bootしたとは扱わず、編集する入口・現在欄・移設契約を読み、保存された案件本文は相対リンク以外の同一性を検査する。

Currentへの案内、当時の配置を記した文章、固定commitの証拠は別のEdgeとして扱った。固定URLは変更せず、移設する本文の相対リンクは同じ対象へ到達するよう深さを直す。新原本どうしのリンクは同じ専門領域内で接続する。コード検索で列挙されない参照・外部consumer・全Git履歴の完全網羅は未確認。

## 4. 実装範囲と意味の保持

- 新しい単一原本：`control-center/github/PLAN.md`、`control-center/github/ARCHIVE.md`。
- 旧二住所：本文を持たない移設案内へ変更。既存のARC-001–010と05補足接続等の節から、新原本の対応節へ進める。
- 案内整合：`control-center/README.md`、`control-center/github/README.md`、Root `README.md`、`__archives/README.md`。
- 理由・承認・結果の所有記録：本STR-013。

PLANのcurrentは今回のHuman Correctionと対象へ更新し、STR-012を先行成果として接続する。診断履歴・D番号・E番号・05補足接続の契約本文は、相対リンクの到達先を保つ調整以外そのまま保持する。ARCHIVEの案件本文・状態・理由・承認・固定証拠も同様に保持する。

ARC-007・009・010等の完了、ARC-002の部分完了と元パス除去保留、Graph／One-Tableの別Branch、旧Plan v005試験の目的変更終了、整理指針当時のJSONL候補と後続STR-009採用を混同しない。旧版を指定するHandoff等は、その版・SHA・EOFとFailure Contractに従う。案内の読了や、新住所の新版の存在を旧契約の成功へ変換しない。

`home/README.md`は内容もblobも保持する。既存`changes/`・整理指針・Ark Domain／章／Thread／Handoff／State・AGENTS／ARK・Skill・Prompt本文・Board・Actorログ・保存原本を変更しない。homeの実装、生活Task、Pet、Reset、新Skill、固定Binding移行は開始しない。Workをdot-0000と扱わず、初穂本人のActorログへ書かない。ChatGPT長期メモリをSourceにもGitHubへの輸出対象にもしない。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。AI・Skill・Graph・文書はKeliである。簡潔なHuman入力を必要な検討・説明の削減へ変換しない。

## 5. 検証と公開の記録

実装前の確認では、9対象のmetadata・canonical_path・必要なExact EOFを照合し、350の相対Markdown参照と52参照元からの旧二住所への124リンクを確認した。該当する節への旧住所の案内と新原本の到達先を確認し、欠落は検出されなかった。

PLANのdiagnosis-history以下、ARCHIVEの§1以下を全長で比較し、相対リンクの移設に伴う調整以外の本文保持を確認した。固定commitの証拠URLは変更していない。読み手が共通親・GitHub原本・homeのSeed・旧住所の案内を区別できるかを執筆上の自己点検として確認した。別AIによる独立読解の実証とはしない。

実装commit [`000b44b2e9710f7a0825fcf5892b7f445e1bef74`](https://github.com/yusukefujiijp/ai-project/commit/000b44b2e9710f7a0825fcf5892b7f445e1bef74)、Tree `2dd63d1512751be21934b02ecb5e954444be74f7` をmainへ公開した。親commitは調査基点と同じ `7516f4c029b43df99633fbe1b38d4469f79a5a36`。公開直前にmainの一致を確認し、expected_shaを指定した非force更新を行った。

2026-10-06T10:20:57Z（JST 19:20:57）までに、9対象をmainから全文再取得し、用意した内容・Git blob SHA・必要なEOFとの一致を確認した。Git commitが指すTreeも照合した。既存473 blobのうち、変更対象6以外の467 blobとmodeを保持し、追加3を含む公開Treeは476 blob。Human作成のhomeはmainから改めて読み、改行一つ・元blob一致を確認した。

これは文書配置・内容・参照・保存の確認である。独立した別AIによる理解、実際の家の整理、長期の探索負担の減少、全Runtimeの利用効果は今回観測していない。検証結果は本記録への後続追記として残し、この記録自体も公開後にRemote再取得して確認する。

## 6. 復元・再検討

復元が必要なら上記基点の旧二原本と、この変更の差分から判断する。単純に古いTree全体へ巻き戻してHumanや他AIの並行変更を消さない。新住所で後続編集があれば先に照合する。旧住所の案内を外す場合も、実際の参照元・契約・残す価値を確認する別判断であり、自動的な次Taskにはしない。

今回の成功は、二原本の配置・必要な案内・意味保持・Remote確認という範囲で評価する。家の整理の効果、他AIの理解、長期の探索負担の減少は、実際に使った時の観測で判断する。

## house-name

### 2026-10-06の後続訂正：homeからhouseへ

Humanは「homeにはhomepage的な意味合いもある」と指摘し、houseの方が良ければ修正するよう依頼した。これは名称と必要な案内の変更権限であり、家の整理計画・実作業の開始依頼ではない。今回の対象は物理的な家・居室などの生活空間なので、領域名を`house/`へ変更する判断を採用した。homeという英語が誤りという意味ではなく、このRepositoryの入口・分野名として対象を明確にする選択である。

調査基点は`fd6b498be94276b993cc661e79c474a0fe3f20a0`。旧`control-center/home/README.md`は改行一つ、blob `8b137891791fe96927ad78e64b0aad7bded08bdc`のままで、house配下はまだ存在しなかった。この同一blobを`control-center/house/README.md`へ移し、旧配置は残さない。共通入口、GitHub入口、PLAN現在欄、本記録の現在へのリンクを整合する。上の§1–6にあるhome作成・保持・検証は当時の記録として残す。

この訂正はSTR-013の領域分離に対する限定的な後続変更として本記録に集約する。新しい案件台帳、第二の家の入口、生活計画は作らない。PLANの診断履歴、Handoff・Skill・Root契約、他Threadやartifacts等の並行成果は保持する。

移動先内容・旧配置の消失・参照・対象外保持を照合し、公開後のRemote再取得結果を追記する。

EOF::STR_013_GITHUB_PLAN_ARCHIVE_RELOCATION::v001
