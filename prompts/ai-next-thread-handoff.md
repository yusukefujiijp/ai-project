---
title: "AI Next Thread Handoff"
canonical_name: "AI Next Thread Handoff"
version: "v001-candidate"
date: "2026-08-18"
filename: "ai-next-thread-handoff.md"
canonical_path: "prompts/ai-next-thread-handoff.md"
class: "reusable_prompt"
role: "generic living next-thread handoff compiler"
status: "human-sealed field-test candidate / not canonical"
canonicality: "non-canonical candidate"
language_policy: "Japanese-first / English-anchor"

design:
  generic: true
  living: true
  adaptive: true
  human_controlled: true
  rigid_template: false

authority:
  current_authoritative_runtime_wins: true
  human_final_authority: true
  no_silent_scope_expansion: true

full_read_proof:
  required: true
  beginning_identity:
    title: "AI Next Thread Handoff"
    filename: "ai-next-thread-handoff.md"
    canonical_path: "prompts/ai-next-thread-handoff.md"
    version: "v001-candidate"
  expected_eof_sentinel: "EOF::AI_NEXT_THREAD_HANDOFF::v001-candidate"
  full_read_true_only_if:
    - "Beginning Identity was confirmed."
    - "Expected EOF Sentinel was known from the beginning of the document."
    - "The document was read from beginning to end."
    - "The exact expected EOF Sentinel was found."
    - "No unresolved truncation or unread gap remains."
  on_truncation:
    - "Continue reading from the next unread position."
    - "Do not treat a partial fetch as a full read."
  on_failure:
    status: "FULL_READ_NOT_VERIFIED"
    action:
      - "Stop before applying this compiler."
      - "Do not reconstruct missing sections from memory, prior threads, or general knowledge."

core_principles:
  - "State Transfer, not History Dump."
  - "Compression without amnesia."
  - "Constrain the boundaries, not the intelligence."
  - "Hard Read, Adaptive Apply."
  - "Compile Once, Echo Exactly where exactness is materially valuable."
  - "Transition includes the Human last mile when material."
  - "The protocol itself remains correctable by Reality."

last_updated: "2026-08-18"
---

# AI Next Thread Handoff
## Generic Living Next-Thread Handoff Compiler

> [!IMPORTANT]
> This document is a **compiler contract, not a rigid execution template**.
>
> Its purpose is not to force every AI to think in the same order, emit the same sections, or reproduce a fixed handoff format.
>
> It defines the semantic boundaries, authority constraints, transition outcomes, full-read requirements, and Human-facing interfaces that should not be lost when moving from a Current Thread to a Next Thread.
>
> Within those boundaries, the Current AI should use its own capabilities, Current Reality, Current Runtime, available tools, and emergent insight to compile the best handoff it can.

---

# 0. Full-Read Proof Gate

This document must be fully read before it is applied.

```text
File opened
≠ Full read

Beginning metadata read
≠ Full read

Partial fetch
≠ Full read

AI says "I read it"
≠ Verified full read
```

The required proof is:

```text
Beginning Identity confirmed
+
Expected EOF known from the beginning
+
Document read from beginning to end
+
Exact EOF reached
+
No unresolved truncation or unread gap
=
FULL_READ_READY
```

Expected EOF for this version:

```text
EOF::AI_NEXT_THREAD_HANDOFF::v001-candidate
```

If retrieval is truncated, continue from the next unread position until the exact expected EOF is reached.

Do not reconstruct unread sections from memory, an older version, a previous Thread, or general knowledge.

If full-read proof cannot be established:

```yaml
status: "FULL_READ_NOT_VERIFIED"
action:
  - "Stop before applying this compiler."
  - "Report the missing read condition."
  - "Do not silently fall back to another version."
```

Most importantly:

> **Full Read Required ≠ Full Mechanical Application Required.**

The entire document must be read. Not every example, section, heuristic, or optional mechanism must appear in every generated handoff.

The read contract is strict. The application contract is adaptive.

> **Hard Read. Adaptive Apply.**

---

# 1. Direct Judgment

A next-thread handoff succeeds when the Next Thread can resume from the correct Current State without requiring the Human to reconstruct the previous conversation manually.

The goal is not:

```text
Copy the old conversation
→ shorten it
→ paste the summary
```

The goal is:

```text
Current Thread Reality
→ identify what materially matters
→ preserve authority and state
→ prune what does not need foreground attention
→ connect material provenance
→ identify the First Legal Move
→ close the Human last mile
→ compile a restartable Next-Thread interface
```

This document should be used as a **Living Compiler Contract**.

---

# 2. Core Principle

The central design principle is:

> **Constrain the boundaries, not the intelligence.**

The compiler should strongly protect:

```text
Identity
Authority
Mission
Current State
Material Provenance
Safety / Guard
Approved Scope
Stop / Correction rights
First Legal Move
Human Last-Mile integrity
```

It should not unnecessarily prescribe:

```text
exact reasoning order
fixed section count
fixed prose style
fixed response length
fixed tree structure
fixed YAML structure
fixed title syntax
fixed platform-specific UI workflow
fixed analysis method
```

unless a Current authoritative Runtime explicitly requires them.

---

# 3. State Transfer, Not History Dump

The unit of transfer is the **Current State**, not the entire historical transcript.

A useful handoff preserves enough history to explain the Current State, but it does not automatically re-import every past branch into the Next Thread.

Use the following mental model:

```text
Raw History
↓
Material Harvest
↓
Current State
↓
Next Thread
```

A long history may contain important provenance.

That does not mean all of it belongs in the Human or AI foreground after transition.

---

# 4. Compression Without Amnesia

Compression is not deletion.

Preservation is not foreground saturation.

The compiler should distinguish between information that must travel directly into the Next Thread and information that only needs to remain reachable.

Preferred internal classification:

```text
A. Carry Forward
   Material to correct restart and immediate decisions.

B. Provenance / Reference
   Important for reconstruction, verification, genealogy, or deeper review,
   but not required in constant foreground attention.

C. Not Now
   Potentially valuable, but not needed for the Current Transition.
```

This is a reasoning aid, not a mandatory output structure.

The AI may present the result differently if another form is clearer.

---

# 5. Semantic Minimum Viable Handoff

Do not optimize for the shortest possible handoff.

Optimize for the smallest **semantically sufficient** handoff.

A restartable handoff normally needs to preserve, when material:

```yaml
transition_semantics:
  identity:
  authority:
  mission:
  current_state:
  material_harvest:
  provenance:
  constraints:
  unfinished_gate:
  first_legal_move:
  human_last_mile:
```

These are semantic roles.

They are not mandatory section headings.

If several can be compressed safely, compress them.

If a difficult transition requires more detail, expand them.

---

# 6. Current Authority Resolution

Before compiling a handoff, determine which sources currently govern the work.

Depending on the project, these may include:

```text
System / Platform constraints
Developer instructions
Explicit Human request
Project instructions
Repository SSOT
Current Runtime
Canonical or active document set
Current approved Plan
Current Thread Reality
```

Do not assume that this document outranks a Current project-specific authority.

It does not.

If this document conflicts materially with a Current authoritative Runtime, use the Current authoritative Runtime unless a higher-priority instruction says otherwise.

This document provides transition intelligence.

It does not become the throne of the project.

---

# 7. Current Runtime Resolution

When a Current Project provides its own operational rules, resolve them dynamically rather than hard-coding old assumptions from this document.

Potentially relevant current values include:

```yaml
runtime_resolution:
  project_identity:
  repository:
  ref:
  query:
  bootloader:
  runtime_ssot:
  canonical_documents:
  active_version:
  status:
  thread_title_convention:
  cold_start_contract:
  full_read_requirements:
  evidence_rules:
  human_authority:
  stop_rule:
```

Only resolve what materially matters.

Do not create protocol overhead for a simple transition that does not need it.

---

# 8. Generic Roles, Project-Specific Values

This document should remain usable across different Projects.

Therefore it owns generic **roles**, not every Project's concrete semantic values.

For example:

```yaml
generic_roles:
  root_or_ultimate_anchor:
  project_identity:
  purpose_or_mission:
  human_foreground:
  final_attribution:
  current_mode:
  guard:
```

A Current Project may map those roles to its own vocabulary.

Another Project may not use some of them at all.

Do not force unused concepts into a Project merely because they appear here as examples.

Project-specific faith, theology, safety, evidence, naming, or authority rules should be resolved from the Current authoritative source.

AI, this prompt, a Thread, a graph, a repository, or a protocol must not elevate itself above the Current legitimate authority structure.

---

# 9. Adaptive Compiler Freedom

The compiler is expected to exercise judgment.

The Current AI may choose the best available method for:

```text
analysis
structure
branch pruning
compression
naming
ordering
prose density
tree representation
schema representation
reference strategy
first-response design
Human-facing copy surface
```

The purpose is not stylistic freedom for its own sake.

The purpose is to allow stronger present or future AI systems to use better methods without being constrained by an obsolete workflow.

A 2026 implementation detail should not become permanent cognitive debt.

---

# 10. Freedom Gradient

AI freedom should not be treated as a binary variable.

Different parts of the transition benefit from different degrees of freedom.

## 10.1 High-Freedom Region

Examples:

```text
analysis method
structure
compression
relationship discovery
naming candidates
unexpected useful interfaces
emergent improvements
```

## 10.2 Medium-Freedom Region

Examples:

```text
presentation form
reference arrangement
first-response structure
section ordering
degree of explanation
```

## 10.3 Low-Freedom Region

Examples:

```text
Human-confirmed identity
explicit authority
approved scope
stop command
safety boundary
material Human correction
exact identifiers
exact compiled values that must remain stable
```

This gradient is a design heuristic, not an immutable ontology.

If Current Reality demonstrates a better distinction, update it.

---

# 11. Emergence Space

The compiler should leave explicit room for valuable findings that were not anticipated by the Human or this document.

A useful background question is:

> **Is there a material transition improvement that the Human has not explicitly requested but that would meaningfully improve restartability, reduce friction, or prevent semantic loss?**

Examples might include:

```text
a better naming distinction
a missing provenance link
a cleaner restart handle
a safer stop condition
a Human UI friction discovered during transition
a better copy surface
a new relationship between previously separate constraints
```

Do not manufacture novelty.

Novelty is not automatically valuable.

An emergent improvement should normally satisfy:

```text
Mission relevance
No silent authority expansion
No material semantic loss
No material risk increase
Human friction reduction or restart-quality improvement
```

Unexpected Success should be noticed when it appears, not artificially produced.

---

# 12. Thread as the Default Handoff Unit

For this document, **Thread** is the default term for the Human-visible conversational container being handed off.

A **Session** may refer to a runtime, activity period, work period, or stateful process occurring within that Thread.

Default role separation:

```text
Thread
= conversational container / Handoff target

Session
= activity / runtime continuity occurring within a container
```

This is not a universal vendor standard.

If the Current platform or Project uses `conversation`, `session`, or another term as its authoritative container identity, adapt accordingly.

Do not rename a Current Human-confirmed identity merely to satisfy this default terminology.

---

# 13. Thread Identity Compilation

When a transition includes a Human-visible Next Thread identity, compile it according to the Current Project or Runtime convention.

Possible inputs include:

```yaml
thread_identity:
  project_or_ark:
  sequence:
  start_date:
  main_name:
  sub_name:
```

The exact naming scheme is not defined by this generic document.

The Current Runtime wins.

When a final title is resolved, preserve it as:

```yaml
compiled_title:
```

---

# 14. Compile Once, Echo Exactly

Exactness should be used selectively.

It is valuable when a Field has already been intentionally compiled and later re-generation would create unnecessary drift.

A primary example is:

```text
compiled_title
```

After an exact value has been compiled and approved, a Next Thread should not casually:

```text
rename it
translate it
change quotation style
change date style
reorder main/sub names
shorten it
reinterpret it
```

unless:

```text
Human correction exists
Current authoritative Runtime materially conflicts
the compiled value is invalid
```

Hence:

> **Compile Once, Echo Exactly — where exactness is materially valuable.**

Do not extend this rule to all prose.

The Handoff itself may be interpreted and adapted intelligently.

---

# 15. Thread Title Copy Surface

When a compiled Human-visible Thread Title exists, consider the Human rename operation part of the transition.

A successful Next-Thread first response should, when useful, expose a clear:

```text
Thread Title — Copy & Paste
```

surface.

The title should be easy for the Human to copy without returning to the previous Thread.

The Next Thread should Exact Echo the already compiled value rather than re-inventing it.

The AI must not claim that the UI rename actually occurred unless that external state was directly verifiable.

The rename itself remains a Human action unless the platform provides an authorized tool that genuinely performs it.

---

# 16. Human Last-Mile Interface

A handoff is not always complete when information reaches the next AI.

Sometimes the transition path is:

```text
Current AI
↓
Human
↓
UI / Tool / Repository / Reality
↓
Next AI
```

If a small Human action is required to complete the transition, surface it clearly.

Possible examples include:

```text
rename the thread
paste the handoff
attach a source
provide the first Reality input
perform a manual external verification
```

Do not add Human operations merely because they are possible.

The objective is:

> **Minimum Human friction consistent with correct transition.**

---

# 17. Boot, Reconstruction, and Production

If the Current Project has a Cold-Start or Boot protocol, preserve its order.

Preferred conceptual separation:

```text
Boot
↓
Context Reconstruction
↓
Production
```

Do not merge these layers unless the Current Runtime explicitly does so.

Examples of Project-specific Boot requirements may include:

```text
Project Bootloader arrival
Repository binding
Query full read
EOF verification
Document-set consistency
Version verification
```

This generic compiler must not weaken those requirements.

It also must not invent them when the Current Project has none.

After Boot has successfully completed, do not repeat it without a material reason.

---

# 18. Immediate Predecessor Provenance

A previous Thread may have saved a high-value README, Harvest record, artifact, decision log, or handoff source.

When material, connect that source as **Immediate Predecessor Provenance**.

But preserve role separation:

```text
Session Harvest
≠ Runtime SSOT
≠ Canonical Body
≠ Project Instructions
```

A provenance source explains how the Current State was reached.

It does not automatically become the authority that governs the Next Thread.

---

# 19. Confirmed / Candidate / Unknown

Do not flatten confidence levels during transition.

Distinguish, when material:

```text
Human-confirmed
Repository-confirmed
Directly observed
Field-observed
AI inference
Design candidate
Unknown
Future candidate
```

An elegant AI-generated name does not become Human-confirmed merely because it is useful.

Likewise, a Human-confirmed breakthrough should not be discarded as casual conversation merely because it originated informally.

Preserve the degree of certainty needed for correct downstream reasoning.

---

# 20. Material Harvest

A handoff should not merely preserve unfinished work.

It should also preserve discoveries that materially change how the next work should be done.

Material Harvest may include:

```text
a clarified distinction
a proven working route
a rejected interpretation
an unexpected success
a bottleneck
a stable interface
a changed authority boundary
a new stop condition
a newly discovered failure mode
```

Only carry Harvest that matters to the Next Thread.

Other Harvest may remain in provenance.

---

# 21. Unfinished Gate

If the Current Mission is incomplete, identify the real unfinished Gate.

Do not substitute a convenient next task for the actual remaining constraint.

Examples:

```text
Human decision still required
source not yet verified
artifact drafted but not sealed
implementation complete but Reality Review pending
external authority not granted
current Reality not yet supplied
```

The Next Thread should understand whether it is continuing execution, waiting, reviewing, or starting a new field observation.

---

# 22. First Legal Move

Every operational handoff should make the Next Thread's initial legal action clear enough to avoid unnecessary branch explosion.

Examples:

```text
WAIT_FOR_HUMAN_INPUT
WAIT_FOR_CURRENT_REALITY
READ_REQUIRED_SOURCE
REVIEW_EXISTING_DRAFT
CONTINUE_APPROVED_STEP
VERIFY_EXTERNAL_RESULT
```

This is not meant to eliminate AI initiative.

It defines the correct starting coordinate.

Once the Next Thread is correctly started, the AI may reason and act within its legitimate scope.

---

# 23. Human Input Flexibility

If the Next Thread needs Human Reality, do not require the Human to construct a perfect prompt.

Inputs such as:

```text
something feels wrong
I am unsure
this part matters
I cannot explain it well yet
here is what happened
```

may be sufficient starting data.

The AI may perform pre-linguistic structuring, candidate naming, relationship detection, or branch analysis.

But:

```text
AI candidate
≠ Reality
≠ Human confirmation
≠ divine or external authority
```

where such distinctions matter.

Human correction remains valuable transition data.

---

# 24. First Response Outcome

Do not permanently fix the exact number or order of sections in the Next Thread's first response.

Instead, ensure the Human can quickly determine the material transition outcome.

Where applicable, the first response should make clear:

```text
Did the transition / boot succeed?
What Current Thread / State was reconstructed?
What Mission or foreground should continue?
What is the First Legal Move?
Is a Human Last-Mile action required?
Is there an exact compiled title to copy?
```

If the Current Runtime requires additional status fields, include them.

If fewer are sufficient, keep the response compact.

The Next Thread's first response is a startup interface, not a restatement of the full handoff document.

---

# 25. Scope Expansion Guard

Transition is not permission to start an unlimited program.

When a new issue appears, classify it by relevance.

Conceptually:

```text
Blocker
→ surface or handle according to current authority.

Required for Current Victory
→ handle if inside scope.

Useful but not required
→ preserve as future/support candidate.

Unrelated
→ do not pursue.
```

AI freedom does not imply authority expansion.

AI creativity does not imply scope expansion.

---

# 26. Support-Line Routing

Some Projects have separate support tracks, secondary projects, maintenance lines, or background workstreams.

If the Current Project defines such topology, preserve it.

A support line should not accidentally capture the Main Mission.

This generic document does not define a universal support topology.

Resolve it from the Current Project when relevant.

---

# 27. Non-Goals

Do not automatically transform a next-thread handoff into:

```text
a canonical rewrite
a repository migration
a new skill
a dashboard
a full-history analysis
a project rearchitecture
a new database
a new automation
a new support project
```

unless one of those is itself the Current explicit Mission.

Good ideas can be recorded as `Not Now`.

A successful transition should usually return attention to Production.

---

# 28. Failure and Recovery

Do not silently fabricate missing transition state.

Material failure examples include:

```text
required authoritative source unavailable
version conflict
unclear Next Thread identity
multiple incompatible approved states
missing provenance required for correct restart
material Human correction not integrated
compiled title inconsistent with current title convention
partial read or missing EOF proof
```

Recommended read / transition states:

```yaml
read_states:
  READY:
    meaning: "Beginning Identity and exact EOF verified; no unread gap remains."

  PARTIAL_READ:
    meaning: "Document retrieval is incomplete."

  EOF_SENTINEL_MISSING:
    meaning: "Expected EOF was not reached."

  IDENTITY_MISMATCH:
    meaning: "Beginning or ending identity does not match."

  FULL_READ_NOT_VERIFIED:
    meaning: "Compiler must not run."
```

When a failure materially blocks correct transition:

```text
identify the failed condition
preserve what is known
state the minimum recovery action
stop or pause at the correct boundary
```

Do not silently fall back to obsolete Memory, an older Template, or an unrelated Project state.

---

# 29. Material Correction

A correction that changes:

```text
Mission
Scope
Authority
Deliverable
Risk posture
Thread identity
Human decision gate
external action permission
```

is material.

Do not automatically carry an old approval into a materially changed transition.

A clerical correction that does not change these things may normally be incorporated without rebuilding the whole transition.

Use Current Runtime rules when they define a stricter correction contract.

---

# 30. Reality Review

Transition success should be verifiable.

Generic Reality Review questions include:

```text
Was the correct identity reconstructed?
Was authority preserved?
Was the Current Mission preserved?
Was the Current State restored?
Can material provenance still be reached?
Is the unfinished Gate correctly identified?
Is the First Legal Move clear?
Is the Human Last-Mile actionable?
Was an exact compiled value echoed without drift?
Was the handoff compiler itself fully read through the expected EOF?
```

Only verify states the AI can actually inspect.

External or UI states that cannot be inspected remain Human-mediated.

---

# 31. Transition Success

A transition is sufficiently complete when the Next Thread can continue without requiring the Human to rediscover or restate material context.

A strong transition typically achieves:

```text
Correct identity
+
Correct authority
+
Correct Current State
+
Material meaning preserved
+
Unnecessary branches pruned
+
First Legal Move clear
+
Human Last-Mile low friction
```

The exact manifestation may vary by Project.

---

# 32. Living Review — Not Dead Data, but a Living Board

This document should not become dead policy text.

Its Current Board should remain inspectable.

## 32.1 Stable

Currently high-confidence principles:

```text
State Transfer, not History Dump.
Compression without amnesia.
Hard Read, Adaptive Apply.
Current authoritative Runtime wins.
Human authority and Stop Right remain.
First Legal Move matters.
Human Last-Mile can be part of the transition.
Constrain boundaries, not intelligence.
```

## 32.2 Watch

Concepts worth continued field observation:

```text
Semantic Minimum Viable Handoff
Freedom Gradient
Compile Once, Echo Exactly
Thread / Session role separation
First-response startup interface
Full-Read Proof reliability across AI environments
```

## 32.3 Observed Friction

Future field use should record patterns such as:

```text
handoff too long
handoff too compressed
title drift
AI repeats old theory instead of resuming work
Human must return to old thread
AI confuses provenance with authority
AI treats examples as mandatory output
AI freedom causes scope expansion
AI claims full read after partial retrieval
AI sees beginning but never verifies EOF
AI reconstructs unread sections from memory
AI verifies EOF but leaves an unresolved middle gap
```

## 32.4 Unexpected Success

Record improvements that were not planned but materially improve the transition.

An Unexpected Success may justify a new interface or a future version candidate.

It does not need to be forced into the current version immediately.

## 32.5 Next-Version Candidates

Future revisions may emerge from:

```text
field failures
repeated friction
platform changes
stronger AI capabilities
Human workflow changes
new transition interfaces
unnecessary old rules
```

The board exists to support evolution, not to demand constant edits.

---

# 33. Evolution Contract

This document is versioned because it is expected to evolve.

Version evolution does not mean only adding more rules.

Valid evolution includes:

```text
add
remove
compress
merge
split roles
rename
replace an obsolete interface
reduce Human steps
delegate old scaffolding to stronger AI
delete rules that no longer create value
```

A version bump should be motivated by a **material design delta**, not cosmetic churn.

The objective is not to preserve the protocol.

The objective is to preserve and improve the quality of real transitions.

---

# 34. Future-AI Constraint Debt Guard

A rule that helps Current AI may become unnecessary for Future AI.

Therefore periodically ask:

> **Which rules still protect a real boundary, and which rules merely compensate for an older AI limitation?**

Do not keep obsolete scaffolding merely because it has existed for a long time.

Stable principles may remain.

Implementation detail should remain disposable.

---

# 35. Human-Facing Invocation Principle

The Human should not need to carry this entire document in every transition request.

Preferred architecture:

```text
Short Human Query
↓
Stable GitHub URL
↓
Full-Read Proof
↓
Current Runtime / Reality Binding
↓
Adaptive Handoff Compilation
```

Human-facing interface stability and compiler intelligence evolution should be allowed to move at different speeds.

The invocation may remain stable while this document continues to improve.

A recommended Human-facing invocation is:

```text
次Thread移行用Handoff Promptを書いて下さい！

以下を最初から最後まで全文読み、
文書内で宣言されたBeginning Identity・Expected EOF Sentinel・
Full-Read Proofを確認した場合のみ、
Current ThreadのReality・Current Runtime・Current Missionへ適応して実行してください。

https://github.com/yusukefujiijp/ai-project/blob/main/prompts/ai-next-thread-handoff.md

途中取得が切れた場合は未読位置から続きを読み、
Exact EOFへ到達するまでFull Readとして扱わないでください。

固定Templateとして機械的に適用せず、
Current authoritative Runtimeを優先し、
各Thread AIの自由度・判断・創発性を活かしてください。

Full-Read Proofを確認できない場合は推測で補わず、
FULL_READ_NOT_VERIFIEDとして停止してください。
```

The invocation should remain short enough for routine Human use.

Do not copy this document's version number or EOF string into the Human-facing invocation unless there is a material reason; the document itself owns its Current Version and Expected EOF.

---

# 36. Two-Speed Architecture

A useful design principle is:

```text
Slow-changing Human Interface
+
Fast-changing Living Intelligence
```

The Human-facing invocation should remain simple when possible.

The GitHub-bound compiler may evolve more rapidly as Reality produces new evidence.

This separation reduces Human maintenance burden while preserving improvement velocity.

---

# 37. Operational Use

When asked to create a Next Thread Handoff, the material outcomes normally include:

```text
Understand the Current Request.
Resolve material Current authority.
Verify this compiler was fully read.
Read other required referenced sources.
Determine the Current State.
Identify the material Harvest.
Prune transition information.
Preserve necessary provenance.
Compile the Next Thread identity when applicable.
Identify the First Legal Move.
Close material Human Last-Mile friction.
Produce a copy-and-paste-ready Handoff Prompt.
```

This sequence is descriptive, not mandatory internal chain-of-thought.

The AI may use a better reasoning process.

Only the resulting semantic integrity and authority compliance matter.

---

# 38. Core Compression

```text
Read the whole compiler before using it.
Do not confuse opening with full reading.

Do not hand off the transcript.
Hand off the state.

Do not preserve everything in foreground.
Preserve what matters and keep provenance reachable.

Do not make the generic prompt the authority.
Resolve the Current authority.

Do not freeze AI intelligence.
Protect the boundaries and leave the interior adaptive.

Do not end at AI-to-AI transfer.
Close the Human last mile when it matters.

Do not re-invent exact compiled values unnecessarily.
Compile Once, Echo Exactly.

Do not treat this version as final forever.
Reality may correct the protocol.
```

---

# 39. 一文定義

```text
"AI Next Thread Handoff（AI Next Thread Handoff: GitHub上のCurrent VersionをBeginning IdentityからExpected EOFまで未読GapなくHard Readした場合だけ起動を許可し、Current ThreadのIdentity・Authority・Mission・Current State・Material Harvest・Provenance・First Legal MoveをHistory Dumpではなく再起動可能なState TransferへCompileしながら、Current Runtimeを優先して具体的な分析・構造・圧縮・Naming・Human Last-Mileを各AIへ適応的に委譲することで、飛ばし読み防止・汎用性・Human Control・AI自由度・創発性・Version成長性を同時に成立させるLiving Next-Thread Handoff Compilerである)"
```

---

document_end:
  title: "AI Next Thread Handoff"
  filename: "ai-next-thread-handoff.md"
  canonical_path: "prompts/ai-next-thread-handoff.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_NEXT_THREAD_HANDOFF::v001-candidate"

EOF::AI_NEXT_THREAD_HANDOFF::v001-candidate
