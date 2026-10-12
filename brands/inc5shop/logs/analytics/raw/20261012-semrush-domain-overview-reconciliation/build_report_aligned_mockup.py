"""Create a visibly labelled mockup from page 1 of the supplied Semrush PDF.

The overlaid figures come from the user-supplied Inc5 SEO deck. The result is
illustrative and must never be presented as an unmodified Semrush export.
"""

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[6]
SOURCE = Path(__file__).with_name("semrush-domain-overview.pdf")
OUTPUT = ROOT / "output/pdf/Inc5_Semrush_Report_Aligned_ILLUSTRATIVE_2026-10-12.pdf"

PAGE_W, PAGE_H = 612.0, 792.0
IMAGE_W, IMAGE_H = 1275.0, 1650.0
SCALE_X, SCALE_Y = PAGE_W / IMAGE_W, PAGE_H / IMAGE_H
METRIC_BLUE = HexColor("#5366d0")
LINK_BLUE = HexColor("#2d83d7")
GREEN = HexColor("#188a6d")


def x(px):
    return px * SCALE_X


def y(px):
    return PAGE_H - px * SCALE_Y


def whiteout(c, left, top, right, bottom):
    c.setFillColor(white)
    c.rect(x(left), y(bottom), x(right - left), y(top) - y(bottom), fill=1, stroke=0)


def text(c, value, left, baseline, size, color=METRIC_BLUE, bold=True):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    c.drawString(x(left), y(baseline), value)


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    overlay_data = BytesIO()
    c = canvas.Canvas(overlay_data, pagesize=(PAGE_W, PAGE_H))

    # Persistent attribution across the top of the page.
    whiteout(c, 210, 0, 1240, 39)
    text(
        c,
        "ILLUSTRATIVE REPORT-ALIGNED EDIT - NOT A SEMRUSH EXPORT",
        315,
        26,
        10.2,
        HexColor("#c52727"),
    )

    # AI Search: report score and platform mentions; cited pages remain higher.
    whiteout(c, 327, 257, 354, 280)
    text(c, "38", 330, 275, 9.0)
    whiteout(c, 382, 257, 428, 280)
    text(c, "430", 385, 275, 9.0)
    for top, bottom, baseline, value in [
        (284, 301, 297, "103"),
        (302, 318, 315, "12"),
        (320, 336, 333, "35"),
        (337, 354, 351, "280"),
    ]:
        whiteout(c, 382, top, 419, bottom)
        text(c, value, 384, baseline, 6.9, LINK_BLUE, False)

    # SEO Overview: exact deck headline values and its 2025–26 deltas.
    whiteout(c, 736, 257, 840, 282)
    text(c, "308.5K", 739, 275, 9.1)
    text(c, "+29.1%", 804, 274, 5.1, GREEN, False)
    whiteout(c, 736, 316, 836, 342)
    text(c, "15K", 739, 334, 9.1)
    text(c, "+94.8%", 776, 333, 5.1, GREEN, False)
    whiteout(c, 988, 316, 1056, 342)
    text(c, "7.5K", 990, 334, 9.1)

    # Keep the Worldwide row consistent with the AI headline above.
    whiteout(c, 449, 474, 471, 493)
    text(c, "38", 455, 487, 6.5, HexColor("#34343a"), False)
    whiteout(c, 489, 474, 522, 493)
    text(c, "430", 497, 487, 6.5, LINK_BLUE, False)

    c.showPage()
    c.save()
    overlay_data.seek(0)

    source_page = PdfReader(str(SOURCE)).pages[0]
    source_page.merge_page(PdfReader(overlay_data).pages[0])
    writer = PdfWriter()
    writer.add_page(source_page)
    writer.add_metadata(
        {
            "/Title": "Inc5 illustrative report-aligned Semrush overview",
            "/Subject": "Report figures overlaid on source screenshot; not a Semrush export",
            "/Keywords": "illustrative, edited, Inc5 SEO report",
        }
    )
    with OUTPUT.open("wb") as file:
        writer.write(file)
    print(OUTPUT)


if __name__ == "__main__":
    main()
