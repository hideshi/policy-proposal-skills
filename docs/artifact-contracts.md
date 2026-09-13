# 成果物契約（Artifact Contracts）

本ドキュメントは具体案リポ `challenges/<slug>/` のスキーマ正本である。各 role スキルと `examples/challenge-template/` はこれに従う。スキル本文中の例と食い違う場合は本契約を優先する。

## ID 規則

| 種別 | 形式 | 例 |
|---|---|---|
| 変数 | `V` + ゼロ埋め2桁以上 | `V01` |
| 出典 | `SRC-` + ゼロ埋め3桁以上 | `SRC-001` |
| 事実 | `F-` + ゼロ埋め3桁以上 | `F-001` |
| 主張 | `CLM-` + ゼロ埋め3桁以上 | `CLM-001` |
| オプション | `OPT-` + 英大文字または数字 | `OPT-A`, `OPT-1` |

追跡の最低鎖:

`Vxx → SRC-xxx + locator → F-xxx → CLM-xxx → OPT-x`

加工値（比率・差分など）は、原値と算式を `findings` または `claim-evidence` に残す。

## 変数状態（`variables.md`）

| 状態 | 意味 |
|---|---|
| `needed` | 未取得 |
| `acquired` | ファイルは取れたが、望ましい粒度・定義の充足は未確認 |
| `partial` | 一部のみ充足（期間・地域・指標が足りない） |
| `verified` | 望ましい粒度で変数を充足し、locator 付き Finding がある |
| `gap` | 公開情報では取れない／粒度不足で埋められない（推測禁止） |

後方互換: 旧 `sourced` は `verified` として扱う。新規記録では `sourced` を使わない。

必須列: `ID | 変数名 | なぜ必要か | 望ましい粒度 | 想定ソース種別 | 必須 | 状態`

- `必須`: `yes` / `no`（オーケストレータの「主要変数」はこの列で定義する）

## 出典（`sources-index.md` + `sources/`）

各 `SRC` の必須フィールド:

- 標題
- 発行主体
- 発行日または版
- 媒体種別（`stat-table` / `report` / `law` / `api` / `html` / `other`）
- 採用可否 Tier: `1` / `2` / `3`（3 は根拠に使わない）
- URL または取得クエリ
- 取得日時（ISO8601 日付で可: `YYYY-MM-DD`）
- ローカルパス（`sources/` 配下）
- sha256（必須。取得直後に計算）
- 対象変数（`Vxx` リスト）
- 対象期間・地域
- メモ

locator 例（Finding / Claim 側で使う）: `p.12`, `表3`, `CSV列 visitors / 行 year=2024`, `§2.1`

## 事実（`findings.md`）

各 Finding の必須フィールド:

- `F-ID`
- `V-ID`
- `SRC-ID`
- locator
- 原値（数値・カテゴリ）
- 単位
- 時点・地域
- 算式（加工した場合。原値のみなら `n/a`）
- メモ（解釈禁止。定義の注記のみ可）

## 主張（`claim-evidence.md`）

必須列:

`CLM-ID | Claim | Claim種別 | Evidence | 対応 | 断定の強さ | 判定 | 差し戻し先`

Claim種別:

- `descriptive`（記述）
- `causal`（因果）
- `predictive`（予測）
- `legal-institutional`（法的・制度的）
- `normative`（規範・価値判断）

対応: `direct` / `indirect` / `gap`

断定の強さ: `assert` / `estimate` / `hypothesis`（日本語併記可: 断定 / 推定 / 仮説）

判定: `PASS` / `WARN` / `FAIL`

Evidence は `F-ID` を優先。無い場合のみ `SRC-ID#locator`。規範的 Claim は資料の `direct` だけでは足りず、利用者が選んだ評価基準への参照を Evidence またはメモに残す。

## オプション（`options.md`）

各 `OPT` の必須項目:

- 介入内容
- 効くと期待する変数（`Vxx`）
- 依拠する事実（`F-ID` / `SRC`）
- 前提・必要データ（`gap`）
- 副作用・分配
- 実装主体と難所
- 検証方法
- 現状維持との差分（`OPT-現状維持` を必ず1つ置く）
- 費用・財源（分かる範囲。不明なら `gap`）
- 法的権限・実施能力
- 期間・可逆性・不確実性

**順位付け（「有力」）**: 既定では行わない。順位や推奨を書く場合のみ、次を同ファイル先頭の「評価設定」に必須記入する。

- 決定主体
- 成功指標
- 制約
- 評価軸と（任意の）重み
- 判断理由

## フェーズ判定（オーケストレータ共通）

各フェーズは次を持つ。

- 必須入力
- 出力
- `PASS` / `WARN` / `FAIL`
- 差し戻し先
- 完了条件

空ファイルの存在だけでは `PASS` にしない。
