---
name: policy-evidence-ingestion
description: "needed 変数について公開データを取得し、具体案リポの sources/ に保存して sources-index.md を更新する（ローカル実体化）ときに使う。"
metadata:
  version: "0.2.0"
---

# 政策根拠データの実体化

## 目的

主張に使う数値・報告書を URL だけに頼らず、具体案リポへ保存して再現可能にする。本スキルは**取得と `sources-index` 更新**を所有する。判定ロジックの正本は [`policy-source-criticism-gate`](../policy-source-criticism-gate/SKILL.md)。

スキーマ正本: [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md)

## 発動タイミング

- `variables.md` に `needed` / `partial` があるとき
- Phase 3

## ループ

`候補探索 → 軸A/B判定 → 取得・保存 → 内容確認 → 変数状態更新 → 必要なら再探索`

## 手順

1. 書き込み先が具体案リポか確認（スキル集なら停止）
2. 各対象変数について Tier 1→2 で候補を探す
3. [`policy-source-criticism-gate`](../policy-source-criticism-gate/SKILL.md) で判定
4. PASS/WARN のみ `sources/` へ保存（PDF/CSV 優先）
5. **sha256 を計算して必須記入**
6. `sources-index.md` に契約フィールドを書く（発行日、媒体、取得クエリ、対象変数など）
7. 検索記録: 使ったクエリ、取得日、不採用候補（Tier3や unfit）をメモに残してよい
8. 変数状態を更新: ファイルのみ → `acquired`、粒度不足 → `partial`、取れない → `gap`。`verified` は Finding 作成後（Phase 4）
9. 推測で埋めない

## フェーズ判定

| | |
|---|---|
| 必須入力 | `variables.md`、具体案リポルート |
| 出力 | `sources/*`、`sources-index.md`、更新された変数状態 |
| PASS | 必須変数がすべて `acquired` 以上または明示 `gap`、各採用 SRC に sha256 |
| WARN | 必須に `partial` が残る |
| FAIL | 必須が `needed` のまま、または sha256／ローカルパス欠落 |
| 差し戻し先 | Phase 2 または source-criticism |
| 完了条件 | FAIL でないこと。`verified` は Phase 4 後 |

## 成果物

- `sources/`
- `sources-index.md`
- 更新された `variables.md`
