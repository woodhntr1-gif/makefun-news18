#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

Renders a newspaper front page entirely with PIL vector shapes and real
text (DejaVu fonts). No network, no raster photos, no AI imagery.
Run:  python3 draw.py [output-path]   (default: entry.png beside this file)
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
PAPER = (247, 243, 232)
INK = (26, 26, 26)
RED = (178, 34, 28)
BLUE = (31, 78, 121)
GREY = (96, 96, 96)
LIGHT = (233, 226, 210)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)   # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)          # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)     # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)            # noqa: E731


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill=INK, leading=None):
    """Draw lines; return y just below the last line."""
    if leading is None:
        leading = int(fnt.size * 1.22)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_bridge_scene(draw, x, y, w, h):
    """Flat vector illustration: the Kerch Bridge with its road arch
    collapsed into the strait. All shapes drawn with PIL primitives."""
    sky = (183, 214, 232)
    sea = (64, 122, 158)
    sea_dark = (43, 96, 130)
    deck = (58, 58, 62)
    arch = (120, 40, 36)
    draw.rectangle([x, y, x + w, y + h], fill=sky)
    # sun + clouds
    draw.ellipse([x + w - 110, y + 18, x + w - 62, y + 66], fill=(250, 214, 120))
    for cx, cy, r in ((x + 70, y + 34, 26), (x + 150, y + 26, 20),
                      (x + 300, y + 44, 22), (x + 700, y + 30, 18)):
        draw.ellipse([cx - r, cy - r // 2, cx + r, cy + r // 2], fill=(240, 244, 248))
    horizon = y + int(h * 0.60)
    draw.rectangle([x, horizon, x + w, y + h], fill=sea)
    # wave lines
    for wy in range(horizon + 12, y + h - 6, 16):
        for wx in range(x + 8, x + w - 40, 64):
            draw.arc([wx, wy, wx + 44, wy + 12], 0, 180, fill=sea_dark, width=3)
    # bridge deck: left span intact, middle span collapsed, right span intact
    deck_y = y + 62
    gap0, gap1 = x + int(w * 0.44), x + int(w * 0.60)
    draw.rectangle([x + 6, deck_y, gap0, deck_y + 14], fill=deck)
    draw.rectangle([gap1, deck_y, x + w - 6, deck_y + 14], fill=deck)
    # support pillars under the intact spans
    for px in (x + 90, x + 300, x + w - 220, x + w - 90):
        draw.rectangle([px, deck_y + 14, px + 12, horizon + 16], fill=(90, 90, 94))
    # standing arch over the left span
    draw.arc([x + 150, deck_y - 48, x + 330, deck_y + 24], 180, 360,
             fill=arch, width=7)
    # collapsed span: deck slab tilted down into the water
    draw.polygon([(gap0 - 6, deck_y + 2), (gap1 + 8, deck_y + 12),
                  (gap1 - 16, horizon + 38), (gap0 - 44, horizon + 22)],
                 fill=(74, 74, 78))
    # splash + smoke
    mid = (gap0 + gap1) // 2
    for sx, sy, r in ((mid - 30, horizon + 30, 16), (mid + 6, horizon + 36, 20),
                      (mid + 36, horizon + 28, 13)):
        draw.ellipse([sx - r, sy - r // 2, sx + r, sy + r // 2],
                     fill=(226, 238, 244))
    for sx, sy, r in ((mid - 30, deck_y - 24, 16), (mid + 6, deck_y - 38, 20),
                      (mid + 36, deck_y - 22, 14)):
        draw.ellipse([sx - r, sy - r // 2, sx + r, sy + r // 2],
                     fill=(120, 120, 118))
    draw.rectangle([x, y, x + w - 1, y + h - 1], outline=INK, width=2)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36                      # side margin
    cw = W - 2 * mx              # content width = 952

    # ---------- masthead ----------
    d.line([(mx, 22), (W - mx, 22)], fill=INK, width=3)
    title = "THE WORLD IN ONE IMAGE"
    tf = SERIF_B(52)
    d.text(((W - d.textlength(title, font=tf)) / 2, 34), title,
           font=tf, fill=INK)
    date = "WEDNESDAY  \u00b7  18 NOVEMBER 2026"
    df = SANS_B(28)
    d.text(((W - d.textlength(date, font=df)) / 2, 100), date,
           font=df, fill=RED)
    tag = "One day. One page. The news that mattered."
    gf = SERIF(20)
    d.text(((W - d.textlength(tag, font=gf)) / 2, 132), tag,
           font=gf, fill=GREY)
    d.line([(mx, 162), (W - mx, 162)], fill=INK, width=3)
    d.line([(mx, 168), (W - mx, 168)], fill=INK, width=1)

    # ---------- lead story ----------
    y = 180
    d.text((mx, y), "LEAD STORY  \u00b7  UKRAINE", font=SANS_B(18), fill=RED)
    y += 28
    head = "KERCH BRIDGE FALLS INTO THE SEA"
    hf = SERIF_B(38)
    d.text((mx, y), head, font=hf, fill=INK)
    y += 48
    lead = ("Ukraine struck the Kerch Bridge for a second day and a section "
            "of its road deck fell into the strait overnight. Traffic "
            "halted; Russia hit two Kyiv bridges in return.")
    y = text_block(d, mx, y, wrap(d, lead, SANS(21), cw), SANS(21),
                   leading=27)
    y += 6
    draw_bridge_scene(d, mx, y, cw, 140)
    y += 140 + 8
    cap = ("The 19 km road-and-rail bridge to Crimea, after the second strike "
           "in two days. Drawing: PIL.")
    y = text_block(d, mx, y, wrap(d, cap, SERIF(16), cw), SERIF(16),
                   fill=GREY, leading=20)
    y += 8
    d.line([(mx, y), (W - mx, y)], fill=INK, width=2)
    y += 12

    # ---------- story grid: 2 columns x 3 rows ----------
    stories = [
        ("MANILA  \u00b7  ASIA",
         "TRUMP IN MANILA; XI NEXT",
         "Trump met President Marcos at the ASEAN summit; tariff talks "
         "follow today. He flies to Shenzhen for Xi."),
        ("MARKETS  \u00b7  WALL STREET",
         "NVIDIA DOUBLES SALES; DOW SINKS",
         "Nvidia revenue hit $115.8bn, up 103%, in its first report "
         "since its CEO's ouster. The Dow fell 849."),
        ("THE GULF  \u00b7  BAHRAIN",
         "DRONES OVER BAHRAIN; U.S. HITS BACK",
         "Iran said its drones hit a U.S. radar at Sheikh Isa; Bahrain "
         "said they were intercepted. The U.S. struck back."),
        ("LONDON  \u00b7  BRITAIN",
         "UK SANCTIONS 8 SETTLEMENT FIRMS",
         "Asset freezes and director bans on firms building in the "
         "West Bank, to protect the two-state solution."),
        ("SOUTH ASIA  \u00b7  WEATHER",
         "CYCLONE AKVAN BEARS DOWN ON INDIA",
         "Landfall is forecast for noon on Friday 20 Nov on the "
         "Andhra coast, winds 120\u2013130 km/h; 74 rescue teams ready."),
        ("SPORT  \u00b7  DHAKA",
         "INDIA'S 10TH SAFF CROWN",
         "India came from behind to beat Pakistan 2\u20131 in the SAFF "
         "final in Dhaka; Sandip Mandi's 88th-minute winner."),
    ]
    col_w = (cw - 28) // 2
    row_h = 122
    for i, (kick, headline, body) in enumerate(stories):
        cx = mx + (i % 2) * (col_w + 28)
        cy = y + (i // 2) * row_h
        d.text((cx, cy), kick, font=SANS_B(16), fill=RED)
        hl = wrap(d, headline, SANS_B(20), col_w)
        hy = text_block(d, cx, cy + 22, hl, SANS_B(20), leading=24)
        text_block(d, cx, hy + 2, wrap(d, body, SANS(17), col_w),
                   SANS(17), leading=21)
        if i % 2 == 0:
            d.line([(cx + col_w + 14, cy), (cx + col_w + 14, cy + row_h - 16)],
                   fill=(200, 192, 172), width=1)
        if i < 4:
            d.line([(mx, cy + row_h - 12), (W - mx, cy + row_h - 12)],
                   fill=(200, 192, 172), width=1)
    y += 3 * row_h + 4
    d.line([(mx, y), (W - mx, y)], fill=INK, width=2)
    y += 8

    # ---------- in brief ----------
    d.text((mx, y), "ALSO TODAY", font=SANS_B(17), fill=RED)
    y += 24
    briefs = [
        "Canada and China extended trade cooperation as Xi Jinping met PM Mark Carney ahead of the APEC summit.",
        "UN: at least 372 civilians were killed in Ukraine in October; over 2,230 in Sudan in Jan\u2013Oct 2026.",
        "PM Modi proposed free e-visas at the ASEAN-India summit; Amazon pledged $7bn for renewables in India.",
    ]
    for b in briefs:
        d.text((mx, y + 1), "\u2022", font=SANS_B(17), fill=RED)
        y = text_block(d, mx + 20, y,
                       wrap(d, b, SANS(16), cw - 20), SANS(16), leading=20)
        y += 2

    # ---------- footer ----------
    d.line([(mx, H - 44), (W - mx, H - 44)], fill=INK, width=1)
    foot = ("Drawn with PIL from reported headlines, 18 Nov 2026  \u00b7  "
            "Sources: Reuters, AP, AFP, Al Jazeera, IMD, IANS")
    ff = SANS(14)
    d.text(((W - d.textlength(foot, font=ff)) / 2, H - 36), foot,
           font=ff, fill=GREY)

    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out}  {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
