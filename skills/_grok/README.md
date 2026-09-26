---
title: Grok Skills Backup
owner: YusukeJP
updated: 2026-09-26
status: backup-only
restore: pending
---

# Grok Skills Backup

このフォルダは、Grokで作成したSkillのbackup専用です。
`skills/` 直下の共有原本（Ark Shared Skills Hub）とは役割を分けます。ここは、Grokセッションが切れても同じ手順を戻すための控えです。

ここは完成品棚ではない。写してあることと、単体で足りることと、Hubで使ってよいことは別の辺です。

## Future AI / 別AIへ

- Hubの検証済み共有原本ではない。Grok user skills の複製である。
- Hubへの掲載は別のHuman承認が要る。
- 6件を同じ重さの完全体と読むな。
- 似たフォルダを自動統合するな。
- All repositories 権限への拡大は、このbackup成功の理由にしない。

関係の短い固定は [RELATION.md](RELATION.md)。

## 置き方

1 Skillを1フォルダにします。必須ファイルは `SKILL.md` です。ある場合は `references/` も同じ配下へ複製します。

frontmatterのトップレベルは agentskills.io の許可キーに合わせます。`name`、`description`、`metadata` を使います。

backupはセッション正本の複製です。運用中の改訂は Grok 側で検証してから、同じパスへ上書きします。

## 収録（2026-09-26、user skills 6件）

| Skill | 完結 | 用途 | 本文 |
|---|---|---|---|
| ark-okf-responder | 起動面のみ | 本文は入口。原本は `prompts/ark-open-knowledge-format.md`。旧名 `S_Ark-open-knowledge-format_v002.md` はエイリアス | [SKILL.md](ark-okf-responder/SKILL.md) |
| cortisol-meal-ops | 単体で動く | 軽い不調向けの食事オペレーション | [SKILL.md](cortisol-meal-ops/SKILL.md) |
| japanese-quality-protocol | 単体で動く | 日本語長文の自然さプロトコル | [SKILL.md](japanese-quality-protocol/SKILL.md) |
| living-graph-mode | 本文+refs | 関係優先の推論。Hub の `analyze-living-graph` とは別物 | [SKILL.md](living-graph-mode/SKILL.md) |
| long-form-response-rhythm | 本文+refs | 長文のリズム構成 | [SKILL.md](long-form-response-rhythm/SKILL.md) |
| one-table-interface | 本文+refs | 一回答一表 | [SKILL.md](one-table-interface/SKILL.md) |

`living-graph-mode` / `one-table-interface` / `long-form-response-rhythm` は互いに参照し合う器である。献立の型や restore 試験より前景に出さない。

各Skillの `references/ark-binding.md` は似たGuardの重複である。Rootが三つあると読むな。今はパスを壊さないため異動しない。

## 戻し方

1. 対象フォルダ全体（`SKILL.md` と `references/`）を、Grok の user skills へ同じフォルダ名で置く。
2. Skill Creator の validate を通す。
3. 呼び出し語で1回動かし、禁止事項と出力順が残っているか見る。

restore 試験は 2026-09-26 時点で未実施。書けたことと戻せることは別の辺。別セッションで一件動かして初めて backup 完了と呼ぶ。

bundled skill（docx / pdf / pptx / xlsx / ffmpeg / skill-creator）はこのbackupに含めません。

## 更新記録

- 2026-09-26: 空READMEを本文へ置換。`cortisol-meal-ops` v1.1 を初回backup。
- 2026-09-26: Grok user skills 6件を `_grok` へbackup。Hubは未触れ。
- 2026-09-26: `ark-okf-responder` の参照を正準 Path へ修正。本文を複製しない。
- 2026-09-26: 収録を完結状態で区別。RELATION.md を追加。restore は未実施のまま。
