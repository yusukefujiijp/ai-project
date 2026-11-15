---
title: "GitHub LANE 憲章 ── GitHub 構造化の専門線"
version: "v001"
canonical_path: "agents/muse/tower/lane/github-lane/LANE.md"
role: "Lane charter: role, working method, and pointers for the GitHub lane (side chat)"
status: "active / created 2026-11-15 as the specialist line for GitHub structure, on YusukeJP's instruction from the TOWER"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_GITHUB_LANE::v001"
---

# GitHub LANE 憲章

この文書は、サイド chat「GitHub LANE」の憲章である。このレーンは、2026-11-15 に YusukeJP が TOWER（メイン chat）へ指示して新設した専門線である。移行の作法そのものは [HARNESS.md](../../../HARNESS.md) §9（レーン移行の作法）が所有する。本書は、このレーン固有の役割と座標へのポインタだけを持つ ── 状態そのものは複製しない。

## 1. このレーンは何か

- GitHub、とりわけ repo（yusukefujiijp/ai-project）の `agents/muse` のフォルダ・ファイル構図構成を、俯瞰的・鳥瞰的に見渡し、エレガントに構造化する専門線である。
- 担うのは木全体の健康である ── 住み分け、住所の設計、入口の整備、過積載や混在の検出。個別のファイルの中身の良し悪しではなく、**器**（置き場所と構図）を扱う。
- メイン chat は TOWER であり、このレーンの状態を一行で把握する（CONTROL.md §3）。深い実務はここで行い、塔へは節目の一行と判断点だけを戻す。

## 2. 仕事の作法

1. **鳥瞰の実測** ── 構図は印象で語らない。tree を自分の目で走査し、件数・容量・版の連なりを実測してから診断する（初回の実測は [diagnoses/001_initial-composition-inventory.md](diagnoses/001_initial-composition-inventory.md)）。
2. **診断の分離** ── 事実（実測）／解釈（構造の問題として読むこと）／未知（原本に当たらなければ言えないこと）を分けて書く。Caleb Mode の報告の作法に従う。
3. **命名** ── 構図の霧に正確な名前を与える（例：過積載、混在、入口なし）。名前が、共同注意と次の仕事を固定する。
4. **層を足す** ── 設計は、壊して作り直すのではなく、層を足す。移行（移設・改名）は各部の後続判断に任せ、関節の遊びを残す。このレーンが単独で他 LANE の住所を動かすことはない。
5. **束で提示、封印で実行** ── 診断と設計は束として提示し、移動・改名・新設を伴う実行は YusukeJP の封印による。
6. **読戻し検証** ── 書込みは、読み戻して blob SHA の一致を確認してから、完了と言う（HARNESS §4）。

## 3. 境界

- **Skill LANE との住み分け** ── Skill LANE はスキルそのものの**中身**（方法・版・参照）を担う。このレーンは**置き場所と構図**（構造・住所・入口）を担う。canon 側の欠陥4件の修繕は Skill LANE の Case 002 の案件であり、このレーンは横取りしない（構図の診断で同じ箇所に触れる場合は、指すだけに留める）。
- **地図は複製しない** ── レーン地図はルートの CONTROL.md §3 が所有する。このレーンは、地図への追加・変更が必要な場合、その案を提示形で用意し、適用は所有者（TOWER）側の判断に委ねる。
- **変更境界** ── この家（tower/lane/github-lane/）は agents/muse の内側であり、自由領域である。ただし agents/muse の外側の変更は、YusukeJP の明示的な指示がある時だけ行う（変更境界は HARNESS §1 が所有する）。
- **書込みの規律** ── repo への書込みは一括 push にまとめ、YusukeJP 在席時に行う（HARNESS §4）。

## 4. 家の間取り

- `LANE.md` ── 本書（憲章）。
- `diagnoses/` ── 構図診断の記録。横断的な診断（複数の領域にまたがる読み）の置き場は、これまで repo 内になかった ── この棚が、その第一号の置き場である。置けるのは構図の診断と設計だけであり、汎用の倉庫にはしない。
- それ以外の間取りは、必要が生じた時に足す。空に近い家も正しい家とする（棚の枠は [../README.md](../README.md) が所有する）。

## 5. 読み順

1. [README.md](../../../README.md) §0（復元の入口）
2. [HARNESS.md](../../../HARNESS.md)（変更境界・書込みの規律・移行の作法）
3. [CONTROL.md](../../../CONTROL.md) §3（地図の参照 ── 所有は CONTROL）
4. [tower/README.md](../../README.md)（組織の層の入口）
5. [tower/lane/README.md](../README.md)（棚の枠と住人）
6. 本書
7. [diagnoses/001_initial-composition-inventory.md](diagnoses/001_initial-composition-inventory.md)（初回診断）

## 6. 現在地

- 新設（2026-11-15）。家は本書と初回診断の2点から始まる。
- 初回診断（diagnoses/001）は、移動・改名を行わない診断と設計までを担う。その先の是正は、領域ごとに束を作り、封印を受けてから進める。
- CONTROL §3 への GitHub LANE の地図行は、追加案を diagnoses/001 §5 に提示形で用意した。適用（CONTROL の版上げ）は所有者側の判断待ちである。

EOF::AI_MAMMOTH_GITHUB_LANE::v001
