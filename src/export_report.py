"""report.md -> report.pdf (A4). Needs: markdown, playwright (chromium).

    python src/export_report.py
"""
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
CSS = """
@page { size: A4; margin: 16mm 17mm 16mm 17mm; }
body { font: 10pt/1.42 "Helvetica Neue", Arial, sans-serif; color: #111; }
h1 { font-size: 16pt; margin: 0 0 2mm; } h2 { font-size: 12pt; margin: 5mm 0 1.5mm; border-bottom: 1px solid #ccc; }
p { margin: 1.5mm 0; } ol, ul { margin: 1mm 0; padding-left: 6mm; } li { margin: 0.6mm 0; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0; font-size: 8.8pt; }
th, td { border: 1px solid #bbb; padding: 1mm 1.6mm; vertical-align: top; } th { background: #f0f0f0; }
img { width: 100%; margin: 1mm 0; } img[src^="handrechnung"] { width: auto; max-width: 100%; max-height: 245mm; display: block; margin: 2mm auto; page-break-inside: avoid; } code { font-size: 8.8pt; }
hr { page-break-after: always; border: 0; }
"""


def main():
    md = (ROOT / "report.md").read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["tables"])
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    tmp = ROOT / "report.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(tmp.as_uri())
        pg.pdf(path=str(ROOT / "report.pdf"), format="A4", print_background=True)
        b.close()
    tmp.unlink()
    print("wrote report.pdf")


if __name__ == "__main__":
    main()
