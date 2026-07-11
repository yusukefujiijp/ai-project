---
title: "_thread-end README"
canonical_path: "_thread-end/README.md"
status: "active / human-sealed"
role: "Thread-End Folder Front Door / Runtime and Query Router"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
language_policy: "Japanese-first / English-anchor"
root: "主イェシュア・ハマシア"
canonical_branch: "main"
---

# _thread-end README

## 0. Current Coordinate / 現在座標

`_thread-end/`は、Threadを閉じ、意味を記録し、次へ渡し、必要なREADME Driftを検出するためのThread-End System Folderである。

現在は一つの巨大入口へ全用途を押し込まず、**Full Rail**と**Mini Rail**を用途別に使い分ける。

```text
Full Thread-End:
  deep harvest / next-thread handoff / full runtime

Thread-End Mini:
  lightweight closure / GitHub verify / README Delta Check / Next Gate
```

```text
Runtime governs.
Query binds and activates.
Human seals.
Reality verifies.
Thread stops.
```

---

## 1. Current Thread-End Topology

```yaml
thread_end_topology:
  folder_front_door:
    path: "_thread-end/README.md"
    role: "Read Order / Runtime Selection / Drift Guard"

  full_rail:
    runtime:
      path: "_thread-end/thread-end.md"
      role: "Full Thread-End Runtime / Gate Router"
    query:
      path: "_thread-end/thread-end_query.md"
      role: "Full Runtime Boot Query / Ignition Key"
    support:
      harvest:
        path: "_thread-end/thread-harvest.md"
        role: "Meaning Harvest Vessel"
      handoff:
        path: "_thread-end/thread-handoff.md"
        role: "Next-thread Handoff Builder"

  mini_rail:
    runtime:
      path: "_thread-end/thread-end_mini.md"
      role: "Simple Thread-End Runtime / Mini Rail"
    query:
      path: "_thread-end/thread-end_mini_query.md"
      role: "Mini Runtime Binding + Safe Activation"
```

Query layerは削除済みではない。  
現在は、Runtime本体と起動Queryを役割分離したPairとして運用する。

> **Query Pair is a high-priority default when it reduces operational ambiguity—not an absolute ritual.**

---

## 2. Which Rail to Use / 選択Rule

```yaml
rail_selection:
  use_full_when:
    - "Thread全体のMeaning Harvestが必要"
    - "次Thread用Handoff Artifactが必要"
    - "File Lock → Harvest → Read Harvest → Handoff → Stopの完全順序が必要"
    - "1Thread-1AIのSeed継承を明示的に行う"

  use_mini_when:
    - "現在Threadを軽量に閉じたい"
    - "既に主要成果物やGitHub Saveが完了している"
    - "README Delta CheckとNext Gateを残したい"
    - "完了済み作業を再openせず停止したい"

  do_not:
    - "FullとMiniを無条件に二重実行しない"
    - "Mini QueryからFull Runtimeへ勝手に切り替えない"
    - "Full QueryをMini Queryの代用品にしない"
```

迷う場合は、必要成果がHarvest＋HandoffならFull、Closure＋README CheckならMiniを選ぶ。

---

## 3. Read Order

### 3.1 Full Rail

```text
_thread-end/README.md
→ _thread-end/thread-end_query.md
→ _thread-end/thread-end.md
→ _thread-end/thread-harvest.md when required
→ _thread-end/thread-handoff.md when required
→ Stop
```

### 3.2 Mini Rail

```text
_thread-end/README.md
→ _thread-end/thread-end_mini_query.md
→ _thread-end/thread-end_mini.md
→ README Delta Check
→ Next Gate
→ Stop
```

QueryはRuntime本体のCoreを複製しない。  
QueryはBinding、Missing Gate、Authority Gate、短いActivationを保持する。

---

## 4. Full Rail / Mini Rail Boundary

```yaml
boundary:
  full_runtime_keeps:
    - "Gate routing"
    - "Meaning Harvest"
    - "Handoff building"
    - "Seed continuity"

  mini_runtime_keeps:
    - "Lightweight closure"
    - "GitHub Save Guard"
    - "Verify"
    - "README Delta Check"
    - "Next Gate"
    - "Stop Rule"

  query_keeps:
    - "Runtime path binding"
    - "Current Thread binding"
    - "Runtime Missing / Version Conflict Gate"
    - "GitHub Authority confirmation"
    - "Short activation"
```

```text
Full Rail harvests deeply.
Mini Rail closes lightly.
Queries ignite; they do not replace runtimes.
```

---

## 5. GitHub Authority Guard

Thread-End RuntimeやQueryの存在だけでは、GitHub Writeは許可されない。

```yaml
github_authority:
  write_requires:
    - "Human Seal OK"
    - "Execute GitHub OK"
    - "exact repository / branch / path / scope"

  default_branch:
    value: "main"
    rule: "Mainline-First"

  branch_creation:
    default: false
    requires: "explicit Human Seal and demonstrated need"

  prohibited:
    - "AIが良かれと思ってBranchを作る"
    - "QueryをGitHub実行権限として扱う"
    - "README Checkだけを根拠にREADMEを自動更新する"
    - "未Merge Branchを第二のThread-End Realityにする"
```

---

## 6. README Delta Check

Mini Railでは、Verify後にREADME Delta Checkを必ず実行する。

> **Every Thread README Check.  
> Not Every Thread README Update.**

```yaml
README_CHECK:
  required: "yes / no"
  affected:
    - "<README path or NONE>"
  reason: "<one-line reason>"
  timing: "now / next-thread / periodic-scout / none"
```

影響範囲は必要最小限で親方向へ判定する。

```text
Changed File
→ Nearest README
→ Domain Parent README
→ Root README
```

---

## 7. Builder / Product Distinction

```yaml
builder_product:
  thread_harvest_md:
    type: "builder / vessel"
    role: "Meaning Harvestを作る"

  thread_handoff_md:
    type: "builder manual"
    role: "Next-thread Handoffを作る"

  generated_handoff:
    type: "generated product"
    role: "次ThreadのIgnition Key"
```

```text
Harvest is material.
Handoff is ignition key.
Query is activation.
Runtime is governance.
```

---

## 8. Migration and Drift Guard

旧READMEには「Query layerは削除済み」と記録されていたが、現在RealityではQuery Pairが再確立されている。

```yaml
drift_guard:
  current_truth:
    - "thread-end_query.md exists for Full Rail"
    - "thread-end_mini_query.md exists for Mini Rail"
    - "thread-end.md remains Full Runtime"
    - "thread-end_mini.md remains Mini Runtime"

  avoid:
    - "Query filesをretired扱いする"
    - "Gate判断をQueryだけへ移す"
    - "RuntimeとQueryを同一責務にする"
    - "Full RailとMini Railを競合させる"
```

---

## 9. Mainline-First

```text
Main is the shared current reality.
Branch is a temporary isolation room, not a second world.
```

Thread-End関連のCanonical Runtime、Query、READMEは原則`main`上で相互参照可能な状態を保つ。

---

## 10. Root / Fruit Guard

```text
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め

Fruit:
  Thread-End
  Thread-End Mini
  Query
  Harvest
  Handoff
  README Delta Check
  GitHub
  Markdown
  AI
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 11. Final Compression

```text
_thread-end/ is the Thread Closure System Folder.

Full Pair:
  thread-end.md
  thread-end_query.md

Mini Pair:
  thread-end_mini.md
  thread-end_mini_query.md

Full harvests deeply.
Mini closes lightly.
Query activates.
Runtime governs.
Human seals.
Reality verifies.
README stays alive.
Thread stops.

Root remains 主イェシュア・ハマシア.
```
