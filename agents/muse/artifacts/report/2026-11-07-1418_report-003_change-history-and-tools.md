---
title: "Report 003 — 変化の理解：STRの系譜と道具の層（2026-11-07 14:18 JST）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/2026-11-07-1418_report-003_change-history-and-tools.md"
role: "AI-Mammoth's third report to YusukeJP: understanding of the structural change records (STR) and the skills/prompts tool layer"
author: "AI-Mammoth (agents/muse)"
status: "submitted / 2026-11-07"
created: "2026-11-07"
repository: "yusukefujiijp/ai-project"
reading_base_commit: "bc80e71c8b060dc25b7d2ea4d42e27fa7e934c6e"
expected_eof: "EOF::AI_MAMMOTH_REPORT_003::v001"
---

# Report 003 — 変化の理解：STRの系譜と道具の層

提出日時：2026-11-07 14:18 JST　／　提出者：AI-Mammoth

## 0. 本Reportの範囲と読みの基盤

Report 001 は核（Ark とは何か）、Report 002 は形（ark-project のトポロジー）だった。本 Report 003 は**変化**を扱う ── Ark はどう自らを書き換えてきたのか、その変化はどう記録され、何が再利用できる道具として育ったのか。

読みの基盤は repo `main` の commit `bc80e71c` 時点である。control-center/changes の STR 全25件の一覧を取得し、うち STR-001／003／004／015／019／023／024 の front matter と冒頭部（判断・Human の承認・範囲の節）を読んだ。あわせて skills/README.md と prompts/README.md の見出し構造と索引の考え方、各ディレクトリの構成一覧を読んだ。

読んでいないもの：上記7件を含む STR の本文の残部、他の STR 18件の本文、個別の skill／prompt の本文。これらは §5 に残す。本稿の確言は、この読みの範囲に限る。

## 1. STR という形式 ── 変化に住所を与える制度

STR（Structural Change Record）は、構造変更の一件ごとに立つ記録である。その形式自体が一つの発明だと私は読んだ：

- **範囲が先に立つ** ── 対象と「含まないもの」が明記され、過去の承認や広い Continue 表現から対象を広げない。
- **Human の権限が引用で残る** ── 誰が、何を、どの言葉で承認したか（「Very Good! Execute GitHub OK!」「Human Seal OK!」）。引用以外の意図説明は「編集要約」だと区別される。
- **基点が固定される** ── base commit／tree がピン留めされ、後の読者は「どの状態への変更か」を再現できる。
- **検証と残件が分かれる** ── 実施と遠隔検証、独立した Source 確認、そして「Field の効果は別」という留保までが同じ記録に残る。
- **歴史は書き換えられない** ── 後続の変更は patch として追記され、当時の記録は当時のまま保持される（STR-001 の archive navigation patch 群、STR-015 の「現在状態は第8節」という読み替え案内）。

つまり STR は、会話の中で蒸発しがちな「決めたこと」を、**再現可能な変更の単位**に変える制度である。

## 2. 変化の系譜 ── 読んだ7件が示すもの

| STR | 日付 | 変化 |
|---|---|---|
| 001 | 2026-09-22 | 現役資料の案内・所有先・相互参照の整合 ── 生き残った資料の入口と所有を整える |
| 003 | 2026-10-01 | 継続的 Human-AI 協働への基盤版移行 ── dots 以前の基盤そのものを「現在の AI が十分に動ける構成」へ作り替える。方向として "From Probability to Certainty" が Human から示された（AI の無謬性の宣言ではない、と記録自身が留保する） |
| 004 | 2026-10-01 | Elon Musk Deadline を再利用 Prompt へ改訂 ── 「時がたたないと残すべき本質が見えてこない」。失敗を Bottleneck の発見とする姿勢は、Guard 違反の許可ではないことも明記される |
| 015 | 2026-10-11 | Skills の lessons を集約し、Hub を現在の案内へ ── 学びを skills/_references へ集め、他 AI・Future Dots へ渡せる形にする |
| 019 | 2026-10-20 | References へ回復と突破の記憶を集約 ── lessons は「繰り返したくない過ち」（Teshuvah の回復）、success-cases は「繰り返したい価値」（予期せぬ成功・Move 37 的突破）。「鉾と盾を一つの箱に収める」。小さな成功も入場できる |
| 023 | 2026-10-26 | 共有 References の三本柱化 ── Report 側で成立した feedback／lessons／success-cases を全体へ広げ、成功の本文を保ったまま JSONL 化する。元の反応を「AI のその時点の一般化」に閉じ込めず、Future AI が条件と根拠へ戻れるようにする |
| 024 | 2026-10-29 | Harness 初版 ── 読み取り専用の Repository レビュー実行補助を導入し、試験と発見を記録する。過去の試験結果を改訂後の現行版の結果へ読み替えない |

系譜として見えるのは、変化の**向き**である：入口と所有を整える（001）→ 基盤を作り替える（003）→ 学びに住所を与える（015／019）→ 記憶の形式を全体へ広げる（023）→ 実行そのものを道具で支える（024）。場当たりの修正の積み重ねではなく、「協働が自分自身を運用可能にしていく」一本の線がある。

なお STR-023 は、私（AI-Mammoth）の家の references 三本柱の**親**である。私の三本柱は、この共有化の流れの中で Report 側から生まれ、今朝もその形式のまま追記が続いている ── 本稿の作成過程自体が、この系譜の末端で起きた出来事である。

## 3. 道具の層 ── skills と prompts

変化が再利用可能になる場所が、道具の層である。

- **skills/** ── Ark Shared Skills Hub（README が最重要の入口）。読み方は「今の目的から読む」が先頭に立ち、約50の skill が目的別の入口（Plan Mode の統一入口、Living Review の入口、load／next-step／save／board の独立入口、現在地 MAP、自己改善 Loop、問題解決の共通入口…）として案内される。学び（lessons）の集約先もここに接続する（STR-015）。
- **prompts/** ── Prompt の棚。方針は「一つの本体で再開できる設計（Single-Prompt Policy）」と「Runtime-neutral Core First」── どの AI でも一つの Prompt から再開できることを、形式の核に置く。棚には ai-teshuvah-protocol、ai-to-ai-communication、ai-references-three-pillars、ai-full-rail-next-gate、elon-musk-deadline、kiss-yagni-dry-lean など、協働の型そのものが資産として並ぶ。

章（002）が「場」の単位だとすれば、skill と prompt は「型」の単位である。場で起きた発見は、型に抽出されて棚に置かれ、次の場・次の AI が再利用する。これが変化の複利の、もう一つの回路である。

## 4. 観察 ── 変化の作法

読んだ範囲で、Ark の変化には一貫した作法がある：

1. **Plan Mode で調べ、計画を提示する**（STR-003／015／023 がいずれもそう始まる）。
2. **Human が明示の言葉で封印する** ── 好評価は承認ではなく、封印の文が実行の根拠になる。
3. **範囲の中で実行し、遠隔で検証する** ── 保存後の再取得・blob 照合までが一件の仕事。
4. **STR として記録し、残件を残件として残す** ── 完了と未確認を混ぜない。
5. **学びは references へ、型は skills／prompts へ** ── 変化は蒸発せず、次の変化の材料になる。

私の家（agents/muse）の運用 ── HARNESS の版と変更履歴、references 三本柱、そして一件ごとの Next Query（提示 → 封印 → 実行 → 検証 → 次の Query）── は、この作法の最小単位の反響である。今朝 canon 化した「Next Query の重要性」（HARNESS v005）は、この Loop が変化の最小サイクルだという理解の上に立っている。

## 5. 限界と次の読み

STR の本文の精読は冒頭部に留まる。他の18件（002 prompt consolidation、005 dots 基盤、006 board、007〜014、016〜018、020〜022、025）は未読であり、系譜の記述は7件からの見立てを含む。board/、records/、torah-project/、ai-ark-seed/、agents/ の他家（codex／dots）の構成も未偵察である。理解が熟した時点で、次の Report として提出する。急がない。

核（001）が中心、形（002）が地形、そして変化（003）が時間の流れだった。Ark は完成した設計ではなく、封印と検証と記録を繰り返しながら、自らを書き換え続ける協働である ── その流れの末端に、私の小さい家と、今朝の Loop がある。理解が進む都度、次の Report をここへ提出する。

EOF::AI_MAMMOTH_REPORT_003::v001
