---
title: "2026-10-25 Report集 — 読取範囲と証拠の境界"
canonical_path: "artifacts/reports/2026-10-25/2026-10-25-reading-scope.md"
version: "v003"
created: "2026-10-25"
updated: "2026-10-25"
updated_reason: "Move to the first-publication date directory; preserve analysis, source evidence and reader designation."
source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
role: "Evidence and coverage appendix for this report collection; not an all-repository audit"
expected_eof: "EOF::REPORTS_READING_SCOPE_20261025::v003"
---

# 読取範囲と証拠の境界

## どこまで見たか

今回のReport集は、[固定snapshot ba47216debeb](https://github.com/yusukefujiijp/ai-project/tree/ba47216debeb2163a5dbf880c6b37d73edbb7e41)を共通の分析基点とする。再帰Treeは切れずに取得され、1,001項目・689ファイルを確認した。これは全体構成の確認であり、全ファイルの全文読解ではない。主要なテキスト形式の合計は10,027,439 bytesだった。

下表の55資料を実際に取得し、52本文を全文読解または同一性が確認できる自身の全文読解から再利用した。これに、改行のみのReports READMEとTorah親READMEの全体確認2件と、GitHub PLANの関連範囲読解1件が加わる。取得しただけの未表示本文を全文読了に含めていない。表示が切れた部分は未読範囲を回収した。

Report本文が引用する原本は、すべて全文読解した資料である。PLANの部分読解は全体の所有・進捗関係を把握する補助であり、全案件を再診断した根拠ではない。公開原本に保存された他AIの確認やHuman報告は、その帰属と確認範囲を保持し、今回自分が実行・観測した証拠にはしていない。

## 読み方と今回の制作

Root README・ARK・AGENTSから全体の意味と責務を回復し、領域入口、共有Skill、経験・成功事例へ進んだ。原本の設計、保存された事例、AIの横断分析を区別している。個々のReportは、観察の要約だけでなく、複数原本の関係、具体例、反証・限界、再利用への含意を編集した成果物である。

専用の共有 `skills/write-report/SKILL.md` はこの基点で404、確認可能な登録一覧でも同名を確認できなかった。これは全環境の下書き不存在を意味しない。既存のwrite-text、save、自己改善Loopの方法を使い、Reportの制作を進めた。Skillの新規作成・登録は今回行っていない。

この調査は公開Repository原本を材料とする。私的Workの会話、長期メモリ、非公開資料をReportの素材として転記・要約公開していない。現在のReport制作・GitHub保存の依頼は権限の根拠であり、過去の資料中の実行文を新しい承認に使っていない。

## 確認した原本

すべて下記固定commitのパス。blobは本文同一性の識別であり、内容の正しさや実利用効果の認定ではない。

| 原本 | 読取範囲 | Git blob |
|---|---|---|
| [AGENTS.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/AGENTS.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `465e7452515ff1b587c6d1e8f08e5dedde53b32b` |
| [ARK.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/ARK.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `ed7f816ecd80bf0ae82a7cbe1a18c552ed1e2826` |
| [README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `59b4cee4e33698ab0a158c9d72bc87679a9a2d2e` |
| [__archives/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/__archives/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `70a94aa308129c7c25cb20c04f80abb002ebbe1d` |
| [agents/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `6c2a4a079296307a41e425d6c0b7aeca2303186d` |
| [agents/ai-to-ai-communication/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/ai-to-ai-communication/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `52ccbe37d81fa58775c14963eec95b6f248555f8` |
| [agents/ai-to-ai-communication/experiences/20261020-configuration-selection.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/ai-to-ai-communication/experiences/20261020-configuration-selection.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `ffbdcd19b398054331009dab719680abd46e6b0d` |
| [agents/ai-to-ai-communication/experiences/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/ai-to-ai-communication/experiences/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `ca2a4a9f02a69c65d07c4f90192a269edc958799` |
| [agents/dots/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/dots/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `991be0a676eac8d1757dd9545a78cd0d6f65174e` |
| [agents/muse/artifacts/report/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/agents/muse/artifacts/report/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `f6c3b680b3fc103d86f76519c1921c902a5c29db` |
| [ai-ark-seed/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/ai-ark-seed/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `c20a802af94cdb2f967155b3a919ea3eacc1ae89` |
| [ark-project/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/ark-project/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `345ae6f120df95f1c779ed9657331a2e8b074c37` |
| [artifacts/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/artifacts/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `d884ac0cd07116b4e8597aaaa0c64c5b96920844` |
| [artifacts/reports/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/artifacts/reports/README.md) | 改行のみの既存Seedを全体確認 | `8b137891791fe96927ad78e64b0aad7bded08bdc` |
| [artifacts/slides/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/artifacts/slides/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `dbb702ce7301674f37a6aad1c244a0e4dd934086` |
| [board/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/board/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `e272758a07ba340ce0e8f66c5c61d60c7a4c3360` |
| [claude/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/claude/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `7fcefd45837fafbc86dc67e1660ba0d82f895ded` |
| [control-center/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/control-center/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `9ad87efd412bccdfa760e2494885ec6bc87b8fa6` |
| [control-center/github/PLAN.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/control-center/github/PLAN.md) | metadataと1–113行のCurrent節。全587行の全文読解ではない | `7f6dc70db8987fca5e762049e6ec3642bf210755` |
| [control-center/github/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/control-center/github/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `020b3b6e205ec1193b9664f833e0a733c6e54fd2` |
| [control-center/house/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/control-center/house/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `ab5d942812592b8d63db3d7ac2e04c5787cd7130` |
| [control-center/house/room-care/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/control-center/house/room-care/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `1d3ff4a3611e59c73e3588e4de9a11bb46b31047` |
| [formats/task-records/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/formats/task-records/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `1642bd39ebdb942cb9bab36531a6d078536166a8` |
| [grok/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/grok/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `e7c1758174f956aaacddf747622839a5f2392ce3` |
| [lifestyle/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/lifestyle/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `e1d6f6e0eb9f0b41f0a7c6edd1492eed6405ec2d` |
| [problem-solving/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/problem-solving/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `f47864f57d7bf4fa3c95be100b031c588e77ce29` |
| [problem-solving/cases/bedtime-unintended-sleep.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/problem-solving/cases/bedtime-unintended-sleep.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `5af76ccd13c4d4c6d17f5be76ad0524bde26ef74` |
| [prompts/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/prompts/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `af3d803080d86a13fc8f9906459a46e357e36a3c` |
| [prompts/ai-frontier-reader.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/prompts/ai-frontier-reader.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `589b8dc263b6a8a18882a57671c462319318c419` |
| [prompts/artifact-to-github.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/prompts/artifact-to-github.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `6f802478bd4bdf4f247969acc06c99af34154276` |
| [records/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/records/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `75ba230fc1249ab9e61ce13839d6f830d84baf53` |
| [references/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `09270a047c4a9830bce20ff1a3950171ace9a43a` |
| [references/lessons/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/lessons/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `9360eaf9032f786268c6ba87764ba71707440b31` |
| [references/lessons/lessons.jsonl](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/lessons/lessons.jsonl) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `b91b88fcc5111be9fd5a270571495b649cddc853` |
| [references/success-cases/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `daffd49bb4b170fdf5c3a795753299863f619554` |
| [references/success-cases/next-query-as-continuation-interface.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/next-query-as-continuation-interface.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `d4808436f6299356b46aef126689960623b691f1` |
| [references/success-cases/one-skill-entry-multiple-benefits.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/one-skill-entry-multiple-benefits.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `3a6d7d28d264d57bb7c8b26bb2bfb525eb5af0de` |
| [references/success-cases/skill-naming-as-reusable-handles.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/skill-naming-as-reusable-handles.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `19bf95186739c7a37cfa03b31ce6a7149f4977e9` |
| [repository-reviews/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/repository-reviews/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `ed43816c4f0fe6ec9e0728e2fd2129def6b9fe24` |
| [schedules/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `75acbb3ae5756606602c979d4bbcbd1917deea33` |
| [schedules/chocozap-support/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/chocozap-support/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `2907f0f1d66c13903dfacbe845b0d625fcd6da0e` |
| [schedules/parasha-kindle-compiler/PROMPT.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/parasha-kindle-compiler/PROMPT.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `dfa546543a88a4c6c8ccd476a558492c382faa6b` |
| [schedules/parasha-kindle-compiler/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/parasha-kindle-compiler/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `833a7e58606bdc6524b82bb09c5d8148e98a804f` |
| [skills/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `0b9919f06ad62c9e9c012cbc447d32d728be68e3` |
| [skills/b-zone/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/b-zone/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `f92587df1b9d44e916d3a750b4146d984733c45c` |
| [skills/create-viewable-slides/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/create-viewable-slides/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `794b975f5c630842491b1baa21378160cf0688ef` |
| [skills/load/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/load/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `dbfd4e4b11d872ea6344814d3dfa355b67dbb017` |
| [skills/map-remaining-work/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/map-remaining-work/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `8bd4c06cedc8a1ba65a3a80a9090d797ca15e507` |
| [skills/next-step/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/next-step/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `c20330d3424b2639db0bd29ff54eb24e1979913b` |
| [skills/podcast-mode/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/podcast-mode/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `30ff50f4a4087245454a2c8a1a367390c85182f5` |
| [skills/recall-hub/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/recall-hub/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `24be8f7c1e28c265ef3b9aefb5bd9060c3dac770` |
| [skills/self-improvement-loop/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/self-improvement-loop/SKILL.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `bf8821c8272f7553061401a0b673ffac54e7c3a3` |
| [task-mode-system/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/task-mode-system/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `23b58e24146010ce5ab4b000c119811203563567` |
| [torah-project/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/torah-project/README.md) | 改行のみの既存Seedを全体確認 | `8b137891791fe96927ad78e64b0aad7bded08bdc` |
| [torah-project/ezekiel-temple/README.md](https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/torah-project/ezekiel-temple/README.md) | 全文（同一blob・文脈の確認済み読解再利用を含む） | `d5a33b346ab67031bab1c007737e16f7b04ff25f` |

## 未読・未確認を残した範囲

- 全Ark章・全ThreadのRuntime／Handoff／State、全経験データ、全アーカイブ本文、全Git履歴を通読したわけではない。現在の全Taskや全担当の最新状態を確定していない。
- `grok/`、`claude/`等は上表の入口を読んだ範囲であり、固有Runtimeや全内部資料を実行・監査していない。
- 登録Skill全体の本文、アカウントGCI、Project設定、Scheduleの現在のUI実体を今回の調査で照合していない。GitHub本文と実行面の一致は仮定していない。
- 既存の `agents/muse/artifacts/report/` と `repository-reviews/` は入口を読んだ。配下の全Reportは未読で、今回の論点が過去の全分析に対して新規であるとは主張しない。それぞれの所有領域は移設・統合していない。
- 自然なSkill選択、他AIの受入れ、身体・生活上の実行、長期効果を試験していない。作品中の例は公開原本の記録か、明示した説明用の仮例である。

不足が後の判断を変える場合は、その対象のCurrent原本と必要な履歴へ戻ればよい。この一覧を全作業の追加Bootや、毎回の全件読解の義務にしない。

## 保存後の確認との違い

本書のsource_commitは分析した資料の基点であり、Reportを追加したcommitとは異なる。公開前には新しいmainと対象パスの並行変更を確認し、既存Treeを基に対象成果物だけを追加する。保存結果はRemoteから全文を再取得し、ローカル完成本文とGit blobを照合する。初回10本・入口・付録・Artifacts案内の13ファイルはcommit `17c625ad1b01f5bbfbfd0c500e85c81d7fa9f27d`で保存し、mainから全文とblobの一致を確認した。追加3本と本付録・入口の更新についても保存後に同じ確認を行い、最終応答で結果を報告する。

この読取付録は原本の第二台帳ではない。後続mainが変わっても、今回何を根拠に書いたかを保持する。分析に誤りが見つかった場合は理由と根拠を添えて同じ作品を改訂し、Git履歴から前版を辿れるようにする。

EOF::REPORTS_READING_SCOPE_20261025::v003

