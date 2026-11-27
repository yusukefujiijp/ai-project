---
title: "Case 004 ── skills/ の生きた参照の初監査（記録）"
version: "v002"
canonical_path: "agents/muse/tower/lane/skill-lane/cases/004_skills-living-reference-audit.md"
role: "Audit record for the Skill LANE: the first living-reference audit of the repository's skills/ — scope, method, findings and boundaries. This case records an audit; it contains no repair"
status: "completed — audit executed 2026-11-16 in the Skill LANE on YusukeJP's seal (no fossil-family defects found); recorded 2026-11-27 in the Case 004 documentation bundle on YusukeJP's seal; v002 (2026-11-27, Case 005): annotated correction of the audited skill count in §1 (47 was a miscount; 49 files were fetched and scanned) and a supplement (§7) recording the stage-2 audit and the Hub observation"
created: "2026-11-27"
updated: "2026-11-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE_CASE_004::v002"
---

# Case 004 ── skills/ の生きた参照の初監査（記録）

修繕の案件ではない。監査そのものの記録である ── Case 001（yomiyasu-switch の版の化石化）と同じ家族の欠陥が、Skill LANE の本来の持ち場である repo の skills/ 本体に潜んでいないかを、初めて全件で確かめた。その結果と、確かめ方の境界を、ここに残す。

## 1. 監査の範囲と方法（事実）

- 対象は、repo の skills/ 配下にある 47 のスキルの、各 SKILL.md である。
- 方法 ── GitHub のコード検索は repo 単位ではなく全体検索であり、この監査には使えない（path:skills の結果は他 repo のものだった）。そのため 47 件全てをファイル単位で直接取得し、URL・40桁のコミット SHA・版番号（semver）・「固定／pin」の言い回しを機械的に抽出して、人手で分類した。

> **注記（2026-11-27、Case 005 による訂正）** ── 本節の「47」（対象の数と、取得した数の2箇所）は数え違いである。実際に取得・走査した SKILL.md は 49 件だった。監査の実質（全件の走査と、欠陥0件の結論）は変わらない。原文は当時の記録として保持し、訂正はこの注記と §7 追補が所有する。数の照合の経緯は [cases/005](005_case004-count-correction.md) が保持する。
- あわせて前段として、agents/muse の引用の棚卸しの最終走査を行った ── artifacts 配下の全体（Report 001〜011 の HTML 対を含む）で「2.5.0」「8つの問い」「第11問」は 0 件、experiments の設計文書2件は全文を読んで該当なし。これで agents/muse の棚卸しは全域で閉じた。

## 2. 結果（事実）

- **化石の家族の欠陥は、0 件だった。** 外部の原本の版を、規範として固定して引いている SKILL.md は無い。
- 参照の圧倒的多数は、この repo 内の共有原本への `/blob/main/` の現行 URL である ── つまり生きた参照だった。
- コミット SHA で固定された URL は 4 件だけあり、全て意図的な「過去の証拠」へのポインタだった。
  - ark-recall-portal ── 改名前の確認済み本文（blob/5746930c…）。旧 Identity・固定 Binding の確認用であり、「この案内だけで旧 Binding の条件を満たしたとはしない」という留保が本文にある。
  - write-ark-markdown ── 同じ型（blob/47d0d3ce…）。改名前の確認済み本文への案内と、移行を意味しない旨の明記がある。
  - map-ark-current-position ── 改名の移行入口そのもの。旧名と遷移先の Identity を区別して記録する役目のファイルである。
  - resolve-github-runtime ── 「代替記録」と明記された固定版へのポインタ（blob/51cb5718…）。
- この二重の規則 ── 現在の契約は現行 URL から、過去の証拠は固定版から ── は、複数のスキルが自分で文にしていた。load の「Current 契約は現行 URL から確認し、過去の証拠は固定版から読む」をはじめ、board、embed-reference-pillars、write-text が同型の規律を持つ。
- 外部への参照の判定 ── yomiyasu-switch の nanaism/yomiyasu は生きた参照のモデルそのもの（Case 001 で改訂済み）。ark-okf-responder の Google の OKF 仕様は現行 URL で引き、「使う時に版を明らかにする」指示を伴い健全。markdown-to-html の Mermaid の「審査済みの pin されたバンドル」は、依存を取り込む作法であり仕様の固定とは別家族。write-social-post の「twitter-text（tested with 3.1.0）」は時点つきの試験記録であり、再利用／導入への分岐を伴うため規範的な固定ではない。chatgpt.com 等のサービス URL は入口であり、版のある原本ではない。
- 「固定」への言及の多くは、「固定しない」という形の、固定を禁じる規律の文だった。

## 3. 解釈

- yomiyasu-switch の化石は、この家の作法の例外だった。skills/ の家はもともと生きた参照で建っており、だからこそ 1 件の化石は音もなく埋もれ、人間の問い（「3 になってないか？」）だけがそれを検出した ── Case 001 の構図が、監査によって裏づけられた。
- 固定が正しい場所もある ── 過去の証拠と、審査済みの依存である。この監査の物差しは「固定の有無」ではなく、「現在の契約を、古い版へ固定していないか」である。

## 4. 境界（未確認）

- skills/README.md（索引）、skills/__archives（定義上、凍結が正しい場所）、skills/_grok、skills/_references、および各スキル内の SKILL.md 以外のファイルは、行単位の監査に入れていない。
- SHA 固定の 4 件は、引用する側の文脈から分類した。固定先の本文そのものは、この監査では開いていない。

## 5. 結論と、この記録の実行

- 修繕すべきものは無かったため、修繕の Case は起こさない。この監査の記録そのものが、本 Case の成果物である。
- 本書は 2026-11-27、YusukeJP の封印を受けた Case 004 バンドル（文書のみ）で新設された。同じ束で、家の README と cases/README は v004 へ進み、CONTROL は v022 へ進んだ ── CONTROL v022 には、§3 の Skill LANE 行への本監査の追随に加えて、TOWER から折り込まれた §3 統括マップの 3 行追加（pstack LANE・Ark-Coaching LANE・Inbox LANE）が含まれる。折り込みの経緯は CONTROL §5 の v022 の条が所有する。

## 6. 検証

- 本書を含む束の全ファイルは、push の後に読み戻し、blob SHA の一致を確認する（その結果は、本書ではなく、封印への完了報告が保持する ── 本書は push の中身の一部であり、自分自身の検証結果を自分の中に書けないためである）。

## 7. 追補（2026-11-27 ── 第2段監査と、数の訂正）

第1段で境界として残した範囲を、第2段で閉じた。その記録と、本書 §1 の数の訂正を、ここに併せて残す。

- **範囲（事実）** ── skills/README.md（Hub 索引そのもの）、skills/_references、skills/_grok、および各スキルフォルダ内の SKILL.md 以外のファイル。対象ファイルは、現在のスキルフォルダ54件と _references・_grok を合わせて 203 件。そのうちテキストファイル 136 件を全て取得して走査した。残る境界は非テキストの7件（アイコン、フォント、CSS、および拡張子の選別から外れた scripts/count_x_post.cjs の1件）である。
- **結果（事実）** ── 化石の家族の欠陥は、第2段でも 0 件だった。各スキルの README は形成・確認の記録であり、固定された commit・blob は全て日付のある確認の証拠だった。移管前の Hub の固定版は「移管前」と明記された移植の出典であり、how と why の README が引く cursor/plugins の固定 commit は、派生の出典の記録である。記録の中の Hub の件数（38／39／40／42／46件）は、各時点の Hub の更新履歴と一致した。
- **数の訂正（事実）** ── 第1段で実際に取得・走査した SKILL.md は 49 件であり、本書 §1 の「47」は Skill LANE 自身の数え違いだった。第2段の数の照合（フォルダの実数と、取得したファイルの実数と、索引の定義の突き合わせ）で検出した。訂正は注記つきの形で行い（§1 の注記）、生きている要約（家の README の現在地、cases/README の一覧）からは数を外した。正確な数は、日付とともに本追補が所有する ── 監査時点（2026-11-16）のスキルフォルダは 49 件、本追補の時点（2026-11-27）では 54 件である。
- **Hub の観察（事実と未確認）** ── Hub の「掲載する共有Skillは48件」は、フォルダ数ではなく掲載件数であり、旧名の移行入口3件を数えない定義が本文にある。2026-11-25 の更新時点では、フォルダ51件 − 入口3件 ＝ 48件で正確だった。現在はフォルダ54件に対し、critical-review、feedback-wait、japanese-quality-protocol の3件が Hub に一度も現れない（54 − 3 − 48 ＝ 3 で、この3件と一致する）。この3件が採用済みで更新待ちなのか、採用前の下書きなのかは、本レーンからは確認できない。Hub の保守はスキル側の作法に属するため、本書では観察として記録するに留める（YusukeJP の判断事項として提示済み）。

EOF::AI_MAMMOTH_SKILL_LANE_CASE_004::v002
