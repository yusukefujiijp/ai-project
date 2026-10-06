---
title: "GitHub整理 — ai-projectの構造を理解し、改善を継承する"
version: "0.2.0"
canonical_path: "control-center/github/README.md"
role: "GitHub organization entry / route to the single plan, case records and originals"
status: "human-authorized domain entry and owner placement; actual reader and field effects separate"
repository: "yusukefujiijp/ai-project"
scope: "ai-project全体。ark-project/内だけに限定せず、他Repositoryへ自動拡張しない"
primary_reader: "Current AI / other AI / Future AI"
created: "2026-10-06"
updated: "2026-10-06"
change_record: "../changes/STR-013-github-plan-and-archive-relocation.md"
expected_eof: "EOF::AI_PROJECT_GITHUB_CONTROL_CENTER::v0.2.0"
---

# GitHub整理

**ai-projectの資料が、何のために存在し、今どこから使い、変更すると何へ影響するかを理解して改善する専門入口。**

現在の焦点・優先順位・残点は[GitHub整理PLAN](PLAN.md#current)、アーカイブ案件は[ARCHIVE](ARCHIVE.md)、通常の構造変更は[changes](#change-records)へ進む。PLAN・ARCHIVEの本文は本フォルダの単一原本。通常変更の記録は既存の`../changes/`へ接続する。旧PLAN・ARCHIVEの住所は案内のみを持ち、状態や本文を重ねて更新しない。共通の整理目的や別領域への接続は[親入口](../README.md)が所有する。

## 1. 依頼から担当資料を選ぶ

| Node | Edge | 判断すること |
|---|---|---|
| 次に何を整理するか | → [PLANの現在欄](PLAN.md#current) | Current Request、根拠、完了済み成果、実際の残点から選ぶ。候補の存在は実行承認ではない |
| この資料は必要か・退役できるか | → [ARCHIVE](ARCHIVE.md)の該当案件と実対象 | 現役価値、保存価値、依存、Human判断、戻し方を読む |
| なぜこの構成になったか | → [通常変更の記録](#change-records) | 誰が、いつ、何を、なぜ、どう変更・検証したかを辿る |
| 過去の原本を確認したい | → [__archives](../../__archives/README.md)・案件の固定証拠 | 今の案内と当時の本文を分ける。旧命令を自動実行しない |
| 時点を比較して診断したい | → [Repository Reviews](../../repository-reviews/README.md) | 日付付き観測とCurrent実体を比較する。古い診断を最新状態としない |
| 整理の方法を使いたい | → [Skills](../../skills/README.md)・[Prompts](../../prompts/README.md) | Plan Mode、Living Review、Graph等から必要な方法を選ぶ |

この構成は、Humanによるhomeの入口Seed作成と、GitHub専用原本を専門領域へ収める訂正を受けたもの。今回の対象・理由・検証は[STR-013](../changes/STR-013-github-plan-and-archive-relocation.md)へ。`../home/`は家の中を整理する兄弟領域であり、GitHubに記録されることだけを理由に本領域の配下や案件へ取り込まない。

本表は全件必読リストではない。指定されたHandoff・必須Sourceはその契約に従い、既知の案件へは直接進める。Root READMEはRepository入口、AGENTSは共通判断・権限、ARKはIdentity、Domain・Thread資料は各Currentを所有する。この専門入口へそれらを移管しない。

## 2. 整理で良くしたいこと

初期の「スパゲッティ」診断は、文書の進歩に、入口・現在地・保存先・役割変更の案内が揃って追随せず、読むAIが食い違いを解く箇所がある、というものだった。観測と反例は[PLANの診断履歴](PLAN.md#diagnosis-history)から辿れる。ファイル数や階層の浅さだけで良否を判定しない。

構造を変える時は、「案内する」「意味を所有する」「固定証拠として参照する」「由来になる」「変更に影響する」を区別する。アーカイブでは現役として使う案内を退役させ、なぜ存在し、なぜ保管したかへ戻れる接続を残す。通常の修正で済む問題、固定Bindingの移行が必要な問題、物理保管の案件を混同しない。

「不要」は現在の運用に残す必要がないという判断であり、歴史や知恵の無価値を意味しない。AIは具体的な対象・理由・影響・保存先・復元条件を調べ、現在有効なHuman承認の範囲で実装・検証まで担う。明確に承認された同じ範囲を再承認で止めない。詳しい権限・品質・中断復旧は[AGENTS](../../AGENTS.md)を使い、ここに別の契約を作らない。

方法・経験原本・成功事例・案件記録は役割が異なる。共有する知恵は元の所有先へ接続し、GitHub整理のために全経験を集め直さない。居室整理のような別対象も、記録媒体だけで本領域へ取り込まない。

## formation

### Player系から、このRepositoryの整理へ

以下は再編前の共通READMEで保持していた形成順序を引き継いだもの。文脈上の「今回」「現在」は各出来事の当時を示す。2026-10-06の後続訂正と新しい権限は[STR-012](../changes/STR-012-control-center-domain-entries.md)で区別する。

形成順序は、後の判断を変えるため残す。

1. Player系三Repositoryの分岐と、Living Reviewの成果を継承する場所が課題になった。統合の検討・改善を経て、YusukeJPは三Repositoryをアーカイブし、既存のArk等へ集中する方向を選んだ。
2. Humanは「まずアーカイブ」を優先し、手動で実施した。2026-09-22のGitHub metadata確認では、scenes-player-kit、shorts-player-kit、shorts-player-coreの三つとも `archived: true`。この確認は、その時点の観測である。
3. 継承先は当初の `ark-project/control-center/` 案から、**ai-project全体を見通すrootの `control-center/`** へHumanが訂正した。
4. Humanが[改行のみのREADMEを作成](https://github.com/yusukefujiijp/ai-project/commit/cc560d14284d99fd9b8a6e6aa896843e73b0c53d)。その後、他AI・Future AIの理解を最重要とし、READMEとPLANの役割を検討した。
5. Humanはさらに「どこがどうスパゲッティなのかの言語化」を最優先とした。調査・計画だけの段階を経て、READMEとPLANの初版をGitHubへ保存・検証した。
6. その後Humanは、案内の修復を先行させる初版計画を訂正し、不要な現役配置のアーカイブを優先した。
7. 既存の `__archives/` を利用し、AIの具体提案→YusukeJPの承認→実体移動→理由と結果の記録、という役割分担を明示した。記録は他AI・Future AIが深く理由と経緯を理解するために必要とされた。
8. この構成案の提示後、Humanの「早速、やってみましょう！」を受け、四文書の整備と最初の案件の具体化へ進んだ。個別の移動承認と実施結果はARCHIVEの案件が所有する。
9. Ark27:06でアーカイブを実施・確認した後、Humanは残す構成の修正改善ランキングを求めた。七候補への実行承認とともに、いつ・誰が・どこを・なぜ・どう直したかをFuture AIが理解できる記録を要求した。今回の具体的な範囲と結果は[STR-001](../changes/STR-001-navigation-and-ownership.md)へ接続する。

Player系で育った[control-centerの保存時点](https://github.com/yusukefujiijp/scenes-player-kit/tree/a0dc266a819e141040256f9afc4a70b6ff295ff9/control-center)は由来である。同資料の「現在の開発先」等はアーカイブ前の座標として読み、後のHuman判断と区別する。

この対話におけるSeedは、**目的・現在地・責務・未完了意図・採用済み秩序・次の一手を次のAIへ渡すこと**。Humanが述べた「一粒の麦」と「比喩的復活」は、この継承の意味を担う。保存できなかったレビューへの反省を、今回は読める根拠と改善計画へ接続する。Player系の開発再開や新Repository作成は、本入口の成立に必要な工程ではない。


## change-records

通常の構造変更の原本は既存の`control-center/changes/`。今回PLAN・ARCHIVEを移したことを、この記録群まで移したという意味にはしない。STR-009は現行Handoffの必須Sourceでもあり、原本群を一斉に動かす必要は今回の二原本整理にはない。日付付きの[整理指針](../20261003-cleanup-direction.md)も現在の住所を保つ。下記は所在と主題の索引であり、各記録の進捗を別々に更新する欄ではない。

- [STR-001: 案内と所有先の整合](../changes/STR-001-navigation-and-ownership.md)：2026-09-22の六修正群とD04分離設計。
- [STR-002: 単一Promptへの統合](../changes/STR-002-single-prompt-consolidation.md)：短期の起動利益と長期の二重管理負担を区別したHuman Correction、Query機能の移管、作成方針撤回、削除・検証・残る移行Gate。
- [STR-003: 継続協働基盤の明示版移行](../changes/STR-003-persistent-collaboration-foundation.md)：Currentと固定来歴の分離、章／07と共通基盤の改訂・保存・検証。旧Gateの成功へ読み替えない。
- [STR-004: Elon Musk DeadlineのPrompt改訂](../changes/STR-004-elon-musk-deadline-revision.md)：旧資料の核と形成史を保持し、締切・品質・完了判定・権限を現在の単一Promptへ整理した理由と検証。

- [STR-005: Dots協働基盤の初版](../changes/STR-005-dots-collaboration-foundation.md)：Current方向、dot-0000の身元、初穂の形成記録を役割分担して接続した理由・六パスの実装・検証。
- [STR-006: Board協働通信の初版](../changes/STR-006-board-communication-foundation.md)：初穂から既存Main／Supportへの紹介・全Session変更報告、宛先別の理解依頼、柔軟な実地Feedbackの入口と保存証拠。

- [STR-007: Dotsの学びの蓄積基盤](../changes/STR-007-dots-lessons-foundation.md)：Dots自身がBottleneck・失敗・回復・方法から学び、Future Dotsへ条件と根拠を渡す最小JSON、読取・保守契約、初期2件の由来。

- [STR-008: Actorログと形成史の保管](../changes/STR-008-actor-logs-and-preserved-history.md)：一つの現役ログ領域、JSONL契約、ARC-008の同一原本保管、判断の成功事例、検証範囲。

- [STR-009: 管理行なしlesson JSONLの採用](../changes/STR-009-headerless-lessons-adoption.md)：同じ2件の意味を保持したschema 2移行、専用フォルダの読取・更新契約、UUID方針と検証境界。

- [STR-010: 全AI横断のAI活用日時記録](../changes/STR-010-cross-ai-daily-records.md)：日別JSONLの用途・粒度・save接続と、既存原本を複製しない設計・確認範囲。

- [STR-011: Prompt棚と現行権限契約の整合](../changes/STR-011-prompt-shelf-authority-alignment.md)：Humanの意味・権限と委任可能な中継・結果統合を分け、mainの正本性と作業方法・公開権限を現行AGENTSへ接続した理由・変更・検証。

- [STR-012: 整理対象別の入口と現在の判断盤面](../changes/STR-012-control-center-domain-entries.md)：共通入口・GitHub専門入口・既存PLANの役割分離、Human Correction、保存と検証の証拠。


- [STR-013: GitHub計画・アーカイブ台帳の専門領域への移設](../changes/STR-013-github-plan-and-archive-relocation.md)：homeのSeedを受けた領域分離、二原本と旧住所の案内、意味・参照・並行変更の保持。

[ARCHIVE](ARCHIVE.md)はARC案件の提案・承認・実施・確認・復元を所有し、[__archives](../../__archives/README.md)は保管実体を案内する。両者の役割を通常変更記録へ重複させない。通信のCurrentは該当Board Topic、Actorの出来事はActorログ、再利用する学びは適用されるlesson契約など、実対象のOwnerを保つ。

## 3. 変更と確認を次のAIへ渡す

役割・案内・形成理由が変われば入口、現在の診断・選択条件が変わればPLAN、個別の承認・実施・確認は該当ARC／STRを更新する。Git履歴は正確な差分・時刻を、案件記録は意味・Human Correction・根拠・残存制約を担う。時点付きのレビューを新しいCurrentで塗り替えない。

保存時には対象・参照・必要なmetadata／EOFを確認し、書込後の実体をRemoteから再取得する。文書の存在、内容の整合、別AIの理解、利用効果は別の成果である。元会話なしに、現在の目的、最新の重要なCorrection／STOP、成果と証拠、未完了／Unknown、次の確認条件を根拠付きで説明できることを目指す。これは全作業へ追加するBoot試験ではない。

現在構成を上限にしない再設計の余地は[PLANの再設計接続](PLAN.md#redesign)へ。物理移設や資料分割は、具体的な読みづらさ・更新責務・契約への影響から判断できる。必要性がまだないフォルダ・方法論・台帳を先に増やさない。新しいModelへの期待や文書保存だけで、構成の優越性・全AIへの有効性を認定しない。

Root・Teshuvah・Human Foreground One・HumanのCorrection／STOP／Final SealとGuardを保持する。AI・GitHub・この入口はKeliであり、Rootや王座ではない。

EOF::AI_PROJECT_GITHUB_CONTROL_CENTER::v0.2.0
