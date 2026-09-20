# Schedules

## 0. Purpose

このDirectoryは、ChatGPT等で実行されるSchedule Taskの **public-safe・versioned・Future-AI-readable source** を保存する。

Schedule UIだけにPromptを置くと、Thread移行・Task再作成・AI交代で「なぜ現在のPromptになったか」が失われる。そこで実行RuntimeとGitHubを分離して接続する。

```text
Human Reality / Feedback
        ↓
Schedule Prompt Design
        ↓
GitHub schedules/  ← Durable / Versioned Source
        ↓
ChatGPT Schedule   ← Execution Runtime
        ↓
Reality Output
        ↓
Human Feedback ───→ next revision
```

GitHubはScheduleを実行しない。Schedule RuntimeはGitHubの存在だけで自動同期されない。
**GitHubは再現可能なSource、Scheduleは実行面**である。

## 1. Design Principles

- **Simple is best! / KISS / DRY / YAGNI / Lean**
- 一つのScheduleにつき一つのfolder。
- Current Promptは各folderの `PROMPT.md` に一つだけ置く。
- 通常の変更履歴はGit historyをPrimaryにし、version fileを毎回複製しない。
- Git導入以前など、Git historyだけでは意味を復元できない転換点だけ `HISTORY.md` に残す。
- READMEはPrompt本文を複製せず、Identity / Runtime coordinate / Sync rule / read orderだけを持つ。
- Schedule内部ID・秘密情報・private dataは保存しない。
- Current Human RealityとGitHubが異なる場合はReality Deltaとして扱い、黙って片方へ寄せない。

## 2. Graph Mode / Relation-First

```text
Source Reality
   ↓
Research Rail
Daily Aliyah Deep Tree
   ↓  Format Best Practice only
Publication Rail
Parasha Kindle Compiler
   ↓
Daily Book Page
   ↓
Human Reading Feedback
   ↓
Prompt Revision
   ↓
GitHub Durable Source
   ↓
Schedule Runtime
   └────────────→ next Daily Book Page
```

重要なのは図そのものではなく、**依存・Feedback・更新経路をFuture AIが復元できること**。

## 3. Current Registry

| Schedule | Status | Runtime | GitHub Source |
|---|---|---|---|
| Parasha Kindle Compiler | active | Daily 18:00 Asia/Tokyo | [parasha-kindle-compiler/](parasha-kindle-compiler/) |

他のScheduleは、GitHub-backed管理が実際に必要になった時だけ追加する。最初から全TaskをMirrorしない。

## 4. Folder Contract

```text
schedules/
├── README.md
└── <schedule-name>/
    ├── README.md
    ├── PROMPT.md
    └── HISTORY.md   # 必要な時だけ
```

- `README.md`: Identity / runtime coordinate / relation / sync rule。
- `PROMPT.md`: Runtimeへ投入するCurrent Prompt。Prompt本文のSSOT候補。
- `HISTORY.md`: Git history以前の重要な意味変化だけ。

## 5. Sync Contract

```text
1. Current Runtime確認
2. Human Feedback / Reality Delta確認
3. PROMPT.md更新
4. GitHub再取得で保存確認
5. 同じPromptをSchedule Runtimeへ反映
6. cadence / timezone / titleが意図せず変わっていないか確認
7. 次の実RunをReality Feedbackとして観測
```

GitHub保存だけでRuntime反映済みと見なさない。
Runtime更新だけでGitHub保存済みと見なさない。
両者が一致して初めて **synced** と扱う。

## 6. Future AI Read Order

1. `schedules/README.md`
2. 対象Scheduleの `README.md`
3. `PROMPT.md`
4. 必要な場合だけ `HISTORY.md`
5. Current Schedule Runtime
6. Current Human Feedback / latest Reality

Current Sourceから入り、必要なHistoryだけ遡る。

## 7. Current Seed

最初のGitHub-backed Scheduleは **Parasha Kindle Compiler**。

- [README](parasha-kindle-compiler/README.md)
- [Current Prompt](parasha-kindle-compiler/PROMPT.md)
- [Bootstrap History](parasha-kindle-compiler/HISTORY.md)

---

GitHub preserves the source.  
Schedule executes the source.  
Reality tests the source.  
Human feedback changes the next source.
