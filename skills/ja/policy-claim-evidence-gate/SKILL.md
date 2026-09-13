---
name: policy-claim-evidence-gate
version: 0.1.0
description: 政策メモやオプション比較の断定・評価語について、SRC との対応強度を判定し、根拠不足の断定を止める。
---

# 政策 claim–evidence ゲート

## 目的

政策文案の主張（Claim）と、保存済み根拠（Evidence）の対応を監査する。学術向け `claim-evidence-gate` の簡略版。

## 発動タイミング

- `options.md` や政策メモに断定・評価語を書く前／書いた直後
- [`policy-proposal-examination`](../policy-proposal-examination/SKILL.md) の Phase 6

## 手順

1. 断定・統計・「不足」「深刻」等の評価語を含む文を抽出する。
2. 各 Claim を `SRC` / 数値とペアにする。
3. 対応を `direct` / `indirect` / `gap` で付ける。
4. 断定の強さを `断定` / `推定` / `仮説` に合わせる。
5. `gap` や indirect のみの主張はトーンを落とすか削除する。
6. 評価語には比較基準（他地域・前年・公式の目安）を要求する。

| Claim | Evidence (SRC / 数値) | 対応 | 断定の強さ |
|---|---|---|---|
|  |  | direct / indirect / gap | 断定 / 推定 / 仮説 |

## 成果物

- `challenges/<slug>/claim-evidence.md`

## やらないこと

- ローカル未保存の数値を Evidence にする
- Tier 3 を Evidence にする
