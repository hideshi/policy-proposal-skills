---
name: policy-option-comparison
version: 0.1.0
description: 事実メモと gap を前提に、課題に対する複数の政策オプションを options.md で比較する（是非の二択に潰さない）。
---

# 政策オプション比較

## 目的

課題に対する介入案を複数並べ、依拠する事実・欠測・副作用・実装主体・検証方法で比較する。

## 発動タイミング

- `findings.md` があり、主要変数が `sourced` または明示的 `gap` のとき
- [`policy-proposal-examination`](../policy-proposal-examination/SKILL.md) の Phase 5

## 手順

各オプションに次を書く。

- 介入内容（誰が何をするか）
- 効くと期待する変数（Vxx）
- 依拠する事実（`SRC` / findings）
- 前提・必要データ（未充足の `gap`）
- 副作用・分配への影響
- 実装主体（国 / 都道府県 / 自治体 / 民間）と難所
- 検証方法（パイロットで見る指標）

「入れる／入れない」の二択にしない。地域変数で向き不向きを書く。

## 成果物

- `challenges/<slug>/options.md`

## やらないこと

- findings に無い事実を前提にする
- gap を隠して断定する
