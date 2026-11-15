---
title: "Case 002 ── canon 側の欠陥4件の修繕"
version: "v001"
canonical_path: "agents/muse/tower/lane/skill-lane/cases/002_canon-defects-repair.md"
role: "Case record for the Skill LANE: re-verification, design, execution and read-back verification of the four canon defects"
status: "completed 2026-11-15 in the Skill LANE — presented from TOWER under YusukeJP's seal, re-verified and designed in this lane, then executed on YusukeJP's further seal"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE_CASE_002::v001"
---

# Case 002 ── canon 側の欠陥4件の修繕

Skill LANE の最初の案件。モデルケース第1号（cases/001）の学び ── 「本体を直しても、引用側に化石が残る。引用の棚卸しまでが、一件の仕事である」── が、そのまま本件の出発点になった。

## 1. 検出と提示

- 欠陥4件は、2026-11-15 の朝、TOWER が agents/muse を独立に再読した際に検出し、補遺として YusukeJP へ提示した。
- その後、仕様002の統合（憲章は README に内包する）が GitHub LANE で完了し、欠陥4(b) の所在が artifacts/report/LANE.md から artifacts/report/README.md へ移った。統合の完了を待つ理由が消えたため、TOWER は「先に進める」と判断し、本件は YusukeJP の封印によって TOWER から Skill LANE へ提示された。
- 提示を受けた段の範囲は「再検証と設計まで」であり、書込みは行わなかった。修繕の実行は、設計を戻したうえで、あらためて YusukeJP の封印を受けた。

## 2. 再検証（基準点：HEAD 5fc0849e）

4件すべてが、現在の repo 原本に現存することを確認した。

1. **HARNESS §3 の yomiyasu 固定** ── HARNESS v010 §3 に「nanaism/yomiyasu v2.5.0（推敲の方法そのもの）」と固定されていた。引用の棚卸しとして agents/muse 全体を検索したところ、「2.5.0」の出現は、この規範文の固定と、cases/001 の歴史的記録（当時の事実の記録であり正当 ── 対象外）の2か所だけだった。
2. **CONTROL の版履歴の v013 重複** ── CONTROL v018 §5 に v013 が2件あった。1件目は Report 010 提出／三本柱 31・20・21、2件目は v016 の後に置かれた移行設計の条で lessons の数は 19。数の推移（18 → 19 → 20）は、2件目が本来は前の出来事を遅れて記録した条であることを示唆する（解釈であり、断定はしない）。
3. **CONCEPT.md の入口なし** ── agents/muse/CONCEPT.md（v001、仮説の定義）は実在するが、README v012 の Router に行がなかった。
4. **古い名前と数** ── (a) GOAL v002 §7 のグラフに「復元検証：8つの問い」。README §3 の問いは現在11問。(b) 旧名「レポート」は artifacts/report/README.md v015 の中に2か所 ── 憲章の節の冒頭「この文書は、サイド chat「レポート」の憲章である」（現在形の自己定義）と、Report 010 の索引行「移行後の「レポート」レーンで執筆された初号」（歴史の記述）。CONTROL §3 と HARNESS §7.5・§9 にもある「レポート」の用例は、いずれも 2026-11-07 当時の出来事の過去形の記録であり、当時の部屋名として正しいため、範囲外とした。

## 3. 設計と判断

- **欠陥1** ── HARNESS §3 の1文だけを外科的に差し替え、版の数字を canon から外して、生きた参照の定め（版は固定せず、正規の場所が宣言する版を使用時に確認し、新しい方を使う。所有は skills/yomiyasu-switch、最後に確認した版の記録は同 switch の last-confirmed.md）へのポインタに置く。
- **欠陥2** ── 版履歴は監査の跡であるため、付け替え・削除・移動は行わない。2件目の v013 の条へ注記を追加し、引用時の区別名を「v013（Report 010）」「v013（移行設計）」と定め、訂正の事実を新しい v019 の条に記録する（注記つき訂正）。
- **欠陥3** ── README の Router の GOAL の行の直後へ、CONCEPT.md への行を1行追加する。復元の読み順そのものは変えず、§3 の検証の問いは増やさない。
- **欠陥4a（判断事項1）** ── 甲案「11の問い」と数に直す案に対し、乙案「README §3 の問いに全て答えられるか」と数を持たないポインタ形を推奨し、採用した。問いの数は 8 → 10 → 11 と既に3回動いており、数の所有者は README §3 一か所だけにするのが、再発を構造で防ぐ形である。
- **欠陥4b（判断事項2）** ── 憲章の冒頭（現在形の自己定義）は「Report LANE」へ現行化する。あわせて、その上にある内包の注記（「憲章の本文は v001 のまま保持する ── 自己言及の2箇所だけを合わせた」）が事実とずれるため、部屋名の現行化を3箇所目として注記側も直す。Report 010 の索引行は甲案 ── 歴史として保持する。書かれた時点で「レポート」が正しい名前であり、直すことは欠陥2で禁じた「監査の跡の黙った書き換え」と同型になるためである。

## 4. 実行（YusukeJP の封印を受けて）

- 全ファイルを1回の push に集約した（仕様003 ── 1束1認識）。本書は、その push に含まれる。
- HARNESS v010 → v011（欠陥1 ── §3 の1文の差し替えと、版履歴への記録）
- CONTROL v018 → v019（欠陥2 ── 2件目の v013 への注記追加と、v019 の条による訂正の記録。§3 の地図そのものに変更はない）
- README v012 → v013（欠陥3 ── Router への CONCEPT.md の行の追加。あわせて本束の各ファイルの前進を相互記録した）
- GOAL v002 → v003（欠陥4a ── §7 グラフの復元検証ノードを、数を持たないポインタ形へ）
- artifacts/report/README v015 → v016（欠陥4b ── 憲章冒頭の部屋名の現行化と、内包の注記の連動修正。Report 010 の索引行は歴史として保持）
- 家の記録 ── 本書（cases/002）の新設、家の README v001 → v002（cases の一覧と憲章5「現在地」の現行化）、cases/README v001 → v002（一覧への 002 の追加）

## 5. 検証

- 読戻し検証 ── push の後に全ファイルを読み戻し、blob SHA が手元の原稿と一致することを確認した。
- grep による解消確認 ── HARNESS §3 の規範文に「2.5.0」の固定が無いこと／README の Router に CONCEPT.md の行があること／CONTROL の v013 が注記つきで2件とも残っていること／GOAL のグラフと report README の憲章冒頭が現行形であること。
- 保持の確認 ── cases/001 の歴史的記録中の「2.5.0」と、Report 010 の索引行の「レポート」は、設計どおり意図的に保持したものであり、欠陥の残存ではない。

## 6. 学び（一般化）

1. 変わる数（問いの数・版の数）は、所有者の外へ複製しない。ポインタで引けば、数は一か所でだけ生きる ── 生きた参照の原則は、版だけでなく数にも適用できる。
2. 監査の跡の訂正は「注記つき訂正」が形である ── 直すことと、直したことを記録することは、別の行為であり、両方要る。
3. 現在形の自己定義と、過去形の歴史の記述は、直し方が違う。同じ旧名でも、前者は現行化し、後者は保持する ── 時制が、判断の物差しになる。

EOF::AI_MAMMOTH_SKILL_LANE_CASE_002::v001
