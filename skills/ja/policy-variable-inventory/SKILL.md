---
name: policy-variable-inventory
version: 0.1.0
description: 課題文が固まったあとに、課題の説明・計測・介入評価に必要な変数を洗い、variables.md に needed/sourced/gap で整理する。
---

# 政策変数インベントリ

## 目的

課題を説明し、介入の効果を後から検証するために必要な変数を列挙する。手段から逆算しない。

## 発動タイミング

- `challenge.md` の課題一文があるとき
- [`policy-proposal-examination`](../policy-proposal-examination/SKILL.md) の Phase 2

## 前提

- [`policy-challenge-framing`](../policy-challenge-framing/SKILL.md) 済み

## 手順

1. 課題一文から「測る／説明する必要があるもの」を列挙する。
2. 各変数に次を付ける。

| 列 | 内容 |
|---|---|
| ID | `V01` 形式 |
| 変数名 | |
| なぜ必要か | 課題との論理 |
| 望ましい粒度 | 地域・時間・手段 |
| 想定ソース種別 | 国統計 / 自治体 / 研究 等 |
| 状態 | `needed` / `sourced` / `gap` |

3. おおむね 8〜15 を目安に、課題に直結しない変数は削る。
4. `challenges/<slug>/variables.md` に書く。

## 成果物

- `challenges/<slug>/variables.md`

## やらないこと

- 特定手段の擁護に必要な変数だけを拾う
- データが無いと分かっているのに `sourced` にする
