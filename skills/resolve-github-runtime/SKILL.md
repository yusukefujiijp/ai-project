---
name: resolve-github-runtime
description: Resolve the current GitHub plugin, bundled-skill, and connector runtime before GitHub work. Use when a GitHub skill path is missing or stale, a plugin version changed, skills and connector tools disagree, a prior turn referenced a versioned plugin cache path, or the first GitHub mutation in a thread needs an update-safe preflight. Classify the runtime once, prevent repeated phantom-path searches, select the legal execution mode, and verify GitHub writes by remote reread.
---

# Resolve GitHub Runtime

## Purpose

Run one bounded preflight that converts a changing GitHub plugin installation into a stable execution decision. This skill is a compatibility router; it does not replace an official GitHub skill or connector.

## Authority Order

Resolve conflicts in this order:

1. Current Human request, stop, and correction.
2. Current callable runtime and tools.
3. Current plugin metadata and exact current files.
4. Repository decision record for the project in scope.
5. Public plugin source and earlier paths as historical evidence only.

Never let an old versioned cache path override the current runtime.

## Single-Pass Preflight

Collect only the evidence needed for the present task:

- current GitHub plugin or release version, when exposed;
- current declared skill list and connector/app declaration;
- exact GitHub `SKILL.md` path exposed for this turn, and whether it exists;
- currently callable GitHub connector tools;
- repository, ref, and target path for the requested operation.

If an exposed skill path is missing, re-resolve current plugin metadata once. Do not repeatedly scan old cache versions. Inspect public source only when the current release and current files remain inconsistent or the Human explicitly requests provenance.

## Runtime Classification

Choose exactly one mode:

| Mode | Evidence | Legal move |
|---|---|---|
| `BUNDLED_SKILL_MODE` | Current metadata declares a GitHub skill and its exact current `SKILL.md` exists | Read that file fully, then follow it |
| `CONNECTOR_ONLY_MODE` | Current metadata declares no GitHub skills, while GitHub connector tools are callable | Use the connector directly; do not search for a phantom skill |
| `HOT_UPDATE_SKEW` | Exposed skill metadata/path belongs to a different release or disagrees with current installed files/tools | Discard the stale path, re-resolve current metadata once, then enter bundled-skill or connector-only mode |
| `NO_CAPABILITY` | Neither a readable current GitHub skill nor callable GitHub tools exist | Stop and report the precise capability blocker |

Do not classify a connector-only release as broken merely because it has no bundled skill. Do not classify a public-source skill as installed merely because it exists upstream.

## Source/Release Relation

When public portable source and the current ChatGPT release differ, label their relation separately:

- `MATCH`: the relevant current declarations agree;
- `SURFACE_OR_CHANNEL_SPLIT`: public portable source includes skills while the current surface exposes a connector-only package;
- `PACKAGING_REGRESSION_CANDIDATE`: the current package contradicts its own declarations;
- `UNKNOWN`: evidence is insufficient.

Treat `SURFACE_OR_CHANNEL_SPLIT` and `PACKAGING_REGRESSION_CANDIDATE` as correctable inferences unless an official source states the cause. Never automatically copy, install, or recreate public plugin skills to repair the mismatch.

## GitHub Execution Contract

After classification:

1. Bind the exact `owner/name`, ref, and target path from the request, repository binding, or prior tool result. Reuse those values verbatim; do not retype them between dependent calls.
2. Read the current repository, ref, and target file.
3. Decide `CREATE`, `UPDATE`, or `NO_CHANGE` from the remote state.
4. Preserve unrelated content and the Human's current changes.
5. Never run simultaneous writes against the same path.
6. Write with the current legal mode.
7. Reread the remote target after the write.
8. Verify exact path, ref, intended content, required EOF sentinel when present, and returned SHA or commit evidence.
9. Report the result without claiming a UI action or capability that was not observed.

For multiple dependent writes, finish and reread the first before starting the next.

On `404` or `NOT_FOUND`, compare the exact repository identifier, ref, and path against the bound receipt before blaming the plugin or changing runtime mode. If the failed call made no remote mutation, reread current state and permit one corrected retry.

## Anti-Loop Rules

- Never persist a versioned plugin cache path as an SSOT across turns.
- Never retry the same missing path more than once in a preflight.
- Never infer global skill removal from one product surface.
- Never recreate an OpenAI-provided GitHub skill unless the Human explicitly requests a separate custom skill after the compatibility diagnosis.
- Run the preflight before the first GitHub mutation in a thread, then reuse the receipt. Re-run only after a version/tool change, a mismatch, or a material tool error.
- If this skill itself is unavailable in an Ark23 context, read `ark-project/ark23/ark23-03/github-plugin-runtime-best-practice.md` as the passive fallback record.

## Receipt

Return or retain this compact state:

```yaml
github_runtime_receipt:
  observed_at: ""
  current_version: "KNOWN_OR_UNKNOWN"
  mode: "BUNDLED_SKILL_MODE | CONNECTOR_ONLY_MODE | HOT_UPDATE_SKEW | NO_CAPABILITY"
  skill_path: "CURRENT_EXACT_PATH_OR_NONE"
  connector: "AVAILABLE | UNAVAILABLE"
  source_release_relation: "MATCH | SURFACE_OR_CHANNEL_SPLIT | PACKAGING_REGRESSION_CANDIDATE | UNKNOWN"
  repository: "owner/name"
  ref: ""
  next_legal_move: ""
  recheck_trigger: "version change | tool mismatch | material error"
```

Keep the Human-facing explanation short unless a mismatch or explicit provenance question requires the full evidence chain.
