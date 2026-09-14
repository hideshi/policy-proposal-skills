# Policy Proposal Skills

課題起点で政策案を検討するための AI エージェント用スキル集です。

特定の政策手段の是非から入らず、**課題を先に固定**し、変数を洗い、公開情報で裏取りし、取得物をローカルに残してから政策オプションを比較します。

成果物のスキーマ正本は [`docs/artifact-contracts.md`](docs/artifact-contracts.md) です。追跡鎖は次のとおりです。

`V → SRC + locator → Finding → Claim → Option`

## スキル（役割別）

カタログと依存関係: [`skills/ja/README.md`](skills/ja/README.md)

| スキル | 用途 |
|---|---|
| `policy-proposal-examination` | 全体手順のオーケストレータ |
| `policy-challenge-framing` | 課題固定 |
| `policy-variable-inventory` | 変数インベントリ |
| `policy-source-criticism-gate` | 採用可否 Tier と Claim/変数への適合性 |
| `policy-evidence-ingestion` | 公開データの取得・ローカル保存 |
| `policy-findings-notes` | 事実抽出 |
| `policy-option-comparison` | 政策オプション比較（既定は順位付けしない） |
| `policy-claim-evidence-gate` | 主張と根拠のゲート |
| `policy-submission-package` | 提出用パッケージ定義と PDF 化 |

## リポジトリの役割分担

| リポジトリ | 中身 | 公開の想定 |
|---|---|---|
| **本リポ** | 手順・契約・雛形・検査・提出サンプル | 公開 |
| 具体案リポ | 課題ごとの出典・事実・政策案 | 非公開でも可 |

開始前に具体案リポのルートを確定すること。本スキル集自身への実データ書き込みは禁止。

## サンプル

- 課題フォルダ雛形: [`examples/challenge-template/`](examples/challenge-template/)
- 提出パッケージ（京都・analysis-pilot）: [`examples/submission-package-sample/`](examples/submission-package-sample/)

## 検査

```bash
python3 scripts/check_skill_frontmatter.py
python3 scripts/check_challenge_artifacts.py /path/to/cases-repo/challenges/<slug>
python3 scripts/build_submission_package.py --challenge-dir /path/to/cases-repo/challenges/<slug> --profile analysis-pilot --pdf
```

## 免責

無保証の検討支援です。詳細は [DISCLAIMER.md](DISCLAIMER.md)。
