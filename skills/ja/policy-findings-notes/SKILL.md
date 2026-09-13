---
name: policy-findings-notes
description: "保存済みソースから変数ごとの事実を findings.md に抜き出すとき（解釈や政策結論を混入させない）に使う。"
metadata:
  version: "0.2.0"
---

# 政策事実抽出

## 目的

ソースから解釈なしの事実を変数ごとに固定する。

スキーマ正本: [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md)

## 発動タイミング

- Tier 1/2 の実体が `sources/` にあるとき
- Phase 4

## 手順

1. 契約どおり `F-ID` / `V-ID` / `SRC-ID` / locator / 原値 / 単位 / 時点・地域 / 算式 を書く
2. locator 必須（ページ・表・列行など）
3. 加工値は原値と算式を残す
4. 解釈・政策結論は書かない
5. 必須変数が Finding で望ましい粒度を満たしたら `variables.md` を `verified` に更新。足りなければ `partial` / `gap`

## フェーズ判定

| | |
|---|---|
| 必須入力 | `sources-index.md` とローカルファイル |
| 出力 | `findings.md`、変数状態の更新 |
| PASS | 必須変数が `verified` または明示 `gap`。各 Finding に locator |
| WARN | 必須に `partial` |
| FAIL | locator 欠落、未保存ソース参照、解釈混入 |
| 差し戻し先 | Phase 3 / source-criticism |
| 完了条件 | FAIL でない |

## 成果物

- `findings.md`
- 更新された `variables.md`
