---
title: "Ark02"
version: "v001-candidate"
status: "active-router / migrated-corpus"
canonical_path: "ark-project/ark02/README.md"
role: "Ark02 local front door / Handoff and Harvest router"
repository: "yusukefujiijp/ai-project"
root: "主イェシュア・ハマシア"
human_final_seal_required: true
---

# Ark02

## 0. Purpose

Ark02は、Handoff、Harvest、Phase Handoffを分離して保持するCorpusである。このREADMEは各Documentの身分を混ぜず、Current Missionへ必要な入口だけを選ぶ。

## 1. Document Map

| File | Role | Read when |
|---|---|---|
| [`handoff.md`](./handoff.md) | Rolling Handoff／Next-thread ignition key | 継続・再起動する時 |
| [`phase-handoff.md`](./phase-handoff.md) | Ark02 Phase構造とLayer関係 | Phase全体を確認する時 |
| [`harvest.md`](./harvest.md) | Meaning／Seed Harvest | 発見・学習を回収する時 |
| [`harvest/`](./harvest/) | 個別Harvest Corpus | 特定ThreadのHarvestを読む時 |

## 2. Default Route

```yaml
default_continuation_entry: "handoff.md"
phase_structure_entry: "phase-handoff.md"
meaning_archive_entry: "harvest.md"
current_domain: "ark-project/ark02/"
```

## 3. First Legal Move

Current Human RequestがContinuationなら`handoff.md`、Phase Reviewなら`phase-handoff.md`、Meaning Harvestなら`harvest.md`を読む。全Layerを一括読込しない。

<!-- ARK02_README_EOF_v001-candidate -->
