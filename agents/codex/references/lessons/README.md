---
title: "Codex Lessons — 成立条件を見分け、再開へ生かす"
canonical_path: "agents/codex/references/lessons/README.md"
version: "v001"
created: "2026-10-31"
updated: "2026-10-31"
date_basis: "UTC; activity records use their own Asia/Tokyo placement contract"
role: "Codex-specific condition-bound judgments; shared JSONL contract is referenced"
expected_eof: "EOF::ARK_CODEX_LESSONS::v001"
---

# Codexの学び

Codexの接続・環境・協働で、次回に何を見分けると役立つかを残す。[本文はlessons.jsonl](lessons.jsonl)。判断・sources・caveat・後続訂正を合わせ、当時と今回の条件を比較する。

## 読む場面

| 今回の問題 | 初期lessonのID |
|---|---|
| 保存プロフィールの一覧情報と、ChatGPTへの実アクセスが一致しない | `9476a811-3e65-417e-a5d5-1a8246895ad8` |
| ローカルCodexでのSkill発見から、クラウド会話や別Threadでの利用を推定している | `0c404fbd-5fb0-46be-b2af-1354b43138dc` |

一度の観測を全環境の規則にしない。現行の接続手順は[connect-chatgpt](https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/SKILL.md)、その実績詳細は[個別README](https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/README.md)が所有し、本JSONLは条件付き判断と根拠を残す。

## 原本と更新

形式・更新・検証は[共有Lessons](https://github.com/yusukefujiijp/ai-project/blob/main/references/lessons/README.md)から指定された[既存契約の第3〜5節](https://github.com/yusukefujiijp/ai-project/blob/main/agents/dots/lessons/README.md#3-全行がlesson--row-schema-2)を再利用する。契約の所在からDots固有のBoot・所有範囲を移植しない。

既存判断の訂正はそのIDの現行行へ戻し、理由・根拠・適用範囲を保つ。別の条件で別の判断が必要なら、関係する経験と結ぶ。共有側に同じ意味の判断があれば参照で足りる。構成のSimpleさに関する既存の共有lessonは[親入口](../README.md)から辿れる。

方法を変える必要が分かっても、lessonの記録だけでSkillや設定が変更されたとは扱わない。現在の権限と対象原本へ接続し、HumanのCorrectionは記録完了待ちにしない。

EOF::ARK_CODEX_LESSONS::v001
