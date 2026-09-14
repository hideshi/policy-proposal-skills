---
name: policy-submission-package
description: "政策案や実証実験案を外部・社内へ提出するとき、含める情報を契約どおりにパッケージし、1つの PDF にする。"
metadata:
  version: "0.1.8"
---

# 提出パッケージと PDF 化

## 目的

課題フォルダの成果物から、提出用の **1 冊**（Markdown 正本 + PDF）を作る。何を入れるかは推測せず、[`docs/artifact-contracts.md`](../../../docs/artifact-contracts.md) の「提出パッケージ」に従う。

## 発動タイミング

- 政策案・実証実験案の双方または一方を、どこかへ提出・共有するとき
- `analysis.md` / `pilot-tickets.md` / `options.md` / `summary.md` などが揃い、外向けに束ねたいとき

## 事前条件

- 書き込み先は**具体案リポ**の `challenges/<slug>/`
- スキル集リポ自身への実データ書き込みは禁止
- PDF エンジン: 推奨 `pandoc` HTML → `weasyprint`（クリック可能なリンク注釈・青＋下線のため）。だめなら `pandoc` + `xelatex`（日本語は Noto CJK 等）。どちらも無ければ HTML のみで PDF は `gap`。余白はスクリプト既定（HTML 横幅 56em・左右 18px、PDF `@page` 上下 14mm・左右 10mm）

## 手順

1. 提出目的を確認し、プロファイルを選ぶ: `analysis-pilot`（既定） / `policy-options` / `full`
2. 契約の必須セクションをチェックリスト化し、欠けている章は作らないか、先に role スキルで埋める
3. `scripts/build_submission_package.py` で `<課題物理名>.md` と `<課題物理名>-マニフェスト.yaml` を生成する（ファイル名＝日本語の課題物理名）（出典 URL は Markdown リンク。表示テキストはパス末尾のファイル名／セグメント、href はフル URL。HTML は青＋下線・`target=_blank`、PDF はリンク注釈）
4. 同じスクリプトで PDF を試す（失敗時は原因と不足パッケージを返す）
5. 表紙の一文要約と利害の原則を利用者が確認してから提出用とする
6. commit/push は明示時のみ

## フェーズ判定

| | |
|---|---|
| 必須入力 | 課題 slug、プロファイル、具体案リポ上の該当ファイル |
| 出力 | `<課題物理名>.md`、可能なら `.pdf`、`<課題物理名>-マニフェスト.yaml` |
| PASS | 契約セクションが揃い、野良数値が無く、利害の原則が冒頭にある。PDF または「PDF 未生成理由」が明示 |
| WARN | 必須に近いファイルが partial（例: pilot-tickets が DRAFT だらけ）だが提出用に注記した |
| FAIL | プロファイルと中身が不一致、効果断定の未監査転載、sources 全文の同梱 |
| 差し戻し先 | 欠けに応じて analysis / options / pilot-tickets / claim-evidence |
| 完了条件 | FAIL でない。提出前に利用者確認 |

## 成果物

- `<課題物理名>.md`
- `<課題物理名>.pdf`（可能な環境）
- `<課題物理名>-マニフェスト.yaml`

## サンプル

見た目の例: [`examples/submission-package-sample/`](../../../examples/submission-package-sample/)（京都・`analysis-pilot`）。

## コマンド例

```bash
python3 /path/to/policy-proposal-skills/scripts/build_submission_package.py \
  --challenge-dir /path/to/policy-proposals/challenges/<slug> \
  --profile analysis-pilot \
  --pdf
```
