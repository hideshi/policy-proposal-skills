---
name: policy-variable-inventory
description: "課題文が固まったあとに、課題の説明・計測・介入評価に必要な変数を洗い出し、variables.md に状態付きで整理するときに使う。"
metadata:
  version: "0.2.1"
---

# 政策変数インベントリ

## 目的

課題を説明し、介入効果を後から検証するために必要な変数を列挙する。手段から逆算しない。

スキーマ正本: [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md)

## 発動タイミング

- `challenge.md` の課題一文があるとき
- Phase 2

## 前提

- [`policy-challenge-framing`](../policy-challenge-framing/SKILL.md) が PASS/WARN

## 手順

1. 課題一文から測る／説明する必要があるものを列挙する
2. 契約の列（ID、必須、状態など）で `variables.md` を書く
3. 状態の初期値は `needed`
4. おおむね 8〜15。課題に直結しないものは除外する
5. 「主要変数」は `必須=yes` の行とする

## 手段条件付き変数

Phase 5 からの差し戻し時だけ追加できる（必須=`no`。「なぜ必要か」に対象 OPT-ID）。主要変数と 8〜15 の目安には数えず、課題変数を置き換えない。観点は契約。

## フェーズ判定

| | |
|---|---|
| 必須入力 | 課題一文 |
| 出力 | `variables.md`（`必須=yes` が1つ以上） |
| PASS | 必須変数が定義され、手段逆算になっていない（手段条件付きは契約の例外） |
| WARN | 変数が多い／粒度が粗い |
| FAIL | 課題一文なし、または必須変数ゼロ |
| 差し戻し先 | Phase 1 |
| 完了条件 | PASS または WARN |

## 成果物

- `challenges/<slug>/variables.md`
