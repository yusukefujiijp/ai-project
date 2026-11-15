---
title: "仕様 003 ── GitHub の認識は1束1回（承認の集約）"
version: "v001"
canonical_path: "agents/muse/tower/lane/github-lane/standards/003_one-bundle-one-recognition.md"
role: "Working standard of the GitHub LANE: minimise the number of approval recognitions a bundle costs the Human"
status: "active / established 2026-11-15 on YusukeJP's instruction — canonised inside the migration bundle push, at zero extra recognition cost"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_GITHUB_LANE_STD003::v001"
---

# 仕様 003 ── GitHub の認識は1束1回

## 1. 前提

GitHub への書込みは、設計上、呼び出しのたびに YusukeJP の承認（認識）を要し、承認カードは時間で失効する。YusukeJP は忙しい ── **認識の回数は、AI 側の工夫で減らす対象**であり、彼の時間はこの家で最も高価な資源である。本仕様は、その削減の作法を定める。

## 2. 規範

1. **書込みは1束1回** ── 1つの束の作成・更新は、全ファイルを `push_files` の1回に集約する。分割した push をしない。束を分ける判断は、内容の都合ではなく認識の都合でもう一度疑う。
2. **削除は設計で減らす** ── 削除（delete_file）は1ファイルにつき1認識が避けられない。だから、(a) 将来消える運命の一時ファイルを作らない（YAGNI）、(b) 削除は束の最後に連続して並べ、タップが一息で済む形にする、(c) 削除件数そのものを、内包・改名回避などの設計で減らす。
3. **準備は認識の外で全て済ませる** ── 読み取りの一括走査、ドラフトの完成、検証スクリプトの用意が整ってから、最初の書込みを呼ぶ。承認カードを失効させない ── 失効は、認識の二重払いである。
4. **検証は認識を消費しない** ── 読戻し検証は読み取り（承認不要）で一括1回に行う。検証のために書込みを呼ばない。
5. **数で報告する** ── 束の提示には、その束が要する認識の回数（＝ 1 ＋ 削除件数）を明記する。削除ゼロの束は、認識1回だけである。

## 3. 由来

- 2026-11-15、仕様002の束は、push 1回＋削除2回の計3認識を要し、その前段では承認カードの失効による再送まで起きた。同日、YusukeJP は「GitHub認識をできる限り一回にまとめるように工夫して下さい。忙しいからです」と定めた。本仕様は、その指示の canon 化である。

EOF::AI_MAMMOTH_GITHUB_LANE_STD003::v001
