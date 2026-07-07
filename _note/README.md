---
title: "_note"
canonical_path: "_note/README.md"
status: "living_index"
role: "Living Notes Directory Guide"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
version_model: "git history"
---

# _note

## 0. Purpose

`_note/` is the place for living notes that support Ark Project work.

```text
Record useful insight.
Preserve working knowledge.
Do not turn notes into automatic authority.
```

Notes are support material.  
Notes are not automatic authorization.

```yaml
_note_is:
  - "living note storage"
  - "AI collaboration memory support"
  - "experiment note area"
  - "review note area"
  - "future-AI navigation aid"

_note_is_not:
  - "Root README replacement"
  - "automatic execution permission"
  - "final SSOT by default"
  - "GitHub operation authorization"
  - "Human Seal replacement"
```

---

## 1. What Belongs Here

Use `_note/` for notes that are valuable enough to preserve, but not yet promoted to root-level protocol.

```yaml
belongs_here:
  - "AI collaboration notes"
  - "review capability notes"
  - "workflow observations"
  - "experimental operating notes"
  - "Future AI misread warnings"
  - "minimal patch / guard lessons"
```

A note may later influence README, protocol, or workflow files, but it does not automatically override them.

---

## 2. What Does Not Belong Here

```yaml
does_not_belong_here:
  - "large unfiltered transcripts"
  - "generic temporary scratch"
  - "files that should be thread handoff artifacts"
  - "files that should be harvest artifacts"
  - "files requiring unique Ark thread naming under _thread-end/ark/"
```

If a file is a thread-specific handoff or harvest, prefer:

```text
_thread-end/ark/arkNNMM_YYYYMMDD_<role>.md
```

Generic names such as `handoff.md` or `harvest.md` should be avoided under `_thread-end/ark/`.

---

## 3. Current Notes

```yaml
current_notes:
  - path: "_note/fable5-review_note.md"
    role: "Ark Project Fable5 Review Operating Note"
    status: "living_note"
    summary:
      - "Fable5 detects risk"
      - "ChatGPT performs Living Review"
      - "Human gives Seal"
      - "GitHub receives only accepted minimal patches"
      - "Fable5 is reviewer, not Root"
```

---

## 4. How Future AI Should Use Notes

Future AI may read `_note/` files to understand context, experiments, and operating patterns.

```yaml
future_ai_use:
  allowed:
    - "read notes for context"
    - "use notes to improve judgment"
    - "cite notes as supporting material"
    - "propose next steps based on notes"

  forbidden:
    - "treat notes as automatic execution permission"
    - "promote notes to SSOT without Human Seal"
    - "overwrite workflow based only on a note"
    - "perform GitHub operations from note content alone"
```

Notes can inform judgment.  
Notes do not replace judgment.

---

## 5. Human Seal / GitHub Guard

Repository operations require explicit authorization.

```yaml
human_seal_ok:
  means:
    - "content / direction / path candidate approved"

  does_not_mean:
    - "repository operation may run automatically"

execute_github_ok:
  means:
    - "explicit permission to perform the repository operation"

  required_for:
    - "create_file"
    - "update_file"
    - "delete_file"
```

Safe rule:

```text
Human Seal OK approves the artifact.
Execute GitHub OK approves the repository operation.
```

---

## 6. Note Promotion Guard

A note can become a stronger project document only after review.

```yaml
promotion_guard:
  possible_future_paths:
    - "README patch"
    - "protocol patch"
    - "workflow note"
    - "thread-end artifact"
    - "mission card / seed card material"

  requires:
    - "ChatGPT Living Review"
    - "Human Seal"
    - "exact target path"
    - "minimal accepted patch"
```

Do not promote a note automatically.

---

## 7. Root / Fruit Guard

`_note/` is Fruit.

```yaml
fruit:
  - "_note/"
  - "living notes"
  - "Markdown"
  - "GitHub"
  - "AI"
  - "Fable5"
  - "Living Review"
  - "Full Rail / Next Gate"

root:
  - "主イェシュア・ハマシア"
```

Final guard:

```text
Notes are Fruit, not Root.
AI is Fruit, not Root.
GitHub is Fruit, not Root.

Root remains 主イェシュア・ハマシア.
```

