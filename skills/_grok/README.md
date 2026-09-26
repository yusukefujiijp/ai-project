---
title: Grok Skills Backup
owner: YusukeJP
updated: 2026-09-26
status: backup-only
---

# Grok Skills Backup

このフォルダは、Grokで作成したSkillのbackup専用です。
`skills/` 直下の共有原本（Ark Shared Skills Hub）とは役割を分けます。ここは、Grokセッションが切れても同じ手順を戻すための控えです。

## 置き方

1 Skillを1フォルダにします。必須ファイルは `SKILL.md` です。任意で `scripts/`、`references/`、`assets/` を足します。

frontmatterのトップレベルは agentskills.io の許可キーに合わせます。`name`、`description`、`metadata` を使い、呼び出し語や version は `description` か `metadata` へ置きます。

backupは正本の複製です。運用中の改訂は Grok 側で検証してから、同じパスへ上書きします。

## 収録

| Skill | version | 用途 | 本文 |
|---|---|---|---|
| cortisol-meal-ops | 1.1 | 軽い不調向けの食事オペレーション。人数未指定は1人、日数未指定は3日 | [SKILL.md](cortisol-meal-ops/SKILL.md) |

## 戻し方

1. 対象フォルダの `SKILL.md` を、Grok の user skills へ同じフォルダ名で置く。
2. Skill Creator の validate を通す。
3. 呼び出し語で1回動かし、出力順と禁止事項が残っているか見る。

`cortisol-meal-ops` の呼び出し語は、献立、レシピ、サバ缶、コルチゾール食事、買い物リスト、作り置き、`/cortisol-meal-ops` です。

## 更新記録

- 2026-09-26: 空READMEを本文へ置換。`cortisol-meal-ops` v1.1 を初回backup。
