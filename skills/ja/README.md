# 日本語スキル

スキーマ正本: [`docs/artifact-contracts.md`](../../docs/artifact-contracts.md)

## 依存関係

```text
policy-proposal-examination (orchestrator)
├─ policy-challenge-framing
├─ policy-variable-inventory
├─ policy-source-criticism-gate  ←→  policy-evidence-ingestion
├─ policy-findings-notes
├─ policy-option-comparison
└─ policy-claim-evidence-gate
（提出時）policy-submission-package
```

差し戻し: 各スキルのフェーズ判定表を参照。

| ディレクトリ | 役割 |
|---|---|
| [`policy-proposal-examination`](policy-proposal-examination/SKILL.md) | 全体手順のオーケストレータ |
| [`policy-challenge-framing`](policy-challenge-framing/SKILL.md) | 課題固定 |
| [`policy-variable-inventory`](policy-variable-inventory/SKILL.md) | 変数インベントリ |
| [`policy-source-criticism-gate`](policy-source-criticism-gate/SKILL.md) | 採用可否 Tier と適合性 |
| [`policy-evidence-ingestion`](policy-evidence-ingestion/SKILL.md) | 取得・ローカル保存 |
| [`policy-findings-notes`](policy-findings-notes/SKILL.md) | 事実抽出 |
| [`policy-option-comparison`](policy-option-comparison/SKILL.md) | オプション比較 |
| [`policy-claim-evidence-gate`](policy-claim-evidence-gate/SKILL.md) | 主張と根拠のゲート |
| [`policy-submission-package`](policy-submission-package/SKILL.md) | 提出用パッケージと PDF 化 |
