---
title: "Projects"
version: "v001-candidate"
status: "active-candidate"
canonical_path: "projects/README.md"
role: "Named Project domain front door / current project router"
repository: "yusukefujiijp/ai-project"
canonical_branch: "main"
language_policy: "Japanese-first / English-anchor"
updated: "2026-08-15"
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
| Ark-Voice | Voice／Radio／Audio系Project | [`ark-voice/README.md`](./ark-voice/README.md) |
| Ark-WTP | Weekly Torah Portion／Lens-as-Dimensions Project | [`ark-wtp/README.md`](./ark-wtp/README.md) |

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

<!-- PROJECTS_README_EOF_v001-candidate -->
