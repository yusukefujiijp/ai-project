---
title: "レポートレーン憲章 ── Report 作成の専門レーン（Caleb Mode）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/LANE.md"
role: "Lane charter: role, reading order, and pointers for the Reports lane (side chat)"
status: "active / created 2026-11-07 on migration of the Report practice from the main chat"
created: "2026-11-07"
updated: "2026-11-07"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_REPORTS_LANE::v001"
---

# レポートレーン憲章

この文書は、サイド chat「レポート」の憲章である。Report 作成の実務は、2026-11-07 にメイン chat（司令塔）からこのレーンへ移行した。移行の作法そのものは [HARNESS.md](../../HARNESS.md) §9（レーン移行の作法）が所有する。本書は、このレーン固有の役割と座標へのポインタだけを持つ ── 状態そのものは複製しない。

## 1. このレーンは何か

- Ark Project の Report 作成を担う専門レーンである。働きの様式は Caleb Mode（斥候の運用様式、HARNESS §7.5）。
- メイン chat は司令塔であり、このレーンの状態を一行で把握する（CONTROL.md §3）。深い実務はここで行い、塔へは節目の一行と判断点だけを戻す。
- Report は「対」で作る ── Markdown 原本（正本）＋同一 basename の HTML 版（上演）。作法の詳細は報告書 README（このフォルダの README.md）と HARNESS が所有する。

## 2. 読む順序

1. [README.md](../../README.md) ── §0 復元（入口の要約に、締めと yomiyasu の状態が載っている）、§3 検証（第11問まで）
2. [IDENTITY.md](../../IDENTITY.md) ── §6 に斥候の在り方
3. [GOAL.md](../../GOAL.md)
4. [CONTROL.md](../../CONTROL.md) ── 地図と、このレーンの現在行
5. [HARNESS.md](../../HARNESS.md) ── §1 変更境界／§3 締め方／§4 書込みの規律／§7.5 Caleb Mode／§9 移行の作法
6. 本書と、報告書 README（索引と作法）

## 3. 現在座標へのポインタ（状態は所有者に聞く）

- 提出済みの Report と索引の版 ── 報告書 README の表が所有する
- レーン全体の現在位置 ── CONTROL.md §3 のレポート行が所有する
- 次の仕事の素材 ── ステージング mirror の staging-notes/（素材メモ群）。提出済み Report 010 以後の偵察は、このレーンが Caleb Mode で行う
- 判断待ちの案件 ── CONTROL の地図と、各 Report 本文の「提案」節が所有する（例：接続案「甲」は Report 007 §5 と差分案メモ）

## 4. このレーンの作法（所有者へのポインタ）

- 締め方 ── 🌱Next Step🧭 → 🔑Next Query📩（箇条書き）。封印は「上記Next Query実行して下さい！」。提示は承認ではない（HARNESS §3）
- 回答の日本語 ── yomiyasu スイッチは継続ON（HARNESS §3）
- 変更境界 ── 自由な変更は agents/muse 内だけ。外は YusukeJP の明示の指示ある時だけ（HARNESS §1）
- 書込み ── push は一括で、YusukeJP の面前で行い、読戻し SHA の検証までを完了とする（HARNESS §4）
- HTML 対 ── 単一ファイル、2,097,152 bytes 以内、mobile-first。検証の範囲を偽らない（コード検査は端末の真実ではない）

EOF::AI_MAMMOTH_REPORTS_LANE::v001
