---
name: policy-proposal-examination
description: "課題起点の政策案検討の全体手順を案内するときに使う。個別作業は role 別スキルへ委譲するオーケストレータ。"
metadata:
  version: "0.3.1"
---

# 課題起点の政策案検討（オーケストレータ）

## 目的

フェーズ順と通過条件を案内し、詳細は role スキルと [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md) に委譲する。

## リポジトリ役割

| 種類 | 置くもの |
|---|---|
| 本スキル集 | 手順・契約・雛形のみ |
| 具体案リポ | `challenges/<slug>/` の実データ |

開始前に具体案リポのルートを確定する。対象が本スキル集自身なら停止する。相対パスは具体案リポ基準。

スイート一括でも個別スキル導入でも、書き込み先確認と契約ドキュメント参照は必須。個別導入時はスキル集の `examples/` が無い場合があるため、契約に従ってテンプレを手作成してよい。

## 不変条件

1. 課題先行
2. 根拠は採用可否 Tier 1/2 のみ。適合性は別判定
3. ローカル実体化 + sha256
4. 追跡鎖 `V → SRC+locator → F → CLM → OPT`
5. 野良数値禁止。欠測は `gap`
6. 空ファイルの存在だけではフェーズ PASS にしない
7. 順位付けは評価設定があるときだけ
8. **利害の原則:** 受益側だけを勝ちにしない。労働者・住民・事業者などへの分配・負荷・安全も同じ課題の一部として扱う。一方的損失を根拠なしに推し進めない。トレードオフは隠さず測り、緩和・補償・中止を設計候補に残す。完全な同時 Win-Win は稀であり、悪化させない／抑えるを現実目標とする

## フェーズ

| Phase | 委譲先 | 完了の目安 |
|---|---|---|
| 1 | [`policy-challenge-framing`](../policy-challenge-framing/SKILL.md) | 課題一文が承認済み |
| 2 | [`policy-variable-inventory`](../policy-variable-inventory/SKILL.md) | 必須変数あり |
| 3a | [`policy-source-criticism-gate`](../policy-source-criticism-gate/SKILL.md) | Tier+適合 |
| 3b | [`policy-evidence-ingestion`](../policy-evidence-ingestion/SKILL.md) | 取得+sha256。3a⇄3b ループ可 |
| 4 | [`policy-findings-notes`](../policy-findings-notes/SKILL.md) | locator 付き Finding。必須は verified/gap |
| 5 | [`policy-option-comparison`](../policy-option-comparison/SKILL.md) | 現状維持+代替。順位付けは評価設定付きのみ |
| 6 | [`policy-claim-evidence-gate`](../policy-claim-evidence-gate/SKILL.md) | FAIL Claim ゼロまたは WARN 受容 |

依存と差し戻しの概略:

`1 → 2 → (3a ⇄ 3b) → 4 → 5 → 6`。FAIL なら表の差し戻し先へ戻る。

## 利用者への返し方

1. 課題一文
2. 必須変数の状態（verified / partial / gap）
3. オプション比較の要約（順位付けした場合のみ、評価軸と理由）。分配・副作用の gap を隠さない
4. 次に取るデータ（優先度付き）
5. 開いている WARN/FAIL
6. 利害（誰が得／損しうるか）の未計測箇所

## 完了条件

- 各フェーズが FAIL でない
- 断定は claim-evidence 上で監査済み
- 追跡鎖が契約どおり結れている
