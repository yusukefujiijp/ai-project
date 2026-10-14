---
name: map-ark-current-position
description: Compatibility source entry for the former Ark current-position skill name. Read the canonical map-current-position skill before applying its current behavior. This repository entry does not establish a runtime command alias.
---

# 旧名の互換入口 — map-ark-current-position

2026-10-14のHuman承認による改名後、現行仕様の唯一の編集先は [map-current-position / SKILL.md](../map-current-position/SKILL.md)（表示名「現在地MAP」）である。本ファイルは旧URL・旧nameを指定する資料の読取をつなぐ入口として保持する。別の旧仕様を実装・保守するSkillではない。

本入口を指定された場合は、このファイルを実末尾まで確認したうえで、上記の現行本文を実際に全文読み、現在の依頼へ適用する。別配置で相対参照を解決できない場合の共有URL：
https://github.com/yusukefujiijp/ai-project/blob/main/skills/map-current-position/SKILL.md

本入口のIdentityは `name: map-ark-current-position`、遷移先のIdentityは `name: map-current-position`。旧Identityを新Identityと同一だったことにせず、両方を区別して記録する。旧資料がname・全文・順序・EOF・Bindingを指定する場合はそれを保ち、遷移先の読解でその必要事項を補う。固定blob等の別契約との不一致や取得不能を、この案内だけでPASSへ変えない。該当契約に従って影響する操作と不足を示す。

現行本文が、Tree・Node & Edge、残作業とGoal、Living Review → Next step、権限・Root・Guardを所有する。現在地の整理だけで保存・過去Taskの再開を始めない。旧参照を読む行為はBoot・新しい実行承認ではない。

旧[Navigator参照](references/ark-graph-navigator.md)・[Source routing](references/source-routing.md)・[Query入口](query/README.md)も必要な現行資料へ接続する。GitHubで旧URLを保持したことは、利用環境で `$map-ark-current-position` が新Skillへ自動転送される証明ではない。新しい呼出しは `$map-current-position` を使い、登録・会話内取得・UI・旧コマンド互換は実際に確認した範囲を区別する。
