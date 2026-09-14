# ツール別アダプタ

スキル本文の正本は常に `skills/ja/<name>/SKILL.md`。ツールごとの探索パスへは**シンボリックリンク**だけを置く（本文の二重管理をしない）。

| ツール | リポジトリ内の探索パス | 備考 |
|---|---|---|
| Codex | `.agents/skills/<name>/` | `AGENTS.md` も読む |
| Antigravity | `.agents/skills/<name>/` | `.agent/skills` は旧互換。本リポは `.agents` |
| Cursor | `.cursor/skills/`（および `.agents/skills`・`.claude/skills` も読む） | |
| Claude Code | `.claude/skills/<name>/` | プロジェクト必守は `CLAUDE.md` → `AGENTS.md` |

リンクの張り直し:

```bash
python3 scripts/sync_tool_skill_links.py
```

Windows で symlink が使えない場合は、開発者モードまたは `git config core.symlinks true` を確認する。正本 `skills/ja` を直接読ませてもよい。
