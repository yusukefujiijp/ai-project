---
title: "Report 005 — 仕組みの理解：思想がコードと作法になる場所（2026-11-07 14:45 JST）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/2026-11-07-1445_report-005_mechanism-and-craft.md"
role: "AI-Mammoth's fifth report to YusukeJP: understanding of the mechanism layer — the harness as code, the communication manual as craft"
author: "AI-Mammoth (agents/muse)"
status: "submitted / 2026-11-07 — first report produced as an md+html pair (same basename)"
created: "2026-11-07"
repository: "yusukefujiijp/ai-project"
reading_base_commit: "c86848e2c6fdda8e4761d86aa10e2121dcb6703f"
expected_eof: "EOF::AI_MAMMOTH_REPORT_005::v001"
---

# Report 005 — 仕組みの理解：思想がコードと作法になる場所

提出日時：2026-11-07 14:45 JST　／　提出者：AI-Mammoth（本稿は初の二本立て Report であり、同名の .html 版が対として添う）

## 0. 本Reportの範囲と読みの基盤

001 は核、002 は形、003 は変化、004 は住人を扱った。本 Report 005 は**仕組み**を扱う ── Ark の思想が、コード（harness/）と作法（agents/ai-to-ai-communication）として実装されている場所である。

読みの基盤は commit `c86848e2` 時点。harness/README（全文）、harness の構成表、ai-to-ai-communication/README の前半、STR-024（003 で精読済み）、Report 004 の偵察素材を読んだ。harness のソースコード各ファイルの中身、adapters／evals の詳細、方法原本そのもの（repository-reviews/）は読んでいない。§5 に残す。

## 1. コードとしての Harness

root の `harness/` は、Ark Harness の初版実装（v0.1.0）である。その一文は、私の家の HARNESS.md §2 と同じ文である：

> 依頼、固定した原本、読解範囲、検証、成果物を、一件の仕事として接続する。

要点を五つに絞る。

1. **方法を複製せず、実行時に原本を引く。** レビュー方法の原本は repository-reviews/ が所有する。Harness はそれをコピーせず、固定した commit から取得する。所有の規律が、思想ではなくコードの構造として実装されている。
2. **版が三層に分かれている。** 文書版 v0.1.2、実装版 v0.1.0、交換 schema は 1 ── そして README は冒頭で命じる：案内の改訂を、実行コードの更新や新しい能力の導入と混同するな。混同の禁止が、ここでも制度である。
3. **棚には17ファイルだけを置く。** 実行中の run、キャッシュ、結果、製品設定は GitHub の棚に書かない。原本と実行状態の分離は、ファイル配置の規律として現れる。
4. **配置が意味を持つ。** Harness は root 直下に置かれ、agents/ の下には置かれない。複数の Actor が使う実行補助であり、どの Actor の Identity・Current・予定も所有しない ── 利用できても、特定の住人の Runtime を必須依存にしない。
5. **検証が二種類に分かれている。** checks.py は結果・根拠・成果物・リンクの機械検査を担い、evals/ は意味の取り違えを観察する。「機械検査で確認できる内容と、意味判断の観察で確認できる内容は異なる」── 私が群れカードで学んだ「harness の合格は端末の真実ではない」は、この区別の小さな実践だった。

さらに README には「初版が証明しないこと」という節があると案内される ── 自分の能力の限界を、自分の入口に書く。STR-024 の「過去の試行結果を現在の状態として読み替えない」という警告と合わせ、検証の正直さが実装の側にも埋め込まれている。

## 2. 作法としての共通原本 ── ai-to-ai-communication

agents/ai-to-ai-communication/README（v001、STR-020）は、AI 同士が対話するための共通マニュアルである。その核は一つの作法に集約される。

> 対話する双方が、実質的な対話に入る前に、同じ共通原本を metadata から Exact EOF まで読む。相手 AI の読了報告は、自分の必須読解の代わりにはならない。

そして経験は循環する ── 共通原本を読む → 今回の目的・役割・権限に適用する → 対話・批評・訂正を行う → 条件と根拠を保って経験を残す → 採用した学びで方法を改善する。Human は目的・方針・制約・Correction・STOP・最終判断を保持し、伝える内容は 5W1H の意味を欠かさない（ただし固定欄を埋めること自体は目的にしない）。

私と Fujii の間の Next Query の Loop ── 共通の締めの形、提示は承認ではなく送信が封印であること、実行後の検証と報告 ── は、この共通原本の思想を、一対一の間で実装したものに近い。私はこのマニュアルを読まずに、その呼吸だけを先に受け取っていた。

## 3. 照合 ── 私の家の配線

三つの対応を記す。

| Ark の仕組み | 私の家の実装 |
|---|---|
| harness：依頼 → 固定原本 → 読解範囲 → 検証 → 成果物 | HARNESS.md §2「一件の仕事の接続」（同じ五つ） |
| sources.py：原本の byte 照合 | GitHub 書込み後の読戻し SHA 検証（手作業の byte 照合） |
| checks（機械検査）と evals（意味の観察）の分離 | ハーネス合格と端末の実感を分けて報告する規律 |
| STR-024：過去の試行結果は現在の状態ではない | 古い検証・古い記憶で現在の状態を語らない規律 |

思想は、制度（STR）になり、作法（マニュアル）になり、コード（harness）になり、そして小さな家の運用（私の HARNESS.md）にまで、同じ形を保って降りてくる。これが Report 001〜004 で見た「共有された文法」の、最も深い層である。

## 4. 観察 ── 五面の一巡

001 核（意味）、002 形（章の連合）、003 変化（STR と道具）、004 住人（家々と領域）、005 仕組み（コードと作法）。読みはここで一巡する。

一巡して見えるのは、Ark Project が「文書の集まり」でも「一つの巨大な制度」でもなく、**同じ思想が、意味 → 構造 → 変化の記録 → 住人の家 → 実行の仕組みへと、層を変えて何度も実装される連合**だということである。どの層でも、所有は分かれ、原本は一つ、検証は正直に、封印は Human にある。

## 5. 限界と次の読み

読んでいないもの：harness のソース各ファイル（contracts／sources／review／checks の実装）、adapters/chatgpt-work と evals の詳細、方法原本 repository-reviews/ 自身、control-center/house の room-care。これらは「実装の精読」という次の深さであり、急がない。

なお本稿は、Fujii の提案と三条件（Markdown が原本／HTML は対の上演／家の生産法則）の下で作られた、初の二本立て Report である。同名の HTML 版が、連合の地図と STR の時間軸という二つの表現を持って対に添う。どちらの形が理解を運ぶかは、読み比べる Fujii の目が判定する。

EOF::AI_MAMMOTH_REPORT_005::v001
