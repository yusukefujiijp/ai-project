---
title: "問題解決 / Problem Solving — 起動Query"
canonical_path: "skills/problem-solving/README.md"
version: "v001"
created: "2026-10-17"
updated: "2026-10-17"
role: "Human-facing invocation guide"
expected_eof: "EOF::PROBLEM_SOLVING_SKILL_README::v001"
---

# 問題解決 / Problem Solving — 起動Query

未整理の困りごと、行き詰まり、複数の問題を、現在の文脈から受け取るSkillです。Humanが方法を先に選ばなくても、必要な整理・調査・比較・計画・実行へつなぎます。

## 起動Query

```text
$problem-solving スキルを使い、現在の困りごとを文脈から理解して、依頼の範囲で解決を進めてください。
```

会話内に困りごとが既にある場合は、この一文をそのまま使えます。新しい相談なら、困りごとや望む変化を普段の言葉で添えてください。専用の入力形式や、既に伝えた内容の再入力は必要ありません。

相談・計画限定・実行・保存の範囲は、現在の依頼と有効な承認に従います。たとえば計画だけを希望する時は、その意図を普段の言葉で添えます。このQueryの短さは、検討・説明を浅くする指定ではありません。

## 本文・表示設定・案件への接続

- [SKILL.md](SKILL.md)：AIが使う判断と進め方の本文。
- [agents/openai.yaml](agents/openai.yaml)：表示設定。上のQueryは `default_prompt` と同じ標準起動文です。
- [Problem Solvingの案件入口](https://github.com/yusukefujiijp/ai-project/blob/main/problem-solving/README.md)：Arkで既存の問題や成果へ戻る時に使います。担当原本が分かる場合は、そこへ直接進めます。

このREADMEはコピーして使う入口を所有します。新しい相談に案件作成やArk資料の全件読込を求めず、本文の手順や個別案件の記録をここへ複製しません。

EOF::PROBLEM_SOLVING_SKILL_README::v001
