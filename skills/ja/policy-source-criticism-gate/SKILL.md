---
name: policy-source-criticism-gate
description: "出典候補の採用前や sources-index の監査時に、発行主体の採用可否と当該 Claim／変数への適合性を分けて判定するときに使う。"
metadata:
  version: "0.2.0"
---

# 政策向け情報源批判ゲート

## 目的

根拠への低信頼情報の混入を防ぐ。**採用可否（Tier）**と**当該 Claim／変数への適合性**を混同しない。

スキーマ正本: [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md)

## 発動タイミング

- 出典候補の採用直前
- [`policy-evidence-ingestion`](../policy-evidence-ingestion/SKILL.md) の前後
- 既存 `sources-index.md` の監査時

## 二軸判定

### 軸A: 採用可否 Tier（発行主体・真正性）

- **Tier 1**: 国統計・白書・法令、国際公的機関、査読付きの確定データ
- **Tier 2**: 自治体公式、公的・準公的研究所、大学公式の紀要・DP
- **Tier 3**: SNS、個人ブログ、まとめ、百科事典本文、商業 PR → **根拠不可**

Tier 1/2 は「候補として利用可能」であり、「その Claim を直接支える」意味ではない。

### 軸B: Claim／変数への適合性

別フィールドで記録する（`適合: fit / partial / unfit`）。

- 地域・期間・対象集団・指標定義が変数の望ましい粒度と一致するか
- 記述／因果／予測など、使いたい Claim 種別に対して資料が答えているか
- 鮮度・版・利益相反・方法開示

「一次資料」と「Tier」は別概念。Tier 2 の報告書は二次整理であることが多い。

## 手順

1. 軸Aで Tier を付ける。Tier 3 は却下し一次を探す
2. 軸Bで対象 `Vxx` または想定 Claim 種別への適合を付ける
3. `fit` 以外を根拠の `direct` に使わない（`partial` は Finding で `partial`／Claim で `indirect`/`WARN`）
4. 判定理由を `sources-index.md` のメモまたは監査欄に残す

## フェーズ判定

| | |
|---|---|
| 必須入力 | URL／ファイル候補と対象 `Vxx` |
| 出力 | Tier + 適合の判定 |
| PASS | Tier 1/2 かつ適合 `fit` |
| WARN | Tier 1/2 かつ `partial` |
| FAIL | Tier 3 または `unfit` |
| 差し戻し先 | 探索のやり直し / Phase 2（変数粒度の見直し） |

## 成果物

- `sources-index.md` 上の判定（本スキルはファイル取得を所有しない）

## やらないこと

- Tier だけで Direct Match を宣言する
- Tier 3 を参考として数値根拠に使う
