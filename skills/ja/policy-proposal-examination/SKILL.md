---
name: policy-proposal-examination
version: 0.2.0
description: 課題起点の政策案検討の全体手順を案内する。個別作業は role 別スキルに委譲するオーケストレータ。
---

# 課題起点の政策案検討（オーケストレータ）

## 目的

政策案検討のフェーズ順を案内し、作業本体は役割別スキルに委譲する。本ファイルに詳細手順を抱え込まない。

## リポジトリ役割

| 種類 | 置くもの |
|---|---|
| 本スキル集 | 手順・雛形のみ（公開可） |
| 具体案リポ | `challenges/<slug>/` の課題・出典・案（非公開可） |

`examples/challenge-template/` を具体案リポへコピーして開始する。スキル集に実データや実政策案をコミットしない。

## 不変条件（全体）

1. 課題先行（手段ありき禁止）
2. 根拠は Tier 1/2 のみ
3. 根拠は具体案リポへローカル実体化
4. 野良数値禁止
5. 欠測は `gap` と書く

## フェーズ

| Phase | やること | 委譲先 |
|---|---|---|
| 1 | 課題固定 | [`policy-challenge-framing`](../policy-challenge-framing/SKILL.md) |
| 2 | 変数洗い出し | [`policy-variable-inventory`](../policy-variable-inventory/SKILL.md) |
| 3a | 情報源 Tier 判定 | [`policy-source-criticism-gate`](../policy-source-criticism-gate/SKILL.md) |
| 3b | 取得とローカル保存 | [`policy-evidence-ingestion`](../policy-evidence-ingestion/SKILL.md) |
| 4 | 事実メモ | [`policy-findings-notes`](../policy-findings-notes/SKILL.md) |
| 5 | オプション比較 | [`policy-option-comparison`](../policy-option-comparison/SKILL.md) |
| 6 | 主張と根拠の監査 | [`policy-claim-evidence-gate`](../policy-claim-evidence-gate/SKILL.md) |

利用者の状態に応じて、途中フェーズから入ってよい。前フェーズの成果物が無ければ戻る。

## 利用者への返し方

長文の前に短く:

1. 課題一文
2. 充足変数 / `gap`
3. 有力オプションと支える `SRC`
4. 次に取るデータ（優先度付き）

## 完了条件

- 各フェーズの成果物があり、断定には `policy-claim-evidence-gate` 上の direct な根拠がある
