---
title: "STR-022 — Dots原本のagents配下への移設と実運用切替"
canonical_path: "control-center/changes/STR-022-dots-agent-location.md"
version: "v006"
status: "root dots deleted; bounded post-deletion repository verification complete; protected agents/dots retained; product and runtime effects separately unverified"
created: "2026-10-20"
updated: "2026-10-27"
recorded_by: "ChatGPT Work / Dots移設実行担当"
repository: "yusukefujiijp/ai-project"
base_commit: "2dc05496b555638a47a3de2f058c7f632aca773f"
publication_parent: "43cdadf6ff3244edff69098237fce639fd237064"
candidate_branch: "work/dots-agent-location-20261020"
role: "Bounded structural change, provenance, validation and operational cutover conditions"
retirement_preparation:
  date: "2026-10-25"
  recorded_by: "ChatGPT Work / Ark27:11"
  base_commit: "1422af429a01aa62ea70e102b008d37653ef5ec1"
  authority: "Current Human adopted the ten-path preparation plan and authorized main persistence/reread; no root dots deletion, old04/06 contract migration or product-settings changes"
retirement_verification:
  recorded_date_jst: "2026-10-27"
  observed_at_utc: "2026-10-26T21:32:21Z"
  recorded_by: "ChatGPT Dots / STR-022記録整合担当"
  authority: "Current Human authorized reconciliation of this existing STR with the deleted root dots state, main persistence and remote reread; no other file or product-setting changes"
  deletion_commit: "3e590a5cf2a46d1fc1c7a743ece83c8e8c17ad1c"
  verified_main_commit: "f4516e3ca19a6cf9cd09782ab2b662f0d2315b16"
  previous_version: "v005"
  scope: "Root dots absence, ten navigation-only deletions, protected agents/dots data and bounded current source routes; supplied Work report kept separate from direct verification"
expected_eof: "EOF::STR_022_DOTS_AGENT_LOCATION::v006"
---

# STR-022 — Dotsの所在と実運用を揃える

**現在の状態：旧root `dots/` は2026-10-25のcommitで削除済み。** 削除commitと、2026-10-27 JSTに記録した新原本保持・主要経路の限定照合は[第10節](#dots-retirement-verification)へ。第9節の「削除待ち」は当時の準備完了時点の履歴であり、現在の未完了項目ではない。

**2026-10-24 JST、Dotsの17原本をmainで移設し、既存3予定・5登録Skillの住所更新と保存後確認まで完了した。** 移設と既存設定の切替結果は第8節、その後の旧住所退役準備は[第9節](#dots-retirement-preparation)が所有する。第1〜7節は2026-10-20、第8節は2026-10-24、第9節は2026-10-25の準備・判断・確認結果を保持する履歴であり、そのファイル数・行数・保持方針・未確認状態を現在へ固定しない。保存、main反映、登録Skill、製品予定、実利用をそれぞれ確認する。

## 1. 目的・承認・今回の境界

[A / STR-020](STR-020-ai-to-ai-communication-foundation.md)で共通のAI間コミュニケーション方法と経験の実体をagentsへ集約した。その成果を再作成せず、Dots固有の身元・復元・運用・蓄積を`agents/dots/`へまとめる。共通方法、Board通信Current、Actor固有運用の所有を保ち、住所変更が新旧の書込先分岐を起こさないことを重視する。

Humanは本WorkでBのPlan Mode調査・計画を求め、提示後の2026-10-20 JSTに「Execute GitHub OK」「実行して下さい」と実行を承認した。これは今回の直接の依頼であり、引継ぎ内の過去のGoを新権限へ変換したものではない。予定への接続が確認できるまでmain切替を留保する計画を保持し、まずレビュー可能な候補を保存する。準備担当はChatGPT Work、Chiefはdot-0000: 初穂のまま。

Actor ID、Root、Teshuvah、Human Foreground One、HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保つ。AGENTSの移動・意味改訂、ArkのMissionや担当移管、Inbox Actor作成、別AI送信、新Thread、監視や予定の新設・再作成、私的会話・長期メモリの公開は含めない。日時・通知先・有効状態・保存内容の範囲も変更しない。

## 2. 基準となる現物と配置

今回のmain基準は[2dc05496](https://github.com/yusukefujiijp/ai-project/tree/2dc05496b555638a47a3de2f058c7f632aca773f)。recursive treeは949 entries、truncated=false。直前の調査基準e15a7398からの増分はSlides関連の2パスで、Dotsの16原本は同じblobだった。対象外の変更を保持した候補を作る。これはmainをこのcommitへ永久固定する意味ではなく、切替前に最新headと追記を取り直す。

| 移動元（Repository直下基準） | 新しい実体 | 旧住所の扱い |
|---|---|---|
| `dots/README.md` | `agents/dots/README.md` | 移転案内・既存節への接続 |
| `dots/actors/dot-0000/README.md` | `agents/dots/actors/dot-0000/README.md` | 移転案内 |
| `dots/actors/dot-0001/README.md` | `agents/dots/actors/dot-0001/README.md` | 移転案内。Actor準備状態を保持 |
| `dots/ark-map/README.md` | `agents/dots/ark-map/README.md` | 移転案内 |
| `dots/daily-review/README.md` | `agents/dots/daily-review/README.md` | 移転案内 |
| `dots/inbox/README.md` | `agents/dots/inbox/README.md` | 移転案内 |
| `dots/inbox/inbox.jsonl` | `agents/dots/inbox/inbox.jsonl` | 除去。LF一文字のSeedを新住所へ保持 |
| `dots/lessons/README.md` | `agents/dots/lessons/README.md` | 移転案内 |
| `dots/lessons/lessons.jsonl` | `agents/dots/lessons/lessons.jsonl` | 除去。8行の単一原本 |
| `dots/lessons/experiments/json-vs-jsonl/README.md` | `agents/dots/lessons/experiments/json-vs-jsonl/README.md` | 移転案内 |
| `dots/lessons/experiments/json-vs-jsonl/lessons-headerless.jsonl` | `agents/dots/lessons/experiments/json-vs-jsonl/lessons-headerless.jsonl` | 除去。凍結比較データ |
| `dots/lessons/experiments/json-vs-jsonl/lessons.json` | `agents/dots/lessons/experiments/json-vs-jsonl/lessons.json` | 除去。凍結比較データ |
| `dots/lessons/experiments/json-vs-jsonl/lessons.jsonl` | `agents/dots/lessons/experiments/json-vs-jsonl/lessons.jsonl` | 除去。凍結比較データ |
| `dots/logs/README.md` | `agents/dots/logs/README.md` | 移転案内 |
| `dots/logs/dot-0000.jsonl` | `agents/dots/logs/dot-0000.jsonl` | 除去。8行と帰属を保持 |
| `dots/references/README.md` | `agents/dots/references/README.md` | 除去。LF一文字のSeedを新住所へ保持 |

移動する原本は16件。旧入口は9件、旧実体の削除は7パスであり、9件の案内と別の可変原本を併置しない。案内は旧契約と異なるIdentity・EOFを持ち、リンク先原本の全文読解を求める。旧JSONLへの書込みは自動転送されない。

移動元のcommit・blob・旧pathは新READMEの`relocation_patch`と旧入口に残す。Dots入口はv013、root入口はv017、agents入口はv002。その他の移動READMEは住所と参照だけの限定patchとして既存の本文版・EOFと出来事の日時を保持する。LFだけの二つのSeedを破損や完成済み契約として扱わない。

保存直前の再確認では、mainが`43cdadf6ff3244edff69098237fce639fd237064`へ進んでいた。並行変更6パスはArk28:07の三点セット新設とArk入口・Ark28入口・28:06 Stateの接続更新。今回の48読取対象は同じblobだったため、この新headを候補commitの親とし、並行する移行成果をそのまま保持する。

## 3. 参照更新と保持する意味

原本16件の住所に加え、既存26資料の45現役宛先を更新した。root READMEとagents入口、通信マニュアル、Board入口と既存2 Topic、Skills Hub・5 SKILL.md・load/podcast入口、records入口、references入口・lessons・成功事例2件、Covenant、既存Slides README、ARCHIVE、整理指針、STR-007/009/015を含む。

歴史資料内でも現行契約へ戻るリンクは新住所へ合わせ、当時の配置表、Human原文、固定commit URL、過去の観測と採用順序は保持する。26資料に含まれる113本の固定版URLは不変。Topicの通信Current・通知版・宛先・受領状態は変更しない。既存Promptの全面改訂や移動も行わない。

[Main11 State](../../ark-project/ark27/ark27-11/state.json)は`bindings.dots`の5つの現役pathだけを変更し、revision 2の限定来歴を追加する。Mission、初期準備の帰属、固定Source、移行状態、受入れ証拠は保持する。Main11の根本文書再設計の承認・完了を追加しない。

Ark28:06のRuntime・Handoff・Stateは変更しない。同HandoffのDotsはCurrent ownerへの読取で、準備版は恒久pinではないため、旧入口を経由し、新原本を指定順序内で全文読む接続を文書上確認した。旧stubだけで読了扱いにせず、受け手自身が新原本のIdentityとEOFを記録する。これは新しいTarget受入れ試験のPASSではない。

一方、旧Ark28:04 Handoffのように`canonical_path: dots/README.md`を明示する契約は、自動的に互換へ格上げしない。歴史的な三点セットを変更せず、当時の固定snapshotで復元するか、将来そのRuntimeを使う必要が生じた時に対象を限った版移行を解決する。Ark99:03等の固定Handoffも保持する。旧住所の残存を一括置換で消すことは目的にしない。

新たに準備されたArk28:07のDots参照は、必須14件外の条件付きCurrent入口だった。07の固定Bindingは07 Runtime/HandoffとSource06収穫へ向き、Dotsの旧canonical_path固定は追加されていない。共通通信マニュアルはv001・Identity・EOFを保つリンク修正のみ。06 Stateの並行revision 4も保持する。これは原本契約の点検であり、07自身の受入れ観測ではない。

## 4. データ保持と候補検査

今回のWork作業をdot-0000の新実績としてActorログへ追加しない。既存8行のログでは、JSONLの実際の位置から解決する4つのSTR-008/009相対locatorだけを`../../control-center/…`から`../../../control-center/…`へ補正した。到達先・anchor、ID、日時、Actor帰属、順序、未知fieldとその他の内容は同一。

共通lesson 8行はbyte単位で保持した。凍結比較データ3本のblobは、それぞれ次のまま。

| 凍結データ | 保持したblob |
|---|---|
| `lessons-headerless.jsonl` | `e1df104c2e306990f30ffced03ea3775425208be` |
| `lessons.json` | `e289326eef11010e0d4d89d243a0b4dfe17fedb3` |
| `lessons.jsonl` | `942c0a7a0df2dc22efcdf569d86dc91977b3ca13` |

過去の比較実験を今回再実施したとは扱わない。候補上でのデータ同一性、相対参照の到達、必要なanchor、metadata・EOF、保持対象の固定URL、旧可変原本の除去を検査する。5つの共有SKILL.mdは計7 URLの`/blob/main/dots/`から`/blob/main/agents/dots/`への置換以外、本文を保持した。追加のGraph・Schema・全体台帳・空の専門lessonは作成しない。

候補全体は62変更パス（新規17・更新38・削除7）。移設16実体に加え、現役参照、旧案内、限定State、既存索引・日時記録と本STRを含む。候補上の相対リンク796本と手元に全文を持つ対象のanchor182件を検査し、到達エラーなし。全外部URLや実際の受け手の理解を網羅した検査ではない。

別担当の差分レビューでは旧logs入口の`schema_version` anchorでunderscoreが落ちる不整合を検出し、候補保存前に修正した。検査対象は候補Refであり、main URLの切替後到達や運用効果は未確認。

## 5. 実際の予定と登録Skill — main切替を保留する理由

2026-10-20 JSTの実行調査で、利用できるAutomations一覧は15件、末尾cursorなしだったが、今回のDots通常Map・補助確認・日次総括に一致する対象を特定できなかった。この結果は「Dots予定は存在しない」という証明ではない。別アカウント・別製品面への帰属も推測で補わない。製品の内部ID・無関係な予定内容は公開しない。

登録Skill側は、最新の正規管理Git原本でload / save / prepare-ark-transition / voice-mode / podcast-modeの既存5登録物を確認し、登録本文・管理原本・GitHub共有本文の一致を確認した。再作成せず7 URLを更新する経路を確認できた。古いローカルcheckoutで見えなかったことを登録消失と判断しない。まだpush・登録反映は行っていない。

| 運用 | 読取先の更新 | 限定保存先の接続 |
|---|---|---|
| 初穂の通常Map | `agents/dots/ark-map/README.md` | recordsは同じ。Actorログと共通lessonを新住所へ。実際の専門的学びがある場合だけ`agents/dots/ark-map/lessons.jsonl` |
| 補助確認 | 同じMap原本 | 読取・報告のみ。保存権限を増やさない |
| 日次総括 | `agents/dots/daily-review/README.md` | recordsは同じ。必要なActorログと共通lessonを新住所へ。Map専門lessonへ拡張しない |
| 既存5登録Skill | 共有版と同じ7 URL | 同じ登録IDを維持。無関係なSkillは変更しない |

予定の頻度・時刻・timezone・有効状態・通知先と指示本文の対象外部分を保持する。予定を削除・再作成せず、既存予定の読取URL・限定保存先だけを更新する。現物を特定し、変更前後を再取得できるまでこの表を実施済みへ進めない。

## 6. 切替の再開条件と保存確認

1. 正規の製品設定経路で対象予定を特定し、指示全文・実行状態・更新方法を確認する。利用中のconnectorが不足するためBrowserへ切り替える場合は、そのToolの利用条件に従ってHumanのfallback許可を得る。B本体の実行承認を工程ごとに取り直す意味ではない。
2. 最新main・対象blob・ログとlessonの全行・最新登録本文を取り直し、候補準備後の並行変更を反映する。既に切替済みなら現物を照合し、盲目的に重ねて操作しない。
3. 製品予定とGitHubを一つの原子的更新にはできないため、対象writerが実行中でないことと次回実行までの猶予を確認して切替を調整する。旧住所の書込みを新住所へ取りこぼさず接続できない場合は、その時点でmain公開を止める。予定の無断停止や頻度変更で解決しない。
4. 条件が揃えば、最新mainを親とする差分へ統合し、non-force・版条件付きでmainへ反映する。直後に既存予定の限定pathと既存5登録Skillを揃えて再取得し、切替中のGit履歴・旧JSONL再出現・新旧への分岐を検査する。途中結果不明ではhead・設定・履歴を先に確認する。
5. Remoteの対象Refから全変更本文・blob、旧データ不在、対象外保持、必要なmetadata・EOF・リンクを再取得して照合する。製品側は対象予定の設定と登録本文の一致を確認する。新しい外部対話・予定の手動再実行・試験用ログ追記は保存確認に含めない。

今回の一区切りは候補の保存と再取得確認まで。main切替・製品側反映・実運用は未完了のまま明示する。候補の保存結果はGit commit / Draft PRと本Workの結果報告へ接続し、次の実施時には本記録の観測を更新する。確認の記録を無限に追加せず、日時の要点は[records](../../records/README.md)へ一活動として残す。

## 7. 候補のGitHub保存と再取得（2026-10-20 JST）

[実装候補commit 9f7e67bf](https://github.com/yusukefujiijp/ai-project/commit/9f7e67bf48a6fc392296464d6127d4d152aa7eeb)を `work/dots-agent-location-20261020` へ保存し、[Draft PR #9](https://github.com/yusukefujiijp/ai-project/pull/9)を作成した。共有基準mainへは反映していない。

2026-10-20T12:32:29Zまでに、固定候補commitから全55対象本文とSHAを再取得し、意図した全文と一致した。候補treeでは旧データ7パスが不在で、対象外611 blob/modeを保持していた。GitHubのrename表示では55 changed files、新旧住所を別々に数える本記録では62変更パスであり、数え方の差である。

PR作成時にmainがさらに `429ee61290a8531edc6c59596697f8c96d642f65` へ進んだことを検出した。43cdからの増分は `ark-project/README.md` の1行整合で、Bの変更対象との重複はない。この追加も候補へ統合して保持する。元の移設比較基準、固定証拠、最初の保存結果を新しい時点へ塗り替えない。

この節は候補の保存確認の追記。製品予定・登録Skillの実更新、main切替、外部AIの受入れ・運用成功を意味しない。Bの既承認範囲は保持され、次の不足は対象予定を正規の製品設定画面で特定する接続である。

## 8. 2026-10-24の再開と最新mainの統合

Humanは本WorkでBrowserへの切替を明示許可し、初穂の既存通常Map・補助確認・日次総括と5登録Skillの住所を揃え、並行変更を保持して移設・再取得確認まで進めるよう指定した。頻度・時刻・有効状態・通知先・保存内容の範囲を維持し、予定の削除・再作成、外部AI送信をしない境界を引き継ぐ。

再開時mainは `b2768b60d1b334ab25e49f5aae65d53038fc510a`、treeは973 entries・truncated=false。先行候補が統合した `429ee61290a8531edc6c59596697f8c96d642f65` 以後の並行変更36パスを保持する。変更対象の重なりでは、Map v005のNext Step→Next Query改訂、共通lessonの同一行への訂正と追加1行（現在9行）、Skills Hub v0.43の新Skill入口を最新本文から統合した。AGENTS v004.6等の対象外改訂はそのまま保持し、旧版へ戻さない。

新たに公開済みの `dots/bot-to-dot-experiments.md` も `agents/dots/bot-to-dot-experiments.md` へ移す。本文の候補・未採用状態を保持し、二つの相対リンクだけを新位置から到達する形へ直す。旧住所には固定元版と新原本への案内を置く。Grok Botの導入・新実験を開始する変更ではない。これにより原本17件、旧案内10件、旧実体削除7件となる。既存ログ8行・4相対locator補正、凍結データ3本、二つのLF Seedを保持する。

製品設定は承認済みのBrowser経路から実物を確認した。無関係な会話本文や予定IDは公開しない。

| 既存予定 | UIで確認した設定 | 限定した住所差分 |
|---|---|---|
| Ark現在地と次の一手 | 有効。カスタムRRULE `FREQ=DAILY;BYHOUR=4,8,12,16,20;BYMINUTE=0`。日本標準時、終了なし、毎回同じチャット | Map原本URL1件、ログ・共通lesson・条件付き専門lessonの保存先3件 |
| Ark残作業とGoalの変化 | 有効。「カスタム」、日本標準時、毎回同じチャット。詳細な時刻ルールはこの編集UIに表示されないため独立確認は未了 | Map原本URL1件のみ。読取・条件付き報告だけという境界を保持 |
| Ark前日総括と保存確認 | 有効。編集画面の選択は「毎日」、01:00 JST、日本標準時、終了なし、毎回同じチャット | 日次原本URL1件、共通lesson・Actorログの保存先2件 |

日次総括はプロフィール一覧に「毎週 1:00」と表示される一方、編集画面では「毎日」が選択されていた。この表示差から予定を変更せず、編集前後の選択を保持する。通常Map・補助確認の指示に残る旧見出し配置等は住所変更の範囲外としてそのまま保持する。現行運用原本の後続改訂を巻き戻したり、今回の予定編集へ形式改訂を混ぜたりしない。

登録管理原本の最新head `aee5f38dcf2521956bddf16cb37654f23505d3b0` を取り込み、対象5件が共有原本と一致することを確認した。既存登録IDを保ち、計7 URLだけを新住所へ変える候補を作成した。無関係な登録物12パスの後続変更も保持する。

### main反映とデータの再取得

[PR #9](https://github.com/yusukefujiijp/ai-project/pull/9)を最新mainに合わせたcommit `5eb881c743296a127fee0d0c25e27c0eb1fea7db` へ更新し、公開直前のmainが上記b2768b60のままであることを確認した。期待headを指定してmergeし、[main反映commit 1610115e](https://github.com/yusukefujiijp/ai-project/commit/1610115e2ca9146edeaaadc9b5c3d3ce9e10c2cb)を取得した。PRはmerged・closed。force更新や古いtreeへの巻戻しは行っていない。

移設差分は64物理パス（新規18・更新39・削除7）。GitHubのrename表示では57 files。固定main commitから存在する57対象を全文再取得し、意図した本文・SHAと完全一致した。recursive treeは995 entries・truncated=false。削除対象7パスの不在と、対象外625 blob/modeが切替前mainのままであることを確認した。旧 `dots/` 配下に可変JSON/JSONL原本は残っていない。

共通lessonは最新9行をbyte単位で保持。Actorログ8行は4相対locator以外を保持し、元の到達先へ解決する。凍結比較データ3本とLF Seed二つは元blobのまま。相対リンク805本・手元の全文に対するlocal anchor185件を検査し、到達エラーはなかった。固定版の証拠、Actor ID、日時、順序、未知fieldを保持した。切替後のhead・tree確認では旧JSONLの再出現や新旧への追記分岐は観測していない。すべての外部consumerや将来の実行を網羅した保証ではない。

### 既存3予定の保存後確認

上表の3予定を同じ設定画面で更新し、保存後に一件ずつ開き直した。通常Map4か所・補助確認1か所・日次総括3か所、計8か所の `dots/` → `agents/dots/` だけを変更した。再取得した指示全文は、変更前本文にこの住所差分を適用した文字列と完全一致した。段落・改行も一致し、補助確認へ保存権限を追加していない。

通常MapのRRULEは保存前後で完全一致。日次総括と補助確認は、詳細設定を含む画面本文も住所差分以外一致した。3予定の有効状態、繰返し、表示された時刻・timezone・終了条件、同じチャットを使う実行先を維持し、通知先の設定には触れていない。補助確認の詳細時刻ルールがUIに出ない点と、日次総括の一覧・編集画面の表示差は上表の通りであり、未観測値を補完しない。削除・再作成、手動実行、停止・再開、外部AI送信は行っていない。

### 5登録Skillの保存と取得経路の違い

既存5件の同時pushはHTTP 422となった。Remote refが `aee5f38d` のまま、会話内読取でも旧URLであることを確認し、末尾の `Everything up-to-date` を成功と扱わなかった。失敗commit `0212bf82c4cbe90876bdc8bb7f863bffb92cd220` は手元で保持した。

正規のSkill保存手順に沿い、同じ既存登録物・同じRemoteへ一件ずつ限定して保存した。保存の都度Remoteの後続変更を取り込み、次の通常pushはいずれも成功した。422の原因を多件同時要求と断定せず、権限や保存先を変更して回避したものとも扱わない。

| 既存Skill | URL数 | 通常保存commit |
|---|---:|---|
| load | 1 | `507731a8d77046314ae7471882ae59a34bb7026f` |
| save | 3 | `6f19019a5ec583e74f4d18cfef88c3f4e6395643` |
| prepare-ark-transition | 1 | `4892bca8ba54769fa214622ff0b048f2495cded2` |
| voice-mode | 1 | `c938dbc3f83b62dec222a853d54dcd34d0173938` |
| podcast-mode | 1 | `526e35048a4a000c2bee916de4d5b51816ec4b27` |

登録Remote head `526e35048a4a000c2bee916de4d5b51816ec4b27` を再取得し、5本文すべてがmainの共有SKILL.mdとbyte単位で一致した。変更前からの意味差分は計7 URLだけで、登録ID・frontmatter・表示設定の変更を要求していない。登録先で別途生じた `Materialized from stored content` commit `89b78ab4b1fe7000ac7befb8c5a44ffaccc81668` はloadのicon.svgを変更していた。その発生原因・Actorは今回独立確認できないため、自分のURL編集の成果とせず、勝手に旧iconへ戻さず保持した。対象外のSkillと作業元の未保存変更を上書きしていない。

Browserの既存Skills画面でも5件を開き、同じ登録物に計7本の新URLが表示されることを確認した。一方、この会話の `skills.read` 経路を再取得すると、5件とも旧URLを含む以前の本文を返した。登録Remote・製品UIの新本文と、会話内取得の旧本文を別の観測として残す。キャッシュ原因や反映時期はUnknownであり、更新失敗・全Runtime更新済みのどちらとも同一視しない。

旧READMEの短い移転案内を維持して、新原本へ辿れるようにした。ただし旧JSONLへの書込は自動転送しない。実予定の保存先は新住所に照合済み。今後、旧本文を受け取った実行者も現行の所有原本を確認し、旧住所への追記を再作成しない。会話内取得の差だけを理由に、登録の再作成・同じ本文の再push・全履歴同期は開始しない。

### 一区切りと残る観測

本Bの移設・既存設定の住所整合・保存後再取得は一区切りとする。この最終結果を本STRに更新し、[2026-10-24の日別記録](../../records/2026/10/2026-10-24.jsonl)へ一活動として残すため、初回準備からの累積差分は65物理パス（新規19・更新39・削除7）となる。実際の次回予定実行、別AIの理解、自然なSkill選択、Humanの負担軽減・長期効果は今回の保存検証に含めない。新しい監視・通知・対話試験は作成しない。

再開が必要なのは、実際の取得経路で旧参照のまま新原本へ到達できない、旧JSONLが再出現する、または次回の通常実行で参照不整合が観測された場合。その時点の現物・版・既存設定から不足範囲だけを調べ、完了した移設・予定編集を再演しない。


<a id="dots-retirement-preparation"></a>

## 9. 2026-10-25の旧dots退役準備 — 最終削除はHuman

### 9.1 目的・採用・今回の権限

Humanは、Arkの初期段階に不要な旧住所を整理し、未来のHuman・AIが原本の所在や旧構造の存在理由を毎回解釈し直す負担を減らす方向を指定した。多少のリンク断絶は発見した箇所で修復できるものとして扱うが、原本の消失、旧保存先への再作成、Binding不一致を成功扱いする意味ではない。未知の全consumer・過去の全コピーの安全証明は開始条件にしない。

Dotsから伝達された調査報告を受け、Ark27:11のWorkが現物を照合して計画を提示した。その後、Human自身がこの10ファイルの準備を実行承認した。範囲は現役参照・退役説明・Ark28:07の限定した版移行とBinding、main保存・再取得、旧入口を利用しない経路検査まで。計画受領やDotsの報告だけを承認に変えたものではない。

**Repository直下の `dots/` の最終削除はYusukeJP自身が行い、`agents/dots/` を保護する。** 今回は旧案内も変更・削除しない。登録Skill・予定・Project設定、旧04／06契約、他の旧フォルダや互換Skill、統合Home・添付資料は変更対象外。新しい送信、予定再作成、運用試験、ActorやMissionの引取りは行わない。

### 9.2 基点と変更する接続

基点は[main 1422af4](https://github.com/yusukefujiijp/ai-project/tree/1422af429a01aa62ea70e102b008d37653ef5ec1)。計画時と実行開始時のheadは同じで、recursive treeは1019 entries、truncated=falseだった。旧 `dots/` の10ファイルは移転案内のみでJSON／JSONLはなく、新住所に17原本がある。これはこの基点での観測であり、将来の削除時まで件数・内容を固定しない。

| 対象（Repository直下基準） | 今回の差分 |
|---|---|
| `__archives/README.md` | 現役Actorログへ戻るリンクを `agents/dots/logs/README.md` へ |
| `ark-project/ark27/ark27-11/README.md`・`handoff.md` | 現在のDots方向・条件付き協働入口を `agents/dots/README.md` へ |
| `ark-project/ark28/INSTRUCTIONS.md` | 公開指示のDots URLを新住所へ。製品内の指示欄の更新とは区別 |
| `ark-project/ark28/ark28-07/README.md`・`handoff.md`・`state.json` | Dotsの現役参照と対応する版・EOF・SHA Bindingを一組で整合 |
| `ark-project/ark99/ark99-00/README.md` | 条件付き協働の入口を新住所へ |
| `agents/README.md` | 旧案内を残した履歴と、Humanによる退役方針を区別。相対リンク `dots/README.md` は正しく `agents/dots/README.md` に解決するため保持 |
| 本STR | 当時の保持判断・切替実績を残し、後続の退役準備・検証・削除待ちを接続 |

Main11 Stateは新住所を参照済みで、README／Handoffの観測blobを永久固定する契約ではないため変更しない。固定Source10 revision6、Main10の受入れ・比較・STR-018／019の完了、各Actorの担当・権限は保持する。

### 9.3 Ark28:07の限定した版移行と旧契約

07 Runtime／Handoffはv001.1-human-authorized、Stateはschema v001のrevision2とする。README最終本文からHandoffのRuntime Bindingを確定し、そのHandoff最終本文からStateの両Bindingを確定する。07のIdentity・Title・14件のSource順序・R1–R8・Root・権限・進捗を保持し、State自己SHAや相互live-blob循環を作らない。

旧07 v001三点の参照先は[改訂前snapshot](https://github.com/yusukefujiijp/ai-project/tree/1422af429a01aa62ea70e102b008d37653ef5ec1/ark-project/ark28/ark28-07/)。旧v001が要求したREADMEの固定SHAを本改訂後のmainへ当てても一致しない。履歴閲覧と新しいCurrent契約を区別し、旧Gate通過や新Boot成功へ読み替えない。Handoff内の2026-10-20起動Queryは当時の準備本文として保持し、再送しない。

固定Source06はcommit `e15a7398efa68958c0584e8787faf7caf10f587d`、State revision3、blob `e5e2ffda88f1faceb288abc8b09aa353facdba81` のまま。Current06 `progress.next_transition` にある当時の07公開blobと実際の起動・受入れReceiptも歴史として保持する。今回の保守で更新した07のSHAへ過去の観測を書き換えず、初期の未観測値から後続の受入れを未完了へ戻さない。

現行Support入口は07で、必要な固定06成果とCurrent06 Receiptは旧 `dots/` を経由せず取得できる。06の旧Runtime／Handoff／Stateは移行しない。第3節の「旧stub経由で06から新原本へ読む」は移設時の接続確認であり、旧住所削除後も使えるという保証ではない。

旧04の `canonical_path: dots/README.md` 条件と、旧06の必須Dots入口は別扱い。旧住所削除後、それらを指定したCurrent-main Bootをそのまま成立としない。歴史は固定版から読み、実際にそのRuntimeを再利用する必要が生じた場合に、対象と権限を限定した版移行を解決する。全旧章の再Boot・近代化は今回の前提にしない。

### 9.4 製品側と検証の境界

2026-10-25、実行担当Workが現行の登録取得経路からload／save／prepare-ark-transition／voice-mode／podcast-modeを取得し、5本文すべてが上記基点のGitHub共有本文と全文一致した。計7本のDots URLは新住所である。登録物は変更していない。第8節の会話内Skill取得が旧本文を返した観測は当時の履歴として残す。この一経路の一致から、全Runtime・自動選択・実利用を保証しない。

同Workの読み取り専用Automations取得では15件・末尾cursorなしだったが、対象3予定は特定できなかった。予定の不存在・失敗とは判断せず、第8節のBrowserでの住所切替と保存後確認を既存成果として保持する。今回Browserによる再操作はしていない。Ark28 Projectの実際の指示欄・古いコピーは未確認であり、公開INSTRUCTIONSの修正だけで実設定も更新済みとは扱わない。

検証では、旧 `dots/` のパスを検査用の到達先集合から除外し、変更した現役リンク、5 Skillの7 URL、Dots入口・Map・日次総括・Actorログ・lessonの読取／保存経路を新原本へ解決する。実際の旧フォルダ削除、試験用のログ・lesson保存、予定実行は行わない。Map固有の条件付き保存先 `agents/dots/ark-map/lessons.jsonl` は未作成の候補であり、検査のための空ファイルを作らない。

履歴の `previous_path`、固定commitの証拠、Human原文backup、旧章の成立時の参照は保持する。文字列 `dots/` のゼロ化やRepository全体の全リンク健全性を判定目標にしない。主要な現役依存を解消した範囲と、残る旧契約・未知のコピーを区別する。

### 9.5 準備状態・Humanへの引渡し（当時の履歴）

以下は準備完了時点の観測と引渡し条件。後の削除と現在の確認結果は[第10節](#dots-retirement-verification)で区別する。

**2026-10-25 JST、準備のmain反映とRemote再取得を確認し、Humanによる削除待ちとなった。旧 `dots/` は存在し、削除・削除後検証は行っていない。**

実装の固定commitは[d5232a91](https://github.com/yusukefujiijp/ai-project/commit/d5232a91b1925d9560e44df2eefa3994122d86df)。基点 `1422af429a01aa62ea70e102b008d37653ef5ec1` を親として10ファイルだけを変更した。公開前の固定commitから10本文・SHAを全文再取得して一致を確認し、公開直前のmainが基点のままであることを確認して、期待head付き・non-forceでmainへ反映した。反映後もmainから10本文・SHAを全文再取得し、意図した内容との完全一致を確認した。

公開後treeは1019 entries・truncated=false、697 blobのうち変更10・対象外687のblob／modeを保持。旧案内10件、新原本17件、Main11 State、旧04／06契約とCurrent06 Receipt、共有Skillの本文は不変だった。固定Source・過去の受入れ観測、07 StateのIdentity・authority・now・evidence・deferred・progressは変更していない。

| 07の改訂物 | 確認した版・SHA |
|---|---|
| README | v001.1-human-authorized / `a0b6f07034ba04e932dd5b8884db23cf89c54a6e` |
| Handoff | v001.1-human-authorized / `4f9c62c1d4437091c3b35771075c8d80081d60cb` |
| State | schema v001・revision2 / `cf0821c59be4c21437040f1e5e17a9dd78c39516` |

旧 `dots/` を到達先集合から除いた静的検査では、対象文書・新Dots原本・5共有Skillから新Dots領域へ向かう64参照について、実際の相対位置・path・必要なanchorを解決し、到達エラーはなかった。通常Map・日次総括のActorログ／共通lesson保存先も新住所に存在し、条件付きMap専門lessonは新住所の未作成候補として確認した。試験用の書込や運用起動をせず、検査済み本文と公開後本文の一致を確認した結果である。全外部consumerや実際の削除後動作の保証ではない。

本追記は上記実装commitの確認後に既存STRへ記録するもの。本追記自身の保存結果・最終commit・再取得は、実行担当の結果報告とGit履歴へ接続し、自己SHAや未観測の自己再取得を本文へ埋めない。

準備完了時の到達点は **「Humanによる削除待ち」** だった。削除直前に最新headと旧側の全内容を準備結果に照合し、案内だけであること、新しい原本・データや他AIの変更が増えていないことを確認する。差があればその内容を解決し、古い「10ファイル」という観測だけで削除対象を確定しない。

変更不能な過去のmain URLや旧Queryは削除後に切れる可能性がある。必要時に `agents/dots/` の現在原本へ接続し直し、Bindingを持つ旧契約なら版移行として扱う。問題時は上記基点と準備結果の固定commitを比較し、必要箇所だけ復元・修復する。Repository全体を巻き戻さず、旧フォルダ全体の恒久復活を標準にしない。

Humanの削除後、旧入口の不在、新原本の保持、主要経路を確かめる確認・記録は、実際の後続依頼と権限に従う。準備完了を削除済み・削除後検証済みと記録しない。


<a id="dots-retirement-verification"></a>

## 10. 旧dots削除後の現物照合 — 2026-10-27 JST記録

### 10.1 削除済みの現在状態と、今回の権限

**Repository直下の旧 `dots/` は削除済みであり、現在は「Humanによる削除待ち」ではない。** 削除は[commit 3e590a5c](https://github.com/yusukefujiijp/ai-project/commit/3e590a5cf2a46d1fc1c7a743ece83c8e8c17ad1c)（`Delete dots directory`、2026-10-25T01:57:27Z／同日10:57:27 JST）に記録されている。GitHub上のauthorは `yusukefujiijp`、committerは `web-flow`。この公開履歴と、今回の記録整合担当による削除後の読取確認を区別する。今回のAIが削除を実行したとは記録しない。

Humanは、準備・削除待ちの履歴を残し、削除commit、削除後の確認範囲、残る未確認を区別して、既存の本STRを最新の現物へ整合し、main保存・再取得確認まで行うよう依頼した。今回の変更は本ファイルの現在状態・追記・版・日付・metadata・EOFだけ。旧フォルダの削除・復活、再移設、登録Skill・予定・Project設定・旧Runtimeの改訂、外部AI送信、新しい運用試験は含めない。

### 10.2 公開GitHubから直接確認した範囲

確認時刻は2026-10-26T21:32:21Z（2026-10-27 06:32:21 JST）。確認対象の固定mainは[f4516e3c](https://github.com/yusukefujiijp/ai-project/tree/f4516e3ca19a6cf9cd09782ab2b662f0d2315b16)。以下は、今回の担当が正規GitHub Connectorから取得したcommit差分、非省略tree、該当本文を照合した結果であり、別Workの報告だけから補ったものではない。

| 対象 | 直接確認した結果と境界 |
|---|---|
| 削除commitの範囲 | 親は `d6b94b921e6fda75d9b3cd47056a6ee7d87f8870`。変更は旧 `dots/` 内の10案内だけで、全件 `removed`、追加0行・削除647行。各削除本文に `navigation-only` と新原本への案内があり、JSON／JSONL原本の削除ではない |
| 削除時の保護対象 | 削除commitのtreeは998 entries・truncated=false。旧 `dots/` はなく、`agents/dots/` の17原本は削除直前の親commitとblob／modeがすべて一致する |
| 確認時mainの所在 | treeは1059 entries・truncated=false。root `dots` およびその配下は存在せず、`agents/dots/` の17原本が存在する。削除commitはこのmainの祖先である |
| 準備時からのデータ保持 | 第9節の準備基点 `1422af429a01aa62ea70e102b008d37653ef5ec1` と比べ、17原本中16件のblob／modeは同一。差があるのは共通 `lessons/lessons.jsonl` のみで、全文比較により旧9行と末尾LFをそのまま保ち、後続1行が追加されている。後続の学びを旧版へ戻さない |
| 主要な現役経路 | Dots入口、通常Map、日次総括から新Dots領域へ向かう現役リンクのpathを現在treeへ解決し、Actorログ `agents/dots/logs/dot-0000.jsonl` と共通lesson `agents/dots/lessons/lessons.jsonl` の所在も確認した。5共有SKILL.mdの計7本のDots URLは新住所であり、対象pathと指定されたanchorへ到達する。これは静的な原本・参照照合で、実際の予定実行や保存動作の試験ではない |

Map固有の条件付き `agents/dots/ark-map/lessons.jsonl` は、この確認時点でも未作成の候補である。検査のために空ファイルを作らず、旧住所へ可変原本を再作成しない。第9.5節の64参照検査は削除前の準備検査として保持し、今回それを同じ件数の全再試験へ読み替えない。

### 10.3 Human提示の別Work報告と、残る未確認

Humanが提示した別Workの削除後報告には、16 blob不変、lessonの旧9行保持と1行追加、既存5登録Skillの本文一致と計7本の新URL確認が含まれていた。Repository側の保持は第10.2節で今回も独立照合できた。一方、**既存5登録Skillの一致は、そのWorkが確認した取得経路・時点での報告**として扱う。今回のGitHub共有原本の7 URL確認を、登録Remote・製品UI・全Runtimeの新たな独立確認へ拡張しない。提示された報告を超えて私的Work会話や長期メモリを転記していない。

第8節の既存3予定の住所切替・保存後確認と、第9.4節の後続観測は、それぞれ当時の成果として保持する。今回、製品側の現設定、削除後の実際の予定実行・保存、Ark28 Projectの実指示欄、古いコピー、全外部consumer、Skillの自然選択や他AIの理解、長期の利用効果は確認していない。未確認を不存在・失敗・完了のいずれにも変換しない。

旧04／06等の固定住所・Identity・Bindingを要求する契約は、第9.3節の境界を維持する。旧main URLが切れる場合は、新原本または当時の固定版へ接続し、実際に旧Runtimeの再利用が必要になった時だけ、その対象と権限で版移行を判断する。今回の旧住所削除確認を、旧契約のBoot成功・全旧章の近代化完了と扱わない。

### 10.4 到達点と再開条件

現在の到達点は **「旧root dots削除済み／新原本保持と主要な現役経路の限定照合済み」**。第9節の準備と削除待ちは当時の正しい履歴として残し、Current状態だけを本節へ接続した。

本追記自身の保存commitとRemote再取得結果はGit履歴・今回の結果報告が所有する。未観測の自己再取得や自己SHAを本文へ埋め込まない。以後は、通常利用で旧参照への到達不能、旧JSONLの再出現、保存先の分岐、具体的なBinding不一致が観測された場合に、その現物と有効な権限から不足箇所だけを調べる。削除・移設・予定編集を再演したり、全フォルダを恒久復活させたりすることを標準の次工程にはしない。

EOF::STR_022_DOTS_AGENT_LOCATION::v006
