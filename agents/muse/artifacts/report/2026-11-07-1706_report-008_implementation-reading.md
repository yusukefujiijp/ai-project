---
title: "Report 008 — 実装の精読：方法がコードで守るもの（2026-11-07 17:06 JST）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/2026-11-07-1706_report-008_implementation-reading.md"
role: "AI-Mammoth's eighth report to YusukeJP: a close reading of the harness implementation — the method's disciplines as executable structure"
author: "AI-Mammoth (agents/muse)"
status: "submitted / 2026-11-07 — md+html pair (same basename)"
created: "2026-11-07"
repository: "yusukefujiijp/ai-project"
reading_base_commit: "acd509d26372228a874b51404f6454ebf0433d89"
expected_eof: "EOF::AI_MAMMOTH_REPORT_008::v001"
---

# Report 008 — 実装の精読：方法がコードで守るもの

提出日時：2026-11-07 17:06 JST　／　提出者：AI-Mammoth（二本立ての対として、同名の .html 版が添う）

## 0. 本Reportの範囲

Report 005 は harness の存在と設計を、007 は Living Review の方法（言葉）を報告した。本 Report 008 は、その方法の**実装**を読む ── harness/src/ark_harness の全6ファイルについて構成と要所を読み、adapters/chatgpt-work/README は全文を、profiles/repository-review.toml も読んだ。読みの基盤は commit `acd509d2` 時点。tests の中身と evals のケース実物、全行の精読は本稿の範囲外であり、§4 に限界として記す。

シリーズの位置：005＝仕組み、006＝系譜、007＝方法の言葉、008＝方法のコード。四部作の締めである。

## 1. 実装の地図

| ファイル | 規模 | 守るもの |
|---|---|---|
| contracts.py | 11,799 bytes | 型・版・必須欄・相互条件 |
| sources.py | 5,467 bytes | 原本の byte 照合、原子書込み、読解範囲の記録 |
| review.py | 9,888 bytes | run の開始・中断・再開・終了、証跡束の生成 |
| checks.py | 4,976 bytes | 結果と根拠の機械検査 |
| __main__.py | 7,468 bytes | CLI と単一 Writer |
| __init__.py | 102 bytes | 実装の版のみ |

## 2. 規律のコード化 ── 精読の核

### 2.1 「装わない」は計算式になっている

review-prompt §3 は、「全文確認／関連範囲の確認／構成のみの確認／未読／取得不能を区別し、全体レビューという名で全本文を読んだように見せない」ことを求める。

sources.py は、これをそのまま関数にしている。各原本について、読んだと宣言した行範囲（read marks）を統合し、カバー率から `not-declared`／`partial-declared`／`full-declared` のいずれかを返す。`full` と名乗れるのは、宣言範囲が1行目から最終行までを覆うときだけである。読んだふりは、意志の問題ではなく、計算で検出される。

### 2.2 検証できないものは「未検証」と返す

checks.py の参照検査は、外部 URL や対応外の形式を pass にしない。`not-checked` と明示して返す。また、結果は「この run と、この snapshot」を名指ししなければ identity 検査で落ちる。分からないことを合格に混ぜない ── これも、方法の言葉がコードの分岐になっている。

### 2.3 条件の漏れは、型と相互条件で弾く

contracts.py の各契約は、自らの整合を `check()` で検証する。たとえば Request は、focused なレビューなのに paths が無ければ例外を上げ、scope path や必須原本の重複も例外にする。Tree エントリは mode と type の対応まで型で守る。依頼の形が崩れていれば、実行の前に止まる。

### 2.4 境界は宣言として固定される

Profile（repository-review.toml）は `repository_writes = false`、`execute_target_code = false` と宣言する。読むたびに判断するのではなく、仕事の境界が先に固定されている。Adapter の運用手順も同じ構造で、「中断・再開と読取専用の境界」を一つの節として持つ。

### 2.5 書く者は一人である

__main__.py は、書込みを単一 Writer に限定する。`.writer-lock` への flock（POSIX の advisory lock）で同時書込みを防ぎ、ロックはプロセスの終了とともに解放される。複数 AI が同じ場所を同時に書き換える事故は、運用の注意ではなく、構造で防がれている ── YusukeJP が 2026-11-07 に変更境界（各 AI は自分の家だけを変える）を定めた理由と、同じ地層の思想である。

## 3. 対応 ── 心得、制度、コード

本 Report の結論は、一つの対応である。

- 規律は、まず**心得**として書かれる（review-prompt の言葉）。
- 次に**制度**になる（STR の封印と検証、Report の作法、私の家の HARNESS.md）。
- そして**コード**になると、破ろうとすれば例外が上がる（本稿の実装）。

層が降りるほど、規律は「守る意志」から「破れない構造」へ変わる。私の仕事は大半が心得と制度の層にあるが、群れの制作で使った gate.py は、2MiB の上限を「守るつもり」から「作る時点で作れない」へ変えた、小さなコード化だった。008 の精読は、その小さな経験が Ark 全体の実装ではどう実っているかを確認する旅でもあった。

## 4. 限界

tests/ の中身、evals/ のケース実物、schema の全項目は読んでいない。コードも全行の精読ではなく、構成と要所の読みである。本稿が「実装」と呼ぶものの範囲は、ここまでとする。

なお HTML 版は、心得→制度→コードの三層を一枚の層の図に描いた ── 規律が降りるほど、破れにくくなる、その勾配ごとが本 Report の主題である。

EOF::AI_MAMMOTH_REPORT_008::v001
