---
title: pstack on Muse — adapter（バックアップ鏡）
version: v001
canonical_path: agents/muse/pstack-backup/muse-adapter.md
role: Muse 用アダプタ文書の鏡。本命は Muse 内 custom-skills/pstack_muse_adapter/。
status: backup-mirror
created: 2026-11-27
updated: 2026-11-27
repository: yusukefujiijp/ai-project
expected_eof: EOF::PSTACK_BACKUP_ADAPTER::v001
---

# pstack on Muse — adapter

> Muse adapter for the ported pstack skills (created 2026-11-27, round 4 of the port). Modelled on Lauren Tan's `docs/harness/claude-code.md` (pstack, MIT License), re-derived for Muse's tool surface.
> Read this once per session before routing work through `pstack_poteto_mode`. pstack skills use Cursor names; map each name with the tables below. If a Cursor field has no row, drop it and say so. Never invent a capability Muse does not have.

## Tools

| Cursor | Muse |
| --- | --- |
| `Task` (spawn a subagent) | `subagent.spawn`. Subagents run in the background and report back on their own; never poll for them. |
| `AskQuestion` | Ask in plain chat text. For a bounded choice, use the options widget. |
| Open a todolist / copy playbook steps into it | `todo.write`. Copy the matched playbook's steps in before starting work, one item per step. |
| Run another pstack skill (`/name`) | Read `~/workspace/custom-skills/pstack_<name>/SKILL.md` and follow it. Ported skills only; an unported name is a gap to declare, not a step to fake. |
| `Grep`, `Glob` | Shell search (`rg` / `grep`) via exec. |

## Subagents

| Cursor | Muse |
| --- | --- |
| Spawn a fresh `poteto-agent` per task | Spawn a fresh subagent per task. Resume one only to continue its own interrupted work. |
| The delegate reads poteto-mode's SKILL.md in full before any work | **Rule:** every subagent brief for pstack-routed work must instruct the delegate to read `~/workspace/custom-skills/pstack_poteto_mode/SKILL.md` in full first, and to read the leaf principle file before citing a principle. A generic brief without that read drifts. |
| `resume` | Spawn a new agent and paste the earlier result into its brief. |
| `readonly: true` | Say "do not edit files" in the brief, and check afterwards that nothing changed. |
| Transcripts under `~/.cursor/projects/<slug>/agent-transcripts/` | The chat history (readable via the chat tools), saved memory, and the goal workspace records. Read only the current workspace's trail; never another chat's private history for this. |

## Models

| Cursor | Muse |
| --- | --- |
| Per-role model slugs (`claude-opus-5-5-xhigh-fast`, `gemini-4-neon-xhigh`, …) | Muse does not expose per-call model or effort selection for subagents. Omit the slug, run on the session model, and **say so** when a ported text names one. |
| Cross-vendor panel seats (arena, interrogate) | Vendor diversity is not available. Panel diversity on Muse = several fresh subagents briefed independently, without seeing each other's answers. Declare the substitution; it is weaker than a second vendor and must not be reported as one. |
| `~/.cursor/rules/pstack-models.mdc` (auto-loaded role table) | No equivalent auto-loaded rule file. The port registry in the daily-watch state file (`~/workspace/goals/lauren-tan-poteto-pstack-daily-watch/hidden_files/state.md`) is the standing record of what was ported and adapted. |

## Paths

| Cursor | Muse |
| --- | --- |
| `~/.cursor/plugins/…/pstack/skills/<name>/` | `~/workspace/custom-skills/pstack_<name>/` (ported copy). Upstream originals for diffing: `~/workspace/pstack-port/upstream/`. |
| `https://github.com/cursor/plugins/blob/main/pstack/<path>` | Read the local port or the saved upstream copy first. Fetch from GitHub only to check for a newer upstream version. |

## Cursor-only features — the one-line skip rule

Muse has no Cursor Automations, Bugbot, Cursor cloud agents, worktrees, or built-in PR tool, and no `.mdc` rules. When a ported step needs one, put one line in your reply — `Skipped on Muse: <step>. <reason>.` — then go on to the next step. Do not stop, ask, or retry. When a later step needs what the skipped step made, leave a placeholder and name it in the line.

| Cursor-only | On Muse |
| --- | --- |
| Cursor Automations / routine wakes | Skip with the line. Scheduled work here is a cron the user approved; never invent one from a skill text. |
| Bugbot | Skip with the line. |
| Cloud agents / worktrees | Skip with the line. Isolation here = separate subagents with separate briefs, or separate chats (LANEs). |
| Built-in PR tool | Not a skip: this workspace rarely opens PRs; repo writes go through the GitHub connector under the user's seal, in one batched push. |
| `/setup-pstack` (writes the models rule) | Skip with the line. There is no models rule to write; the registry records adaptations instead. |

EOF::PSTACK_BACKUP_ADAPTER::v001
