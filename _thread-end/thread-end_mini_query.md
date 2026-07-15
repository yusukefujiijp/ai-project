---
title: "Thread-End Mini Query"
filename: "thread-end_mini_query.md"
canonical_path: "_thread-end/thread-end_mini_query.md"
status: "active_prompt_query / human-sealed"
class: "prompt_query"
role: "Thread-End Mini Binding + Adaptive Thread Migration Activation"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
language_policy: "Japanese-first / English-anchor"
paired_runtime:
  path: "_thread-end/thread-end_mini.md"
  role: "Simple Thread-End Runtime / Adaptive Thread Migration Rail"
relationship:
  thread_end_query_md: "do_not_replace"
  thread_end_md: "do_not_replace"
  thread_end_mini_md: "activate"
bundle_support:
  mode: "adaptive"
  primary_transport: "ZIP when migration_bundle"
  fallback_transport: "individual files"
root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Query / Markdown / GitHub / ZIP are Fruit and Keli, not Root."
---

# Thread-End Mini Query

## 0. Purpose

このQueryは、`_thread-end/thread-end_mini.md`を現在ThreadへBindingし、軽量Thread-Endまたは必要時のThread Migration Bundleを安全に起動する。

```text
Runtime governs.
Query binds and activates.
Router chooses the density.
Human seals repository writes.
Reality verifies.
Thread stops.
```

このQueryは既存の`_thread-end/thread-end_query.md`を置き換えず、自動GitHub Write、上書き、削除、Branch / Workflow / Issue / PR作成を認可しない。

---

## 1. Binding

```yaml
binding:
  RUNTIME_FILE: "_thread-end/thread-end_mini.md"
  TARGET_THREAD: "current_thread"

  GITHUB_SAVE_REQUESTED: "yes / no / unclear"
  HUMAN_SEAL: "confirmed / not_confirmed"
  EXECUTE_GITHUB_OK: "confirmed / not_confirmed"
  THREAD_END_ARTIFACT: "<path candidate | NONE | AUTO_PROPOSE>"
  CRITICAL_DRAFT_REVIEW: "required / not_required / unclear"

  THREAD_MIGRATION_REQUIRED: "yes / no / unclear"
  BUNDLE_MODE: "light_close / handoff_pair / migration_bundle / auto_recommend"
  SOURCE_THREAD: "<Ark coordinate | unknown | AUTO_DETECT>"
  NEXT_THREAD: "<Ark coordinate | unknown | AUTO_PROPOSE>"
  NEXT_THREAD_START_DATE: "<YYYY-MM-DD | unknown | AUTO_PROPOSE>"
  MANIFEST_REQUIRED: "yes / no / auto"
  ZIP_REQUIRED: "yes / no / auto"
  INDIVIDUAL_DOWNLOAD_FALLBACK: "yes / no / auto"
```

```yaml
binding_guard:
  - "不明項目を推測だけでconfirmedへ昇格しない"
  - "SOURCE_THREADは会話Evidenceから復元する"
  - "NEXT_THREADとStart DateはHuman確認前に確定しない"
  - "auto_recommendは提案でありHuman Sealではない"
  - "BUNDLE_MODEはContext Complexityに適応させる"
```

---

## 2. Runtime Gate

```yaml
runtime_gate:
  if_missing:
    output: "THREAD-END MINI RUNTIME MISSING"
    action:
      - "Stop."
      - "Do not substitute another Runtime."
      - "Do not reconstruct from memory."

  if_conflict:
    output: "THREAD-END MINI VERSION CONFLICT"
    action:
      - "List visible conflicting paths."
      - "Stop."
```

---

## 3. Activation Command

```text
_thread-end/thread-end_mini.mdをactive Runtimeとして読み、
現在Threadへ適用して下さい。

Plan Mode
→ Draft Body
→ Fable5 Review when required
→ Revision
→ Human Seal
→ Thread-End Complexity Router
→ Handoff Artifacts
→ Manifest Validation when migration_bundle
→ ZIP Packaging when migration_bundle
→ Download Delivery
→ Execute GitHub OK when repository write is requested
→ GitHub Save when authorized
→ Verify
→ README Delta Check
→ Next Thread Launcher
→ Next Gate
→ Stop

完了済み工程は再実行せず、
Realityを確認して次の未完了Gateから続けて下さい。

Light Closeで十分ならZIPを生成しないで下さい。

Handoff Pairで十分ならManifestとZIPを強制しないで下さい。

Migration Bundleが適切なら、
Long-form Handoff、Companion Query、Integrity Manifest、ZIPを生成して下さい。

ZIPをPrimary Download、
個別FileをInspection / Fallbackとして提示して下さい。

次Threadを自動開始せず、
現在ThreadではBundle ReadyとLauncher Readyまでで停止して下さい。

GitHub Writeは、
Human SealとExecute GitHub OKの両方があり、
exact repository / branch / path / scopeが明確な場合だけ実行して下さい。

README Delta Checkを必ず実行し、
Next Gate後に停止して下さい。
```

---

## 4. Bundle Authority Gate

```yaml
bundle_authority_gate:
  artifact_generation:
    execute_github_ok_required: false

  github_storage:
    requires:
      - "GITHUB_SAVE_REQUESTED = yes"
      - "HUMAN_SEAL = confirmed"
      - "EXECUTE_GITHUB_OK = confirmed"
      - "exact repository and path"

  forbidden_default_infrastructure:
    - "temporary branch"
    - "temporary workflow"
    - "issue trigger"
    - "pull request"
    - "multi-step GitHub reconstruction"

  if_infrastructure_is_needed:
    - "Stop before creation."
    - "Classify as Material Scope Expansion."
    - "Request Fresh Human Seal."
```

---

## 5. Bundle Integrity Gate

```yaml
bundle_integrity_gate:
  when: "BUNDLE_MODE = migration_bundle"
  required:
    - "expected artifacts exist"
    - "Manifest is generated from actual files"
    - "bytes / lines / sha256 match"
    - "ZIP opens"
    - "ZIP contents match Manifest"

  if_failed:
    output: "THREAD MIGRATION BUNDLE INTEGRITY FAIL"
    action:
      - "Do not claim Bundle Ready."
      - "Do not present failed ZIP as primary."
      - "Report the exact failed check."
      - "Preserve safe individual artifacts."
```

---

## 6. GitHub Authority Gate

```yaml
github_authority_gate:
  write_allowed_only_when:
    - "GITHUB_SAVE_REQUESTED = yes"
    - "HUMAN_SEAL = confirmed"
    - "EXECUTE_GITHUB_OK = confirmed"
    - "exact repository and path are clear"

  if_not_authorized:
    - "Draft or propose only."
    - "Record missing authority."
    - "Do not create a branch."
    - "Do not write to GitHub."
```

`Human Seal OK`だけではGitHub Write権限にならない。  
`Execute GitHub OK`だけでも内容承認にはならない。

---

## 7. README Delta Check

```yaml
readme_delta_check:
  required: true
  output:
    required: "yes / no"
    affected: "<README path or NONE>"
    reason: "<one-line>"
    timing: "now / next-thread / periodic-scout / none"
  guard:
    - "Every Thread README Check."
    - "Not Every Thread README Update."
    - "Do not turn README into a Thread diary."
    - "Bundleを作っただけでREADME更新を自動要求しない"
    - "Policy / Role / Read Orderが変わった時だけ候補"
```

---

## 8. Stop Rule

```yaml
stop_after:
  - "Standard Output returned"
  - "Adaptive Bundle Mode selected"
  - "Required artifacts generated"
  - "Integrity verified when applicable"
  - "Downloads and Launcher returned when applicable"
  - "README Delta Check recorded"
  - "Next Gate clear"

do_not_after_stop:
  - "Do not begin or simulate the next Thread."
  - "Do not expand scope."
  - "Do not create additional variants."
  - "Do not continue GitHub cleanup."
```

```text
Done is done.
Harvest is preserved.
The interface is packaged when needed.
README is checked.
Next Gate is clear.
Stop.
```

---

## 9. Short Launcher

```text
_thread-end/thread-end_mini_query.mdを読んで下さい。

paired Runtimeである_thread-end/thread-end_mini.mdを読み、
現在Threadを閉じて下さい。

Thread-End Complexity Routerを使用し、
Light Close / Handoff Pair / Thread Migration Bundleから
現在Contextに適したModeを選んで下さい。

高Context移行では、
Long-form Handoff、Companion Query、Integrity Manifest、ZIPを生成し、
ZIPをPrimary、個別FileをFallbackとして提示して下さい。

Bundle生成とGitHub Writeを混同しないで下さい。

GitHub WriteはHuman Seal OKとExecute GitHub OKの両方がある場合だけ実行して下さい。

README Delta Check、Next Thread Launcher、Next Gateを書いた後に停止して下さい。
```

> **Thread closes. Memory is structured. Interface is packaged. Human transports. Next mission reboots.**
