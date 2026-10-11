---
title: "STR-015 — Skills lessons集約とHubの現在案内"
canonical_path: "control-center/changes/STR-015-skills-lessons-consolidation.md"
version: "v001"
created: "2026-10-11"
updated: "2026-10-11"
recorded_by: "Work / Ark28:05"
status: "shared-source cutover saved and verified; installed update HTTP 422; legacy retirement held"
base_commit: "96dbc5413b3ef32a4f9496819ff15930b9519678"
expected_eof: "EOF::STR_015_SKILLS_LESSONS::v001"
---

# STR-015 — 学びを集め、適用条件と接続を保つ

## 1. 目的・Humanの判断・範囲

Ark28:05のHumanは、ai-projectへの限定集中とSkills分散の改善を検討し、skills/README.mdを最重要の入口と指定した。skills/_references/lessons.jsonlへskills内のlessonを集約し、既存の良い部分を他AI・Future Dotsへ渡したいと依頼した。Plan Modeで調査・計画を提示した後、2026-10-11の同Threadで「Execute GitHub OK」「Human Seal OK」と実行・継続を明示した。これは現会話の編集要約であり、取得可能な会話URL・メッセージIDは本記録で仮作成しない。

承認された目的は、入口・手順・学びの所有関係を明確にし、既存4件を意味ごと集約し、現在の参照元を切り替え、既知の利用側を確認して旧配置を整理すること。Grok／Claudeのprefix方式や_grok移設、root／Dotsのlesson移管、全Skill改訂、新Repository、通知、外部AI送信は対象外。Ark27 Main／Ark28 Supportの関係も変更しない。

## 2. 実行前のCurrentと保存する価値

基準は[実行前main](https://github.com/yusukefujiijp/ai-project/tree/96dbc5413b3ef32a4f9496819ff15930b9519678)。計画時の1c053e8から変更を確認し、Radio登録の後続成功と旧Voice資料のARC-011保管を保持した。lesson本体はRadio 1件・Voice 3件で変更なし。指定先のlessonsと同階層READMEは改行一つのSeedであり、有効な集約済みデータとは扱わなかった。

- Radio：手動の音声ボタンによる利用価値を保持し、定刻配信を必須にしない。
- Voice：本人の低い使用頻度だけで、他者の突発要望に備える価値を退役させない。
- Voiceの意味保存：未完成の問いの元表現・文脈・Unknownを移行先へ渡す。旧設計候補であり、実地成功とはしない。
- Voiceの二つの実り：内容の発見と対話方法の効果を区別する。方法の効果は未確認のまま保持する。

今回の保存対象4件：
- Radio：73e44fc7-1abe-4192-aff6-fdf54f5c2004
- Voice：ff598ad2-d8e4-4df7-b0e8-969179981138
- Voice：1ea1cb26-98e8-454d-a78c-da15bf30801b
- Voice：1a5ccae3-78cf-45bd-9409-239852706f21

[旧Radio原本](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/radio-mode/references/lessons.jsonl)と[旧Voice原本](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/voice-mode/references/lessons.jsonl)から、行と順序をそのまま継承する。ID、日時、全field、sources、caveatを保持する。固定commitの出典を、現在の保管先へ機械的に書き換えない。

## 3. 所有先と変更

- [Skills Hub](../../skills/README.md#skills-lessons)：現在の読取・更新先を冒頭へ置く。従来一覧直後の形成記録は同じREADMEの第7節へ内容を変えず移す。旧アンカーと各Skillの履歴を保持する。
- [集約lesson](../../skills/_references/lessons.jsonl)：Skillsの学びの担当原本。保管場所の集約を、全行の全Skillへの一般化にしない。
- [references案内](../../skills/_references/README.md)：Hubへ戻る短い案内のみ。契約・移行状態の第二原本にしない。
- [Radio](../../skills/radio-mode/SKILL.md)／[Voice](../../skills/voice-mode/SKILL.md)：集約先とHubへ接続し、今回の目的・条件に合う行の本文・出典・留保を一緒に読む。Triggerや基本手順・表示設定は変更しない。
- [全体references入口](../../references/README.md)、[整理PLAN](../github/PLAN.md)、[ARC-011](../github/ARCHIVE.md#arc-011)：現役のlesson導線だけを集約先へ合わせる。別領域の所有範囲・過去案件・凍結資料は変更しない。
- JSONLの形式・更新は[既存契約§3〜5](../../dots/lessons/README.md#3-全行がlesson--row-schema-2)を参照する。schema 2を保持し、Dots固有のBootは移植しない。

原本の集約先を先に公開し、登録済み利用側を切り替えてから旧ファイルを除去する。移行中の旧二ファイルは互換読取用snapshotであり、追記・二重更新しない。全Future AIの未知のcopyの消滅は証明できないため、既知の登録物・現役導線を確認する範囲と、未確認の取得経路を分けて記録する。

## 4. 確認状態

2026-10-11の開始時点で、登録済みRadio／VoiceのSkill本文をこの会話の参照経路から実際に取得し、GitHub共有版との一致を確認した。どちらも旧lesson URLを参照していた。Radioの初回拒否と、後続の承認済み通常登録の成功は歴史として保持し、今回を拒否回避の再登録として扱わない。

**GitHub共有原本：保存・照合済み。** [第一段階commit](https://github.com/yusukefujiijp/ai-project/commit/c9f58361bdc3d6c9a0ad1a92740e5db5392ade0b)で10ファイルをmainへ原子的に反映した。読取時のmainをexpected revisionとして非forceで更新し、変更範囲が指定10パスだけで削除なしであることをTreeで確認した。保存後は10ファイルすべてを固定commitから再取得し、意図した全文との一致を確認した。

**形式・意味保持：確認済み。** 元のRadio／Voice全4行を厳密JSONとして検査し、UTF-8・LF・末尾LF、空行なし、重複key／IDなし、schema 2、型・UTC日時・sourcesを確認した。集約結果は旧二ファイルをRadio→Voiceの順につないだ全bytesと一致する。SHA-256は `94111c52c452e69c7c3db439ae6654436c4d4d5204807e1e1a1fab9ee805dc44`。10,023文字の形成記録本文を同一内容で第7節へ移し、radio-voice-formationアンカーを保持した。新しい相対参照23件の所在と、固定commit出典3原本への到達を確認した。出典本文を今回新たに全文再検証したという意味ではない。

**限定読解：二つの独立文脈で確認。** 元会話・計画・期待回答を渡さず、候補Hub／Skill、集約lesson、既存形式契約と相談入力を渡した。一つはRadioの初回利用・混在するVoice lessonの適用・保存先相談で、条件付き読解、所有先、保存禁止を区別した。もう一つは未完成のVoiceの問いをTextへ移す設計相談で、元表現とUnknownを保持し、意味保存・二つの実りの二lessonを未実証の設計として扱った。構成した相談への限定応答であり、Humanの実経験としてlessonへ追加していない。

**登録先更新：未完了。** 開始時の登録先Remoteは367d4faefabaa91365e0ecd4b05782e06d5667e6。無関係な未保存変更を保持するため同じSkills Repositoryの隔離worktreeで、既存Radio／VoiceのSKILL.mdだけを変更した。両方が公式quick_validateを通過し、Trigger frontmatter・表示設定を保持、GitHubへ保存した新本文との一致を確認した。作業commitはb22ca47227b4912b88f0c65d2216b7262f3e2c4a。

通常の保存先へ一度pushしたところ、HTTP 422／RPC failed／remote disconnectを受けた。「Everything up-to-date」という末尾表示を成功とせず、Remote refを再取得して367d4faのままであることを確認した。さらにRadio／Voiceを会話内のSkill参照経路から再取得し、両方とも旧本文・旧lesson URLのままであることを確認した。422の具体的原因はUnknown。初回Radio登録時の拒否と同じ原因とは推定しない。同一要求の再送・別名・別経路での保存は行わず、ローカルの作業commitを保持した。

**旧配置：退役保留。** 登録済み二Skillがまだ旧URLを利用するため、旧Radio／Voiceの二JSONLは除去しなかった。集約先の原本化・案内更新は保存済みだが、導入先を含む完全な切替・旧配置の整理は未完了である。

GitHubの保存、登録先の保存、会話内取得、Human UI、自然な自動選択、Radioの聴き心地、Voice内直接呼出し、実生活効果はそれぞれ別のEvidenceである。今回の移設だけで全AI互換性や長期効果を実証しない。

## 5. 中断・復元・今後

中断した場合は現在の集約先、共有SKILL.md、登録先、旧配置の有無を確認し、保存済み部分を繰り返さず残工程へ戻る。登録先の切替が確認できなければ旧ファイルの退役を保留し、別名のSkillや恒久的なMirrorを増やして不足を隠さない。今回の最小回復は、正規Skill保存先のHTTP 422の原因を確認・解消し、最新の共有版と登録先の差分を照合して同じ二Skillへ反映すること。登録先・実際の参照本文を確認してから旧二ファイルを退役し、GitHubを再取得する。基準以降のHuman訂正・STOP・並行変更があれば保持する。同じ承認Scopeを再計画する必要はないが、権限・アクセス条件が原因なら解決前に再送しない。

旧原本の正確な内容は第2節の固定commitとGit履歴で復元できる。後続のlesson更新があれば、旧snapshotで集約先を上書きしない。復元の必要・現在の権限・利用側の依存を確かめ、保存済み4件の同一性だけで後続の全状態を戻せるとは扱わない。

新しい経験やHuman Correctionがあれば、今回の適用範囲・参照・更新のどこで判断が変わるかを見て担当原本へ戻す。通常の支援ごとの新lesson登録、全履歴読込、追加Trialは義務にしない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利。HumanのCorrection・STOP・Final Sealと適用Guardを保持し、AI・Skill・文書をKeliとして扱う。

EOF::STR_015_SKILLS_LESSONS::v001
