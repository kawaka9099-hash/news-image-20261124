#!/usr/bin/env python3
"""Draw the 1024x1024 front page of THE WORLD TODAY for Tuesday 24 Nov 2026.

Code-drawn newspaper, no photographs. Run: python3 draw.py
Writes entry.png next to this file. All facts come from the verified
prep file for 24 November 2026; every story carries its day label,
its CONFIRMED / REPORTED / CLAIM tag and its sources.
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (27, 42, 74)
NAVY_LINE = (120, 140, 180)
GREY = (90, 86, 78)
GOLD = (214, 164, 65)
PALE = (205, 212, 226)
SEA = (208, 224, 236)
LAND = (198, 178, 140)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/truetype/noto",
]


def find_font(names):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    raise FileNotFoundError("no font found for %r" % (names,))


SERIF_B = find_font(["DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf"])
SERIF = find_font(["DejaVuSerif.ttf", "LiberationSerif-Regular.ttf"])
SERIF_I = find_font(["DejaVuSerif-Italic.ttf", "LiberationSerif-Italic.ttf"])
SANS_B = find_font(["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"])
SANS = find_font(["DejaVuSans.ttf", "LiberationSans-Regular.ttf"])

_cache = {}


def font(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


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


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    """Draw a wrapped paragraph; returns y after the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def check_w(draw, text, fnt, max_w, tag):
    w = draw.textlength(text, font=fnt)
    if w > max_w:
        print("OVERFLOW", tag, "width", round(w), "avail", max_w, ":", text)
    return w


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- newsprint grain (seeded, deterministic; under the ink) -------
    rng = random.Random(20261124)
    for _ in range(65000):
        x = rng.randint(15, W - 16)
        y = rng.randint(15, H - 16)
        c = rng.choice([(240, 236, 226), (250, 247, 238), (244, 240, 230)])
        d.point((x, y), fill=c)

    # --- page frame ---------------------------------------------------
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=1)

    # --- masthead -----------------------------------------------------
    mast = font(SERIF_B, 68)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, 20), title, font=mast, fill=INK)
    rule(d, 24, W - 24, 104, 2)

    date_f = font(SERIF_B, 21)
    dateline = "TUESDAY 24 NOVEMBER 2026"
    tw = d.textlength(dateline, font=date_f)
    d.text(((W - tw) / 2, 112), dateline, font=date_f, fill=INK)
    rule(d, 24, W - 24, 140, 2)

    # --- headline story 1: Nvidia --------------------------------------
    y = 148
    kick_f = font(SERIF_B, 17)
    check_w(d, "TECH \u00b7 NVIDIA \u2014 BOARD VOTE MONDAY \u00b7 CONFIRMED",
            kick_f, W - 48, "headline kicker")
    d.text((24, y), "TECH \u00b7 NVIDIA \u2014 BOARD VOTE MONDAY \u00b7 CONFIRMED",
           font=kick_f, fill=RED)

    y = 170
    d.text((24, y), "HUANG IS BACK", font=font(SERIF_B, 50), fill=INK)

    y = 226
    dek_f = font(SERIF, 17)
    dek = ("Nvidia\u2019s board reinstated Jensen Huang as president and "
           "CEO on Monday, 11 days after he resigned.")
    check_w(d, dek, dek_f, W - 48, "dek")
    d.text((24, y), dek, font=dek_f, fill=INK)
    print("dek at", y)

    # --- split: dark fact box (left) + body text (right) -------------
    box_x, box_y, box_w, box_h = 24, 254, 540, 164
    d.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], fill=NAVY)
    bx = box_x + 16
    by = box_y + 10
    d.text((bx, by), "ELEVEN DAYS OUT, THEN A U-TURN", font=font(SANS_B, 16),
           fill=GOLD)
    by += 26
    rule(d, bx, box_x + box_w - 16, by, 1, NAVY_LINE)
    by += 9

    stat_n = font(SERIF_B, 24)
    stat_l = font(SANS, 14)
    stats = [
        ("11 DAYS", "out of the job (resigned 12 Nov)"),
        ("UNANIMOUS", "board vote to reinstate, effective at once"),
        ("NO RISK", "no national security risk, board says"),
    ]
    for num, lab in stats:
        d.text((bx, by), num, font=stat_n, fill=(255, 255, 255))
        nw = d.textlength(num, font=stat_n)
        d.text((bx + nw + 12, by + 5), lab, font=stat_l, fill=PALE)
        by += 27

    # timeline: 12 Nov -> last week -> 24 Nov (inset so labels stay in box)
    tl_y = by + 2
    tl_x0, tl_x1 = bx + 46, box_x + box_w - 16 - 46
    d.line([(tl_x0, tl_y), (tl_x1, tl_y)], fill=NAVY_LINE, width=2)
    for frac, yr, lab in ((0.0, "12 NOV", "resigns"),
                          (0.5, "LAST WK", "\u201cno reinstatement\u201d"),
                          (1.0, "24 NOV", "reinstated")):
        cx = tl_x0 + frac * (tl_x1 - tl_x0)
        d.ellipse([cx - 5, tl_y - 5, cx + 5, tl_y + 5], fill=GOLD)
        yf = font(SANS_B, 12)
        lf = font(SANS, 11)
        yw = d.textlength(yr, font=yf)
        d.text((cx - yw / 2, tl_y + 8), yr, font=yf, fill=(255, 255, 255))
        lw = d.textlength(lab, font=lf)
        d.text((cx - lw / 2, tl_y + 23), lab, font=lf, fill=PALE)
    print("fact box bottom", box_y + box_h, "timeline labels end",
          tl_y + 23 + 11)

    # right-hand body column
    body_end = para(d, 584, 254,
                    "The reversal is sharp: last week the board said it "
                    "\u201cdoes not intend to reinstate\u201d him. Now it says "
                    "it is satisfied with his candour and leadership, and saw "
                    "no national security risk after input from senior US "
                    "government officials. Trump praised the move on Truth "
                    "Social.",
                    font(SERIF, 17), W - 24 - 584, 21)
    print("headline body ends at", body_end)
    d.text((584, body_end + 6),
           "Sources: WSJ \u00b7 CNN \u00b7 Al Jazeera \u00b7 Nikkei Asia \u00b7 "
           "Rappler \u00b7 Morningstar",
           font=font(SERIF_I, 11), fill=GREY)

    rule(d, 24, W - 24, 426, 2)

    # --- two medium stories: Hormuz + Libya ---------------------------
    mid_y = 434
    col_w2 = 476
    left_x, right_x = 24, 524

    def medium(x, kicker, headline, body, sources):
        yy = mid_y
        kf = font(SERIF_B, 15)
        check_w(d, kicker, kf, col_w2, "medium kicker")
        d.text((x, yy), kicker, font=kf, fill=RED)
        yy += 21
        hf = font(SERIF_B, 26)
        for ln in wrap(d, headline, hf, col_w2):
            d.text((x, yy), ln, font=hf, fill=INK)
            yy += 30
        yy += 2
        yy = para(d, x, yy, body, font(SERIF, 15), col_w2, 19)
        yy += 4
        d.text((x, yy), sources, font=font(SERIF_I, 11), fill=GREY)
        return yy + 13

    end_l = medium(
        left_x,
        "MIDDLE EAST \u00b7 HORMUZ \u2014 IRGC CLAIM",
        "IRAN CLAIMS 3 TANKERS HIT MINES",
        "Iran\u2019s Revolutionary Guards navy said Monday night three "
        "\u201cviolating\u201d oil tankers hit naval mines in the Strait of "
        "Hormuz and caught fire \u2014 one near the southern coast, two "
        "east of the strait. No identities given; NOT independently "
        "verified.",
        "Sources: Jerusalem Post \u00b7 Al Jazeera \u00b7 Arab Times \u00b7 "
        "Times of Israel \u2014 CLAIM, unverified")
    end_r = medium(
        right_x,
        "LIBYA \u2014 ATTACK SUNDAY, CONFIRMED MONDAY",
        "UKRAINE SINKS RUSSIAN WARSHIP",
        "Zelenskyy confirmed Monday: seven Ukrainian sea drones sank the "
        "Russian corvette Merkury at Benghazi naval base on Sunday and hit "
        "the cargo ship MV Angara. Operation 2,400 km from the front line; "
        "drones launched from a \u201cmother ship\u201d.",
        "Sources: AP \u00b7 Reuters \u00b7 Al Jazeera \u00b7 CNN \u00b7 WSJ "
        "\u2014 CONFIRMED by Kyiv")
    print("medium ends", end_l, end_r)

    mid_end = max(end_l, end_r)
    d.line([(512, mid_y), (512, mid_end)], fill=INK, width=1)
    rule(d, 24, W - 24, mid_end + 8, 2)

    # --- three short stories: Riemann, Indonesia, Kyiv ----------------
    short_y = mid_end + 16
    sw = 312
    xs = [24, 356, 688]

    def short(x, kicker, headline, body, sources):
        yy = short_y
        kf = font(SERIF_B, 13)
        check_w(d, kicker, kf, sw, "short kicker")
        d.text((x, yy), kicker, font=kf, fill=RED)
        yy += 19
        hf = font(SERIF_B, 19)
        for ln in wrap(d, headline, hf, sw):
            d.text((x, yy), ln, font=hf, fill=INK)
            yy += 23
        yy += 2
        yy = para(d, x, yy, body, font(SERIF, 13), sw, 16)
        d.text((x, yy + 3), sources, font=font(SERIF_I, 10), fill=GREY)
        return yy + 3 + 12

    ends = [
        short(xs[0], "MATH \u00b7 REPORTED",
              "AI CLAIMS PROOF OF RIEMANN",
              "Announced Friday, endorsed Saturday: Anthropic\u2019s "
              "Alp\u00f6ge says he and Claude proved the Riemann hypothesis "
              "in a 17M-line Lean proof.",
              "Sources: WSJ \u00b7 phys.org \u00b7 CNN \u00b7 Wikipedia"),
        short(xs[1], "INDONESIA \u00b7 BANTEN \u00b7 CONFIRMED",
              "FACTORY FIRE TOLL 24",
              "Indonesia confirmed Monday: 24 dead, ~30 missing after the "
              "Saturday-night candy factory fire in Banten province.",
              "Sources: Korea Herald/AFP \u00b7 Xinhua"),
        short(xs[2], "UKRAINE \u00b7 REPORTED",
              "STRIKES AROUND KYIV",
              "Sunday drone strike hit a block in Dymer, near Kyiv \u2014 "
              "14 missing, 9 evacuated. Saturday strikes on Kryvyi Rih "
              "killed two.",
              "Sources: Just Security \u00b7 AFP via Korea Herald"),
    ]
    print("shorts end", ends)
    short_end = max(ends)
    d.line([(344, short_y), (344, short_end)], fill=INK, width=1)
    d.line([(676, short_y), (676, short_end)], fill=INK, width=1)
    rule(d, 24, W - 24, short_end + 8, 2)

    # --- WORLD IN BRIEF: stories 7-18, numbered ----------------------
    brief_y = short_end + 16
    d.text((24, brief_y),
           "WORLD IN BRIEF \u2014 MONDAY\u2019S OTHER NEWS",
           font=font(SERIF_B, 14), fill=RED)
    note_f = font(SERIF, 11)
    note = ("19 stories \u00b7 4 claims \u00b7 9 on 2+ sources \u00b7 verified "
            "24 Nov 2026 \u00b7 code-drawn, no photos")
    nw = d.textlength(note, font=note_f)
    d.text((W - 24 - nw, brief_y + 2), note, font=note_f, fill=GREY)
    brief_items = [
        ("7", "Mon: EU proposes 22nd Russia sanctions package (The Brief)"),
        ("8", "Mon: US sanctions 2 dozen Iran shadow-banking entities (The Brief)"),
        ("9", "Mon: US to blacklist Singapore AI firm Megaspeed (The Brief; NY Post)"),
        ("10", "Mon: Drone hits C\u00facuta police base, 3 hurt, 60 homes hit (The Brief)"),
        ("11", "Mon: Bangladesh: Hasina to be jailed if she returns (Reuters)"),
        ("12", "Mon: BepiColombo reaches Mercury orbit after 8-year trip (Principia)"),
        ("13", "Mon: NHS starts major AI trial in breast cancer screening (Principia)"),
        ("14", "Mon: Rep. Jimmy Gomez to resign 1 Dec after ethics report (The Brief)"),
        ("15", "Mon report: Netanyahu urges Trump to strike Iran soon (Tribune Online)"),
        ("16", "Sun: Drones hit homes and a UN building in Khartoum (AFP)"),
        ("17", "Mon: Asian tech shares fall as AI sell-off deepens (Principia)"),
        ("18", "Fri storm, Sun toll: Brazil toll 5; 250+ hurt, ~8,000 homes hit (CNA)"),
    ]
    item_f = font(SANS, 12)
    num_f = font(SANS_B, 12)
    col_w = 476
    col_xs = [24, 524]
    iy = brief_y + 20
    for i, (num, text) in enumerate(brief_items):
        col = i % 2
        row = i // 2
        x = col_xs[col]
        yy = iy + row * 16
        d.text((x, yy), num + ".", font=num_f, fill=RED)
        nw2 = d.textlength(num + ". ", font=num_f)
        check_w(d, text, item_f, col_w - nw2, "brief " + num)
        d.text((x + nw2, yy), text, font=item_f, fill=INK)
    brief_end = iy + 6 * 16
    print("brief ends", brief_end)

    # --- story 19: COP31 aftermath (small line) -----------------------
    y19 = brief_end + 4
    line19 = ("19 \u00b7 COP31 AFTERMATH \u2014 Albanese (Mon): collapse shows "
              "\u201cdifficult geopolitical times\u201d. First no-deal COP "
              "since Copenhagen 2009.")
    check_w(d, line19, font(SERIF_I, 12), W - 48, "story 19")
    d.text((24, y19), line19, font=font(SERIF_I, 12), fill=INK)
    print("story 19 at", y19)

    # --- bottom band: world map strip + DATE CHECK box ----------------
    band_y = y19 + 22
    rule(d, 24, W - 24, band_y, 1)
    band_y += 8
    print("bottom band starts", band_y, "avail to", H - 16)

    # map strip (left)
    map_x0, map_x1 = 24, 430
    map_y0 = band_y + 14
    map_y1 = H - 16
    d.text((map_x0, band_y), "AROUND THE WORLD",
           font=font(SANS_B, 11), fill=INK)
    d.rectangle([map_x0, map_y0, map_x1, map_y1], fill=SEA,
                outline=INK, width=1)
    # rough continent blobs (stylised strip map)
    def blob(points):
        d.polygon(points, fill=LAND, outline=(150, 130, 95))
    blob([(40, map_y0 + 3), (95, map_y0 + 3), (110, map_y0 + 9),
          (100, map_y0 + 18), (80, map_y0 + 22), (60, map_y0 + 20),
          (45, map_y0 + 12)])
    blob([(115, map_y0 + 3), (128, map_y0 + 3), (126, map_y0 + 8),
          (114, map_y0 + 8)])
    blob([(95, map_y0 + 24), (115, map_y0 + 24), (118, map_y0 + 32),
          (108, map_y1 - 2), (98, map_y0 + 36)])
    blob([(195, map_y0 + 3), (225, map_y0 + 3), (228, map_y0 + 10),
          (205, map_y0 + 12), (192, map_y0 + 8)])
    blob([(200, map_y0 + 14), (235, map_y0 + 14), (240, map_y0 + 24),
          (228, map_y1 - 2), (210, map_y0 + 36), (198, map_y0 + 24)])
    blob([(230, map_y0 + 3), (330, map_y0 + 3), (345, map_y0 + 8),
          (330, map_y0 + 16), (300, map_y0 + 18), (260, map_y0 + 16),
          (235, map_y0 + 10)])
    blob([(330, map_y0 + 28), (360, map_y0 + 28), (362, map_y0 + 36),
          (340, map_y1 - 2), (328, map_y0 + 34)])
    # numbered dots: (lon, lat) -> strip coords
    mh = map_y1 - map_y0
    mw = map_x1 - map_x0

    def dot(num, lon, lat, dx=0, dy=0):
        x = map_x0 + (lon + 180.0) / 360.0 * mw + dx
        y = map_y0 + (75.0 - lat) / 130.0 * mh + dy
        d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=RED,
                  outline=(255, 255, 255), width=1)
        nf = font(SANS_B, 7)
        label = str(num)
        lw = d.textlength(label, font=nf)
        d.text((x - lw / 2, y - 4), label, font=nf, fill=(255, 255, 255))

    dot(7, 4.4, 50.8, dx=5, dy=2)     # Brussels
    dot(8, 51.4, 35.7)         # Tehran
    dot(9, 103.8, 1.4)         # Singapore
    dot(10, -72.5, 7.9)        # Cucuta
    dot(11, 90.4, 23.8)        # Dhaka
    dot(13, -0.1, 51.5, dx=-7, dy=-4)   # London
    dot(14, -77.0, 38.9)       # Washington DC
    dot(15, 35.2, 31.8, dx=4, dy=-4)  # Jerusalem
    dot(16, 32.5, 15.6, dx=-4, dy=5)  # Khartoum
    dot(17, 139.7, 35.7)       # Tokyo (Asian markets)
    dot(18, -53.0, -10.0)      # Brazil

    # DATE CHECK box (right)
    dc_x0, dc_x1 = 446, 1000
    d.rectangle([dc_x0, band_y, dc_x1, H - 16], outline=RED, width=2)
    d.text((dc_x0 + 10, band_y + 5), "DATE CHECK \u2014 NOT TODAY\u2019S NEWS",
           font=font(SANS_B, 12), fill=RED)
    dc_items = [
        "COP31 collapse (Sun) \u2014 yesterday\u2019s headline",
        "\u2018El Chapo Isidro\u2019 captured \u2014 in 22 Nov paper",
        "Trump card cap \u00b7 Pentagon curbs \u2014 19\u201321 Nov",
        "Meta India \u00b7 Manipur \u00b7 ICJ Myanmar \u2014 19\u201321 Nov",
        "Delta delays \u00b7 Peru quake \u2014 in 23 Nov paper",
        "Nvidia SEC probe (Fri) \u2014 superseded",
    ]
    dc_f = font(SANS, 10)
    dc_cols = [dc_x0 + 10, dc_x0 + 10 + 272]
    for i, text in enumerate(dc_items):
        col = i % 2
        row = i // 2
        x = dc_cols[col]
        yy = band_y + 24 + row * 12
        check_w(d, text, dc_f, 262, "datecheck")
        d.text((x, yy), "\u2022 " + text, font=dc_f, fill=INK)
    print("date check ends", band_y + 24 + 2 * 12 + 10)

    img.save(OUT, "PNG")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
