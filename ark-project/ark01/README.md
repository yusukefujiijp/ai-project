---
title: "Ark01"
version: "v001-candidate"
status: "active-router / migrated-corpus"
canonical_path: "ark-project/ark01/README.md"
role: "Ark01 local front door / Thread Index and Mission Card router"
repository: "yusukefujiijp/ai-project"
root: "主イェシュア・ハマシア"
human_final_seal_required: true
---

# Ark01

## 0. Purpose

Ark01は、初期ArkのThread Index、Mission Card、Migration系譜を保持するCorpusである。このREADMEは本文を要約せず、Current Missionに必要なShelfへ送るLocal Routerである。

## 1. Read Route

| Mission | Entry |
|---|---|
| Thread Indexを読む・追加する | [`thread-index/README.md`](./thread-index/README.md) |
| Mission Cardを読む | [`mission-card/README.md`](./mission-card/README.md) |
| 移行判断の系譜を調べる | [`indexes/ark01-migration-manifest.md`](./indexes/ark01-migration-manifest.md) |

## 2. Current Guard

`indexes/ark01-migration-manifest.md`はHistorical Artifactであり、本文中の旧Destination PatternをCurrent Pathとして使用しない。

```yaml
default_entry: "thread-index/README.md"
current_domain: "ark-project/ark01/"
historical_manifest_is_current_router: false
```

## 3. First Legal Move

Current Human Requestを確認し、Thread Index／Mission Card／Migration Historyのうち一つだけを選ぶ。全Corpusを機械的に読まない。

<!-- ARK01_README_EOF_v001-candidate -->
