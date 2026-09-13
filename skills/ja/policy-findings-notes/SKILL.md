---
name: policy-findings-notes
version: 0.1.0
description: 保存済みソースから変数ごとの事実だけを findings.md に抜き出し、解釈や政策結論を混入させない。
---

# 政策事実メモ

## 目的

ソースを読んだ結果を、解釈なしの事実として変数ごとに固定する。

## 発動タイミング

- `sources/` と `sources-index.md` に Tier 1/2 の実体があるとき
- [`policy-proposal-examination`](../policy-proposal-examination/SKILL.md) の Phase 4

## 手順

1. 変数ごとに、ソースから読み取れる事実だけを書く。
2. 数値は単位・時点・地域をセットにする。
3. 出典は `SRC-xxx` を付ける。
4. 「だから〇〇政策が必要」などの解釈は書かない（[`policy-option-comparison`](../policy-option-comparison/SKILL.md) へ）。

## 成果物

- `challenges/<slug>/findings.md`

## やらないこと

- 未保存ソースや記憶上の数値で埋める
- findings に政策オプションの結論を書く
