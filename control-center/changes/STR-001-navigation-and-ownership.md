---
title: "STR-001 — 現役資料の案内・所有先・相互参照の整合"
record_id: "STR-001"
version: "v001.1"
canonical_path: "control-center/changes/STR-001-navigation-and-ownership.md"
role: "Scoped structural change history / 5W1H / evidence and remaining decisions"
status: "six repair groups and D04 design saved / remote full-content verified / fixed-chapter direct-entry constraint retained"
repository: "yusukefujiijp/ai-project"
ref: "main"
record_date_utc: "2026-09-22"
main_owner: "Ark27:06"
human_authority: "YusukeJP — current explicit approval of the seven proposals and GitHub execution with a 5W1H record"
implementation_actor: "Ark27:06 execution AI in the current conversation"
base_commit: "945f789a845350455a8b56162a1fc8cd58576eff"
base_tree: "eb8961fbde7f175de4192247804661d475918747"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_001::v001.1"
---

# STR-001 — 現役資料の案内・所有先・相互参照の整合

アーカイブ後に残す資料について、入口・自己パス・内容の所有先を整える案件。六候補の局所修正とD04の分離設計を扱う。原本を多数移動する案件や、旧Handoffの固定条件を更新する案件ではない。

本書は変更の理由と確認範囲を所有する。全体の優先順位は[PLAN](../PLAN.md)、司令塔の目的は[README](../README.md)、個別アーカイブは[ARCHIVE](../ARCHIVE.md)が所有する。この記録を現在のHandoff・Runtime・全作業の必須Bootへ昇格させない。

## authority-and-5w1h

Humanは、前回答の七候補について「上記AI回答を実行してOK！」と実行を承認し、「いつ誰がどこを直したというような5W1H的な記録」を、他AI・Future AIの理解のため残すよう要求した。ここに引用した二箇所はCurrent Human入力の部分引用。その他の意図説明はAIによる編集要約であり、逐語議事録ではない。

| Node | Edge | 今回の5W1H |
|---|---|---|
| When | 調査・保存・確認の時点 | 記録日はUTC 2026-09-22。対応するJST日付は保存時刻により翌日になり得る。正確な実装・確認時刻は下のverificationとGit履歴。Human発言の未提示時刻は作らない |
| Who | Humanの意思決定→AI実装→GitHub記録 | YusukeJPが目的・対象・保存・記録を承認。Ark27:06の実行AIが読取・設計・編集・検証を担当。GitHub commitのauthor/committerと、この意味上の分担は別に辿れるようにする |
| Where | Repository→対象文書 | `yusukefujiijp/ai-project` / `main`。変更場所は下のfile-manifest。control-centerの対象はrepo全体であり、ark-project配下だけではない |
| What | 七候補→六件の局所修正＋D04設計 | D01・D02・D05・E01・D07・D08を修正。D08は前回答6位のMode案へ今回付けた診断ID。D04は分離案比較と今回の適用方針を記録 |
| Why | Human Correction→継承可能な構成 | Humanは長年のフォルダ・ファイル構成の悩みの改善と、複数AIによる部分改訂の整合を求めた。作者が違っても、正しい住所・役割・変更の理由を辿れる状態を目指す |
| How | Current Source→局所編集→差分確認→保存→Remote再取得 | 現行mainと対象本文・固定参照を調べ、現在案内だけを意味に沿って整合。関連ファイルを一つのtree/commitで保存し、対象本文・blob・配置・対象外保持を再取得して確認する |

Humanの「予期せぬ成功」「最高AIによる統一」という評価・期待は、この改善を続ける動機として保持する。改善効果や他AIの理解をモデルの名称・期待値だけで認定しない。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・司令塔・記録はKeliであり、HumanのCorrection・STOP・Final Sealと適用Guardを保持する。

## source-and-boundary

- 作業前main：[945f789a845350455a8b56162a1fc8cd58576eff](https://github.com/yusukefujiijp/ai-project/commit/945f789a845350455a8b56162a1fc8cd58576eff)。正確なtreeは `eb8961fbde7f175de4192247804661d475918747`、317ファイル。前のランキングと同じmainであることを再確認した。
- 適用AGENTSはrepo rootの一つ。確認済みArk27:06 Bootと共通移行契約の読解を保持し、本件を新しい移行・Target起動へ変換していない。
- 直接のSourceはCurrent Human入力、対象のGitHub本文、配置Tree、固定章参照。ChatGPT長期メモリは転記・同期・輸出していない。
- Confirmedは確認した記載・配置・保存内容、Candidateは原因と将来効果の解釈、Unknownは未観測の利用・記録外の試験等。古いSourceの記載と現在の実行結果を分ける。
- 本件の参照調査は対象に関係するもの。全ファイル全文・全Git履歴・外部の全呼出しを監査したという主張ではない。

## d01

**問題**：System §9は不存在の `_thread-start/thread-start_query.md` と `_thread-end/thread-end_query.md` を通常入口として案内し、Note §2は旧 `_thread-end/ark/` を一律の保存先としていた。

**変更**：Systemは明示Handoffを優先し、指定がないArk開始を既存DomainのCurrent Front-Line Resolutionへ案内する。移行準備は共通契約、保存されたThread-End方式の利用はその入口へ分けた。Noteは選ばれた契約の役割・対象単位・Exact Pathsへ保存判断を委ねる。

例えば、現行ArkのThread単位 `handoff.md` と、旧方式の平置きArtifactには違う名前の理由がある。旧名からunderscoreだけを取る置換では、この意味を修復できない。SystemのGrowth Entry原文と当時の旧Skill・次手の記録は保持し、新しいGateに時間上の境界を示した。

**成立条件**：通常案内が実在し、目的と役割が一致する。明示Handoffの優先、通常入口の所有先、準備と受入れ、旧方式の適用条件を区別できる。新Thread作成・試験は実施しない。

## d02

**問題**：ARK §12に不存在の `_tasks/lessons.md` が残り、AGENTS §1の内容別所有先と食い違っていた。

**変更**：出来事は該当経験原本、成功の意味・成立条件はsuccess-cases、承認された方法改訂は方法の所有資料へ接続する。Task経験索引を全領域の台帳にしない。同じFile Ecology内のThread-End説明も、現行共通移行契約と保存された方式の役割へ合わせた。

**保持**：ARKのIdentity、Root、Human–AI関係、本文の原理、v002-candidateとEOFを保持。ナビゲーションの局所修正としてdate・理由・本記録を付けた。新しい学習台帳は作成していない。

## d05

**問題**：Query側だけでなく、OKF本体側の自己パス・paired_query・本文の正準住所にも旧 `s_special/` が残っていた。両実体は `prompts/` に存在する。

**変更**：二文書中の現在の自己パス・相互参照を実在する住所へ整合した。対象文字列の出現箇所を確認し、旧ローカルBootstrap名、EngineとIgnition Keyの役割、言語・Source・判断原則は保持した。

**成立条件**：両側から同じペアへ戻れ、YAML・コードブロック・通常本文でも現在の住所が一致する。Query起動や回答品質のField Testは保存検証と別である。

## e01

**問題**：repo全体の構造改善を所有するcontrol-centerが、Root READMEから案内されていなかった。

**変更**：Repository Routerへ目的付きの一行を追加した。PLANや全診断をRootへコピーせず、構造整理に関係する時だけ司令塔へ進める。Root READMEの全体レビュー日を、今回の局所修正日で塗り替えない。

## d07

**問題**：Voice READMEはREADMEだけが確認済みと案内していたが、System候補は既に存在する。

**変更**：Systemの所在をリンクし、保存本文にある候補版・pending Human content seal・not_startedを記載した。更新先一覧も既存Systemへ接続した。

**境界**：存在確認はSystemの採用でも、実地試験でもない。古いnot_startedを、記録外の現実が現在まで未実行である証明にしない。System本文は変更していない。

## d08

**問題**：Mode READMEはJournalingのみを案内し、Field Test候補を載せていなかった。Journalingの自己パスは実在名と異なり、関連Skillは不存在の旧 `_skill/` を指していた。READMEの推奨命名 `_mode.md` と既存Field Testの `-mode.md` も異なっていた。

**変更**：二Modeを記録上の成熟段階付きで索引化し、Skill案内を共有Hubへ接続。Journalingの自己パスを修復し、AI-Keli / AI-Activeの概念と元パスは歴史参照として保持した。本文は元からこのFile単体で起動・維持・終了できることを目指しており、旧関連Skillを実行必須Sourceとは扱わない。現在Skillへの対応はUnknownのままとする。

**命名判断**：既存Field Testは現在の名前を明示した例外として保持した。参照を変える物理改名より、正しい所在・役割をまず案内する。推奨命名と例外の区別をREADMEに示し、今回の変更から改名・新Mode・次Trialを開始しない。Field Test本文、JournalingのReflection手順と候補身分は保持した。

## d04

**設計の論点**：章Identityを固定して継承したい一方、Current Threadの入口は移行で変わる。同一ファイルを両方の所有先にすると、一行の入口修正でも固定blobが変わる。

確認した固定章は `ark-project/ark27/README.md`、blob `e7caf9882a212cbda186362001e49791cff8a8ce`、EOF `ARK27_CHAPTER_EOF_v001`。章内の旧01入口は残る。Domain §0.1は既に06の通常入口を所有し、明示Handoffを優先する。

| Node | Edge | Handoff blob / State blob（変更前） |
|---|---|---|
| Ark27:01 | [Handoff](../../ark-project/ark27/ark27-01/handoff.md)・[State](../../ark-project/ark27/ark27-01/state.json)→同一固定章 | `2bf15bbbe6f03e626b482d90c86e14db16b55554` / `dd957fd3c9c70c029834c17f90fac4342f3efb5a` |
| Ark27:02 | [Handoff](../../ark-project/ark27/ark27-02/handoff.md)・[State](../../ark-project/ark27/ark27-02/state.json)→同一固定章 | `61e846419811a1281f1faa4c5c51c9cbd02fe6e8` / `d183d9c65130c3c47977e10bb92be9eaf07b5fca` |
| Ark27:03 | [Handoff](../../ark-project/ark27/ark27-03/handoff.md)・[State](../../ark-project/ark27/ark27-03/state.json)→同一固定章 | `b247381ddab8c0ede84b908fea99736ca0594d09` / `3611edb0358f0ff4eaac6f6e43160a5668f60b59` |
| Ark27:04 | [Handoff](../../ark-project/ark27/ark27-04/handoff.md)・[State](../../ark-project/ark27/ark27-04/state.json)→同一固定章 | `395bfd448576c159beaf1b28d09e1f90cf0de6e1` / `8c4e0ebf7255339e8c4ddbc45bb2b1ab1cd2133d` |
| Ark27:05 | [Handoff](../../ark-project/ark27/ark27-05/handoff.md)・[State](../../ark-project/ark27/ark27-05/state.json)→同一固定章 | `e5abc45dc112770a469a8f00087b7dce5389291c` / `40921ef0a4b578e4ac89e305d265077dc161bf9f` |
| Ark27:06 | [Handoff](../../ark-project/ark27/ark27-06/handoff.md)・[State](../../ark-project/ark27/ark27-06/state.json)→同一固定章 | `0ff05139c7349c8d79ae5e315c6aa956d2e18b1e` / `f954878148a07d0aa042b2e93ed8d29baab96684` |

この12文書の該当固定参照を直接照合した。過去の全Bootを再実行したという意味ではない。

| Node | Edge | 利益と制約 | 今回の判断 |
|---|---|---|---|
| A：既存Domainを可変入口にする | System／一般案内→Domain §0.1→Current Handoff | 新しい現在地の複製を増やさず、固定章を保持できる。章READMEへの直接流入は旧入口のまま | 今回はこの案を適用。D01がDomainへ接続し、ここに残存制約を明記 |
| B：章ごとの可変入口を別途置く | 新しい章入口→現在地の所有先 | 章単位で直接入る用途を支援できる。既存Domainとの重複、Project UIの案内変更、旧章READMEからの導線は別途解決が必要 | 直接入口の必要が具体化した場合の候補。今回の新規ファイル作成は不要と判断 |
| C：章本文と固定Bindingを明示的に移行する | 固定章→新しい安定Core／可変入口 | 元の章直入口を修復し得るが、旧契約のExact SHAと衝突する。新しい値へ一括置換しても互換性の証明にならない | 将来の独立した移行案件。旧契約の再現方法と対象範囲を確定してから扱う |

**設計の到達点**：通常入口の現在地はDomain、Threadの意味・初期化・可変状態は既存三ファイル、当時の章Identityは固定章資料として扱う。Current Thread番号をSystemへ新しく複製しない。今回の実装では章・Handoff・State・Project設定本文を保持する。

**残る判断**：章READMEだけから開始すると旧01入口へ入る制約は未解消。これを解消済みと報告しない。将来B/Cを選ぶ場合は、直接入口の目的、固定参照する12文書、必要なら実UI案内の状態を確認し、旧明示Handoffの扱いと互換経路を設計する。通常Unknownの全解消を本件の局所修正の前提にしない。

## file-manifest

以下の変更前blobは作業前commit、変更後blobは実装commitの再取得時点の実体。対象パスを同じまま修正し、移動・削除はない。本記録とPLANは、その検証結果の追記でさらに改訂されるため、右列の値を将来のCurrent blob固定条件にしない。

| Node | Edge | 変更前blob | 実装commitで確認したblob |
|---|---|---|---|
| [_system/ark-system.md](../../_system/ark-system.md) | D01：Gate Indexと時間境界 | `6dd14fb2c28239de223e33678544a00e82fade1a` | `c10ac44f7743e3ceb442c8f753897bca3f090ee1` |
| [_note/README.md](../../_note/README.md) | D01：用途別保存案内 | `5f3208407831310944f54fdcb85911e5734b7cea` | `bca4449a8a76c5099a24e5fa45495e0dedf7b9a9` |
| [ARK.md](../../ARK.md) | D02：学びの所有先・移行役割 | `12d209d83c61c249875c5a5e58efa8c24c33d6c1` | `154acc0f0633d5e9cd4f66517c519f49b944af5c` |
| [prompts/ark-open-knowledge-format.md](../../prompts/ark-open-knowledge-format.md) | D05：本体の現在住所・Pair | `20682aad7fc92f83a9863a2cd285f160dbe73ba6` | `aacfdc28e58c516f4f312b2ccca8c843550eb1f5` |
| [prompts/ark-open-knowledge-format_query.md](../../prompts/ark-open-knowledge-format_query.md) | D05：Queryの現在住所・Pair | `c4a50e3205fa2f310f618f2abbc5478908f04b83` | `29932c4796a6742c47aa281eee60b392b01897d5` |
| [README.md](../../README.md) | E01：司令塔への入口 | `65a3abf1ae41e57a1757a00e9dc3234128dcac51` | `db97b05360e8077a79877d1c1d21d125e32f6da0` |
| [projects/ark-voice/README.md](../../projects/ark-voice/README.md) | D07：作成済み候補の存在・身分 | `c0753238863a3d2ab5178b615ce8a747cca47f4b` | `59e5d6225ef7eb0c39fd242f32a5550e402803c7` |
| [mode/README.md](../../mode/README.md) | D08：Mode索引・Skill案内・命名例外 | `23878a74117978baa6cec4ad4300c87824dc6cb3` | `eb29b68d58944507198a7273fbfccfcfb635a775` |
| [mode/ai-journaling_mode.md](../../mode/ai-journaling_mode.md) | D08：自己パス・関連Skillの時間境界 | `625e201220a5fee0032436c195d774ac7abb2d8b` | `20086fc0883f9ca4799f17c20a8ffad6a4441516` |
| [control-center/README.md](../../control-center/README.md) | 記録の責務と形成経緯 | `dff12a401d510280c8c73d1dc26ba2008c316d9b` | `2f6e83c0ce54d62375f28225c9bce0aa5919b4c4` |
| [control-center/PLAN.md](../../control-center/PLAN.md) | 既存診断・優先順位とSTR-001の接続 | `68af185c7ae332c4c48725a79ffd15d3b718ee2d` | `4fc7a3a6d5992f9d60fd87f2eff3284e90630730` |
| `control-center/changes/STR-001-navigation-and-ownership.md` | 5W1H、設計比較、変更前後・検証結果 | 新規作成 | `8a9a62b47cdabbc6938b5d79d3b4d324029244b1` |

司令塔READMEとPLANは、役割・現在の診断状態・本記録への入口を更新する。本記録だけを追加する。旧アーカイブ案件・保存物、固定章、Thread三ファイル、他ProjectのSourceは今回の編集対象ではない。

## verification

**実装commitと12対象のRemote全文・blob一致を確認した。六候補の局所修正とD04設計の保存が完了。** 本節は確認後の追記であり、前の保存予定を成功へ読み替えたものではない。

| Node | Edge | 確認した結果 |
|---|---|---|
| 実装保存 | 変更前main→[実装commit](https://github.com/yusukefujiijp/ai-project/commit/9dd82cc37d9e95e03505949c18f66ffd26914a99) | `9dd82cc37d9e95e03505949c18f66ffd26914a99` / tree `4a4ec7b7308f48f534454dd7c4644ef1c77c98bf` |
| When | GitHub保存→Remote確認 | 保存UTC `2026-09-22T15:55:43Z`、JST `2026-09-23T00:55:43+09:00`。12対象の確認完了UTC `2026-09-22T15:56:10Z` |
| Who | 意味上の実装担当→GitHub記録者 | 実装・検証はArk27:06実行AI。GitHubが返したauthor/committer名はいずれも `yusukefujiijp`。Humanの依頼・承認と区別して記録 |
| What / Where | 既存11文書更新＋本記録1文書追加 | 9つの案内・本文、司令塔README・PLAN、変更記録。移動・削除なし。正確な場所とblobはfile-manifest |
| Remote本文 | 意図した全文→保存実体 | 12対象すべてを実装commitから直接再取得し、全文の文字列一致とGit blob一致を確認。main refも実装commitに一致 |
| 構造 | 新規・変更リンク→実在先 | ローカル検査で新規・変更リンク63出現を確認。相対リンクは参照元ごとの組合せで56件。対象パス・取得可能な参照見出し、12文書のmetadata・Identity・宣言EOFを照合 |
| 実効パス | System Gate／OKFペア→対応先 | Gate内の5実在パス、OKF本体とQueryの相互参照を確認。旧歴史パスを現行経路として要求しない |
| 保持 | 作業前317ファイル→実装後318ファイル | 対象外の既存306ファイルはblob・modeが同一。固定章、01–06の三ファイル、アーカイブ原本、Voice System、Field Test本文を保持 |
| 本文内の保持 | 編集対象の現在案内→歴史・行動本文 | System §10以後、ARKのFile Ecology外の本文、Journaling §3以後、PLANの05補足接続史が元本文と一致することを確認 |
| 実利用 | 文書・保存検証→別AIの理解／利用効果 | 本件では独立した別AI試験、Human UI操作、Mode起動、Field Test、実生活効果を観測していない |

変更の全差分は[基点から実装commitの比較](https://github.com/yusukefujiijp/ai-project/compare/945f789a845350455a8b56162a1fc8cd58576eff...9dd82cc37d9e95e03505949c18f66ffd26914a99)から確認できる。今回はAI自身の意味・差分点検と保存確認であり、独立した別AIの理解を代行認定しない。

本節とPLANの完了状態は、この確認結果を根拠に後続commitで保存する。記録自身の最終SHAを本文へ埋める循環を作らない。後続保存も再取得し、現在版はGit履歴・fileのCurrent実体で確認する。

## reuse-and-revision

Future AIは、必要な案件節→file-manifest→変更前commit／実装commitへ辿れる。以前の診断を再び未修正として扱う前に、本記録の完了範囲とCurrent本文を比較する。新しいHuman Correctionや利用結果で改善案を更新でき、当時の順位や解釈を将来の上限にしない。

後から修正を戻す必要が生じた場合は、対象ファイルの基点差分を使い、後続のHuman・他AIの変更を保持して必要な範囲だけ戻す。main全体を過去commitへresetしない。

再発防止の判断は、資料を追加・移動・改訂したとき、必要な入口・自己パス・Pair・固定参照への影響を同じ変更範囲で扱うこと。これを全資料再読・恒久CI新設・巨大台帳の義務へ拡張しない。文書整合の確認、Remote保存、別AIの実理解、実利用の効果はそれぞれ別に観察する。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_001::v001.1
