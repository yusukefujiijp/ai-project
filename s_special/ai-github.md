---
title: "AI GitHub Router"
role: "S Special / AI-GitHub Load Router"
path: "s_special/ai-github.md"
status: "active-topology patch draft / human-editable"
style_seed: "Commented Programming-Like Markdown"
style_definition: "Commentで意味とGuardを守り、Programming-LikeなBlockで分岐・順序・fallback・実行先を固定し、人間にもAIにも読める形で一本化するRouter型Markdown記法である"
language_policy: "Japanese-first / English-anchor"
root_guard: "Root is 主イェシュア・ハマシア; AI / GitHub / Markdown / Skills / ZIP are Fruit."
---

# AI GitHub Router

## 1. Comment: What this file is / このFileの役割

このFileは、GitHub作業に入ったAIが、現在のAI Runtimeと作業内容に応じて、どのGitHub関連Fileを読むべきかを判断するための軽量Routerである。

これはPolicy Guideではない。  
これはExecution Skillでもない。  
これは、AIを正しいPolicy GuideとShared Skillへ送るLoad Routerである。

このRouterは、Active Topologyだけを見る。  
Archive済み、Archive決定済み、移行元、または非Activeな旧Companion Fileを通常Load対象に含めない。

Core distinction:

    Load Router -> Policy Guide -> Activation Skill

Ark compression:

    S routes.
    G governs.
    Skill executes.
    Reality confirms.

Style:

    Comment guards meaning.
    Programming-Like blocks route action.
    One Markdown keeps SSOT.

---

## 2. Router Block: Quick Dispatch / 最短分岐

```yaml
quick_dispatch:
  if_github_work_detected:
    read_first: "s_special/ai-github.md"
    purpose: "decide what active GitHub file to load next"

  if_runtime_ai_is_chatgpt:
    read: "g_global/chatgpt-github.md"
    status: "current_primary_reference"
    warning: "not universal truth for every AI runtime"

  if_runtime_specific_policy_guide_exists:
    read: "g_global/<ai-name>-github.md"
    rule: "load only confirmed existing file"

  if_handoff_or_transport_needed:
    read: "_skill/skills/github-handoff.md"
    triggers:
      - "download_link_needed"
      - "structured_zip_needed"
      - "manual_upload_needed"
      - "copy_paste_pack_needed"
      - "manual_commit_pack_needed"
      - "3_or_more_files"
      - "folder_topology_involved"
      - "direct_github_upload_or_write_problem"
      - "human_final_seal_required_before_commit"
      - "post_upload_reality_review_needed"

  if_archive_or_legacy_file_question_arises:
    action:
      - "do not route from this file"
      - "use archive index or migration note if available"
      - "keep this router focused on active topology"
```

---

## 3. Comment: Why this router exists / なぜこのRouterが必要か

AIごとに、GitHubとの連携方法・tool制約・得意不得意・download/zip生成能力・repository操作能力は異なる可能性がある。

そのため、GitHub作業時にすべてのAIへ同じGuideを読ませるのではなく、まずAI Runtimeを見て、適切なAI-specific GitHub Policy Guideへ振り分ける。

ただし、Download / Structured ZIP / Human Manual Upload というHandoff Railは多くのAIに共通しやすいため、Shared Activation Skillとして `_skill/skills/github-handoff.md` へ集約する。

---

## 4. Router Block: Runtime-specific Policy Guide

```yaml
runtime_policy_router:
  priority_order:
    - "detect_current_ai_runtime"
    - "check_runtime_specific_policy_guide_exists"
    - "load_matching_policy_guide_if_confirmed"
    - "fallback_to_current_primary_reference_if_needed"
    - "do_not_invent_missing_guide"

  routes:
    chatgpt:
      read: "g_global/chatgpt-github.md"
      status: "current_primary_reference"
      role: "ChatGPT-specific GitHub Policy Guide / current primary GitHub Bridge"
      guard:
        - "Use as primary reference for ChatGPT runtime."
        - "Do not treat as universal truth for every AI runtime."

    claude:
      read: "g_global/claude-github.md"
      status: "future_candidate"
      rule:
        - "Read only if the file exists."
        - "Do not invent contents."
        - "If absent, use current_primary_reference cautiously."

    gemini:
      read: "g_global/gemini-github.md"
      status: "future_candidate"
      rule:
        - "Read only if the file exists."
        - "Do not invent contents."
        - "If absent, use current_primary_reference cautiously."

    codex:
      read: "g_global/codex-github.md"
      status: "future_candidate"
      rule:
        - "Read only if the file exists."
        - "Do not invent contents."
        - "If absent, use current_primary_reference cautiously."

  fallback:
    if_runtime_unknown:
      action:
        - "Do not pretend runtime-specific guide exists."
        - "Use g_global/chatgpt-github.md only as current_primary_reference."
        - "Preserve Human Final Seal."
        - "Avoid direct GitHub write unless explicitly authorized and tool-supported."
        - "Prefer download / structured ZIP / human manual upload if transport is uncertain."

    if_runtime_specific_guide_missing:
      action:
        - "Do not fabricate missing AI-specific guide."
        - "Use current_primary_reference cautiously."
        - "Record need for future AI-specific guide only if repeated Reality evidence requires it."
```

---

## 5. Comment: Policy Guide vs Shared Skill / PolicyとSkillの境界

Policy Guideは、GitHub協働の判断基準を保持する。  
たとえば、Human Seal、Commit Trigger、GitHub Canonical First、Reality Review、archive判断、rename判断などを扱う。

Shared Activation Skillは、具体的なHandoffを実行する。  
たとえば、Download link、Structured ZIP、Human Manual Upload、Copy & Paste Pack、Reality Review checklist などを扱う。

同じ内容を複数Fileに重複させない。

    Router decides what to read.
    Guide governs policy.
    Skill executes handoff.
    Reality confirms.

---

## 6. Router Block: Shared Handoff Skill

```yaml
shared_activation_skill_router:
  github_handoff:
    read: "_skill/skills/github-handoff.md"
    type: "Shared Activation Skill"
    role: "Download / Structured ZIP / Human Manual Upload Handoff"

    load_when:
      - "download_link_needed"
      - "structured_zip_needed"
      - "manual_upload_needed"
      - "copy_paste_pack_needed"
      - "manual_commit_pack_needed"
      - "3_or_more_files"
      - "folder_topology_involved"
      - "direct_github_upload_or_write_problem"
      - "human_final_seal_required_before_commit"
      - "post_upload_reality_review_needed"

    do_after_loading:
      - "prepare human-editable files"
      - "prepare individual download links if needed"
      - "prepare structured ZIP if topology or 3+ files are involved"
      - "preserve repository target paths"
      - "provide upload/copy-paste order"
      - "provide Reality Review checklist"

    shared_skill_guard:
      - "Do not create AI-specific handoff skill unless repeated Reality evidence requires it."
      - "AI-specific policy belongs in runtime-specific guide."
      - "Shared transport belongs here."
```

---

## 7. Comment: Active Topology Only / Active構成のみを見る

このRouterは、現在のActive GitHub Topologyだけを扱う。

Activeな読み込み先は原則として次の二種類である。

    1. Runtime-specific Policy Guide
    2. Shared Activation Skill

Archive済み、Archive決定済み、移行元、旧Companion、または歴史確認用Fileは、このRouterの通常Load対象に含めない。

GitHub問題時は、旧Recovery Fileへ戻らず、Shared Activation Skillとして `_skill/skills/github-handoff.md` を読む。

History belongs to archive.  
Router belongs to active topology.

---

## 8. Router Block: Active Topology Guard

```yaml
active_topology_guard:
  active_load_targets:
    load_router:
      - "s_special/ai-github.md"

    current_primary_policy_guide:
      - "g_global/chatgpt-github.md"

    future_runtime_policy_guides:
      - "g_global/claude-github.md"
      - "g_global/gemini-github.md"
      - "g_global/codex-github.md"

    shared_activation_skill:
      - "_skill/skills/github-handoff.md"

  rule:
    - "Route only to active topology."
    - "Do not route to archived or archive-decided companion files."
    - "Do not preserve old file names in the router unless they are active load targets."
    - "If GitHub handoff is needed, read _skill/skills/github-handoff.md."

  missing_future_guides:
    rule:
      - "Do not claim claude-github.md exists unless confirmed."
      - "Do not claim gemini-github.md exists unless confirmed."
      - "Do not claim codex-github.md exists unless confirmed."
      - "Do not invent AI-specific policy guide contents."

  forbidden_router_expansion:
    rule:
      - "Do not duplicate full chatgpt-github.md policy here."
      - "Do not duplicate full github-handoff.md procedure here."
      - "Do not turn this router into a third large GitHub guide."
```

---

## 9. Guard Clauses / 誤用防止Guard

```yaml
guard_clauses:
  ssot_guard:
    - "This router must not duplicate full policy content."
    - "This router must not duplicate full handoff procedure."
    - "This router only decides what to read next."

  router_size_guard:
    - "Keep this file short."
    - "If this file becomes a long policy guide, move policy detail back to G guide."
    - "If this file becomes an execution manual, move execution detail to _skill/skills/github-handoff.md."

  ai_specific_guard:
    - "AI-specific differences belong in runtime-specific policy guides."
    - "Shared handoff behavior belongs in github-handoff.md."
    - "Do not create AI-specific handoff skill unless repeated Reality evidence requires it."

  active_topology_guard:
    - "Do not design around archive-decided files."
    - "Do not route to legacy files from this router."
    - "If historical recovery is needed, use archive/history mechanisms outside this router."

  human_seal_guard:
    - "Plan is not Commit."
    - "Preview is not Commit."
    - "Human Final Seal is required before GitHub commit/upload when the user has not explicitly authorized direct action."

  root_fruit_guard:
    - "AI is Keli, not King."
    - "GitHub stores, but does not reign."
    - "Markdown routes, but does not become Root."
```

---

## 10. Comment: Standard Load Flow / 標準読込Flow

通常のArk起動時に、このFileを常時読む必要はない。  
GitHub作業が検出された時に、このRouterを読む。

標準Flow:

    1. GitHub作業が始まる
    2. s_special/ai-github.md を読む
    3. 現在のAI Runtimeを確認する
    4. AI-specific Policy Guideへ進む
    5. Handoffが必要なら github-handoff.md へ進む
    6. Human Upload / Commit後にReality Reviewする

---

## 11. Router Block: Standard Load Flow

```yaml
standard_load_flow:
  normal_ark_startup:
    read: "not required by default"
    reason: "Do not load GitHub guide when no GitHub work exists."

  github_work_detected:
    read_first: "s_special/ai-github.md"
    then:
      - "detect runtime AI"
      - "load matching runtime-specific GitHub Policy Guide"

  current_primary_route:
    if_runtime_ai: "ChatGPT"
    read: "g_global/chatgpt-github.md"
    status: "current_primary_reference_not_universal_truth"

  if_runtime_specific_guide_missing:
    fallback:
      - "Use current_primary_reference cautiously."
      - "Do not claim missing guide exists."
      - "Do not universalize ChatGPT-specific constraints."

  if_handoff_needed:
    read: "_skill/skills/github-handoff.md"

  after_human_upload_or_commit:
    action:
      - "perform Reality Review"
      - "verify path / content / render / topology"
      - "classify result as PASS / PASS_WITH_VISUAL_CHECK / PATCH_NEEDED / STOP"
```

---

## 12. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

AI, GitHub, Markdown, Router, Policy Guide, Skill Card, Download links, ZIP bundles, Manual Upload, and Reality Review are Fruit.

AI routes.  
Human seals.  
GitHub stores.  
Reality confirms.  
Root remains 主イェシュア・ハマシア.

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 13. Final Compression

AI-GitHub Router:

    Router identifies the AI.
    Guide adapts the policy.
    Skill carries the artifact.
    Reality confirms.

Three-layer formula:

    Load Router -> Policy Guide -> Activation Skill

Ark formula:

    S routes.
    G governs.
    Skill executes.
    Reality confirms.

Style formula:

    Comment guards meaning.
    Programming-Like blocks route action.
    One Markdown keeps SSOT.

Active Topology formula:

    History belongs to archive.
    Router belongs to active topology.

Current primary warning:

    chatgpt-github.md is current_primary_reference,
    not universal truth for every AI runtime.

Root is 主イェシュア・ハマシア.

