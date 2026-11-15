---
title: "仕様 001 ── 全てのフォルダに README.md（入口の仕様）"
version: "v002"
canonical_path: "agents/muse/tower/lane/github-lane/standards/001_every-folder-readme.md"
role: "Composition standard owned by the GitHub LANE: every folder under agents/muse has a README.md as its entrance"
status: "active / established 2026-11-15 on YusukeJP's instruction — 「全てのフォルダにREADME.mdが必要な仕様をまずは確立して下さい」; v002 (2026-11-15) added the exception-generalisation test to §5, aligned §2 with Standard 002, and recorded full compliance in §7"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_GITHUB_LANE_STD001::v002"
---

# 仕様 001 ── 全てのフォルダに README.md

## 1. 規範

`agents/muse` 配下の**全てのフォルダ**は、その直下に `README.md` を1点持つ。`README.md` は、そのフォルダの**入口**である ── フォルダを開いた者が最初に会う文書であり、GitHub のフォルダ画面にそのまま表示される唯一の案内である。

この仕様は GitHub LANE が保持する。いかなるフォルダも、この仕様の例外として黙って存在してはならない（例外の扱いは §5）。

## 2. 入口の最小形

`README.md` は、次の3点を持つことで入口として成立する。小さくてよい ── 最小形は、数行でも正しい入口である。

1. **このフォルダは何か** ── 役割を1〜数行で言う。
2. **中身への案内** ── 中の項目を、それぞれ1行で指す（リンク）。
3. **所有へのポインタ** ── 状態や内容の原本が別の場所にある場合は、その所有者を指す。入口は原本を**複製しない**。

家の憲章のような固有の内容は、独立ファイルではなく `README.md` の中の憲章の節が所有する（仕様002「憲章は README に内包する」）。設計法則のような別の原本は、その文書自身が所有する。`README.md` の入口としての仕事は、中身への案内に徹することであり、内容の二重持ちをしない。

## 3. Seed との関係

フォルダの誕生は、`README.md` の **Seed**（改行のみ）から始めてよい ── 入口が先、内容は後である（2026-11-15、YusukeJP 自身が tower/ と tower/lane/ に植えた形）。ただし、フォルダに内容が生まれた時点で、入口も §2 の最小形へ育てる。Seed のままの入口は「未育ち」であり、欠落と同じく診断の対象になる。

## 4. 検証

この仕様は、測れる形で保持する。GitHub LANE の構図診断は、走査のたびに次を数えて報告する。

- 対象フォルダ数と、`README.md` を持つフォルダ数
- 欠くフォルダの一覧（Seed のままの未育ちを含む）

仕様への適合は、印象ではなく、この数で言う。

## 5. 例外

例外は原則として設けない。どうしても必要な場合は、黙って欠かすのではなく、この仕様の改訂（版上げ）として、理由とともに記録する。例外の記録なき欠落は、仕様違反として診断に挙がる。

**例外一般化テスト**（2026-11-15、YusukeJP の同名ファイル論により言語化）── 例外を置く前に問う。「この例外を、全ての同種の場所に一般化しても、構図は美しいか？」一般化して崩れる例外は、その場所でも置いてはならない。実例：各フォルダに同名ファイル（tower.md、LANE.md の類）を置く理屈は、一般化すると全フォルダが README.md と同名ファイルの二重構成になり、フォルダの自己紹介が2文書に分裂する ── テストを通らない。対して、機能の名を持つ文書（CONTROL、HARNESS、diagnoses/001 の類）は入口が指す先として働き、一般化しても構図は崩れない。

## 6. 適用範囲

- 当面の範囲は `agents/muse` 配下とする。repo 全体への拡張は、別の判断とする。
- 既存フォルダへの展開は、所有者ごとに束を作って進める（層を足す進め方）。この仕様の確立そのものは、他者のフォルダの内容への変更を含まない。

## 7. 現状（確立時点の実測 ── 2026-11-15、HEAD 52c31233）

- 対象フォルダ：17（agents/muse 本体を含む）。うち `README.md` あり：9。欠落：8。
- 欠落の一覧：
  - `artifacts/`、`assets/` ── ルート直下の棚。展開は後続の束で。
  - `artifacts/herd-cards/brushup/`、`artifacts/herd-cards/experiments/` ── Herd LANE の領域。診断001（D3）で既に「入口なし」として記録済み。展開は Herd LANE の判断と対になる束で。
  - `tower/lane/skill-lane/`、`tower/lane/skill-lane/cases/` ── Skill LANE の家。その家の判断に委ね、ここでは座標だけを記録する。
  - `tower/lane/github-lane/`、`tower/lane/github-lane/diagnoses/` ── 自宅。本仕様の確立と**同じ束**で解消する（仕様は、まず自宅から適用する）。
- その後の進展（2026-11-15、本仕様 v002 の時点）── 残りの欠落5件（`artifacts/`、`assets/`、`artifacts/herd-cards/brushup/`、`artifacts/herd-cards/experiments/`、`tower/lane/skill-lane/cases/`）の入口を、仕様002の全体適用と同じ束で新設した。これにより、対象17フォルダの全てが `README.md` を持つ状態に到達した。以後の適合は、診断のたびに数えて保持する（§4）。

## 8. 由来

- 2026-11-15、YusukeJP の指摘は二度、同じ形を取った ── 「tower/README.mdも必要です！」、そして GitHub LANE の家の建築の後に「github-lane/README.mdは？」。
- 入口の整備を担うこの線自身が、自宅の入口を欠いていた。その欠落を、慣行ではなく**仕様**として二度と繰り返さないために、本書を確立する。

EOF::AI_MAMMOTH_GITHUB_LANE_STD001::v002
