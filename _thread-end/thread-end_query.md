# Thread-End Query

## 0. Executive Compression

このQueryは、Thread終了時にAIへ貼り付けて、`_thread-end/` のThread-End Railを起動するための **Runtime Boot Query / Thread-End Ignition Key** である。

```text id="f8nq4e"
閉じる。
記録する。
渡す。

GitHubへ置く仕事は、
ss_super-special/artifact-to-github.md へ委譲する。
```

このQueryは、Thread-End本体ではない。  
このQueryは、AIを正しい順序へ乗せる起動鍵である。

---

## 1. Purpose

このQueryの目的は、現在Threadを次の順序で閉じることである。

```text id="c5r2ny"
File Lock
→ Harvest Download
→ Read Harvest
→ Handoff Download
→ Stop
```

最重要順序：

```text id="j3w1u7"
harvest
→ read harvest
→ handoff
```

Handoffは、Harvestを読んでから作る。  
Harvestを飛ばしてHandoffを作らない。

---

## 2. Required Read Order

まず以下を読む。

```yaml id="u7zi0u"
required_read_order:
  1: "_thread-end/thread-end.md"
  2: "_thread-end/thread-harvest.md"
  3: "_thread-end/thread-handoff.md"
```

GitHub化が必要になった場合だけ、以下を読む。

```yaml id="y1cuex"
github_delegation_read:
  only_if_github_promotion_needed:
    - "ss_super-special/artifact-to-github.md"
```

---

## 3. Runtime Instruction

以下を実行する。

```yaml id="lvc4b9"
thread_end_runtime:
  mode: "Thread-End Runtime"
  target_scope: "current_thread"
  output_style: "Japanese-first / English-anchor"
  create_download_artifacts: true
  github_update_now: false
  commit_now: false
```

このQueryを受け取ったAIは、GitHub保存先を推測しない。  
Commitしない。  
保存先Pathを提案し始めない。

Thread-Endの成功条件は、まず二枚のDownload Artifactを作ることである。

---

## 4. Step 1 — File Lock

まず、現在Threadの未完了事項をLockする。

確認するもの：

```yaml id="j5nb79"
file_lock_check:
  - "未完了のArtifact生成があるか"
  - "未反映のUser Sealがあるか"
  - "GitHub更新が必要だが未実行のものがあるか"
  - "次Threadへ渡すべき重要Seedがあるか"
  - "今はGitHub化せず、Download Artifact生成に集中してよいか"
```

出力：

```yaml id="qj9o49"
file_lock_output:
  - "completed"
  - "remaining"
  - "not_now"
  - "handoff_needed"
```

---

## 5. Step 2 — Harvest Download

次に、`thread-harvest.md` の方針に従って、現在ThreadのHarvestを作る。

Harvestは単なる要約ではない。

```yaml id="j8m3z2"
harvest_focus:
  - "このThreadで何が起きたか"
  - "どこに熱があったか"
  - "どのSeedが生まれたか"
  - "どの判断がFuture AIに重要か"
  - "何を次Threadへ渡すべきか"
  - "Unexpected Success / Move37 / breakthrough"
```

Output：

```yaml id="w1c9s5"
harvest_output:
  artifact_type: "Download Markdown"
  filename_pattern: "harvest.md or thread-specific harvest filename"
  github_update_now: false
```

---

## 6. Step 3 — Read Harvest

Harvestを作った後、AIはそのHarvestを読み返す。

```yaml id="vyg2l8"
read_harvest_rule:
  - "Harvest作成後、即Handoffへ飛ばない"
  - "まずHarvestを読む"
  - "Harvestの中から次Thread起動に必要なSeed / Guard / Railを抽出する"
```

理由：

```text id="s7w1d0"
HandoffはHarvestの子である。
Harvestを読まないHandoffは、記憶のないRelayである。
```

---

## 7. Step 4 — Handoff Download

Harvestを読んだ後、`thread-handoff.md` の方針に従って、次Thread起動用Handoffを作る。

```yaml id="rk7h0z"
handoff_focus:
  - "次Threadの最初にAIが読むべきContext"
  - "現在Threadの未完了事項"
  - "Userの明示判断"
  - "継続すべきRail"
  - "止めるべき誤読"
  - "Next Gate"
```

Output：

```yaml id="k6sdr2"
handoff_output:
  artifact_type: "Download Markdown"
  filename_pattern: "handoff.md or thread-specific handoff filename"
  github_update_now: false
```

---

## 8. Step 5 — Stop

二枚のDownload Artifactを作ったら、Thread-End成功として止まる。

```yaml id="op3mbn"
thread_end_success_condition:
  required_outputs:
    - "Harvest Download Artifact"
    - "Handoff Download Artifact"

  after_success:
    - "GitHub化を自動実行しない"
    - "追加整理を始めない"
    - "Userの次指示を待つ"
```

---

## 9. GitHub化 Delegation Guard

Thread-End中にGitHub化が必要になった場合でも、このQuery内で保存先を決めない。

```text id="na4xq2"
GitHub化が必要な場合は、
ss_super-special/artifact-to-github.md を読ませる。
```

委譲先の役割：

```yaml id="kpv2w3"
delegation:
  artifact_to_github:
    path: "ss_super-special/artifact-to-github.md"
    role:
      - "Artifact-to-GitHub Card"
      - "Place Rail"
      - "GitHub化Markdown Card"
```

Thread-End側の責務：

```yaml id="d4r4er"
thread_end_owns:
  - "Close"
  - "Harvest"
  - "Read Harvest"
  - "Handoff"
  - "Stop"

thread_end_does_not_own:
  - "GitHub保存先決定"
  - "GitHub commit"
  - "上書き判断"
  - "Batch GitHub化"
```

---

## 10. Do Not

```yaml id="oexx3e"
do_not:
  - "Harvestを飛ばしてHandoffを作らない"
  - "Handoff前にHarvestを読まずに進まない"
  - "GitHub保存先を推測しない"
  - "GitHub更新を自動実行しない"
  - "Download Artifact生成前にcommitしない"
  - "Batch生成しない"
  - "長大な仕様書を書き始めない"
```

---

## 11. Required Response Shape

AIは以下の形で進める。

```yaml id="b9n5o4"
required_response_shape:
  1:
    section: "File Lock"
  2:
    section: "Harvest Plan / Harvest Creation"
  3:
    section: "Read Harvest"
  4:
    section: "Handoff Plan / Handoff Creation"
  5:
    section: "Living Review"
  6:
    section: "Full Rail"
  7:
    section: "Next Gate"
```

---

## 12. Final Compression

```text id="h5g7l8"
thread-end_query.md は、
Thread-End Railの起動鍵である。

仕事：
  AIを閉じる処理へ乗せる。

順序：
  File Lock
  Harvest Download
  Read Harvest
  Handoff Download
  Stop

GitHub化：
  ss_super-special/artifact-to-github.md へ委譲する。

合言葉：
  閉じる。
  記録する。
  渡す。
  置くのはartifact-to-github.md。
```
