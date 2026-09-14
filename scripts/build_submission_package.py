#!/usr/bin/env python3
"""Build submission-package.md (+ optional PDF) for a policy challenge folder."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from pathlib import Path

PROFILES = {
    "analysis-pilot": [
        "cover",
        "challenge",
        "facts",
        "gaps",
        "sources",
        "analysis",
        "pilots",
    ],
    "policy-options": [
        "cover",
        "challenge",
        "facts",
        "gaps",
        "sources",
        "options",
        "distribution",
    ],
    "full": [
        "cover",
        "challenge",
        "facts",
        "gaps",
        "sources",
        "analysis",
        "options",
        "distribution",
        "pilots",
        "claims",
    ],
}

PRINCIPLE = (
    "利害の原則: 受益側だけを勝ちにしない。"
    "労働者・住民・事業者などへの分配・負荷・安全も同じ表で見る。"
    "一方的損失を根拠なしに推さない。トレードオフは測り、緩和・補償・中止を設計候補に残す。"
)


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def first_heading_block(md: str, max_chars: int = 4000) -> str:
    md = md.strip()
    if not md:
        return "_（ファイルなし）_\n"
    if len(md) <= max_chars:
        return md + "\n"
    return md[:max_chars].rstrip() + "\n\n_（長いため要約抜粋。正本は課題フォルダを参照）_\n"


def extract_summary_facts(summary: str) -> str:
    if not summary:
        return "_summary.md なし。findings / claim-evidence を参照。_\n"
    # Prefer the PASS table section if present
    m = re.search(r"## いま言える数字.*?(?=\n## |\Z)", summary, re.S)
    if m:
        return m.group(0).strip() + "\n"
    return first_heading_block(summary, 3000)


def extract_gaps(summary: str, analysis: str) -> str:
    parts = []
    for label, text in (("summary", summary), ("analysis", analysis)):
        m = re.search(r"## 残.*?(?=\n## |\Z)", text, re.S)
        if m:
            parts.append(f"### from {label}\n\n{m.group(0).strip()}\n")
    return "\n".join(parts) if parts else "_残ギャップ節が見つからない。variables の gap を確認。_\n"


def extract_sources_index(si: str, limit: int = 200) -> str:
    if not si:
        return "_sources-index.md なし_\n"
    blocks = re.findall(r"### (SRC-\d+)\n(.*?)(?=\n### SRC-|\Z)", si, re.S)
    lines = [
        "| SRC | 標題 | 発行主体 | Tier | URL |",
        "|---|---|---|---|---|",
    ]
    for sid, body in blocks[:limit]:
        title = re.search(r"- 標題:\s*(.*)", body)
        pub = re.search(r"- 発行主体:\s*(.*)", body)
        tier = re.search(r"- 採用可否 Tier:\s*(.*)", body)
        url = re.search(r"- URL または取得クエリ:\s*(.*)", body)
        url_s = url.group(1).strip() if url else ""
        if url_s:
            murl = re.search(r"https?://\S+", url_s)
            url_s = murl.group(0).rstrip(")。,]") if murl else url_s.split()[0]
        url_s = url_s.replace("|", "\\|")
        lines.append(
            f"| {sid} | {title.group(1).strip() if title else ''} | "
            f"{pub.group(1).strip() if pub else ''} | "
            f"{tier.group(1).strip() if tier else ''} | "
            f"{url_s} |"
        )
    if len(blocks) > limit:
        lines.append(f"\n_他 {len(blocks) - limit} 件は sources-index.md 参照。_\n")
    return "\n".join(lines) + "\n"


def extract_claims_flags(ce: str) -> str:
    if not ce:
        return "_claim-evidence.md なし_\n"
    flags = []
    for line in ce.splitlines():
        if "| CLM-" in line and ("**FAIL**" in line or "**WARN**" in line or "| FAIL" in line or "| WARN" in line):
            flags.append(line)
    if not flags:
        return "_表形式の WARN/FAIL 行を抽出できず。正本を参照。_\n"
    return "抽出（機械）:\n\n" + "\n".join(flags[:80]) + "\n"


def build_md(challenge_dir: Path, profile: str, title: str | None) -> tuple[str, dict]:
    slug = challenge_dir.name
    challenge = read(challenge_dir / "challenge.md")
    summary = read(challenge_dir / "summary.md")
    analysis = read(challenge_dir / "analysis.md")
    options = read(challenge_dir / "options.md")
    pilots = read(challenge_dir / "pilot-tickets.md")
    sources_index = read(challenge_dir / "sources-index.md")
    claims = read(challenge_dir / "claim-evidence.md")
    today = dt.date.today().isoformat()
    included = PROFILES[profile]
    used_files = []

    def note_file(name: str, content: str) -> None:
        if content.strip():
            used_files.append(name)

    note_file("challenge.md", challenge)
    note_file("summary.md", summary)
    note_file("analysis.md", analysis)
    note_file("options.md", options)
    note_file("pilot-tickets.md", pilots)
    note_file("sources-index.md", sources_index)
    note_file("claim-evidence.md", claims)

    display_title = title or f"提出パッケージ: {slug}"
    parts: list[str] = []

    if "cover" in included:
        one_liner = ""
        m = re.search(r"## 課題一文\n\n(.+)", summary)
        if m:
            one_liner = m.group(1).split("\n")[0].strip()
        elif challenge:
            m2 = re.search(r"課題一文[：:]*\s*(.+)", challenge)
            one_liner = m2.group(1).strip() if m2 else ""
        parts.append(
            f"# {display_title}\n\n"
            f"- 課題 slug: `{slug}`\n"
            f"- 生成日: {today}\n"
            f"- プロファイル: `{profile}`\n"
            f"- 位置づけ: 提出用パッケージ（リポジトリ正本の要約・再構成）\n\n"
            f"## 提出用の一文\n\n{one_liner or '_要確認_'}\n\n"
            f"## 利害の原則\n\n{PRINCIPLE}\n"
        )

    if "challenge" in included:
        parts.append("## 課題と対象\n\n" + first_heading_block(challenge or summary, 5000))

    if "facts" in included:
        parts.append("## いま言える事実\n\n" + extract_summary_facts(summary))

    if "gaps" in included:
        parts.append("## 残ギャップ\n\n" + extract_gaps(summary, analysis))

    if "sources" in included:
        parts.append("## 出典一覧（要約）\n\n" + extract_sources_index(sources_index))

    if "analysis" in included:
        parts.append("## 課題分析\n\n" + first_heading_block(analysis, 8000))

    if "options" in included:
        parts.append("## 政策オプション比較\n\n" + first_heading_block(options, 10000))

    if "distribution" in included:
        # Pull 副作用・分配 oriented chunks loosely from options
        dist = "\n".join(
            line for line in options.splitlines() if "副作用" in line or "分配" in line or "労働" in line
        )
        parts.append(
            "## 副作用・分配・検証の要点\n\n"
            + (dist[:4000] + "\n" if dist else "_options.md の副作用・分配欄を正本参照。_\n")
        )

    if "pilots" in included:
        parts.append("## 実証実験の起票\n\n" + first_heading_block(pilots, 12000))

    if "claims" in included:
        parts.append("## 主張と根拠（WARN/FAIL 要約）\n\n" + extract_claims_flags(claims))

    parts.append(
        "\n---\n\n"
        "本 PDF/Markdown は提出用パッケージである。"
        "数値の正本は課題フォルダの findings / sources を優先する。\n"
    )

    manifest = {
        "slug": slug,
        "profile": profile,
        "generated": today,
        "sections": included,
        "source_files": used_files,
    }
    return "\n\n".join(parts), manifest


def write_manifest(path: Path, manifest: dict) -> None:
    lines = ["# auto-generated", f"slug: {manifest['slug']}", f"profile: {manifest['profile']}", f"generated: {manifest['generated']}", "sections:"]
    for s in manifest["sections"]:
        lines.append(f"  - {s}")
    lines.append("source_files:")
    for f in manifest["source_files"]:
        lines.append(f"  - {f}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_pdf(md_path: Path, pdf_path: Path) -> tuple[bool, str]:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False, "pandoc が無い"
    xelatex = shutil.which("xelatex")
    if not xelatex:
        # fallback: HTML only message
        html_path = pdf_path.with_suffix(".html")
        cmd = [pandoc, str(md_path), "-o", str(html_path), "--standalone", "-f", "markdown", "-t", "html"]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            return False, f"HTML フォールバックも失敗: {e.stderr[-500:]}"
        return False, f"xelatex が無いため PDF 未生成。HTML を出力: {html_path}"

    cmd = [
        pandoc,
        str(md_path),
        "-o",
        str(pdf_path),
        "--pdf-engine=xelatex",
        "-V",
        "documentclass=ltjsarticle",
        "-V",
        "geometry:margin=20mm",
        "--metadata",
        "lang=ja",
    ]
    # Prefer Noto if available; ignore if engine rejects
    fonts = [
        "-V",
        "CJKmainfont=Noto Sans CJK JP",
        "-V",
        "mainfont=Noto Sans CJK JP",
    ]
    try:
        subprocess.run(cmd + fonts, check=True, capture_output=True, text=True)
        return True, str(pdf_path)
    except subprocess.CalledProcessError:
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            return True, str(pdf_path)
        except subprocess.CalledProcessError as e:
            return False, e.stderr[-800:] or e.stdout[-800:] or "pandoc PDF 失敗"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--challenge-dir", type=Path, required=True)
    ap.add_argument("--profile", choices=sorted(PROFILES), default="analysis-pilot")
    ap.add_argument("--title", default=None)
    ap.add_argument("--pdf", action="store_true")
    args = ap.parse_args()
    challenge_dir = args.challenge_dir.resolve()
    if not challenge_dir.is_dir():
        print(f"not a directory: {challenge_dir}", file=sys.stderr)
        return 2

    md, manifest = build_md(challenge_dir, args.profile, args.title)
    md_path = challenge_dir / "submission-package.md"
    manifest_path = challenge_dir / "submission-manifest.yaml"
    md_path.write_text(md, encoding="utf-8")
    write_manifest(manifest_path, manifest)
    print(f"wrote {md_path}")
    print(f"wrote {manifest_path}")

    if args.pdf:
        pdf_path = challenge_dir / "submission-package.pdf"
        ok, msg = build_pdf(md_path, pdf_path)
        print(("PDF OK: " if ok else "PDF skipped/failed: ") + msg)
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
