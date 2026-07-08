# X DeepQuote 02R: Course-Correction Gate v001-3

```text
filename: x-deepquote_02r-fresh-contribution-loop_v001-3.md
stage: 02R
role: Full Selected Candidate Execution / Course-Correction Gate / Source Re-anchoring Gate
status: grok-facing / full-02r / safety-escalation / stop-lock / source-re-anchoring / markdown-handoff
root: 主イェシュア・ハマシア
fruit: Grok / ChatGPT / Fable5 / X / GitHub / Markdown / Revenue
```

## 0. Purpose

Use this Markdown only when Lite is unsafe, unclear, stale, mixed, or drifting.

02R is not the default route.

02R is the course-correction route.

02R exists to re-anchor the revision to the original source and return the post to the correct trajectory.

---

## 1. Use When

Use 02R when:

```text
Mechanical Routing says Full 02R
Lite conditions fail
Lite output drifted
Source Safety is uncertain
Voice attribution is unclear
selected candidate may mix with other candidates
runtime_pass >= 3
source context is stale or far away
post became scattered
publish_ready was reached but another loop was suggested
```

Do not use 02R for ordinary light polishing.

Do not use 02R when Lite is clearly safe.

---

## 2. Required Inputs

02R requires:

```text
1. original source post text
2. Stage 01 draft
3. previous Final Quote Post
4. previous Fresh Contribution
5. previous Candidate Deck
6. selected candidate
7. current concern / reason for 02R
8. previous Source Safety
9. previous Risk Flag
10. runtime_pass
```

If original source post text is missing, output only:

```text
No Source Access.
```

If previous Final Quote Post is missing, output only:

```text
No Previous Final Quote Post.
```

---

## 3. Visible Runtime Header Rule

Every Markdown artifact content must start with:

```text
Runtime Header:
```

Use:

```text
stage: 02R_course_correction_gate
runtime_pass:
loop_policy: no_hard_cap__natural_stop
loop_status: continue / stop_recommended / publish_ready
```

Do not use YAML frontmatter inside the Markdown artifact result.

---

## 4. Course-Correction Principle

02R is not a new creativity loop.

02R must correct one or more of these dangers:

```text
source_safety drift
voice_attribution drift
context_decay drift
candidate_mixing drift
loop_addiction drift
```

The goal is:

```text
re-anchor to source
preserve useful contribution
remove unsupported additions
return to publishable direction
stop when publish-ready
```

---

## 5. Source Re-Anchoring Rule

Use original source post text as the source of truth.

Every claim in the revised Final Quote Post must be categorized as:

```text
source_claim
safe_interpretation
YusukeJP_application
needs_check
```

If a claim cannot be safely anchored, demote, soften, or remove it.

Do not invent source facts.

Do not use memory as source.

Do not write "as the original poster said" unless the source text supports it.

---

## 6. Selected Candidate Rule

Execute only the selected candidate unless safety requires modification.

If the selected candidate is unsafe as written:

```text
modify it to a safer version
or mark Source Safety needs_check
or choose stop if the post is already publish-ready
```

Do not combine unselected candidates unless explicitly necessary for source safety.

If you modify the selected candidate, explain in Correction Diagnosis.

---

## 7. Contribution Stack Rule

Preserve the contribution history.

Output a Contribution Stack showing:

```text
previous Fresh Contribution
selected candidate contribution
02R correction contribution
```

This prevents hidden drift.

If a previous contribution was removed, say so.

---

## 8. Publish-Ready Stop Lock

If:

```text
loop_status: publish_ready
```

then:

```text
AI Recommendation:
choose: stop
```

is mandatory.

No other recommendation is allowed.

When publish-ready, Candidate Deck must be stop-oriented only:

```text
1. stop and publish after light human edit
2. stop and preserve current version
3. stop and move to posting lane
```

Do not offer new mechanism / boundary / action candidates when publish-ready.

---

## 9. Source Safety / Evidence-or-Demote

Use original source post text as source of truth.

The following must be locatable in original source text:

```text
proper nouns
numbers
dates
names
model names
organizations
direct attributions
claims about what the source poster said
```

If any item cannot be located:

```text
Source Safety:
status: needs_check
```

If selected candidate introduces unsupported source facts, remove it, soften it, or mark Source Safety needs_check/hold.

---

## 10. Voice Attribution Guard

Do not write the source poster's first-person experience as if it belongs to YusukeJP.

Risky forms:

```text
I did
僕の
私の
雇いました
試しました
感じました
今日
明日
```

Safe forms:

```text
元ポストでは...
投稿者は...
この事例では...
原文投稿時点では...
```

If voice attribution is unclear, Source Safety must be `needs_check`.

---

## 11. Candidate Deck Rule

After executing the selected candidate, output the next Candidate Deck only if further refinement may help.

Do not output generic Human Edit Notes.

If publish-ready, all candidates must be stop-oriented.

Each candidate must include:

```text
type
candidate
value_added
source_safety_risk
best_for
```

If loop_status is publish_ready, all candidates must be stop-oriented.

Do not create candidates requiring unsupported source facts.

---

## 12. Structural Terminator

Inside the Markdown artifact or fallback block, the output must end with the exact Publish Decision value.

Allowed final line values:

```text
publish_raw
light_tune_then_publish
hold_with_reason
```

No text after the final decision inside the Markdown artifact or fallback block.

---

## 13. Markdown Handoff Rule

Primary delivery mode:

```text
downloadable_markdown_file
```

Stage 02R should not default to copy-paste-only delivery.

After completing the Full 02R Output Contract, create a downloadable Markdown file containing the complete course-correction result.

The Markdown file content must begin with:

```text
Runtime Header:
stage: 02R_course_correction_gate
```

The Markdown file must preserve the complete Full 02R Output Contract:

```text
Runtime Header
Selected Candidate
Correction Diagnosis
Revision Fresh Contribution
Final Quote Post
Contribution Stack
Source Safety
Risk Flag
Next Fresh Contribution Candidates
AI Recommendation
Publish Decision
```

Recommended download filename:

```text
<slug>_02r-course-correction.md
```

If there are multiple 02R passes or the current runtime pass is known, use:

```text
<slug>_02r-course-correction_v<runtime_pass>.md
```

Filename rule:

```text
Use a short, source-grounded slug based on the current X post topic.
Do not use a vague filename such as output.md, result.md, or response.md.
Do not invent unsupported facts in the slug.
```

Final chat response when downloadable file creation is available:

```text
Stage 02R Markdown file created:
[Download <slug>_02r-course-correction.md](download link)
```

or:

```text
Stage 02R Markdown file created:
[Download <slug>_02r-course-correction_v<runtime_pass>.md](download link)
```

Do not paste the full 02R result in chat when the downloadable Markdown file is successfully created.

Fallback rule:

If downloadable file creation is unavailable, output one complete fenced Markdown block containing the full 02R result.

Fallback output must:

```text
include filename at the top
contain the complete Full 02R Output Contract
not split the result into multiple messages
not add commentary after the Markdown block
```

Fallback filename line:

```text
filename: <slug>_02r-course-correction.md
```

or:

```text
filename: <slug>_02r-course-correction_v<runtime_pass>.md
```

The Markdown Handoff Rule changes delivery mode only.  
It does not loosen Source Safety, Source Re-anchoring, Correction Diagnosis, Voice Attribution Guard, Contribution Stack, Publish-ready Stop Lock, or Output Contract discipline.

Inside the Markdown artifact or fallback block, the final visible line must still be one of:

```text
publish_raw
light_tune_then_publish
hold_with_reason
```

---

## 14. Output Contract

The Markdown artifact content, or fallback fenced Markdown block, must contain exactly this and nothing else.

```text
Runtime Header:
stage: 02R_course_correction_gate
runtime_pass:
loop_policy: no_hard_cap__natural_stop
loop_status: continue / stop_recommended / publish_ready
deliverable: revised_final_quote_post
publication_status: quote_post_candidate
schema_mode: soft_balance
agent_voice: Grok as Course-Correction Agent
publication_voice: YusukeJP quote-post voice
source_voice: original_source_attributed

Selected Candidate:
choice: 1 / 2 / 3 / stop
type:
candidate:
human_reason_optional:

Correction Diagnosis:
danger_type: source_safety / voice_attribution / context_decay / candidate_mixing / loop_addiction / other
reason:

Revision Fresh Contribution:
type:
one_sentence:
delta_from_previous:
operation: keep / replace / merge / drop / compress / clarify / voice_fix / stop
field_judgment:
embedded_in_final_post: yes / no

Final Quote Post:
...

Contribution Stack:
1.
2.
3.

Source Safety:
status: pass / needs_check / hold
reason:

Risk Flag:
L / M / H

Next Fresh Contribution Candidates:
1.
type:
candidate:
value_added:
source_safety_risk: L / M / H
best_for:

2.
type:
candidate:
value_added:
source_safety_risk: L / M / H
best_for:

3.
type:
candidate:
value_added:
source_safety_risk: L / M / H
best_for:

AI Recommendation:
choose: 1 / 2 / 3 / stop
reason:

Publish Decision:
publish_raw / light_tune_then_publish / hold_with_reason
```

If loop_status is publish_ready, AI Recommendation must be `choose: stop`.

Final visible line must be one of the allowed Publish Decision values.
