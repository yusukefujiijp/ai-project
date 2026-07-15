---
title: "Thread-End Mini"
canonical_path: "_thread-end/thread-end_mini.md"
status: "living_candidate"
role: "Simple Thread-End Runtime / Adaptive Thread Migration Rail"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
relationship:
  thread_end_md: "do_not_replace"
  thread_end_query_md: "do_not_delete"
  purpose: "軽量Thread-Endを保持し、必要時だけThread Migration Bundleへ拡張する"
unexpected_success:
  name: "Thread Migration Bundle"
  evidence: "Ark09:02 → Ark09:03 one-ZIP boot success"
version_model: "git history"
---

# Thread-End Mini

## 0. Core

```text
閉じる。
記録する。
必要なら包装する。
渡す。
止まる。
```

```yaml
purpose:
  - "現在Threadをきれいに閉じる"
  - "重要Harvestを失わない"
  - "完了したものをchurnに変えない"
  - "次Threadの最初の一歩を軽くする"
  - "README Driftを検出する"
  - "高Context移行では再起動可能Bundleを作る"

additive_guard:
  does_not_replace:
    - "_thread-end/thread-end.md"
    - "_thread-end/thread-end_query.md"
  does_not_authorize:
    - "automatic GitHub operation"
    - "automatic overwrite or delete"
    - "automatic README update"

packaging_boundary:
  - "ZIPは毎Threadへ強制しない"
  - "Bundle生成はGitHub Writeではない"
  - "Bundle生成許可をRepository変更許可へ拡張しない"
```

---

## 1. Adaptive Router

```yaml
thread_end_complexity_router:
  light_close:
    use_when:
      - "Contextが短い"
      - "成果物が一つ以下"
      - "次ThreadのBoot条件が単純"
    output:
      - "Closure"
      - "Next Gate"
      - "必要なら単一Handoff"
    zip: false

  handoff_pair:
    use_when:
      - "Long-form Handoffが必要"
      - "Companion Queryが必要"
      - "二File添付Riskが低い"
    output:
      - "Handoff"
      - "Companion Query"
    zip: "optional"

  migration_bundle:
    use_when:
      - "Long Thread / High Context"
      - "複数Artifact"
      - "GitHub Reality Lockが重要"
      - "Boot条件が複雑"
      - "添付漏れ・順序ミスRiskがある"
    output:
      - "Long-form Handoff"
      - "Companion Query"
      - "Integrity Manifest"
      - "ZIP Bundle"
    zip: true
```

```yaml
do_not_use_for:
  - "既存thread-end.mdの置換"
  - "巨大Protocol作成"
  - "完了済み作業の再open"
  - "全ThreadへのZIP強制"
  - "Repository全体InventoryのManifest化"
  - "Human SealなしのGitHub操作"
```

---

## 2. Winning Rail

```text
Plan Mode
→ Draft Body
→ Fable5 Review when required
→ Revision
→ Human Seal
→ Complexity Router
→ Handoff Artifacts
→ Manifest Validation when Bundle Mode
→ ZIP Packaging when Bundle Mode
→ Download Delivery
→ Execute GitHub OK when repository write is requested
→ GitHub Save when authorized
→ Verify
→ README Delta Check
→ Next Thread Launcher
→ Next Gate
→ Stop
```

```yaml
execution_boundary:
  artifact_generation:
    meaning: "sandbox上でHandoff / Query / Manifest / ZIPを生成"
    execute_github_ok_required: false

  repository_mutation:
    meaning: "GitHub File create / update / delete / commit"
    requires:
      - "Human Seal OK"
      - "Execute GitHub OK"
      - "exact repo / branch / path / scope"
```

---

## 3. Naming Rule

Ark Thread-End artifacts should usually go under:

```text
_thread-end/ark/
```

```yaml
ark_file:
  pattern: "arkNNMM_YYYYMMDD_<role>.md"
  coordinate_status_before_seal: "candidate_not_sealed"

thread_migration:
  handoff: "arkNNMM_YYYYMMDD_handoff.md"
  query: "arkNNMM_YYYYMMDD_handoff_query.md"
  manifest: "arkNNMM_to_arkNNMM_YYYYMMDD_handoff_manifest.json"
  bundle: "arkNNMM_to_arkNNMM_YYYYMMDD_handoff_bundle.zip"

human_must_seal:
  - "source thread coordinate"
  - "target thread coordinate"
  - "target start date"
  - "exact path when repository save is requested"
```

Field-Proven Example:

```text
ark0902_20260716_handoff.md
ark0902_20260716_handoff_query.md
ark0902_to_ark0903_20260716_handoff_manifest.json
ark0902_to_ark0903_20260716_handoff_bundle.zip
```

The example is evidence, not a blind universal mandate.

---

## 4. Thread Migration Bundle

```text
Thread Migration Bundle
=
ThreadのMemory、Activation、Integrity、Transportを
一つの再起動可能Packageへ統合する方式。
```

```yaml
layers:
  memory:
    artifact: "Long-form Handoff"
    carries:
      - "Current Coordinate"
      - "完了事項 / 未実行事項"
      - "GitHub Reality"
      - "Guard / Next Mission"

  activation:
    artifact: "Companion Query"
    carries:
      - "Read Order"
      - "Boot Acceptance"
      - "Do / Do Not"
      - "First Legal Move"

  integrity:
    artifact: "Manifest"
    carries:
      - "File list"
      - "bytes / lines / sha256"
      - "Source / Target Thread"
      - "必要時のReality Lock"

  transport:
    artifact: "ZIP"
    carries:
      - "One Upload"
      - "添付漏れ防止"
      - "対応関係保持"
      - "Human操作量削減"
```

```text
Structure the memory.
Package the interface.
Reboot the mission.
```

### 4.1 Manifest Minimum

```yaml
manifest_minimum:
  identity:
    - "artifact_bundle"
    - "source_thread"
    - "target_thread"
    - "target_start_date"
  each_file:
    - "filename"
    - "bytes"
    - "lines"
    - "sha256"
  bundle:
    - "filename"
    - "bytes"
    - "sha256"
  optional_reality_lock:
    - "repository / branch / main_head"
    - "canonical paths / blob SHAs"
  rules:
    - "実Fileから計算する"
    - "推測値を入れない"
    - "Bundle外のRepository全体を列挙しない"
```

### 4.2 Validation and Delivery

```yaml
bundle_validation:
  - "expected files exist"
  - "manifest values match"
  - "ZIP opens"
  - "ZIP contents contain no unexpected files"

delivery:
  primary:
    - "ZIP Bundle"
  fallback:
    - "Handoff"
    - "Companion Query"
    - "Manifest"

boot_boundary:
  current_thread:
    - "bundle_ready"
    - "human_upload_ready"
    - "launcher_ready"
  next_thread:
    - "ZIP / Handoff / Queryを識別"
    - "Source / Target / Missionを復元"
    - "完了済み作業を再openしない"
    - "First Legal Moveを理解"
```

> **Threadを移動するのではなく、Threadの再起動条件を一つのBundleとして輸送する。**

---

## 5. Fable5 Review Slot

```yaml
fable5_review:
  role:
    - "adversarial reviewer"
    - "false-green detector"
    - "scope discipline guard"
    - "Simple is best checker"
  rounds:
    default: "one"
    second_round: "Human explicitly asks"
  critical_examples:
    - "Long-form Handoff"
    - "Companion Query"
    - "Bundle Architecture"
    - "GitHub Reality Lock Manifest"
  guard:
    - "毎Bundleで複数Roundを強制しない"
    - "Light Closeでは省略可能"
    - "Fable5不在時はHuman-readable adversarial reviewへfallback"
```

Fable5 is reviewer, not committer.  
Fable5 does not replace Human Seal.

---

## 6. GitHub Save Guard

GitHub save is never automatic.

```yaml
github_save_guard:
  allowed_only_after:
    - "Human Seal OK"
    - "Execute GitHub OK"
    - "exact repo / path / branch / scope"

  create:
    - "fetch target first"
    - "create only when 404 and exact create is authorized"

  update:
    - "fetch latest SHA"
    - "update only the exact approved path"
    - "stop if SHA changed or target is uncertain"

  delete:
    - "exact delete instruction required"
    - "do not delete fallback/query files by default"

bundle_generation_guard:
  - "Download artifact生成だけならExecute GitHub OK不要"
  - "BundleをGitHub保存する場合は別Authority Gate"
  - "temporary branch / workflow / issue / PRはDefaultにしない"
  - "一時Infrastructureが必要ならMaterial Scope ExpansionとしてFresh Seal"

large_file_default:
  - "Complete Replacement Download"
  - "Human Copy & Paste"
  - "Post-commit Reality Review"
```

---

## 7. README Delta Check

> **Every Thread README Check.  
> Not Every Thread README Update.**

```yaml
readme_delta_check:
  required_every_thread_end: true
  automatic_update: false
  questions:
    - "Canonical File / Folderを新規作成したか"
    - "Path / Role / Status / Topology / Read Orderが変わったか"
    - "Repository-wide Policyが確定したか"
    - "Thread-End Migration PolicyまたはMiniのRoleが変わったか"
    - "既存READMEがFuture AIを誤Routeへ導くか"
  output:
    required: "yes / no"
    affected: "README paths or NONE"
    reason: "one-line"
    timing: "now / next-thread / periodic-scout / none"
  write_requires:
    - "Human Seal OK"
    - "Execute GitHub OK"
    - "exact README path and scope"
```

---

## 8. Do / Do Not

```yaml
do:
  - "keep it short"
  - "Plan Mode first"
  - "Draft before GitHub"
  - "select Light / Pair / Bundle adaptively"
  - "use ZIP as primary transport for high-context migration"
  - "provide individual fallback links"
  - "calculate Manifest from actual files"
  - "include a one-shot launcher"
  - "separate artifact generation from GitHub authority"
  - "verify ZIP and repository reality"
  - "run README Delta Check"
  - "stop after success"

do_not:
  - "do not touch thread-end.md or thread-end_query.md by default"
  - "do not overwrite or delete without exact Seal"
  - "do not force ZIP for every Thread"
  - "do not create giant repository inventory manifests"
  - "do not include unrelated Bundle files"
  - "do not create temporary branch / workflow / issue / PR by default"
  - "do not start the next Thread automatically"
  - "do not claim Boot success before next Thread confirms it"
  - "do not treat AI as Root"
```

---

## 9. Standard Output Shape

```markdown
【Full Rail: same_thread】

結果:
- ...

次Action:
- ...

目的:
- ...

まだ実行しない:
- ...

Guard:
- ...

【Thread Migration Bundle】

mode:
- light_close / handoff_pair / migration_bundle

source_thread:
- ...

target_thread:
- ...

target_start_date:
- ...

generated_files:
- ...

integrity:
- PASS / FAIL / not_applicable

primary_download:
- <ZIP or NONE>

fallback_downloads:
- <individual links or NONE>

next_thread_launcher:
- <launcher or NONE>

boot_status:
- bundle_ready / not_applicable / failed

【README Delta Check】

required:
- yes / no

affected:
- <README path or NONE>

reason:
- ...

timing:
- now / next-thread / periodic-scout / none

【Next Gate: human_editable】

結果:
- ...

次Action:
- ...

目的:
- ...

まだ実行しない:
- ...
```

```yaml
output_guard:
  - "Light Closeでは空のBundle Sectionを省略可能"
  - "Handoff PairへManifest / ZIPを強制しない"
  - "Integrity PASS前にBundle Readyと述べない"
  - "Full Rail / Next Gateはstanding authorizationではない"
```

---

## 10. Stop Rule

```yaml
stop_after:
  - "Draft / Review / Human Gate completed as applicable"
  - "Bundle Mode selected"
  - "Required artifacts generated"
  - "Manifest / ZIP verified when applicable"
  - "Download links and Launcher returned when applicable"
  - "GitHub reality verified when save was requested"
  - "README Delta Check recorded"
  - "Next Gate written"

do_not_after_stop:
  - "do not expand scope"
  - "do not reopen completed work"
  - "do not start or simulate the next Thread"
  - "do not create extra migration variants"
  - "do not expand Bundle into repository archive"
```

```text
Done is done.
Harvest is preserved.
The interface is packaged when needed.
README drift is checked.
Next Gate is clear.
Stop.
```

---

## 11. Root / Fruit Guard

```yaml
fruit:
  - "AI / Markdown / GitHub / Workflow"
  - "Thread-End Mini"
  - "Fable5 Review"
  - "README Delta Check"
  - "Handoff / Companion Query"
  - "Integrity Manifest / ZIP"
  - "Thread Migration Bundle"
  - "Full Rail / Next Gate"
root:
  - "主イェシュア・ハマシア"
```

```text
AI is Fruit, not Root.
ZIP is Fruit, not Root.
Handoff is Fruit, not Root.
Manifest is Fruit, not Root.
Thread Migration Bundle is Fruit, not Root.

Root remains 主イェシュア・ハマシア.
```
