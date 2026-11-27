---
title: pstack-backup — Muse 内 pstack 移植の差分バックアップと再建手順
version: v001
canonical_path: agents/muse/pstack-backup/README.md
role: Muse 内（~/workspace/custom-skills/）にある pstack 移植のうち、カスタムされた差分だけを保存し、原文移植を上流から再建する手順を保持する。復元専用の鏡であり、編集の本命は Muse 内。
status: backup-mirror
created: 2026-11-27
updated: 2026-11-27
repository: yusukefujiijp/ai-project
expected_eof: EOF::PSTACK_BACKUP_README::v001
---

# pstack-backup — 差分だけを保存する

## これは何か

Lauren Tan (@poteto) の pstack（本体は cursor/plugins、MIT）を Muse へ移植した22本のうち、**我々のカスタムが入っているものだけ**のバックアップ。原文のままの移植はここに置かない。本体は上流にあり、毎朝のウォッチが上流を向いている。丸ごとの複製は版の化石化を招く（原則: 参照は原本へ）。

## 編集の方向（厳守）

- 本命は Muse 内: `~/workspace/custom-skills/pstack_*/` と `~/AGENTS.md`。編集は常にそちら。
- ここは復元専用の鏡。ローカルが失われた時だけ、ここから戻す。
- 鏡の更新は、ローカル更新後のバンドルに同梱する（1バンドル1認識）。

## 保存物

| ファイル | 中身 | 本命の所在 |
|---|---|---|
| muse-adapter.md | Muse 用アダプタ文書（完全な原作） | custom-skills/pstack_muse_adapter/ |
| poteto-mode.md | 適応版ルーター（承認規律・Playbooks 節を含む） | custom-skills/pstack_poteto_mode/ |
| never-block-on-the-human.md | 日本語の適応注記つき原則 | custom-skills/pstack_principle_never_block_on_the_human/ |
| rule-table.md | /correct 対応表（規則↔執行者）の鏡 | ~/AGENTS.md の Correction rule table 節 |

## 移植レジストリ（上流 v0.15.48 から、2026-11-27 時点で22本）

- ルーター: pstack_poteto_mode（適応版）
- アダプタ: pstack_muse_adapter（Muse 原作）
- 原則12: prove_it_works / encode_lessons_in_structure / attack_the_premise / laziness_protocol / sequence_verifiable_units / guard_the_context_window / build_the_lever / fix_root_causes / explain_the_number / separate_before_serializing_shared_state / minimize_reader_load / never_block_on_the_human（適応注記つき）
- スキル4: reframe / sharpen / figure_it_out / correct
- プレイブック4: authoring_a_skill / investigation / session_pickup / eval

## 再建手順（原文移植が失われた場合）

1. 上流 cursor/plugins の pstack から、対象スキルの SKILL.md（プレイブックは skills/poteto-mode/playbooks/<name>.md）を取得する。
2. フォルダ名は `pstack_<name>`（原則は pstack_principle_<name>、プレイブックは pstack_playbook_<name>）。
3. SKILL.md の冒頭に頭注を付ける: 上流の版、出典 URL、「Original by Lauren Tan (@poteto), MIT License」、適応点。本文は原文のまま。
4. skill.yaml を添える: name（フォルダ名と一致）、title、description（一文）、category「Work and knowledge」、include_in_prompt: false。
5. 機械照合する: 上流の本文行が移植側に全て存在すること（見出し記号の差は許容し、報告する）。
6. ルーターの Playbooks 節と原則インデックスが、新しい構成と一致するよう直す。

EOF::PSTACK_BACKUP_README::v001
