---
title: "House — 家・生活空間の整理とCare"
version: "v001-human-authorized"
canonical_path: "control-center/house/README.md"
repository: "yusukefujiijp/ai-project"
role: "Physical living-space domain entry / route to adopted areas and retain deferred possibilities"
created: "2026-10-20"
origin: "Human-created blank seed in 2026-10-06; home renamed house to avoid homepage ambiguity"
status: "room-care entry prepared; other areas remain candidates"
expected_eof: "EOF::HOUSE_DOMAIN_ENTRY::v001-human-authorized"
---

# House — 家・生活空間の整理とCare

家・居室などの物理的な生活空間について、現在の目的に合う領域へつなぐ入口。最初に具体化するのは[room-care](room-care/README.md)である。現在の居室の状態や全生活Taskをここで一括管理しない。

## 形成と今回の選択

Humanが改行のみの入口を作り、homepageとの紛らわしさから `home` を `house` へ訂正した形成は、[Control Center](../README.md)と[STR-013](../changes/STR-013-github-plan-and-archive-relocation.md)が所有する。[具体化前の固定Seed](https://github.com/yusukefujiijp/ai-project/blob/97ae0d8c492f2009ad9d523600545aedf2d6cf61/control-center/house/README.md)は改行のみだった。

その後、Humanは居室専用Projectに `house` は広すぎると指摘し、`room-care` を高く評価した。一方、house配下の別領域を考える実験から、親としてのhouseには有効な広がりがあると判断した。**広い親houseを保ち、最初の具体的な子をroom-careにする**。専門名を曖昧に戻す判断ではなく、異なる範囲を異なる名前に分けた選択である。

Humanは家・生活空間の課題に多くの共通項があると見ている。この再利用の可能性は保持するが、YusukeJPの実践前に全ての人へ有効な方法だとは認定しない。

## 現在の接続

| Node | Edge | 役割・状態 |
|---|---|---|
| [room-care](room-care/README.md) | 居室の困りごと → 片付け・清掃・整理整頓・維持改善 | 現在採用した最初の領域。目的・形成理由・実践上の判断を所有 |
| [Ark101: room-care](../../ark-project/ark100-199/ark101_room-care/README.md) | 専門Projectでの協働 → room-careの現実 | Projectの入口・instructions・起動Promptを所有。居室の実践資料はroom-careへ |
| [Control Center](../README.md) | 整理する対象 → 専門領域 | 共通の整理目的と対象別の案内。houseをGitHub整理の子案件にしない |

## 保留する派生案

`daily-flow`（家での生活の流れ）、`supplies`（消耗品・在庫）、`maintenance`（設備の維持）、`laundry`（洗濯）、`indoor-environment`（室内環境）、`space-design`（空間設計）、`item-locations`（物の所在）、`emergency-readiness`（非常時の備え）は、探索で得たAI提案の候補名である。Humanは派生可能性を評価し、まずroom-careに集中することを選んだ。個々の候補の正式採用、独立フォルダ作成、同時Task開始は未確定である。

今はroom-careと重なる内容も、具体的な必要が出た時に既存資料で扱えるかを先に判断する。役割・更新主体・探しやすさに実益がある場合に分け、分類表を埋めるためだけの空フォルダは作らない。

## Evidenceと運用

ここにあるのは入口整備と採用方針であり、居室の改善・継続利用・一般化の実証ではない。後続Human入力、写真・説明、実行報告から現在を更新する。新規Repositoryは作らず、必要な成果はai-project内の担当資料へ接続する。Root・Human Authority・品質・Guardは[AGENTS](../../AGENTS.md)と[ARK](../../ARK.md)を保持する。

EOF::HOUSE_DOMAIN_ENTRY::v001-human-authorized
