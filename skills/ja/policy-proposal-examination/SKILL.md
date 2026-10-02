---
name: policy-proposal-examination
description: "課題起点の政策案検討の全体手順を案内するときに使う。個別作業は role 別スキルへ委譲するオーケストレータ。"
metadata:
  version: "0.3.4"
---

# 課題起点の政策案検討（オーケストレータ）

## 目的

フェーズ順と通過条件を案内し、詳細は role スキルと [`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md) に委譲する。

## リポジトリ役割

| 種類 | 置くもの |
|---|---|
| 本スキル集 | 手順・契約・雛形のみ |
| 具体案リポジトリ | `challenges/<slug>/` の実データ |

開始前に具体案リポジトリのルートを確定する。対象が本スキル集自身なら停止する。相対パスは具体案リポジトリ基準。

スイート一括でも個別スキル導入でも、書き込み先確認と契約ドキュメント参照は必須。個別導入時はスキル集の `examples/` が無い場合があるため、契約に従ってテンプレートを手作成してよい。

## 不変条件

1. 課題先行
2. 根拠は採用可否 Tier 1/2 のみ。適合性は別判定
3. ローカル実体化 + sha256
4. 追跡鎖 `V → SRC+locator → F → CLM → OPT`
5. 出典のない数値は使わない。欠測は `gap`
6. 空ファイルの存在だけではフェーズ PASS にしない
7. 順位付けは評価設定があるときだけ
8. **利害の原則:** 受益側の改善だけで成功としない。労働者・住民・事業者などへの分配・負荷・安全も同じ課題の一部として扱う。一方的損失を根拠なしに推し進めない。トレードオフは隠さず測り、緩和・補償・中止を設計候補に残す。すべての主体が同時に改善する状況は稀であり、悪化させない／抑えるを現実目標とする

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

### 条件付きの枝（制度確認）

Phase 5 で、手段候補に制度上の要件がありうるときだけ発動する（例: AI の開発・提供・利用）。課題一文は変えない。手段条件付き変数を足し、`2 → (3a ⇄ 3b) → 4` を再実行して Phase 5 に戻る。その後は通常どおり Phase 6 へ進む。不発動は FAIL にしない。

完了の目安は、対象 OPT の制度要件が契約の判定条件に従って `verified` または `gap` で明示されていること。同じ確認を非 AI の代替案にも行う。

## 利用者への返し方

1. 課題一文
2. 必須変数の状態（verified / partial / gap）
3. オプション比較の要約（順位付けした場合のみ、評価軸と理由）。分配・副作用の gap を隠さない
4. 次に取得するデータ（優先度付き）
5. 開いている WARN/FAIL
6. 利害（誰が受益／不利益を受けうるか）の未計測箇所

## 提出パッケージ

外向け・提出用に 1 冊（Markdown + PDF）へまとめるときは [`policy-submission-package`](../policy-submission-package/SKILL.md) に委譲する。中身の定義は `docs/artifact-contracts.md` の「提出パッケージ」。

## 完了条件

- 各フェーズが FAIL でない
- 断定は claim-evidence 上で監査済み
- 追跡鎖が契約どおり結ばれている
