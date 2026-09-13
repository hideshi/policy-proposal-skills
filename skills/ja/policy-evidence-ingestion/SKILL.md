---
name: policy-evidence-ingestion
version: 0.1.0
description: needed 変数について公開データを取得し、具体案リポの sources/ に保存して sources-index.md にメタデータを残す（ローカル実体化）。
---

# 政策根拠データの実体化

## 目的

主張に使う数値・報告書を URL だけに頼らず、具体案リポへ保存して再現可能にする。

## 発動タイミング

- `variables.md` に `needed` があるとき
- [`policy-proposal-examination`](../policy-proposal-examination/SKILL.md) の Phase 3

## 前提

- [`policy-variable-inventory`](../policy-variable-inventory/SKILL.md)
- 保存前に [`policy-source-criticism-gate`](../policy-source-criticism-gate/SKILL.md) で Tier 判定

## 手順

1. 各 `needed` 変数について Tier 1 → Tier 2 の順で探す。
2. Tier 判定する。Tier 3 は根拠保存の対象外（手掛かりなら一次へ）。
3. PDF・CSV 優先で `challenges/<slug>/sources/` に保存する。HTML のみの場合は本文・表を抽出し、元 URL を必ず残す。
4. `sources-index.md` に追記する。

```markdown
### SRC-001
- 標題:
- 発行主体:
- Tier: 1 | 2
- URL:
- 取得日: YYYY-MM-DD
- ローカルパス: sources/...
- 対象変数: V01
- 対象期間・地域:
- メモ:
```

5. 可能なら sha256 を残す。
6. 取得できない／粒度不足は変数を `gap` にし、推測で埋めない。
7. 取れた変数は `sourced` に更新する。

## 成果物

- `challenges/<slug>/sources/*`
- `challenges/<slug>/sources-index.md`
- 更新された `variables.md`

## やらないこと

- ローカル未保存のまま数値を findings / options に書く
- Tier 3 を sources に「根拠」として登録する
