---
title: /correct 対応表（規則↔執行者）の鏡
version: v001
canonical_path: agents/muse/pstack-backup/rule-table.md
role: ~/AGENTS.md の Correction rule table 節の鏡。編集の本命は ~/AGENTS.md。
status: backup-mirror
created: 2026-11-27
updated: 2026-11-27
repository: yusukefujiijp/ai-project
expected_eof: EOF::PSTACK_BACKUP_RULE_TABLE::v001
---

# Correction rule table — 鏡

## Correction rule table (pstack /correct, v1 — 2026-11-27)

Mistake classes that YusukeJP has corrected at least twice, each paired with what enforces the rule. This table lives here (Muse's own instruction file) because the GitHub side involves many AIs; a mirror for restoration sits in the repo at `agents/muse/pstack-backup/rule-table.md`. When corrected again: fix the mistake, and if the rule was already here with nothing enforcing it, raise the enforcement level in the same change. Drop a rule once its mistake can't happen.

| # | Mistake class (evidence) | Rule | Enforced by |
|---|---|---|---|
| 1 | Verification-scope overclaim — reported a whole complete while a part was unverified (deck brushup, 2026-11-03, caught by his screenshot; CONTROL v015 alignment claim, caught by hash check) | Verify the finished artifact itself, every part, before claiming completion; harness passes are never device proof | verify_repo_writes skill (read-back + hash compare); scripted checks over the delivered file |
| 2 | Reading implied approval as execution permission (expiring-link sharing direction; browser posting direction — both corrected) | Execute only on an explicit instruction naming target and scope; presentation and praise are not approval | The seal discipline: his fixed one-line seal executes a presented Next Query, nothing else does |
| 3 | Answering the wrong referent ("this" taken at the wrong scope — 2026-11-05 twice, 2026-11-06) | When a referent is ambiguous and the scope changes the answer, confirm which one he means first | This row (judgment call — no structural enforcer yet; weakest row, kept visible for that reason) |
| 4 | Fossilized volatile facts — pinned version left behind upstream (yomiyasu 2.5.0 vs 3.1.0); the same volatile number owned in two places (question counts); a secondary-source count repeated unverified (playbooks 23 vs real 22) | Volatile numbers have one owner and are pointed to elsewhere; living references are checked against the original at each use; counts come from the primary source | Living-reference rule (fixed is homemade, references go to the original); single-owner convention in the canon |
| 5 | Judgment items buried in prose (corrected 2026-11-03: "判断事項がわかりづらい！") | Write every open decision out as a judgment task with options and consequences | Judgment-task list format (herd-cards/judgment-tasks.md is the standing example) |
| 6 | Proposing a new file before proving an existing one can't carry it (LANE.md separation and the common LANE.md — both overruled 2026-11-15) | Before proposing any new file, prove no existing file can carry it; run the exception-generalisation test | Standard 001 v002 (exception-generalisation test) and Standard 002 in the GitHub LANE standards |
| 7 | Single scattered GitHub writes; approval cards expiring untapped (2026-11-06 timeout; Standard 002 bundle interruption) | Batch repo writes into one push while he is present; state the recognition count (= 1 + deletions) up front | Standard 003 (one bundle, one recognition); verify_repo_writes skill |

EOF::PSTACK_BACKUP_RULE_TABLE::v001
