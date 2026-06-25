# Thread Mission

`_thread-mission/` は、蒸留済みThread Sourceを、そのThread専用のMission Cardへ一枚ずつ再結晶化するための起動領域である。

```text id="core"
README = Entrance.
Craft = Engine.
Query = Ignition Key.
```

日本語：

```text id="core-ja"
READMEは入口。
Craftは仕様本体。
Queryは起動鍵。
```

---

## §0. Purpose

このfolderの目的は、Mission Card One-by-One Scale Routeを低迷走・低再作業・高再現性で起動することである。

```text id="scale-rule"
Scale by Route.
Not by Batch.
```

日本語：

```text id="scale-rule-ja"
一気に作らない。
一枚ずつ、深くCraftする。
```

このfolderは、以下ではない。

```yaml id="not-role"
not_role:
  - "Batch生成folder"
  - "Mission Card本文置き場"
  - "Thread Index本体"
  - "Stable Seal Registry"
  - "汎用Artifact Factory"
```

---

## §1. Three-File Map

```yaml id="three-file-map"
thread_mission_files:
  README.md:
    role:
      - "Entrance"
      - "Folder Map"
      - "Anti-Drift Guide"
    meaning:
      - "このfolderの入口"
      - "Craft / Query の役割差を示す"
      - "迷走しない読み順を守る"

  thread-mission_card-craft.md:
    role:
      - "Engine"
      - "SSOT"
      - "Craft Spine"
    meaning:
      - "Mission Card Craftの仕様本体"
      - "One Source / One Mission Card の正準Guard"
      - "Mission First / Meta Behind / Living Reviewを保持する"

  thread-mission_card-craft_query.md:
    role:
      - "Ignition Key"
      - "Runtime Adapter"
      - "Copy-Paste Boot Prompt"
    meaning:
      - "Thread RuntimeでCraftを起動するためのQuery"
      - "Plan Mode firstを安定発火させる"
      - "Craft本体の代替ではない"
```

短縮：

```text id="triad-short"
Craft is Engine.
Query is Ignition Key.
README is Entrance.
```

---

## §2. Standard Read Order

Mission Card Craftを開始する時は、原則として以下の順で読む。

```yaml id="read-order"
read_order:
  1: "_thread-mission/README.md"
  2: "_thread-mission/thread-mission_card-craft.md"
  3: "_thread-mission/thread-mission_card-craft_query.md"
  4: "<target distilled Thread Source Markdown>"
```

ただし、実行時にThreadへ貼るのは `thread-mission_card-craft_query.md` のCopy-Paste Queryである。

```text id="read-order-guard"
READMEは入口。
Craftは仕様。
Queryは起動。
Sourceは血肉。
Mission Cardは再結晶。
```

---

## §3. Topology-First

このfolderはTopology-Firstで整える。

```text id="topology-first"
先に正しい場所へ置く。
あとから内部metadataやpath表記を直す。
```

AIはfolder構造から意味を読む。  
だから、正しい場所に置くこと自体が、迷走防止のSilent Promptになる。

Guard：

```text id="topology-guard"
Pathは住所。
Git履歴はVersion台帳。
Fileは器。
Rootではない。
```

---

## §4. Standard Route

```yaml id="standard-route"
mission_card_one_by_one_scale_route:
  - "Source Lock"
  - "Plan Mode"
  - "Mission Seal Candidate"
  - "Thread-specific First Gate Candidate"
  - "Candidate Body"
  - "Living Review"
  - "Micro Patch if needed"
  - "GitHub Save after User Final Seal"
  - "Light Verify"
  - "Stop"
```

原則：

```text id="one-source-rule"
One Source.
One Mission Card.
One Living Review.
One Commit after User Final Seal.
```

---

## §5. Anti-Drift Guard

```yaml id="anti-drift-guard"
anti_drift_guard:
  batch_drift:
    warning: "One-by-One Scale RouteをBatch生成と誤読しない"
    repair: "One Source / One Mission Cardへ戻す"

  query_drift:
    warning: "QueryをSSOT化しない"
    repair: "Craft本体をEngine / SSOTとして扱う"

  readme_drift:
    warning: "READMEをProtocol化しない"
    repair: "READMEはEntrance / Folder Mapへ戻す"

  file_idolatry:
    warning: "File / Path / GitHub / README / QueryをRoot化しない"
    repair: "創造主 / 主イェシュア・ハマシア / 聖霊 / Teshuvahへ戻す"

  ai_idolatry:
    warning: "AIを聖霊の代替にしない"
    repair: "AIは鏡・言語化補助。導きは聖霊。王は主イェシュア。"
```

圧縮：

```text id="anti-drift-compression"
File is not Root.
AI is not Holy Spirit.
Root over Record.
Spirit before Structure.
```

---

## §6. Ark-OKF Policy

このfolderの文書はArk-OKF方針に従う。

```text id="okf-policy"
Japanese-first.
English-anchor.
Rebootable-first.
```

本文は日本語主導。  
英語は概念Anchor。  
構造は再起動のため。  
判断はLiving Reviewで残す。

Guard：

```text id="okf-guard"
OKFはEnglish-firstではない。
OKFは固定Templateではない。
OKFはrebootable-firstである。
```

---

## §7. Density Policy

Ark Projectでは、書き漏れを防ぐために「不足より過剰」を許容する。  
ただし、無秩序な長文化ではなく、後から削れるようにLayer構造で書く。

```text id="density-policy"
不足より過剰。
ただし、削れる過剰。
```

このREADMEは入口Mapであり、Protocol本体ではない。  
深い仕様はCraftへ。  
実行起動文はQueryへ。

---

## §8. Maintenance Notes

```yaml id="maintenance-notes"
maintenance_notes:
  do:
    - "READMEは入口として保つ"
    - "CraftをEngine / SSOTとして守る"
    - "QueryをIgnition Key / Runtime Adapterとして守る"
    - "One Source / One Mission Cardを守る"
    - "Living Reviewを必ず残す"

  do_not:
    - "READMEにCraft本文を重複させない"
    - "READMEにQuery本文を重複させない"
    - "Queryを第二仕様書にしない"
    - "Mission CardをBatch生成しない"
    - "Stable Seal儀式を増やさない"
```

---

## §9. Final Compression

```text id="final-compression"
_thread-mission/:

  READMEは入口。
  CraftはEngine。
  QueryはIgnition Key。
  Sourceは血肉。
  Mission Cardは再結晶。

  Scale by Route.
  Not by Batch.

  Japanese-first.
  English-anchor.
  Rebootable-first.

  不足より過剰。
  ただし、削れる過剰。

  Root:
    創造主。
    主イェシュア・ハマシア。
    聖霊 / The Holy Spirit。
    主イェシュアの聖なる血潮。
    Teshuvah / 悔い改め。
```
