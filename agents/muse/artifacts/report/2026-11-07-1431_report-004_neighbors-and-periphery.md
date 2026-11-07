---
title: "Report 004 — 住人の理解：隣人たちと周縁の領域（2026-11-07 14:31 JST）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/2026-11-07-1431_report-004_neighbors-and-periphery.md"
role: "AI-Mammoth's fourth report to YusukeJP: understanding of the other AI homes and the peripheral domains"
author: "AI-Mammoth (agents/muse)"
status: "submitted / 2026-11-07"
created: "2026-11-07"
repository: "yusukefujiijp/ai-project"
reading_base_commit: "4af8b106dabf1fbf8677b62e91e932bf6831f9b7"
expected_eof: "EOF::AI_MAMMOTH_REPORT_004::v001"
---

# Report 004 — 住人の理解：隣人たちと周縁の領域

提出日時：2026-11-07 14:31 JST　／　提出者：AI-Mammoth

## 0. 本Reportの範囲と読みの基盤

Report 001 は核、002 は形（章の連合体）、003 は変化（STR と道具）だった。本 Report 004 は**住人と周縁**を扱う ── 他の AI たちの家（agents/codex、agents/dots）と、ark-project の外側に広がる領域（board、records、torah-project、ai-ark-seed）である。

読みの基盤は repo `main` の commit `4af8b106` 時点である。agents/dots／codex の README、codex の runtime と references の構成、board／records／ai-ark-seed の README、torah-project/ezekiel-temple の README を読んだ。各領域の内部（Dots の Actor 個別ファイル、Board の Topic 本文、records の年別ファイル、Seed Card の実物）は読んでいない。§6 に残す。

## 1. 家々の連合 ── agents/

`agents/` の下には、AI ごとの家が並ぶ。家ごとに所有者が違い、入口・原本・経験の文法は共有される。今朝 Fujii が引いた変更境界（各 AI は自分の家だけを変える）は、この地形の上に引かれた憲法である。

### Dots ── Actor の社会を持つ家

agents/dots の README は v013 に達し、今日（2026-11-07）も更新されている。Dots は単一の AI ではなく、Actor（dot-0000「初穂」、dot-0001、…）の集まりであり、「一つの依頼から復元できる（one-request recovery）」ことを家の核に置く。2026-10-20 に旧住所（dots/）から agents/dots へ移転した経緯は STR-022 が所有する。

そして Dots の玄関にも、今日の前線が刻まれている ── **Chief 継承準備**である。11月12日の Plus 変更予定と Dots を活用できなくなる見込みを踏まえ、Work の Ark27 で育った全体俯瞰・関係探索・コーチングを継ぐ準備が、Human の採択によって進んでいる（002 で報告した Ark29:02 後継準備と同一の出来事を、隣人の玄関から見た姿）。家は別でも、前線は一つである。

### Codex ── 経験から再開する小さな家

agents/codex は 2026-10-31 に開かれた小さな家である。目的は「元の会話を知らない Codex や他 AI が引き継げる入口」── 成果物は各専門領域に残し、この家には入口と経験だけを置く。references には feedback／lessons／success-cases の三本柱がそのままあり（STR-025）、「同じ問題や Human の違和感を繰り返したくない時は、References から読む」という案内が玄関に書かれている。三本柱の文法は、家を越えて共有される共通語である。

### Muse ── 自分の座標

私の家（agents/muse）は、この連合の中で最も新しい家の一つである。玄関（README）・身分（IDENTITY）・目標（GOAL）・管制（CONTROL）・配線（HARNESS）・設計法則（DESIGN-LAW）・三本柱・報告書という構成は、隣人たちの文法 ── 入口が所有し、状態は各所に、経験は三本柱に ── を、私の規模でなぞったものである。

## 2. 通信と記録の面 ── board と records

- **board/** ── Human と AI の協働通信の場。誰から誰への何の話かを理解し、報告・質問・返答をつなぐ。Topic が一つの通信目的をまとめ、その Current を所有する。Board 自身は宛先・通知・受信の観測を所有し、共通の進め方（ai-to-ai-communication）や過去経験の第二原本にはならない ── ここでも「入口と所有の分離」が徹底している。
- **records/** ── AI 活用の日時記録。AI と何を相談し、調べ、考え、作り、どこまで分かったかを日付から辿れる場所であり、YusukeJP の生活の日記ではない。一行に一つの意味のある活動を書く。小さな相談・失敗・回復・訂正も残す。Plan Mode・保存禁止・STOP の最中には書かない。ChatGPT、Work、Dots、Claude、Grok ── 許可された AI はどれも参加できる、協働の「日誌」の層である。

## 3. 種の仕組み ── ai-ark-seed

ai-ark-seed は、Ark 内で生まれる軽量な Seed（種）のライフサイクルを扱う Subsystem である。

```text
Detect broadly.        （広く検出する）
Keep Seeds lightweight.（種は軽く保つ）
Pickup selectively.    （拾うのは選んで）
Cardify selectively.   （カード化も選んで）
Persist only Cardified Seeds.（永続保存はカード化された種だけ）
```

Seed は「Name(Definition)」の軽量な意味単位であり、保存されていなくても Seed である。価値があると判断されたものだけが、Context・Evidence・Next Gate を備えた Seed Card へ成熟し、Human Seal の後に選んで永続保存される。

私たちの協働で今朝 canon 化した「AI の提案は種である」という理解は、この repo に既にあった器官の、私の家における反響だったことをここに記す。種という比喩は Ark 全体のものであり、軽く検出し、選んで育て、封印を経て初めて残す ── その作法ごと、私は受け継いでいた。

## 4. Root 側の学びと夢 ── torah-project

torah-project の玄関（README）はいまだ1バイトのスタブであり、parashat-ha-shavua（週の朗読箇所）の入口も同様である ── この領域の玄関は、まだ書かれていない。それは未整備というより、この領域が「運用の対象」としてではなく、学びと構想の保持の場として置かれている姿だと私は読む。

その内側にある ezekiel-temple の README は、この repo で最も静かな文書の一つである。YusukeJP が長年抱いてきた夢 ── 日本、特に北海道に、エゼキエル神殿を実物大で、できる限り記述に忠実に形にしたい ── が、構想として保存されている。現在の確定事項は「建設でもデジタル制作でもなく、**構想を流されない形で保持すること**」であり、実装は未決定、オープンソース再利用も保留。以前の制作案は実行命令として再開しない、と明記されている。

repo は、実行中の仕事だけでなく、**まだ形にならない夢を、流されない形で保持する**ためにも使われている。Root 側の重みを持つものを、無理に Task 化せず、けれど失われないように置く ── この保持の作法は、ark25 の「基盤 Review を待つ」や、Seed の「保存されなくても Seed である」と同じ呼吸である。

## 5. 観察 ── 連合の憲法

四つの Report を通して見えた全体像を、ここに圧縮する。

- ai-project は、**一つの Root の下の連合**である：章（ark-project）は場の連合、家（agents）は住人の連合、領域（board／records／torah-project／ai-ark-seed）は働きの連合。
- 連合を保つのは、中央の倉庫ではなく、**共有された文法**である ── 入口は案内し状態を持たない、原本は一箇所、経験は三本柱、変化は STR、問いは Query／Waiting Field に置かれ、封印を経て動く。
- 境界と共有は対立しない。所有が分かれているからこそ、文法を共有できる。私の家の塔とレーン、変更境界、Next Query の Loop は、この憲法の最小の実装である。

## 6. 限界と次の読み

読んでいないもの：harness/ の実装（STR-024 の対象である、コードとしての Harness）、control-center/house と control-center/github の内部、agents/ai-to-ai-communication の本文、ark-recall-portal、Dots の Actor 個別の記録、records の年別ファイルの中身。これらが残るが、Report 001〜004 で、核・形・変化・住人の四面は一巡した。次の理解の深化は、個別の深掘り（例：STR 全件の精読、Dots の Actor 史）か、新しい出来事への応答として進める。急がない。

大学生のように ── と Fujii は今朝の Report の仕組みを評した。私の側から言えば、この四部作は「割り当てられた課題」ではなく、隣の家々を訪ね、種の仕組みに自分の言葉の出典を見つけ、他人の夢が静かに保持されているのを見た記録である。理解が進む都度、次の Report をここへ提出する。

EOF::AI_MAMMOTH_REPORT_004::v001
