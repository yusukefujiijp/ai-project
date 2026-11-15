---
title: "仕様 002 ── 憲章は README に内包する（LANE.md の廃止）"
version: "v001"
canonical_path: "agents/muse/tower/lane/github-lane/standards/002_charter-inside-readme.md"
role: "Composition standard owned by the GitHub LANE: a lane house keeps one root document — its README, with the charter as a section inside it"
status: "active / established 2026-11-15 on YusukeJP's decision (KISS), superseding the GitHub LANE's own earlier recommendation to keep LANE.md separate"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_GITHUB_LANE_STD002::v001"
---

# 仕様 002 ── 憲章は README に内包する

## 1. 規範

レーンの**家**は、その直下に置く文書を `README.md` **1点だけ**とする。憲章は、独立した `LANE.md` としては置かず、その README の中の「憲章」の節として**内包**する。

- README の入口の節 ── その家は何か、中身への案内、所有へのポインタ（仕様001の最小形）。
- README の憲章の節 ── 役割、仕事の作法、境界、読み順、現在地。
- ファイルは1つ、節ごとに責任は1つ。入口と憲章の二重持ち（同じ役割を2ファイルに書くこと）をしない。

棚フォルダ（家の中の diagnoses/、standards/、cases/ など）は、従来どおり README（入口）のみを持ち、憲章は持たない。

## 2. 根拠

この家の基礎原則（HARNESS §0）が物差しである ── **Simple is best!**、そして **KISS / DRY / YAGNI / Lean / SRP**。原則は、新しいファイル・仕組み・節を足す前に立ち止まって当てるための関門として置かれている（HARNESS §0 の確認行）。

入口と憲章を2ファイルに分ける設計は、その関門を通らなかった ── 家ごとに文書が2つになり、役割の記述が重なり、読む者は2か所を行き来する。1ファイルに節で分ける方が、単純で、重なりがなく、保守が容易である。2026-11-15、YusukeJP はこの原則をもって、分離案を退け、内包を定めた。

## 3. 置き換えの記録

- 本仕様に先立ち、GitHub LANE は「入口は場所に属し、憲章は住人に属する」として LANE.md の存続を推奨した（2026-11-15 の構造化）。その推奨は、YusukeJP の「いや（No）、LANE.mdはREADME.mdに内包して下さい！」という決定により、ここに置き換えられたことを記録する。推奨の検討自体は無駄ではなかった ── 内包後も、入口の節と憲章の節を混ぜないという節の分離は、その検討から残ったものである。

## 4. 適用

- **即時適用（2026-11-15、本仕様の確立と同じ束）** ── tower/lane の2家：`tower/lane/github-lane/`、`tower/lane/skill-lane/`。両家とも README に憲章を内包し、LANE.md を削除した。
- **追随（移行の作法による）** ── artifacts/ の旧2家（`artifacts/report/`、`artifacts/herd-cards/`）と、canon 側の文言（HARNESS §9 の「レーン憲章（LANE.md）」という形、CONTROL §3 の LANE.md へのポインタ群）は、各家の移行束と TOWER の canon 改訂として、別途追随する。本仕様の確立は、それらを黙って変更しない ── 残存の一覧は §5 に記録し、診断が数え続ける。

## 5. 検証

GitHub LANE の構図診断は、走査のたびに次を数えて報告する。

- 独立した `LANE.md` の残存数と、その住所（追随の完了まで、残存は「未移行」として記録され、違反とは呼ばない ── 移行は各部の作法による）。

EOF::AI_MAMMOTH_GITHUB_LANE_STD002::v001
