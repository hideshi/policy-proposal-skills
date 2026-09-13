# Policy Proposal Skills

課題起点で政策案を検討するための AI エージェント用スキル集です。

特定の政策手段（例: ライドシェアの是非）から入らず、**課題を先に固定**し、変数を洗い、国・都道府県・自治体・独立研究機関などの公開情報で裏取りし、取得物をローカルに残してから政策オプションを比較します。

情報源の階層（Tier）と、主張（Claim）と根拠（Evidence）の対応は、[scholarly-agent-skills](https://github.com/hideshi/scholarly-agent-skills) の `source-criticism-gate` / `claim-evidence-gate` の考え方を政策検討向けに簡略化したものです。

## スキル

| スキル | 用途 |
|---|---|
| [`policy-proposal-examination`](skills/ja/policy-proposal-examination/SKILL.md) | 課題固定 → 変数 → 公開データ収集・ローカル保存 → オプション比較 → claim–evidence |

## リポジトリの役割分担

| リポジトリ | 中身 | 公開の想定 |
|---|---|---|
| **本リポ** (`policy-proposal-skills`) | 手順・雛形・ルール（スキル） | いずれ公開 |
| 具体案リポ（利用者が用意） | 課題ごとの出典・事実・政策案 | 非公開でも可 |

具体の政策案・取得した統計ファイルは本リポに置かない。`examples/challenge-template/` は空の雛形のみ。

## 導入

具体案リポのルートで、本スキルをサブモジュールまたは隣接クローンとして参照し、エージェントに `skills/ja/policy-proposal-examination/SKILL.md` を読ませる。

```bash
# 例: 隣接配置
# ~/repo/policy-proposal-skills
# ~/repo/<your-policy-cases>
```

課題ディレクトリは具体案リポ側に作り、`examples/challenge-template/` をコピーして始める。

## 免責

無保証の検討支援です。数値・出典・政策オプションに誤りが残り得ます。詳細は [DISCLAIMER.md](DISCLAIMER.md)。
