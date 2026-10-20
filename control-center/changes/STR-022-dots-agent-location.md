---
title: "STR-022 — Dots原本をagents配下へ移す候補と実運用切替"
canonical_path: "control-center/changes/STR-022-dots-agent-location.md"
version: "v002-candidate"
status: "prepared candidate; main cutover held pending actual Dots schedule access"
created: "2026-10-20"
updated: "2026-10-20"
recorded_by: "ChatGPT Work / Dots移設実行担当"
repository: "yusukefujiijp/ai-project"
base_commit: "2dc05496b555638a47a3de2f058c7f632aca773f"
publication_parent: "43cdadf6ff3244edff69098237fce639fd237064"
candidate_branch: "work/dots-agent-location-20261020"
role: "Bounded structural change, provenance, validation and operational cutover conditions"
expected_eof: "EOF::STR_022_DOTS_AGENT_LOCATION::v002"
---

# STR-022 — Dotsの所在と実運用を揃える

**Bの移設候補を作成した。共有基準mainへの切替は保留している。** 実際のDots予定を特定して読取URL・限定保存先を揃えられていないため、候補Refを運用の追記先にしない。保存した候補、main反映、登録Skill反映、製品予定の更新、次の実利用は別々の成果として確認する。

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

EOF::STR_022_DOTS_AGENT_LOCATION::v002
