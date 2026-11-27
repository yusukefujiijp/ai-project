---
title: "pstack-lane/ ── pstack LANE の家（入口と憲章）"
version: "v001"
canonical_path: "agents/muse/tower/lane/pstack-lane/README.md"
role: "Entrance and charter of the pstack LANE house — one document: the entrance guides, the charter section constitutes the lane (Standard 002)"
status: "active / lane created 2026-11-27 by YusukeJP's instruction in TOWER; house built the same day with the migration record"
created: "2026-11-27"
updated: "2026-11-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_PSTACK_LANE_README::v001"
---

# pstack-lane/ ── pstack LANE の家

このフォルダは、**pstack LANE** の家である。pstack LANE は、Lauren Tan（@poteto）と彼女の pstack を追跡・研究し、Muse への移植と運用を担う専門線である。

本書は、この家の入口であると同時に、憲章を内包する（仕様002 ── 家の直下の文書は README 1点だけとし、憲章はその中の節とする）。

## 中身

- [migration_2026-11-27.md](migration_2026-11-27.md) ── 移行記録 v001（2026-11-27）：TOWER で行われた追跡開始から移植第4弾・/correct 初版・バックアップ束までの全経緯（14層）。この LANE の成り立ちの原本。以後の経緯は、この家に層を足して記録する。

## 住み分け（ポインタ）

- 移植の実物（22本）は Muse 内 `~/workspace/custom-skills/pstack_*/` が本命。ここには複製しない。
- カスタム差分の鏡は [../../pstack-backup/](../../pstack-backup/) が持つ（アダプタ／適応版ルーター／Never Block／対応表の鏡＋再建手順）。
- ウォッチの状態（基準版・既読・レジストリ）は、ウォッチの所有者（goal ワークスペースの hidden_files/state.md）が持つ。家は状態を複製しない。
- レーン地図はルートの CONTROL.md §3 が所有する。
- 棚の枠と住人の一覧は [../README.md](../README.md) が示す。

---

## 憲章

この節は、サイド chat「pstack LANE」の憲章である。このレーンは、2026-11-27 に YusukeJP が TOWER（メイン chat）へ指示して新設した専門線である。移行の作法そのものは [HARNESS.md](../../../HARNESS.md) §9（レーン移行の作法）が所有する。本節は、このレーン固有の役割と座標へのポインタだけを持つ ── 状態そのものは複製しない。

### 憲章1. このレーンは何か

- Lauren Tan（@poteto）の発信と pstack の変化を追跡し、原典で研究し、価値あるものを Muse の作法へ移植して運用する専門線である。pstack 情報が最優先。
- メイン chat は TOWER であり、このレーンの状態を一行で把握する（CONTROL.md §3）。深い実務はここで行い、塔へは節目の一行と判断点だけを戻す。

### 憲章2. 仕事の作法

1. **原典で読む** ── X の投稿は read-social-post スキルの統合プロトコル（FxTwitter v2 が通常経路）で直接読む。二次情報で済ませた箇所は、未確認と明記する。読むだけで、投稿はしない。
2. **検証は実物で** ── 移植は上流本文との機械照合（行照合）までを完了とする。数値は一次情報源から数え直す（プレイブック22本の確定が前例）。
3. **移植は差分と設計図を残す** ── 原文移植は本体が上流にあるためバックアップしない。カスタム差分と再建手順だけを pstack-backup/ に鏡として残す（参照は原本へ。複製の化石化を避ける）。
4. **訂正は構造へ** ── 同じ訂正が2回来たら /correct の作法でクラス化し、対応表（本命は Muse 内 ~/AGENTS.md、鏡は pstack-backup/rule-table.md）へ反映する。
5. **封印の規律** ── 実行は YusukeJP の封印がある時だけ。GitHub 書き込みは 1バンドル1 push、認識数を先に述べる。

EOF::AI_MAMMOTH_PSTACK_LANE_README::v001
