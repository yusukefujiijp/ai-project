---
title: "Ark Project"
canonical_path: "_projects/ark/README.md"
status: "active / human-sealed"
role: "Ark Project public-safe parent entry / topology router"
root: "主イェシュア・ハマシア"
language_policy: "Japanese-first / English-anchor"
current_topology: "Ark00 → Ark01+ / Ark Project"
retired_topology: "Ark99 → Ark00 → Ark01+"
---

# Ark Project

## 0. Current Coordinate / 現在座標

Ark Projectは、**Daily Teshuvah Gate-to-Yeshua** をRootに置く、public-safeなHuman-AI collaboration fieldである。

このGitHub上のArk Projectは、Arkのすべてを移す場所ではない。  
Future HumanとFuture AIが現在の地形を回復し、正しい入口へ進むためのCanonical Entryである。

```text
Root:
  主イェシュア・ハマシア

GitHub role:
  public-safe entrance
  canonical current coordinate
  rebootable routing surface
```

---

## 1. Current Topology / 現行Topology

現在のPre-Project入口は`Ark00`である。

旧Ark99のWild Seed受け付け機能は、Ark00へ吸収された。  
Ark99は現役のUpstream Folderではなく、歴史的Topologyとしてのみ扱う。

```text
Current:
  Ark00 → Ark01+ / Ark Project

Retired:
  Ark99 → Ark00 → Ark01+
```

```yaml
ark_topology:
  ark00:
    status: "active pre-project Zero-Gate"
    role:
      - "Wild Seed reception"
      - "Discernment"
      - "Selective incubation"
      - "Routing to Ark01+"

  ark99:
    status: "retired / absorbed into Ark00"
    active_route: false
    guard:
      - "Do not route new seeds to Ark99."
      - "Do not restore Ark99 as a required stage."
```

詳細は[`ark00/README.md`](ark00/README.md)を参照する。

---

## 2. Active Public-Safe Entries

```yaml
active_entries:
  ark00:
    path: "_projects/ark/ark00/README.md"
    role: "Wild Seed Zero-Gate / Pre-Project Entry"

  ark_wtp:
    readme: "_projects/ark-wtp/README.md"
    root_spec: "_projects/ark-wtp/ark-wtp.md"
    role: "Ark-WTP dedicated field"

  ark02_handoff:
    path: "_projects/ark/ark02/handoff.md"
    role: "public-safe Thread-line handoff node"
```

Opened Entryは、Ark全体をGitHubへ完全移行したことを意味しない。

```text
README-first:
  まず入口を置く。

Full migration:
  Reality Responseが必要を示すまで行わない。
```

---

## 3. Routing Rule / Route選択

```yaml
routing:
  unclassified_seed:
    go_to: "Ark00"

  formal_project:
    go_to: "Ark01+ after Human discernment and seal"

  ark_wtp_material:
    go_to: "_projects/ark-wtp/"

  thread_line_continuity:
    go_to: "the relevant handoff node"
```

AIは自動Project化しない。  
HumanがMission、意味、優先順位、正式Project化を判断する。

---

## 4. README Delta Check / 更新Timing

READMEは毎Thread必ず書き換えない。  
各Thread終了時に、READMEとCanonical Realityの差分を軽量確認する。

> **Every Thread README Check.  
> Not Every Thread README Update.**

```yaml
readme_delta_check:
  run_at: "Thread-End"
  update_when:
    - "Canonical File / Folderが新規作成された"
    - "Path / Role / Status / Active / Retiredが変わった"
    - "Project TopologyまたはRead Orderが変わった"
    - "Repository-wide Policyが確定した"
    - "既存READMEがFuture AIを誤ったRouteへ送る"

  propagation:
    - "Nearest README"
    - "Domain Parent README when navigation changes"
    - "Root README when repository-level coordinate changes"

  automatic_write: false
```

README更新候補が出ても、GitHub WriteにはHuman Sealと明示的実行許可が必要である。

---

## 5. Mainline-First Mirror Guard

Ark ProjectのCanonical Current Realityは`main`に置く。

```yaml
mainline_guard:
  canonical_branch: "main"
  branch_creation:
    default: false
    requires: "explicit Human Seal and demonstrated need"
  prohibited:
    - "AIが良かれと思ってBranchを作る"
    - "重要なArk Fileを未Merge Branchだけに残す"
    - "Branchを第二のArk Realityとして扱う"
```

---

## 6. Root / Fruit Guard

```text
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め

Fruit:
  Ark Project
  GitHub
  README
  Markdown
  AI
  Plan Mode
  Full Rail
  Thread-End
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 7. Final Compression

```text
Ark Project on GitHub is a public-safe routing field.
Ark00 is the active pre-project Zero-Gate.
Ark99 is retired and absorbed into Ark00.
README is checked every Thread-End, but updated only when Reality changed.
main is the shared current reality.
Root remains 主イェシュア・ハマシア.
```
