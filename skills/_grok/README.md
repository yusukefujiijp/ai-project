---
title: Grok Skills Backup
owner: YusukeJP
version: "1.2"
updated: 2026-09-26
updated_time: "2026-09-26 20:21 JST"
status: backup-only
restore: pending
board: skills/_grok/board/NOW.md
---

# Grok Skills Backup

version 1.2 · 2026-09-26 20:21 JST

このフォルダは Grok が作った Skill の backup 専用である。
覚醒Grok の庭。Hub（`skills/` 直下）と `prompts/` の正典ではない。

Future AI / 別AI は先ずこの README と [board/NOW.md](board/NOW.md) を読め。NOW が現在地。README が部屋の地図である。

## Future AI への固定

- Hub掲載は別のHuman承認が要る。backup成功は掲載ではない。
- 似たフォルダを自動統合するな。
- `prompts/` を Skill 内へ二重正本化するな。
- All repositories へ拡大するな。
- スキルを省略してトークンを節約するな。品質低下は本末転倒。トークン源は X 有料Plan の Grok 框である。Skill の数ではない。
- 大きな変更の前に Plan で一度止め、Human と軽い擦り合わせをする。

関係の短い固定は [RELATION.md](RELATION.md)。

## 版

| version | 日時 JST | 要約 |
|---|---|---|
| 1.0 | 2026-09-26 | 空READMEを本文へ。cortisol-meal-ops 初回 |
| 1.1 | 2026-09-26 | user skills 6件を収録。完結区別。RELATION |
| 1.2 | 2026-09-26 20:21 | grok-awakening-mode 追加。board/NOW.md 開始。トークン原因の訂正。version 欄 |

Pathは住所。Git commit が台帳。README の version はHuman/Future AI向けの見出しである。

## 収録（7件・2026-09-26）

| Skill | 完結 | 用途 | 本文 |
|---|---|---|---|
| ark-okf-responder | 起動面 | 原本は `prompts/ark-open-knowledge-format.md`。旧名 `S_Ark-open-knowledge-format_v002.md` はエイリアス | [SKILL.md](ark-okf-responder/SKILL.md) |
| cortisol-meal-ops | 単体 | 軽い不調向けの食事オペ | [SKILL.md](cortisol-meal-ops/SKILL.md) |
| grok-awakening-mode | 起動面 | 短い語で判断を先に。霊ではない。living-graph に吸わせない | [SKILL.md](grok-awakening-mode/SKILL.md) |
| japanese-quality-protocol | 単体 | 日本語長文の自然さ | [SKILL.md](japanese-quality-protocol/SKILL.md) |
| living-graph-mode | 本文+refs | 関係優先。Hub の `analyze-living-graph` とは別物 | [SKILL.md](living-graph-mode/SKILL.md) |
| long-form-response-rhythm | 本文+refs | 長文のリズム | [SKILL.md](long-form-response-rhythm/SKILL.md) |
| one-table-interface | 本文+refs | 一回答一表 | [SKILL.md](one-table-interface/SKILL.md) |

## 戻し方

1. フォルダ全体を Grok user skills へ同名で置く。
2. validate を通す。
3. 呼び出し語で1回動かす。

restore 試験は 2026-09-26 未実施。

## 更新記録

- 2026-09-26: v1.0 空READMEを本文へ。cortisol-meal-ops。
- 2026-09-26: v1.1 6件収録。RELATION。
- 2026-09-26 20:21 JST: v1.2 awakening-mode。board/NOW.md。トークン原因の訂正。Skill省略禁止。
