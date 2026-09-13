---
name: policy-claim-evidence-gate
description: "政策メモやオプション比較の断定・評価語について、保存済み根拠との対応を判定し、根拠不足の断定を止めるときに使う。"
metadata:
  version: "0.2.0"
---

# 政策 claim–evidence ゲート

## 目的

Claim と Evidence の対応を監査する。**原稿を勝手に書き換えず**、判定と差し戻し先を返す。

スキーマ正本: [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md)

## 発動タイミング

- `options.md` や政策メモに断定・評価語があるとき
- Phase 6

## 手順

1. 断定・統計・評価語を含む文を `CLM-ID` 化する
2. Claim種別を付ける（descriptive / causal / predictive / legal-institutional / normative）
3. Evidence は `F-ID` 優先、なければ `SRC#locator`
4. 対応 `direct/indirect/gap`、断定の強さ、判定 `PASS/WARN/FAIL`、差し戻し先を記入
5. 規範的 Claim は評価基準への参照が無ければ FAIL または WARN
6. 評価語には比較基準を要求する
7. FAIL の Claim はトーンを落とすか削除するよう差し戻す（本ゲートは提案まで）

## フェーズ判定

| | |
|---|---|
| 必須入力 | 監査対象文、findings / sources |
| 出力 | `claim-evidence.md` |
| PASS | 強い断定がすべて direct + 適切な種別 |
| WARN | indirect や基準不足が残るが明示 |
| FAIL | 未保存数値、Tier3、locator なし、規範 Claim の基準なし |
| 差し戻し先 | Phase 4/5 または option の評価設定 |
| 完了条件 | FAIL Claim がゼロ、または利用者が WARN 受容を明示 |

## 成果物

- `claim-evidence.md`
