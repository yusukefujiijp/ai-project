---
title: "Thread-End Mini Query"
filename: "thread-end_mini_query.md"
canonical_path: "_thread-end/thread-end_mini_query.md"
status: "active_prompt_query / human-sealed"
class: "prompt_query"
role: "Thread-End Mini Binding + Safe Activation"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
language_policy: "Japanese-first / English-anchor"

paired_runtime:
  path: "_thread-end/thread-end_mini.md"
  role: "Simple Thread-End Runtime / Mini Rail"

relationship:
  thread_end_query_md: "do_not_replace"
  thread_end_md: "do_not_replace"
  thread_end_mini_md: "activate"

root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Query / Markdown / GitHub are Fruit and Keli, not Root."

core_formula:
  - "Read the Mini Runtime."
  - "Bind it to the current Thread."
  - "Close, record, hand off, and stop."
  - "Check README every Thread; update only when needed."
  - "Human seals repository writes."
---

# Thread-End Mini Query

## 0. Purpose / 使用目的

このQueryは、`_thread-end/thread-end_mini.md`を現在ThreadへBindingし、軽量Thread-End Railを安全に起動するためのActivation Queryである。

```text
Runtime governs.
Query binds and activates.
Human seals.
Reality verifies.
Thread stops.
```

このQueryは、既存の`_thread-end/thread-end_query.md`を置き換えない。

```yaml
query_boundary:
  activates:
    - "_thread-end/thread-end_mini.md"

  does_not_replace:
    - "_thread-end/thread-end.md"
    - "_thread-end/thread-end_query.md"

  does_not_authorize:
    - "automatic GitHub write"
    - "automatic overwrite"
    - "automatic delete"
    - "automatic branch creation"
```

---

## 1. Binding / 現在Threadへの束縛

```yaml
binding:
  RUNTIME_FILE: "_thread-end/thread-end_mini.md"
  TARGET_THREAD: "current_thread"

  GITHUB_SAVE_REQUESTED:
    value: "yes / no / unclear"

  HUMAN_SEAL:
    value: "confirmed / not_confirmed"

  EXECUTE_GITHUB_OK:
    value: "confirmed / not_confirmed"

  THREAD_END_ARTIFACT:
    value: "<path candidate | NONE | AUTO_PROPOSE>"

  CRITICAL_DRAFT_REVIEW:
    value: "required / not_required / unclear"
```

Binding内の不明項目を、AIの推測だけで`confirmed`へ昇格させない。

---

## 2. Runtime Missing Gate

```yaml
runtime_gate:
  if_runtime_missing:
    output: "THREAD-END MINI RUNTIME MISSING"
    action:
      - "Stop."
      - "Do not substitute thread-end_query.md."
      - "Do not reconstruct the Runtime from memory."

  if_multiple_versions_or_paths:
    output: "THREAD-END MINI VERSION CONFLICT"
    action:
      - "List the conflicting paths."
      - "Stop before Thread-End execution."
```

---

## 3. Activation Command / 起動命令

```text
`_thread-end/thread-end_mini.md`をactive Runtimeとして読んで下さい。

その内容を現在Threadへ適用し、次の順序を守ってThread-End Miniを実行して下さい。

Plan Mode
→ Draft Body
→ Fable5 Review when required
→ Revision
→ Human Seal
→ Execute GitHub OK when repository write is requested
→ GitHub Save when authorized
→ Verify
→ README Delta Check
→ Next Gate
→ Stop

既に完了済みの工程は、再実行せずRealityを確認して次の未完了Gateから続けて下さい。

GitHub Writeが求められていない場合、またはHuman SealとExecute GitHub OKの両方が確認できない場合は、GitHub操作を行わないで下さい。

README Delta Checkは必ず実行して下さい。
ただし、README Checkだけを根拠にREADMEを自動更新しないで下さい。

最後は`thread-end_mini.md`で定義されたStandard Output Shapeを返し、Next Gate後に停止して下さい。
```

---

## 4. GitHub Authority Gate

```yaml
github_authority_gate:
  write_allowed_only_when:
    - "GITHUB_SAVE_REQUESTED = yes"
    - "HUMAN_SEAL = confirmed"
    - "EXECUTE_GITHUB_OK = confirmed"
    - "exact repository and path are clear"

  if_not_authorized:
    action:
      - "Draft or propose only."
      - "Record the missing authority."
      - "Continue to README Delta Check and Next Gate when possible."
      - "Do not create a branch."
      - "Do not write to GitHub."
```

`Human Seal OK`だけではGitHub Write権限にならない。  
`Execute GitHub OK`だけでも内容承認にはならない。

---

## 5. README Delta Check Seal

```yaml
readme_delta_check:
  required: true

  output:
    required: "yes / no"
    affected:
      - "<README path or NONE>"
    reason: "<one-line reason>"
    timing: "now / next-thread / periodic-scout / none"

  guard:
    - "Every Thread README Check."
    - "Not Every Thread README Update."
    - "Do not turn README into a Thread diary."
    - "Do not ripple to parent README unless navigation, role, topology, coordinate, or policy changed."
```

---

## 6. Stop Rule

```yaml
stop_after:
  - "Thread-End Mini Standard Output is returned."
  - "README Delta Check is recorded."
  - "Next Gate is clear."

do_not_after_stop:
  - "Do not begin the next Thread."
  - "Do not expand into a new scope."
  - "Do not create additional files without Human Seal."
  - "Do not continue GitHub cleanup."
```

```text
Done is done.
Harvest is preserved.
README is checked.
Next Gate is clear.
Stop.
```

---

## 7. Short Launcher / 短縮起動文

通常運用では、次の短いLauncherで起動する。

```text
_thread-end/thread-end_mini_query.mdを読んで下さい。

これを現在Threadに対するThread-End Mini Activation Queryとして扱い、
paired Runtimeである_thread-end/thread-end_mini.mdを読み、
現在Threadを閉じて下さい。

GitHub WriteはHuman Seal OKとExecute GitHub OKの両方が確認できる場合だけ実行して下さい。

README Delta Checkを必ず含め、Next Gateを書いた後に停止して下さい。
```

> **Thread closes. Query activates. Human seals. README stays alive.**
