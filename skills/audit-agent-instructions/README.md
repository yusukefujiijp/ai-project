---
title: "Agent Instruction Audit / audit-agent-instructions"
version: v001
updated: 2026-10-20
status: skill usage and invocation guide
---

# Agent Instruction Audit / audit-agent-instructions

Skill・AGENTS.md・Task Promptの過剰な制約、早すぎる停止、不要な文脈読込などを見直し、目的に沿う判断と検証済み完了を支えるスキルです。通常の仕事を無断で全指示監査へ拡張せず、今回指定された対象と範囲を扱います。

## 起動Query

監査したい指示と、提案までか改訂も含むかを現在の依頼で伝えます。次は現行UIの標準起動文です。

```text
Use $audit-agent-instructions to audit these instructions for unnecessary constraints and propose or apply improvements within my requested scope.
```

### Skill機構のないAIへ、監査と改善案だけを依頼する

次は旧HubのCross-AI入口を保持した、外部変更を行わないQueryです。

~~~text
次の共有Skillを読んで、今回の依頼に適用してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/audit-agent-instructions/SKILL.md
今回は指定した指示文の監査と改善案までです。必要な参照資料だけ追加で読み、外部変更は行わないでください。
~~~

## 判断と出典

短くすることや自由度だけを目標にしません。対象の実物と観測された失敗を読み、発見しやすさ、Context、裁量、検証、権限、継続、探索、移植性から今回の判断を改善する観点を選びます。必須Sourceの全文読解・順序や、実際の要件を守る決定的手順は保持します。

監査・計画限定では提案まで、明確に承認された改訂では編集と必要な確認まで進みます。作成・導入の方法は利用環境のskill-creation workflowへ従い、このスキルが追加の権限を与えることはありません。

[出典ノート](references/source-notes.md)は、記事の根拠・帰属や更新の必要性を判断するときに参照します。通常利用ごとのWeb再読は要求しません。

## 形成と確認の範囲

[移管前Hub](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#2-available-skills)は、作成・導入・限定した独立応答確認と、全AI互換性が未検証である範囲を記録しています。現行の共有表示設定は自動選択を許可しますが、別AIでの同じ挙動や実際の自動選択を証明するものではありません。

## 文書の役割と更新

このREADMEは説明・起動Query・形成と確認範囲を、[SKILL.md](SKILL.md)は実際の判断と手順を所有します。QueryはこのREADMEで管理し、別のQuery専用フォルダへ分けません。[表示設定](agents/openai.yaml)の標準起動文にはUI上の役割があるため、対応するQueryの変更時は意味の整合を確認します。READMEの全文を毎回の起動条件にはしません。

2026-10-20のREADME整備では、現行本文・表示設定と[移管前Hubの固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)を根拠に、このスキルの入口と記録を個別化しました。本文中の日付付きの確認は各時点の証拠であり、今回の文書移動による再試験や全環境の動作保証を意味しません。共有・導入の共通方針は[Skills Hub](../README.md#4-source-and-distribution)を参照します。
