# Policy Proposal Skills

課題起点で政策案を検討するための AI エージェント用スキル集です。

特定の政策手段の是非から入らず、**課題を先に固定**し、変数を洗い、公開情報で裏取りし、取得物をローカルに残してから政策オプションを比較します。

情報源の階層（Tier）と claim–evidence 対応は、[scholarly-agent-skills](https://github.com/hideshi/scholarly-agent-skills) の考え方を政策向けに分けたものです。

## スキル（役割別）

| スキル | 用途 |
|---|---|
| [`policy-proposal-examination`](skills/ja/policy-proposal-examination/SKILL.md) | 全体手順のオーケストレータ |
| [`policy-challenge-framing`](skills/ja/policy-challenge-framing/SKILL.md) | 課題固定 |
| [`policy-variable-inventory`](skills/ja/policy-variable-inventory/SKILL.md) | 変数インベントリ |
| [`policy-source-criticism-gate`](skills/ja/policy-source-criticism-gate/SKILL.md) | 情報源 Tier 判定 |
| [`policy-evidence-ingestion`](skills/ja/policy-evidence-ingestion/SKILL.md) | 公開データの取得・ローカル保存 |
| [`policy-findings-notes`](skills/ja/policy-findings-notes/SKILL.md) | 事実メモ |
| [`policy-option-comparison`](skills/ja/policy-option-comparison/SKILL.md) | 政策オプション比較 |
| [`policy-claim-evidence-gate`](skills/ja/policy-claim-evidence-gate/SKILL.md) | 主張と根拠のゲート |

カタログ: [`skills/ja/README.md`](skills/ja/README.md)

## リポジトリの役割分担

| リポジトリ | 中身 | 公開の想定 |
|---|---|---|
| **本リポ** | 手順・雛形・ルール（スキル） | いずれ公開 |
| 具体案リポ（利用者が用意） | 課題ごとの出典・事実・政策案 | 非公開でも可 |

具体の政策案・取得ファイルは本リポに置かない。`examples/challenge-template/` は空の雛形のみ。

## 導入

```bash
# 例: 隣接配置
# ~/repo/policy-proposal-skills
# ~/repo/<your-policy-cases>
```

課題ディレクトリは具体案リポ側に作り、`examples/challenge-template/` をコピーして始める。全体の流れは `policy-proposal-examination`、個別作業は上表の role スキルへ。

## 免責

無保証の検討支援です。詳細は [DISCLAIMER.md](DISCLAIMER.md)。
