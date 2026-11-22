#!/usr/bin/env python3
"""Draw the news-image-20261121 front page: 'The World in One Page'.

Saturday 21 November 2026 - 40 stories, 6 continents, one page.
Lead: Russian missiles hit Poland - Warsaw calls it a deliberate
provocation, NATO a grave violation of its airspace. Strip 1: Wall
Street slumps into correction as AI shares sell off (Nasdaq -5.28%,
Nvidia -14%). Strip 2: the ICJ's Myanmar genocide verdict stands as
the week's landmark ruling. Verified against Reuters, AP, BBC, FT,
The Hindu, IMD and UN reporting for 20-21 November 2026. Hero: a
PIL-drawn globe, no photo. Output: 1024x1024 PNG, deterministic
(no randomness, no network, no clock).
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (17, 17, 17)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = os.path.join(F, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(F, "DejaVuSerif.ttf")
SANS = os.path.join(F, "DejaVuSans.ttf")
SANS_B = os.path.join(F, "DejaVuSans-Bold.ttf")
HERE = os.path.dirname(os.path.abspath(__file__))

COL = {
    "ASIA": (0, 87, 183), "EUROPE": (15, 118, 110), "AFRICA": (166, 90, 0),
    "AMERICAS": (166, 25, 46), "OCEANIA": (109, 40, 217), "WORLD": (120, 90, 0),
    "SPORT": (51, 65, 85),
}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def trunc(draw, text, fnt, max_w):
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while text and draw.textlength(text + "...", font=fnt) > max_w:
        text = text.rsplit(" ", 1)[0] if " " in text else text[:-1]
    return text + "..."


def draw_globe(d, cx, cy, r):
    """Stylised globe: cream disc, teal meridians, red alert badge."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(233, 240, 238),
              outline=(15, 118, 110), width=3)
    for k in range(-2, 3):
        rx = int(r * abs(k) / 2.6) or 6
        d.ellipse([cx - rx, cy - r, cx + rx, cy + r],
                  outline=(15, 118, 110), width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=(15, 118, 110), width=2)
    for dy in (-r // 2, r // 2):
        w = int(math.sqrt(max(r * r - dy * dy, 0)))
        d.line([(cx - w, cy + dy), (cx + w, cy + dy)],
               fill=(15, 118, 110), width=2)
    # continent blobs
    d.ellipse([cx - 52, cy - 48, cx - 8, cy - 6], fill=(15, 118, 110))
    d.ellipse([cx + 6, cy - 30, cx + 44, cy + 8], fill=(15, 118, 110))
    d.ellipse([cx - 30, cy + 14, cx + 12, cy + 48], fill=(15, 118, 110))
    d.ellipse([cx + 30, cy + 26, cx + 54, cy + 52], fill=(15, 118, 110))
    # alert badge: two missiles
    bx, by = cx + r - 34, cy - r + 6
    d.ellipse([bx - 26, by - 26, bx + 26, by + 26], fill=(166, 25, 46),
              outline=WHITE, width=2)
    d.text((bx, by - 11), "x2", font=font(SANS_B, 17), fill=WHITE, anchor="ma")


# (region, headline, deck) - 37 grid stories; lead + 2 strips make 40.
ITEMS = [
    ("ASIA", "Trilateral ends with few results", "Trump, Xi, Putin leave Shenzhen thin."),
    ("ASIA", "US wants peace deal by January", "FT: Kyiv pressed to settle by New Year."),
    ("ASIA", "Iran war nears ninth month", "Trump: no rush, decision maybe in 2027."),
    ("ASIA", "Saudis stop Houthi missiles", "Riyadh intercepts three; Hodeidah struck."),
    ("ASIA", "Tanker hit by fire in Hormuz", "UKMTO reports strike off Khasab."),
    ("ASIA", "US sanctions four Iranians", "Over handling of Iranian oil revenues."),
    ("ASIA", "N. Korea expands uranium plant", "Satellite images show the growth."),
    ("ASIA", "Akvan: Odisha counts the cost", "Landfall Friday; 105,000 evacuated."),
    ("ASIA", "India beat Pakistan 2-1, win SAFF", "Title sealed in the Dhaka final."),
    ("ASIA", "SpaceX unit to drop Chinese AI", "Models to go, report says."),
    ("EUROPE", "Denmark expels Russian diplomat", "Alleged plot to kill Ukrainian rapper."),
    ("EUROPE", "Estonia to shut border 1 Dec", "Crossings to Russia close."),
    ("EUROPE", "UK and EU sign three deals", "Food, carbon, youth mobility in Brussels."),
    ("EUROPE", "EU adopts EUR 1bn Ukraine aid", "Joint kit buys, delivery by end 2027."),
    ("EUROPE", "EU lines up EUR 45bn loan", "Provisional loan opens reparations door."),
    ("EUROPE", "UK pledges 1,000 drones", "GBP 260m package for Ukraine."),
    ("EUROPE", "France seeks UN Council meet", "Strikes kill 8 in Kyiv, embassies hit."),
    ("EUROPE", "Hungary lifts EU block", "Last accession chapters unblocked."),
    ("AMERICAS", "Nvidia -14% as SEC probes books", "Board refuses to reinstate Huang."),
    ("AMERICAS", "Palisades Fire arsonist guilty", "Jury convicts Rinderknecht in LA."),
    ("AMERICAS", "Trump pardons Pete Rose", "Posthumous pardon for baseball star."),
    ("AMERICAS", "Senate rejects war-powers bid", "Iran resolution fails 51-48."),
    ("AMERICAS", "US sanctions Comancheros", "'Ndrangheta too; assets blocked."),
    ("AMERICAS", "US clears 880,000 AI chips", "Sales to China, buyers linked to army."),
    ("AMERICAS", "Argentina rout Costa Rica 7-0", "Paz scores twice in friendly."),
    ("AMERICAS", "Canada men hit record ranking", "25th in the world, a new high."),
    ("AFRICA", "Morocco books 2027 AFCON", "Beats Niger to seal qualification."),
    ("AFRICA", "Mali joins World Rugby fully", "119th full member union."),
    ("AFRICA", "Somalia accuses UAE of bases", "Mogadishu alleges secret sites."),
    ("AFRICA", "Libya seizes cocaine, pills", "Haul found in the east, officials say."),
    ("OCEANIA", "Jepchirchir banned three years", "Loses Sydney Marathon title for doping."),
    ("OCEANIA", "Oceania Rugby suspended", "Council membership paused in probe."),
    ("OCEANIA", "Eales, Pichot join rugby board", "Southern-hemisphere seats in Dublin."),
    ("OCEANIA", "Tuvalu to COP31: no permission", "Pacific: move off fossil fuels."),
    ("WORLD", "GTA VI: $1.84bn in a day", "19.1m copies; biggest launch ever."),
    ("WORLD", "Voyager 1 hits one light-day", "NASA confirms the milestone."),
    ("WORLD", "COP31 presses climate finance", "Talks push resilient infrastructure."),
]


def main():
    assert len(ITEMS) == 37, len(ITEMS)
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 26
    # ---- masthead ----
    d.text((W // 2, 14), "THE WORLD", font=font(SERIF_B, 64), fill=INK, anchor="ma")
    d.text((W // 2, 92), "SATURDAY 21 NOVEMBER 2026  \u2022  40 STORIES  \u2022  6 CONTINENTS  \u2022  ONE PAGE",
           font=font(SANS_B, 15), fill=INK, anchor="ma")
    d.line([(M, 120), (W - M, 120)], fill=INK, width=4)
    d.line([(M, 126), (W - M, 126)], fill=INK, width=1)

    # ---- lead: Russian missiles hit Poland, globe hero right ----
    d.text((M, 136), "POLAND  \u2022  NATO AIRSPACE", font=font(SANS_B, 14), fill=COL["AMERICAS"])
    d.text((M, 156), "RUSSIAN MISSILES", font=font(SERIF_B, 33), fill=INK)
    d.text((M, 194), "HIT POLAND", font=font(SERIF_B, 33), fill=INK)
    deck = ("Two missiles and a suspected drone came down in Poland \u2014 "
            "Warsaw calls it a deliberate provocation, NATO a grave "
            "violation of its airspace.")
    y = 236
    for ln in wrap(d, deck, font(SERIF, 16), 560):
        d.text((M, y), ln, font=font(SERIF, 16), fill=INK)
        y += 21
    hx, hy, hw, hh = 600, 136, 398, 170
    d.rectangle([hx, hy, hx + hw, hy + hh], fill=(16, 42, 54))
    draw_globe(d, hx + hw // 2, hy + 72, 62)
    d.rectangle([hx, hy, hx + hw, hy + hh], outline=INK, width=2)
    d.rectangle([hx, hy + hh - 26, hx + hw, hy + hh], fill=(166, 25, 46))
    d.text((hx + hw // 2, hy + hh - 22), "WARSAW: DELIBERATE PROVOCATION",
           font=font(SANS_B, 13), fill=WHITE, anchor="ma")

    # ---- strip 1: Wall Street slumps into correction ----
    ty = 318
    d.rectangle([M, ty, W - M, ty + 40], fill=INK)
    d.text((M + 14, ty + 4), "WALL ST SLUMPS INTO CORRECTION  \u2022  ",
           font=font(SANS_B, 15), fill=(255, 213, 79))
    d.text((M + 14, ty + 22), "Nasdaq -5.28%, Nvidia -14% as AI shares sell off",
           font=font(SANS, 14), fill=WHITE)
    d.text((W - M - 14, ty + 4), "AMERICAS", font=font(SANS_B, 15), fill=(255, 213, 79), anchor="ra")

    # ---- strip 2: ICJ Myanmar genocide verdict ----
    gy = 364
    d.rectangle([M, gy, W - M, gy + 40], fill=(24, 24, 64))
    d.text((M + 14, gy + 4), "ICJ: MYANMAR GUILTY OF GENOCIDE  \u2022  ",
           font=font(SANS_B, 15), fill=(255, 213, 79))
    d.text((M + 14, gy + 22), "First state ever found guilty, 9-6; reparations to come",
           font=font(SANS, 14), fill=WHITE)
    d.text((W - M - 14, gy + 4), "WORLD", font=font(SANS_B, 15), fill=(255, 213, 79), anchor="ra")

    # ---- 37-item grid: 3 cols x 13 rows ----
    gx, gy2 = M, 416
    cw = (W - 2 * M - 24) // 3
    chh = 42
    for i, (reg, head, deck) in enumerate(ITEMS):
        x = gx + (i % 3) * (cw + 12)
        y = gy2 + (i // 3) * chh
        col = COL[reg]
        d.line([(x, y + 3), (x, y + chh - 7)], fill=col, width=4)
        d.text((x + 10, y), reg, font=font(SANS_B, 9), fill=col)
        d.text((x + 10, y + 11), trunc(d, head, font(SERIF_B, 12), cw - 12),
               font=font(SERIF_B, 12), fill=INK)
        d.text((x + 10, y + 27), trunc(d, deck, font(SANS, 10), cw - 12),
               font=font(SANS, 10), fill=(60, 60, 60))

    # ---- footer ----
    d.text((W // 2, 984), "Sources: Reuters, AP, BBC, FT, The Hindu, IMD, UN  \u2022  Saturday 21 November 2026",
           font=font(SANS, 11), fill=GREY, anchor="ma")
    out = os.path.join(HERE, "news.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
