---
title: "STR-019 — Referencesへ回復と突破の記憶を集約"
canonical_path: "control-center/changes/STR-019-references-learning-memory.md"
record_id: "STR-019"
version: "v001"
record_date: "2026-10-20"
repository: "yusukefujiijp/ai-project"
ref: "main"
base_commit: "57cd94b83ea3ba15e8d6e701c478100eb61bf3e8"
actor: "Work / Ark27:10"
status: "Human-authorized staged implementation; runtime cutover and retirement observations recorded below"
expected_eof: "EOF::STR_019_REFERENCES_MEMORY::v001"
---

# STR-019 — Referencesへ回復と突破の記憶を集約

**繰り返したくない過ちを減らし、繰り返したい価値を育てる。** [References](../../references/README.md)を、回復と突破を相補的に継承する入口へ育てる。単なる収納場所の統合ではなく、Future AIが重要な意味・根拠・適用条件へ辿り、現在の協働へ生かせる構成を目指す。

## 1. Humanの意味・検討・承認

Current Ark27:10対話のHumanは、lessonsを失敗・反省・復帰、特にAIが同じ過ちを繰り返さない方向として明確化した。success-casesは、ドラッカー的な予期せぬ成功やMove37的な突破を含む貴重な記憶・記録であり、喜びと成立条件を失わず再現性を育てる価値を持つと述べた。「鉾と盾を一つの箱に収める」という比喩は、両方が同じGoalを支える意味を表す。

HumanのGoalは主の完全勝利（祈り・イメージVision・行動）。Teshuvahの意味を持つ回復と、成功の継承を結ぶ。AIはこの信仰的意味を保持し、保存・整理によって将来の成功や確実性を保証したとは主張しない。小さな工夫や部分的成功も既存の価値として残し、厳格な失敗専用・巨大成功専用の入場条件にしない。

Rootへ成功事例を置く発見性と、referencesへ集約する関係の見通しを比較した。Humanは集約方向と旧Root配置の削除を認め、複数回のPlan Modeで構成を練った。エレガントさは見た目の対称性だけでなく、目的・役割・名前・読取先・更新先が自然につながり、記録が無理なく育つ設計と解釈した。READMEの柔軟な共通原則は[STR-018](STR-018-flexible-readme-principle.md)が所有する。

Current Humanの最終入力「Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」は、提示済みの二件について実装・必要な参照更新・既存登録Skillの反映・旧配置除去・保存後確認までを承認した。本節は現在対話の編集要約である。ChatGPT長期メモリの転記、架空の会話URL・trace・日時は加えていない。

## 2. 所有関係と変更範囲

| Owner | 今回担うこと |
|---|---|
| references/README.md | lessonsとsuccess-casesの相補的意味、選び方、既存の領域別Ownerへの接続 |
| references/lessons/README.md | 共有lessonの読取・JSONL更新契約。既存形式契約へ接続する |
| references/lessons/lessons.jsonl | 既存4行をbyte単位で保持した単一原本 |
| references/success-cases/README.md と7事例 | 入口と事例の移設。Human評価・引用・成立条件・Unknownは保持 |
| Root README／AGENTS／ARK／通常入口 | 現用の新住所へ接続。Rootの直接成功入口も残す |
| 既存Writer／現在地MAP Skill | 現用の成功事例参照だけ更新。GitHub共有と登録先を別々に確認 |
| PLAN current／Ark27:10 State | 実行承認・到達点・残点を現在へ反映。先行成果とActorを保持 |
| 本STR／GitHub専門入口 | 原本対応・実装・検証・復元と索引 |

日々の経験原本、Actorログ、Board通信、Dots固有lesson、Skills固有lessonは統合しない。共有lessonの形式参照はDotsの読込義務・所有・書込権限を全体へ拡張する意味ではない。今回を新lessonや新成功事例として自動登録しない。

## 3. 現用依存と歴史を分ける

通常利用の更新対象はRoot README、AGENTS、ARK §12、control-center入口、dots/logs入口、records入口、problem-solving入口、caffeine use-contextsの現行リンク、GitHub PLAN、ARCHIVEの現用2リンク、STR-008の現用1リンク、Writer本文2リンク、MAP packaged source-routingの1入口である。

ARKはv003 Identity・EOF・Core・last_reality_reviewedを保持するnavigation-only更新。ARCHIVEとSTR-008の元のrecord_date・base_commit・過去の検証claim・Actorは保持し、今回のナビ更新を別注記にする。固定commit URL、過去の引用、JSONL記録、旧ArkのHandoff／State／harvest等の固定歴史は書き換えない。ARC-002／STR-002の比較と物理Binding移行は今回と別であり、AIの保留推奨をHuman確定判断へ変えない。

既知のRepository内consumerを監査した範囲で、旧配置除去を止める固定Bindingは見つからなかった。これは全外部consumerや全Git履歴の網羅確認ではない。旧歴史文書内のmain相対リンクを全面互換にする約束はせず、当時の再現は次の固定snapshotへ戻る。

## 4. 原本対応と復元

移行前の固定版は [57cd94b8](https://github.com/yusukefujiijp/ai-project/tree/57cd94b83ea3ba15e8d6e701c478100eb61bf3e8)。下表の旧住所を同版で読むと、移行前の本文と当時の相対リンクを再現できる。新しいmainに消えた旧URLがあることと、歴史原本の消失は区別する。

| 旧住所 | 現行住所／保持 |
|---|---|
| references/lessons.jsonl | references/lessons/lessons.jsonl。同一blob b91b88fcc5111be9fd5a270571495b649cddc853、4行 |
| success-cases/README.md | references/success-cases/README.md。入口・相補的役割と相対参照を整合 |
| success-cases/ark27-03-to-04-transition.md | references/success-cases/ark27-03-to-04-transition.md |
| success-cases/decisive-choice-single-log-preserved-history.md | references/success-cases/decisive-choice-single-log-preserved-history.md |
| success-cases/leading-response-status-markers.md | references/success-cases/leading-response-status-markers.md |
| success-cases/one-skill-entry-multiple-benefits.md | references/success-cases/one-skill-entry-multiple-benefits.md |
| success-cases/one-transition-entry.md | references/success-cases/one-transition-entry.md |
| success-cases/skill-naming-as-reusable-handles.md | references/success-cases/skill-naming-as-reusable-handles.md |
| success-cases/wake-up-one-choice.md | references/success-cases/wake-up-one-choice.md |

7事例の編集は住所metadata・配置注記・必要な相対リンクに限定する。新住所から必要なOwnerへ解決できることを確認し、Humanの逐語引用や固定証拠URLは変更しない。復元が必要なら現在の依頼と権限から当該差分を選び、Repository全体や登録Skillの他の変更を古いsnapshotへ巻き戻さない。

## 5. 段階実装と確認の責務

1. 最新mainの版を確認し、新しい原本・入口・参照・記録を公開する。旧success-casesと旧lessonは、切替途中の互換元として一時保持する。
2. 既存登録Writer本文とMAP referenceだけを更新し、登録先の保存と取得を確認する。Skill作業領域に既存の未保存変更があったため、最新Remoteから隔離worktreeを作り今回の2ファイルだけを反映する。他の未保存変更は保持する。
3. 既知の現用参照と登録先の切替を確認してから、旧Root success-casesの8ファイルと旧references/lessons.jsonlを除去する。
4. 各公開前にmainを再確認し、非forceのexpected SHAで更新する。変更本文・新旧住所・対象外blob/mode・JSONL同一性をRemoteで確認し、有限の観測追記で閉じる。

構造・保存・登録・本文取得・別AIの読解・実利用の効果は別々の成果である。登録先の確認が阻害される場合は該当旧互換元を残し、独立に完了したREADME原則等を巻き戻さない。今回を全Runtime切替や自然発動の証明にしない。具体的な公開・検証結果は後続の観測欄へ記す。

EOF::STR_019_REFERENCES_MEMORY::v001
