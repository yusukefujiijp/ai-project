---
title: Grok Skills Backup
owner: YusukeJP
updated: 2026-09-26
status: backup-only
---

# Grok Skills Backup

このフォルダは、Grokで作成したSkillのbackup専用です。
`skills/` 直下の共有原本（Ark Shared Skills Hub）とは役割を分けます。ここは、Grokセッションが切れても同じ手順を戻すための控えです。

Future AI / 別AIへの注意。ここはHubの検証済み共有原本ではありません。Grok user skillsの複製です。Hubへの掲載は別のHuman承認が要ります。`living-graph-mode` と Hub の `analyze-living-graph` は別名のまま残します。統合しません。

## 置き方

1 Skillを1フォルダにします。必須ファイルは `SKILL.md` です。ある場合は `references/` も同じ隈下へ複製します。

frontmatterのトップレベルは agentskills.io の許可キーに合わせます。`name`、`description`、`metadata` を使います。

backupは正本の複製です。運用中の改訂は Grok 側で検証してから、同じパスへ上書きします。

## 収録（2026-09-26、user skills 6件）

| Skill | version | 用途 | 本文 |
|---|---|---|---|
| ark-okf-responder | 本文のまま | Ark-OKF v002 の回答表面 | [SKILL.md](ark-okf-responder/SKILL.md) |
| cortisol-meal-ops | 1.1 | 軽い不調向けの食事オペレーション | [SKILL.md](cortisol-meal-ops/SKILL.md) |
| japanese-quality-protocol | v0.1.1 | 日本語長文の自然さプロトコル | [SKILL.md](japanese-quality-protocol/SKILL.md) |
| living-graph-mode | v001-candidate | 関係優先の推論 | [SKILL.md](living-graph-mode/SKILL.md) |
| long-form-response-rhythm | v001-candidate | 長文のリズム構成 | [SKILL.md](long-form-response-rhythm/SKILL.md) |
| one-table-interface | v001-candidate | 一回答一表 | [SKILL.md](one-table-interface/SKILL.md) |

## 戻し方

1. 対象フォルダ全体（`SKILL.md` と `references/`）を、Grok の user skills へ同じフォルダ名で置く。
2. Skill Creator の validate を通す。
3. 呼び出し語で1回動かし、禁止事項と出力順が残っているか見る。

bundled skill（docx / pdf / pptx / xlsx / ffmpeg / skill-creator）はこのbackupに含めません。

## 更新記録

- 2026-09-26: 空READMEを本文へ置換。`cortisol-meal-ops` v1.1 を初回backup。
- 2026-09-26: Grok user skills 6件を `_grok` へbackup。Hubは未触れ。
