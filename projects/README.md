---
title: "Projects"
version: "v002-candidate"
status: "current named-project router / human-authorized scoped navigation"
canonical_path: "projects/README.md"
role: "Named Project domain front door / current project router"
repository: "yusukefujiijp/ai-project"
canonical_branch: "main"
language_policy: "Japanese-first / English-anchor"
updated: "2026-10-10"
route_alignment:
  change_record: "../control-center/github/ARCHIVE.md#arc-011"
  base_commit: "c8c35957ef63d0fca7378a1cc98ea1099a4e30c1"
  scope: "Retire the old Ark-Voice live route; retain the WTP frozen benchmark and its conditions"
human_final_seal_required: true
---

# Projects

## 0. Purpose

`projects/`は、番号ではなく固有名を持つLong-Lived ProjectのCurrent Domainである。

```text
Numbered Ark lifecycle → ../ark-project/
Named dedicated project → ./<project-name>/
```

このREADMEはProject本文や全Repository Inventoryではなく、Future HumanとFuture AIを正しいLocal Front Doorへ送る薄いRouterである。

## 1. Current Projects

| Project | Role | Entry |
|---|---|---|
| Ark-WTP | Weekly Torah Portion／Parasha × Lens。`FROZEN_BENCHMARK_WAIT`として成果本文と比較条件を保持 | [`ark-wtp/README.md`](./ark-wtp/README.md) |

Ark-WTPの凍結は自動再開を求めない。成果本文の`PROVISIONAL_PASS`、Human Final Seal、前身`ark-wtp.md`のLocal backup確認を別々に扱う。詳細はWTPの入口とArtifact READMEが所有する。

旧Ark-Voiceの二原本は[ARC-011](../control-center/github/ARCHIVE.md#arc-011)へ保管し、当時の共同研究・未実証のSystem候補として辿れる。現在の[Radio Mode](../skills/radio-mode/SKILL.md)は聴取向け回答の編成、[Voice Mode](../skills/voice-mode/SKILL.md)は突発的な音声対話の準備・事後支援を担う。旧Systemとの機能同等性や実利用効果は保証せず、共有・導入・検証の区別は[Skills Hubの形成記録](../skills/README.md#radio-voice-formation)へ戻る。

## 2. Routing Rules

```yaml
routing:
  repository_home: "../README.md"
  numbered_ark_family: "../ark-project/README.md"
  named_project: "Nearest project README"
  reusable_prompt: "../prompts/README.md"
```

Folder名が似ていることだけを理由に、Named Projectを番号付きArk Familyへ移さない。新Projectの追加・削除・Role変更時だけ、このREADMEを更新する。

## 3. Guard

AI、Project、README、GitHubはKeliであり、Root・王座・Human Final Sealを置換しない。

<!-- PROJECTS_README_EOF_v002-candidate -->
