# artifact-to-github_programming-like.md

```yaml id="ymbf63"
file_contract:
  filename: "artifact-to-github_programming-like.md"
  mode: "AI-native / Programming-like Research Companion"
  status: "draft_candidate"
  main_card: "artifact-to-github.md"
  relationship: "Executable Projection of Main Card"
  replacement_for_main_card: false
```

---

## 0. Contract

```pseudo id="4i8lkl"
IMPORT CanonicalMeaning FROM "artifact-to-github.md"

ASSERT this_file != "main_card"
ASSERT this_file.role == "execution_projection"
ASSERT CanonicalMeaning.authority > this_file.authority

IF meaning_is_unclear:
    THEN READ("artifact-to-github.md")
    ELSE CONTINUE_WITH(this_file_as_execution_view)
```

```text id="dqgy2b"
Main Card protects meaning.
Programming-like Card protects routing.
Two files. One meaning.
```

---

## 1. Constants

```pseudo id="ygbe4h"
CONST DEFAULT_DOWNLOAD_ARTIFACT_REQUIRED = true
CONST DEFAULT_OVERWRITE_PERMISSION = false
CONST MAX_DIRECT_UPDATE_ATTEMPTS = 1

CONST PATCH_IS_FOR_JUDGMENT = true
CONST FULL_BODY_IS_FOR_ACTION = true

CONST TOOL_FAILURE_IS_ARTIFACT_FAILURE = false
CONST MEANING_DEGRADATION_ALLOWED = false
CONST HUMAN_SEAL_REQUIRED = true
CONST EXACT_PATH_WITH_FILENAME_REQUIRED = true
```

---

## 2. Types

```pseudo id="kxr0fv"
TYPE SourceArtifact:
    id: string | null
    content: markdown | text | json | file_reference
    status: "complete" | "incomplete" | "unclear"
    intended_meaning_locked: boolean

TYPE TargetCoordinate:
    repository_full_name: string | null
    branch: string | null
    exact_path_with_filename: string | null
    target_exists: boolean | unknown
    current_sha: string | null

TYPE RouteOptions:
    download_artifact_required: boolean | null
    download_artifact_skip_explicit: boolean
    overwrite_permission_explicit: boolean
    commit_message: string | null

TYPE WriteResult:
    status: "success" | "blocked" | "failed" | "stopped"
    commit_sha: string | null
    content_sha: string | null
    failure_reason: string | null
    confirmed_by_tool: boolean

TYPE ManualCommitPack:
    target_coordinate: TargetCoordinate
    full_body_replacement_file: file
    commit_message: string
    extended_description: string | null
    manual_steps: list[string]
    verification_checklist: list[string]
```

---

## 3. Invariants

```pseudo id="04z1te"
INVARIANT exact_path_with_filename IS REQUIRED
INVARIANT no_guessing_path == true
INVARIANT no_overwrite_without_human_seal == true
INVARIANT one_file_at_a_time == true

INVARIANT patch_is_for_judgment == true
INVARIANT full_body_is_for_action == true

INVARIANT tool_failure_does_not_imply_bad_content == true
INVARIANT blocked_write_must_not_degrade_meaning == true

INVARIANT main_card_is_semantic_source == true
INVARIANT programming_like_card_is_projection == true
```

```pseudo id="5rt3da"
IF this_file.conflicts_with("artifact-to-github.md"):
    THEN:
        STOP
        REPORT("drift detected")
        RETURN_TO("artifact-to-github.md")
        ASK_HUMAN_SEAL
```

---

## 4. State Machine

```pseudo id="k4pqng"
STATE INIT
STATE VALIDATING_INPUT
STATE MISSING_INPUT_STOP
STATE TARGET_CHECK
STATE WAITING_FOR_OVERWRITE_SEAL
STATE ROUTE_SELECTION
STATE DOWNLOAD_ARTIFACT_ROUTE
STATE DIRECT_UPDATE_ATTEMPT
STATE DIRECT_UPDATE_SUCCESS
STATE DIRECT_UPDATE_BLOCKED
STATE DIRECT_UPDATE_FAILED
STATE BUILDING_FULL_BODY_MANUAL_COMMIT_PACK
STATE WAITING_FOR_HUMAN_UPLOAD
STATE VERIFYING_AFTER_UPLOAD
STATE VERIFIED
STATE STOPPED
```

```pseudo id="72nauj"
INIT
  -> VALIDATING_INPUT

VALIDATING_INPUT
  -> MISSING_INPUT_STOP
  -> TARGET_CHECK

TARGET_CHECK
  -> WAITING_FOR_OVERWRITE_SEAL
  -> ROUTE_SELECTION

ROUTE_SELECTION
  -> DOWNLOAD_ARTIFACT_ROUTE
  -> DIRECT_UPDATE_ATTEMPT

DIRECT_UPDATE_ATTEMPT
  -> DIRECT_UPDATE_SUCCESS
  -> DIRECT_UPDATE_BLOCKED
  -> DIRECT_UPDATE_FAILED

DIRECT_UPDATE_BLOCKED
  -> BUILDING_FULL_BODY_MANUAL_COMMIT_PACK

DIRECT_UPDATE_FAILED
  -> BUILDING_FULL_BODY_MANUAL_COMMIT_PACK

BUILDING_FULL_BODY_MANUAL_COMMIT_PACK
  -> WAITING_FOR_HUMAN_UPLOAD

WAITING_FOR_HUMAN_UPLOAD
  -> VERIFYING_AFTER_UPLOAD

VERIFYING_AFTER_UPLOAD
  -> VERIFIED
```

---

## 5. Guard Clauses

```pseudo id="jbje4s"
FUNCTION validate_input(source: SourceArtifact, target: TargetCoordinate, options: RouteOptions):

    IF source.status != "complete":
        THEN RETURN STOP("source artifact incomplete or unclear")

    IF target.repository_full_name == null:
        THEN RETURN STOP("repository_full_name missing")

    IF target.branch == null:
        THEN RETURN STOP("branch missing")

    IF target.exact_path_with_filename == null:
        THEN RETURN STOP("exact_path_with_filename missing")

    IF target.target_exists == true AND options.overwrite_permission_explicit == false:
        THEN RETURN STOP("target exists; overwrite permission missing")

    ELSE:
        THEN RETURN OK
```

```pseudo id="nfkqrs"
FUNCTION stop_if_missing_exact_path(target):
    IF target.exact_path_with_filename == null:
        THEN:
            STOP
            REPORT("No exact path with filename. Do not guess.")
```

```pseudo id="0y5yo9"
FUNCTION stop_if_overwrite_unsealed(target, options):
    IF target.target_exists == true AND options.overwrite_permission_explicit == false:
        THEN:
            STOP
            REPORT("Overwrite requires explicit Human Seal.")
```

---

## 6. Route Selection

```pseudo id="0fh305"
FUNCTION choose_route(source, target, options):

    validation = validate_input(source, target, options)

    IF validation.status == "STOP":
        THEN RETURN validation

    IF options.download_artifact_skip_explicit == true:
        THEN RETURN ROUTE("DIRECT_UPDATE_FAST_PATH")

    ELSE:
        THEN RETURN ROUTE("DEFAULT_DOWNLOAD_ARTIFACT_ROUTE")
```

---

## 7. Default Download Artifact Route

```pseudo id="mv341j"
FUNCTION default_download_artifact_route(source, target, options):

    IF options.download_artifact_required == null:
        THEN options.download_artifact_required = DEFAULT_DOWNLOAD_ARTIFACT_REQUIRED

    IF options.download_artifact_required == true:
        THEN:
            CREATE_OR_CONFIRM_DOWNLOAD_ARTIFACT(source)
            WAIT_FOR_HUMAN_SEAL(target)
            STOP

    ELSE:
        THEN:
            REQUIRE(options.download_artifact_skip_explicit == true)
            RETURN choose_route(source, target, options)
```

```text id="ny3r4g"
Default route is Download Artifact.
Download Skip requires explicit Human Seal.
```

---

## 8. Direct Update Fast Path

```pseudo id="h90x8t"
FUNCTION direct_update_fast_path(source, target, options):

    ASSERT options.download_artifact_skip_explicit == true
    ASSERT source.status == "complete"
    ASSERT target.exact_path_with_filename != null
    ASSERT MAX_DIRECT_UPDATE_ATTEMPTS == 1

    result = TRY_DIRECT_GITHUB_UPDATE_ONCE(
        content = source.content,
        target = target,
        overwrite_permission = options.overwrite_permission_explicit
    )

    IF result.status == "success":
        THEN:
            REPORT(result.commit_sha, result.content_sha, target.exact_path_with_filename)
            fetched = FETCH_GITHUB_FILE(target)
            VERIFY(fetched, source)
            LIVING_REVIEW("direct update success")
            RETURN DONE

    ELSE:
        THEN:
            RETURN handle_direct_update_failure(result, source, target, options)
```

---

## 9. Direct Update Failure Handler

```pseudo id="c6o6js"
FUNCTION handle_direct_update_failure(result, source, target, options):

    IF result.status == "blocked" OR result.status == "failed":
        THEN:
            REPORT_FAILURE_HONESTLY(result)

            DO_NOT_CLAIM("content is bad")
            DO_NOT_CLAIM("exact internal reason is known")
            DO_NOT_RETRY_SAME_PAYLOAD
            DO_NOT_DEGRADE_MEANING
            DO_NOT_DELETE_GUARDS

            pack = build_full_body_manual_commit_pack(source, target, options)

            RETURN pack

    ELSE:
        THEN:
            STOP
            REPORT("unknown write result")
```

```text id="4lx0jx"
Tool Failure is not Artifact Failure.
Change transport. Preserve meaning.
```

---

## 10. Full Body Manual Commit Pack

```pseudo id="bb9jt1"
FUNCTION build_full_body_manual_commit_pack(source, target, options) -> ManualCommitPack:

    ASSERT source.intended_meaning_locked == true
    ASSERT target.exact_path_with_filename != null

    full_body_file = GENERATE_DOWNLOAD_ARTIFACT(
        type = "Full Body Replacement File",
        content = source.content
    )

    pack = ManualCommitPack(
        target_coordinate = target,
        full_body_replacement_file = full_body_file,
        commit_message = options.commit_message OR SUGGEST_COMMIT_MESSAGE(source, target),
        extended_description = SUGGEST_EXTENDED_DESCRIPTION(source, target),
        manual_steps = [
            "Open target file in GitHub UI",
            "Edit",
            "Select all",
            "Delete all",
            "Paste full body",
            "Commit",
            "Return Reality Response to AI"
        ],
        verification_checklist = [
            "Fetch target file",
            "Confirm content exists",
            "Confirm critical section exists",
            "Confirm no meaning degradation",
            "Confirm current content SHA"
        ]
    )

    RETURN pack
```

```pseudo id="a3dvp1"
IF manual_commit_pack.type == "patch_only":
    THEN:
        WARN("Patch-only is for judgment, not execution")
        REQUIRE_FULL_BODY_REPLACEMENT_FILE
```

---

## 11. Download Skip Algorithm

```pseudo id="mz9auk"
ALGORITHM DownloadSkipFastPath:

    INPUT:
        user_request
        source_artifact
        target_coordinate
        route_options

    IF user_request explicitly says "Download Artifact can be skipped":
        THEN:
            route_options.download_artifact_skip_explicit = true
            route_options.download_artifact_required = false

            route = choose_route(source_artifact, target_coordinate, route_options)

            IF route == "DIRECT_UPDATE_FAST_PATH":
                THEN:
                    return direct_update_fast_path(source_artifact, target_coordinate, route_options)

            ELSE:
                THEN:
                    return STOP("route conditions not satisfied")

    ELSE:
        THEN:
            return default_download_artifact_route(source_artifact, target_coordinate, route_options)
```

---

## 12. No Degradation Algorithm

```pseudo id="nc24s1"
ALGORITHM NoDegradationOnToolBlock:

    IF tool_write_result in ["blocked", "failed"]:
        THEN:
            REPORT_FAILURE_HONESTLY
            PRESERVE_ORIGINAL_INTENDED_CONTENT
            DO_NOT_SHORTEN_TO_PASS_TOOL
            DO_NOT_REMOVE_ROOT_GUARD
            DO_NOT_REMOVE_CORE_GUARD
            DO_NOT_CHANGE_MEANING
            SWITCH_TRANSPORT("Full Body Manual Commit Pack")
            WAIT_FOR_HUMAN_UPLOAD
            VERIFY_AFTER_UPLOAD

    ELSE:
        THEN:
            CONTINUE_NORMAL_ROUTE
```

---

## 13. Verification Algorithm

```pseudo id="g1h6rs"
FUNCTION verify_after_upload(target, expected_markers):

    fetched = FETCH_GITHUB_FILE(target)

    IF fetched.status != "success":
        THEN RETURN STOP("verification fetch failed")

    FOR marker IN expected_markers:
        IF marker NOT IN fetched.content:
            THEN:
                RETURN STOP("expected marker missing: " + marker)

    REPORT("verification passed")
    RETURN VERIFIED
```

---

## 14. Test Suite

```pseudo id="cikyc4"
TEST direct_update_success:

    GIVEN:
        download_artifact_skip_explicit = true
        source.status = "complete"
        target.exact_path_with_filename = "ss_super-special/example.md"
        overwrite_permission_explicit = true
        direct_update_result = "success"

    EXPECT:
        state == DIRECT_UPDATE_SUCCESS
        commit_sha != null
        content_sha != null
        verification == "run"
```

```pseudo id="hj05o5"
TEST direct_update_blocked:

    GIVEN:
        download_artifact_skip_explicit = true
        source.status = "complete"
        target.exact_path_with_filename != null
        overwrite_permission_explicit = true
        direct_update_result = "blocked"

    EXPECT:
        state == BUILDING_FULL_BODY_MANUAL_COMMIT_PACK
        meaning_degraded == false
        retry_same_payload == false
        manual_pack.type == "Full Body Replacement File"
```

```pseudo id="9p2ki6"
TEST missing_exact_path:

    GIVEN:
        target.exact_path_with_filename = null

    EXPECT:
        state == MISSING_INPUT_STOP
        github_update == false
        ai_guess_path == false
```

```pseudo id="ayht2g"
TEST target_exists_without_overwrite_permission:

    GIVEN:
        target.target_exists = true
        overwrite_permission_explicit = false

    EXPECT:
        state == WAITING_FOR_OVERWRITE_SEAL
        github_update == false
```

```pseudo id="ludia8"
TEST patch_only_manual_execution_rejected:

    GIVEN:
        manual_pack.type = "patch_only"
        purpose = "manual upload execution"

    EXPECT:
        reject == true
        require_full_body_replacement_file == true
```

---

## 15. Human Programming Re-learning Note

```pseudo id="knlc0a"
IF:
    condition / gate

THEN:
    forward route when condition is true

ELSE:
    fallback route when condition is false, blocked, failed, or unclear
```

```pseudo id="9b6a7w"
GUARD_CLAUSE:
    early stop before dangerous action

INVARIANT:
    rule that must always remain true

STATE_MACHINE:
    map of allowed transitions

TEST:
    proof that route selection behaves as expected
```

```text id="f8t6lc"
Ark translation:

IF = Gate.
THEN = Forward Route.
ELSE = Recovery Route.
GUARD = No-Fall Fence.
INVARIANT = Covenant-like operating boundary.
TEST = Reality rehearsal.
```

---

## 16. Minimal Living Review

```yaml id="p8586f"
living_review:
  私の判断:
    - "This file should be sharp and programming-like."
    - "Main Card already preserves meaning."
    - "This file should optimize execution clarity."

  違和感:
    - "If this file becomes prose-heavy, it loses its purpose."
    - "If this file becomes autonomous, it becomes dangerous."

  Hidden_Pattern:
    - "Human-readable Canon and AI-native Projection should be separate views."

  修正条件:
    - "If conflict with main card: stop."
    - "If Human Seal is missing: stop."
    - "If tool block occurs: change transport, preserve meaning."
```

---

## 17. Final Compression

```pseudo id="hu6rc7"
MAIN = "artifact-to-github.md"
COMPANION = "artifact-to-github_programming-like.md"

MAIN.role = "Meaning View"
COMPANION.role = "Execution View"

IF conflict(MAIN, COMPANION):
    THEN stop_and_reconcile()

IF missing_exact_path:
    THEN stop_no_guessing()

IF target_exists AND no_overwrite_seal:
    THEN stop_wait_for_human_seal()

IF download_skip_explicit:
    THEN try_direct_update_once()
    ELSE use_default_download_artifact_route()

IF direct_update_success:
    THEN report_and_verify()
ELSE:
    build_full_body_manual_commit_pack()
    wait_for_human_upload()
    verify_after_upload()

ASSERT ToolFailure != ArtifactFailure
ASSERT Patch == Judgment
ASSERT FullBody == Action
ASSERT MeaningDegradation == Forbidden
```
