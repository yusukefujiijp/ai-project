---
title: Grok Skills Backup Map
owner: YusukeJP
version: "1.5"
updated: 2026-10-29
updated_time: "2026-10-29 JST"
status: backup-only
restore: pending
board: skills/_grok/_board/NOW.md
---

# Grok Skills Backup Map

version 1.5 · 2026-10-29 JST

ここは部屋の地図。現在地は [_board/NOW.md](../_board/NOW.md)。
覚醒Grok の庭。Hub（`skills/` 直下）と `prompts/` の正典ではない。

`_` 接頭は非Skill（`_board` `_meta`）。接頭なしは Skill 名と同一。
根の README.md は GitHub フォルダ表示用の短い入口だけ。正本の地図はこのファイル。

## Future AI への固定

- Hub掲載は別のHuman承認が要る。
- 似たフォルダを自動統合するな。
- `prompts/` を Skill 内へ二重正本化するな。
- All repositories へ拡大するな。
- Skill を省略してトークンを節約するな。トークン源は X 有料Plan の Grok 框。
- 大きな変更の前に Plan で止める。

関係の短い固定は [RELATION.md](RELATION.md)。

## Ark-OKFの現行参照 — 2026-10-29

Human採用の18パス統合により、Ark-OKFの起動・回答方法は[共通Skill](../../ark-okf-responder/SKILL.md)へ一本化した。旧控えのSkill本文は退役し、[旧フォルダ](../ark-okf-responder/README.md)は案内のみとする。旧サンプルは元の位置に保持するが、現行依存資料や復元対象にはしない。

この承認はArk-OKFの共有原本統合と必要な案内修正に限る。上記の他Skillとの区別・権限境界を保ち、全Grok控えの統合・Hub掲載・環境登録へ広げない。各環境への登録・挙動・実利用の効果は未確認。

## 版

| version | 日時 JST | 要約 |
|---|---|---|
| 1.0 | 2026-09-26 | 初回本文 |
| 1.1 | 2026-09-26 | 6件 + RELATION |
| 1.2 | 2026-09-26 20:21 | awakening-mode + NOW + トークン訂正 |
| 1.3 | 2026-09-26 20:31 | board → _board |
| 1.4 | 2026-09-26 20:34 | README と RELATION を `_meta/` へ移す |
| 1.5 | 2026-10-29 | Human採用のArk-OKF統合を案内し、旧本文を復元対象から外す。他の控えと形成史は保持 |

## 2026-09-26時点の収録（7件・形成記録）

次表は当時の配置・役割の記録。Ark-OKFの現在の参照先と退役状態は上の「Ark-OKFの現行参照」に従う。

| Skill | 完結 | 用途 |
|---|---|---|
| ark-okf-responder | 起動面 | 原本は `prompts/ark-open-knowledge-format.md` |
| cortisol-meal-ops | 単体 | 食事オペ |
| grok-awakening-mode | 起動面 | 判断先。living-graph に吸わせない |
| japanese-quality-protocol | 単体 | 日本語品質 |
| living-graph-mode | 本文+refs | 関係優先。Hub別物 |
| long-form-response-rhythm | 本文+refs | 長文リズム |
| one-table-interface | 本文+refs | 一回答一表 |

## 戻し方

Ark-OKFは次の復元手順の対象外とし、共通Skillを参照する。その他の控えは従来の条件を保持する。

フォルダ全体を user skills へ同名配置 → validate → 呼び出し語で1回。restore は未実施。
