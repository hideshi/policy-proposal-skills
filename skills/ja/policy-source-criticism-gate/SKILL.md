---
name: policy-source-criticism-gate
version: 0.1.0
description: 政策根拠として使うURL・統計・報告書の信頼性を Tier 1/2/3 で判定し、Tier 3 を根拠から除外する。
---

# 政策向け情報源批判ゲート

## 目的

政策案の根拠に、信頼性の低い情報源が混入するのを防ぐ。学術向け `source-criticism-gate` を政策公開データ向けに簡略化したものである。

## 発動タイミング

- 新しい出典候補を採用する直前
- [`policy-evidence-ingestion`](../policy-evidence-ingestion/SKILL.md) の取得前・保存前
- 既存の `sources-index.md` を監査するとき

## 判定基準

### Tier 1（最優先・根拠可）

- 国の統計・白書・法令・審議会資料
- 国際公的機関（OECD、World Bank、UN 系など）
- 査読付き学術論文・公的リポジトリの確定データ

### Tier 2（根拠可）

- 都道府県・市区町村の公式統計・計画・議会資料
- 公的・準公的な独立研究機関・シンクタンクの報告書
- 大学公式ドメインの紀要・ディスカッションペーパー

### Tier 3（根拠不可）

- SNS、個人ブログ、まとめ、Wikipedia 本文、商業 PR
- 手掛かりにする場合は一次（Tier 1/2）へ辿り、一次だけを根拠にする

## 手順

1. 発行主体とドメインで Tier を付ける。
2. Tier 1/2 のみ採用可とする。
3. Tier 3 は却下し、代替の一次を探す。
4. 判定結果を `sources-index.md` の Tier 欄、または監査メモに残す。

## 成果物

- 各 SRC の Tier 判定（`sources-index.md`）

## やらないこと

- Tier 3 を「参考」として本文・比較表の数値根拠に使う
- 発行主体を確認せずドメイン見た目だけで Tier 1 にする
