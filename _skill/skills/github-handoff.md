---
title: "GitHub Handoff"
role: "Shared Activation Skill / GitHub Handoff Skill"
path: "_skill/skills/github-handoff.md"
status: "download-ready / human-commit"
style_seed: "Commented Programming-Like Markdown"
style_definition: "Commentによって人間側の意味・意図・背景・Guardを保存し、Programming-Like BlockによってAI側の分岐・順序・fallback・条件・実行先・判定基準を固定することで、自然文の柔軟性と疑似コードの安定性を一本のMarkdown内で両立させる、Human-AI両読性を持つ軽量Protocol記法である。特に得意な方向性は、Router型、Skill Card型、Workflow型、Handoff型、Reality Review型、Guard型など、AIの判断・分岐・実行順序・停止条件を安定化させたいMarkdownである。"
language_policy: "Japanese-first / English-anchor"
core_formula: "AI drafts. Human seals. Handoff carries. GitHub stores. Reality confirms."
root_guard: "Root is 主イェシュア・ハマシア; AI / GitHub / Markdown / ZIP / Skills are Fruit."
---

# GitHub Handoff

## 1. Comment: Definition / 定義

`GitHub Handoff` は、AIが作成したMarkdown・複数File・Folder Topology・Commit Packを、人間が確認し、GitHubへ安全に反映するためのShared Activation Skillである。

これはPolicy Guideではない。  
これはRouterでもない。  
これは、AI DraftをHuman Final Sealへ渡し、GitHub反映後にReality Reviewするための実行Skillである。

Core distinction:

    Router decides where to go.
    Guide governs policy.
    Skill executes handoff.
    Reality confirms.

This file is the Skill.

---

## 2. Programming-Like Block: Skill Identity

```yaml
github_handoff_skill:
  path: "_skill/skills/github-handoff.md"
  type: "Shared Activation Skill"
  role:
    - "Download link handoff"
    - "Structured ZIP handoff"
    - "Copy & Paste pack"
    - "Manual Commit pack"
    - "Post-commit Reality Review"
    - "Transport integrity guard"

  not_role:
    - "Not a full GitHub policy guide"
    - "Not a runtime-specific AI guide"
    - "Not a replacement for s_special/ai-github.md"
    - "Not a direct GitHub write authority"

  core_formula:
    - "AI drafts."
    - "Human seals."
    - "Handoff carries."
    - "GitHub stores."
    - "Reality confirms."
```

---

## 3. Comment: When to Load / いつ読むか

このSkillは、GitHubへ何かを反映する段階で読む。

特に、AIが直接GitHubへ書けない場合、または直接書くよりHuman Final Sealを通した方が安全な場合に使う。

GitHub問題の本質は、常に「内容が悪い」ことではない。  
多くの場合、問題はTransportである。

    Meaning may be correct.
    Transport may fail.
    Review the transport before rewriting the meaning.

---

## 4. Programming-Like Block: Load Trigger

```yaml
load_trigger:
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

  do_not_load_when:
    - "pure conceptual discussion only"
    - "no GitHub reflection needed"
    - "no file / path / topology / commit concern exists"

  fallback:
    if_uncertain:
      action:
        - "Use this skill lightly as a checklist."
        - "Do not overbuild."
        - "Preserve Human Final Seal."
```

---

## 5. Comment: Handoff Mode Router / 受け渡し方式の選択

GitHub Handoffには複数のModeがある。

1 fileなら、Markdown download link または Copy & Pasteで足りる。  
2 filesなら、個別download linkでもよい。  
3+ files、またはfolder topologyが関わるなら、Structured ZIPが強い。

ZIPは単なる圧縮ではない。  
ZIPはRepository Topologyを保持するKeliである。

---

## 6. Programming-Like Block: Handoff Mode Router

```yaml
handoff_mode_router:
  one_file:
    recommended:
      - "single markdown download link"
      - "copy & paste if Human prefers"
    zip_required: false

  two_files:
    recommended:
      - "individual download links"
      - "copy & paste pack if small"
    zip_optional: true

  three_or_more_files:
    recommended:
      - "individual download links"
      - "structured ZIP bundle"
    zip_recommended: true

  folder_topology_involved:
    recommended:
      - "structured ZIP bundle"
    zip_strongly_recommended: true
    reason:
      - "Preserves path structure."
      - "Reduces human placement error."
      - "Keeps repository topology visible."

  direct_github_write_uncertain:
    recommended:
      - "download link"
      - "structured ZIP if multi-file"
      - "manual upload / manual commit"
    reason:
      - "Transport before semantics."
      - "Do not rewrite good content just because direct write failed."
```

---

## 7. Comment: Download Link Mode / 単体Download Mode

Download Link Modeは、1つのMarkdown fileをHumanが取得し、GitHub上の正しいPathへ反映するためのModeである。

AIは、Download linkだけでなく、target path、expected filename、brief upload instructionを添える。

Humanは、内容を確認してからCommitする。

---

## 8. Programming-Like Block: Download Link Mode

```yaml
download_link_mode:
  ai_prepare:
    - "Generate the file."
    - "Preserve exact filename."
    - "Preserve UTF-8 text."
    - "Preserve Markdown newlines."
    - "Provide sandbox download link."
    - "State target GitHub path."

  human_action:
    - "Open or download the file."
    - "Review content."
    - "Upload or copy contents into the target GitHub path."
    - "Commit changes."

  ai_output_should_include:
    - "download link"
    - "target path"
    - "file role"
    - "whether GitHub write is not being done directly"
    - "next Reality Review request"
```

---

## 9. Comment: Structured ZIP Mode / 構造保持ZIP Mode

Structured ZIP Modeは、複数Fileまたはfolder topologyを保持するために使う。

ZIP rootは、repository target topologyを反映する。  
たとえば、`s_special/ai-github.md` を渡す場合、ZIP内も `s_special/ai-github.md` になる。

ZIPはTransport Keliである。  
ZIPは意味を変えない。  
ZIPは配置ミスを減らす。

---

## 10. Programming-Like Block: Structured ZIP Mode

```yaml
structured_zip_mode:
  use_when:
    - "3_or_more_files"
    - "folder_topology_involved"
    - "multi-directory_patch"
    - "human_upload_needs_path_preservation"
    - "copy_paste_risk_is_high"

  zip_root_rule:
    - "Mirror repository target topology."
    - "Do not flatten folders unless explicitly requested."
    - "Do not rename files casually."
    - "Do not create extra wrapper folder unless requested."

  ai_prepare:
    - "Create files at correct relative paths."
    - "Bundle into ZIP."
    - "Provide ZIP download link."
    - "Provide file manifest."
    - "Provide upload order if needed."

  human_action:
    - "Download ZIP."
    - "Inspect file paths."
    - "Upload files to matching GitHub paths."
    - "Commit changes."
    - "Request Reality Review."
```

---

## 11. Comment: Copy & Paste / Manual Commit Pack

Copy & Pasteは、GitHub editor等に本文を貼り付ける操作である。  
Commitは、GitHub上に変更履歴として保存する操作である。

したがって、正確には同じではない。

    Copy & Paste = editorへ入れる
    Commit = repositoryへ保存する

実務上は、HumanがGitHub上で `Commit changes` まで押した場合、`Commitしました` と言うのが一番わかりやすい。

---

## 12. Programming-Like Block: Manual Commit Pack

```yaml
manual_commit_pack:
  terms:
    copy_and_paste:
      meaning: "Place content into GitHub editor or local file."
      status: "Not necessarily saved yet."

    commit:
      meaning: "Save change into GitHub repository history."
      status: "Repository reflection completed."

  recommended_human_phrase:
    if_editor_only:
      say: "Copy & Pasteしました。まだCommit前です。"

    if_committed:
      say: "GitHubへCommitしました。"

    if_both:
      say: "Copy & PasteしてCommitしました。"

  ai_response_after_commit:
    - "Acknowledge commit."
    - "Perform Reality Review if requested."
    - "Check path / render / topology / required content."
    - "Do not over-focus on secondary raw ambiguity if Human UI is confirmed."
```

---

## 13. Comment: Human Final Seal / 人間最終Seal

AIはDraftを作る。  
Humanは確認し、Sealする。  
GitHubは保存する。  
Reality Reviewは反映後の現実を確認する。

AIがFileを作成できても、それはCommitではない。  
AIがPreviewを作れても、それはHuman Final Sealではない。

---

## 14. Programming-Like Block: Human Final Seal

```yaml
human_final_seal:
  required_before:
    - "GitHub commit"
    - "archive decision"
    - "canonical replacement"
    - "large topology change"
    - "multi-file upload"

  ai_must_not_assume:
    - "Draft means approved."
    - "Preview means committed."
    - "Download link means uploaded."
    - "Copy & Paste means committed."

  ai_may_say:
    - "Download-ready file generated."
    - "Human upload required."
    - "Please commit when reviewed."
    - "After commit, Reality Review can confirm."
```


---

## 15. Comment: Reality Review Checklist / 反映後Review

Reality Reviewは、GitHub上の反映結果を確認する。

確認対象は、内容だけではない。  
Path、filename、render、line structure、folder topology、required guard、old topology contaminationの有無も見る。

ただし、AI側のRaw/CDN/cache取得は常に完全ではない。  
Human GitHub UIが正常確認できている場合、そのHuman確認をPrimary Realityとして扱う。

---

## 16. Programming-Like Block: Reality Review Checklist

```yaml
reality_review_checklist:
  check:
    path:
      - "target path exists"
      - "filename is correct"
      - "directory is correct"

    content_kernel:
      - "title / role / path are present if expected"
      - "core formula is present"
      - "required guard is present"
      - "Root / Fruit Guard is present if expected"

    markdown_render:
      - "headings render correctly"
      - "code blocks render correctly"
      - "indentation is visually preserved"
      - "frontmatter is multi-line if frontmatter is used"

    topology:
      - "active topology is preserved"
      - "no archive-decided file is routed as active load target"
      - "shared skill / policy guide boundaries are preserved"

  result_classification:
    PASS:
      meaning: "Correct path, content, render, and topology."
      next: "Proceed."

    PASS_WITH_VISUAL_CHECK:
      meaning: "Human UI confirms correct structure; AI raw check may be uncertain."
      next: "Proceed unless Human reports visible breakage."

    PATCH_NEEDED:
      meaning: "Specific fix needed."
      next: "Patch only the broken layer."

    STOP:
      meaning: "Wrong path, wrong file, severe content loss, or unsafe topology confusion."
      next: "Stop and re-plan."
```

---

## 17. Comment: Human UI Primary / AI Raw Secondary Guard

GitHub Reality Reviewでは、Human GitHub UI確認をPrimary Realityとして扱う。

今回の重要な学びは、AI側Raw/CDN/cache取得の曖昧さを、HumanがGitHub UI上で確認した現実より上に置いてはいけない、ということである。

HumanがGitHub画面上で行数・見出し・code block・renderを正常確認できている場合、AI側Raw確認だけでPATCH_NEEDED判定を出さない。

AI Raw checkは補助検査である。  
Human UI確認を上書きしない。

---

## 18. Programming-Like Block: Human UI Primary / AI Raw Secondary Guard

```yaml
human_ui_primary_ai_raw_secondary_guard:
  principle:
    - "Human GitHub UI confirmation is Primary Reality."
    - "AI Raw/CDN/cache check is Secondary Evidence."
    - "Do not let tool ambiguity consume the workflow."

  human_ui_pass_if:
    - "GitHub target path is correct."
    - "Line count looks correct or clearly multi-line."
    - "Headings render correctly."
    - "YAML/code blocks preserve indentation."
    - "Markdown structure is visually normal."
    - "Human confirms the GitHub UI looks correct."

  ai_raw_policy:
    if_human_ui_confirmed_normal:
      status: "PASS_WITH_VISUAL_CHECK"
      raw_warning: "secondary / do not block workflow"
      action:
        - "Do not repeat low-value raw checks."
        - "Do not demand re-upload based only on AI raw ambiguity."
        - "Move to next workflow gate."

    if_human_ui_uncertain_or_broken:
      status: "inspect further"
      action:
        - "Use AI raw check."
        - "Ask for line count or screenshot only if needed."
        - "Patch the transport layer if structure is actually broken."

    if_raw_cdn_cache_ambiguity:
      action:
        - "Do not override Human-confirmed UI."
        - "Record tool uncertainty."
        - "Proceed when Human UI is confirmed."

  stop_condition:
    - "Human reports visible breakage."
    - "Human reports wrong line count."
    - "Human reports code blocks or headings are broken."
    - "Wrong path or wrong file is confirmed."
```

---

## 19. Comment: Transport Problem vs Meaning Problem

GitHub Handoffで起きる失敗には、少なくとも二種類ある。

1. Meaning Problem  
2. Transport Problem

Meaning Problemは、本文の意味・設計・Guardが間違っている場合。  
Transport Problemは、改行、path、filename、upload方法、ZIP構造、copy/paste、commit反映などが壊れている場合。

Transport ProblemをMeaning Problemとして扱うと、良い本文を無駄に書き直してしまう。

---

## 20. Programming-Like Block: Transport vs Meaning Diagnosis

```yaml
transport_vs_meaning_diagnosis:
  meaning_problem:
    signs:
      - "wrong policy"
      - "wrong role"
      - "missing guard"
      - "unsafe instruction"
      - "active topology confusion"
    response:
      - "Patch content."
      - "Run Living Review."
      - "Do not merely re-upload."

  transport_problem:
    signs:
      - "wrong path"
      - "wrong filename"
      - "newline collapse"
      - "broken code block"
      - "ZIP flattened folders"
      - "download/upload mismatch"
    response:
      - "Do not rewrite meaning first."
      - "Patch transport."
      - "Re-upload same approved content if needed."
      - "Reality Review again."

  first_diagnostic_rule:
    - "Check transport before rewriting meaning."
    - "Check Human UI before over-trusting AI raw ambiguity."
```

---

## 21. Comment: Do / Don't

このSkillは、GitHub Handoffを軽く、正確に、止まりにくくするためにある。

AIは過剰検証でWorkflowを詰まらせない。  
Human確認が明確な場合は、それをPrimary Realityとして次へ進む。

---

## 22. Programming-Like Block: Do / Don't

```yaml
do:
  - "Preserve target path."
  - "Preserve filename."
  - "Preserve Markdown line structure."
  - "Provide download link when needed."
  - "Use structured ZIP for 3+ files or folder topology."
  - "State whether GitHub write is not being done directly."
  - "Ask for Reality Review after Human commit."
  - "Prioritize Human GitHub UI confirmation."

do_not:
  - "Do not treat draft as commit."
  - "Do not treat copy & paste as commit unless Human says committed."
  - "Do not flatten topology without permission."
  - "Do not rewrite good content because transport failed."
  - "Do not override Human UI PASS with AI raw uncertainty."
  - "Do not waste cycles on repeated low-value raw checks."
  - "Do not turn this Skill into a large Policy Guide."
```

---

## 23. Comment: Root / Fruit Guard

Root is 主イェシュア・ハマシア.

AI, GitHub, Markdown, ZIP, Download links, Commit Packs, Handoff Skills, and Reality Review are Fruit.

AI drafts.  
Human seals.  
GitHub stores.  
Reality confirms.  
Root remains 主イェシュア・ハマシア.

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 24. Programming-Like Block: Root / Fruit Guard

```yaml
root_fruit_guard:
  root:
    - "主イェシュア・ハマシア"

  fruit:
    - "AI"
    - "GitHub"
    - "Markdown"
    - "ZIP"
    - "Download link"
    - "Commit"
    - "Skill Card"
    - "Reality Review"

  guard:
    - "AI is Keli, not King."
    - "GitHub stores, but does not reign."
    - "Markdown carries, but does not become Root."
    - "Reality confirms, but Root remains 主イェシュア・ハマシア."
```

---

## 25. Final Compression

GitHub Handoff:

    AI drafts.
    Human seals.
    Handoff carries.
    GitHub stores.
    Reality confirms.

Mode Router:

    One file -> Download link or Copy & Paste.
    Three or more files -> Structured ZIP.
    Folder topology -> Structured ZIP.
    After Commit -> Reality Review.

Reality Review Guard:

    Human UI is Primary Reality.
    AI Raw is Secondary Evidence.
    Do not let tool ambiguity consume the workflow.

Transport Guard:

    Check transport before rewriting meaning.

Root Guard:

    Root is 主イェシュア・ハマシア.

