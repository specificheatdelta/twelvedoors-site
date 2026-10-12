"""Twelve Doors Interactive: the logo, drawn in code (no fonts, so no font licences).

The mark is the plan of a bara-dari ("twelve doors"), a pavilion with twelve doors (three in each wall), like Kamran Mirza's
Bara-dari on the Ravi in Lahore (1540). Twelve piers frame the twelve doors; from a gold star at the heart
(the idea), twelve streams of water and air flow out through every door, in all directions, unhindered.

The wordmark is monoline geometric capitals, drawn as strokes.

Run:  python brand/src/logo.py   (writes SVGs to brand/ and assets/img/)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

SAND = '#B4553A'      # Mughal red sandstone
SAND_LIGHT = '#E58A68'
WATER = '#17707A'     # the Ravi
WATER_LIGHT = '#4FB3B8'
GOLD = '#D9A23A'      # ideas
INK = '#2B2118'
CREAM = '#F7EFDF'

# ---------- the mark (200 x 200) ----------

import math

OUTER = (39.0, 161.0)
WALL = 14.0
DOOR = 16.0
# Doors sit where twelve evenly spaced directions (every 30 degrees) cross the walls, so each stream leaves
# through its own door: the middle door of each wall, and two at 30 degrees either side of it.
_off = (OUTER[1] - OUTER[0] - WALL) / 2 * math.tan(math.radians(30))
DOORS = (100 - _off, 100.0, 100 + _off)
PIER_SPANS = ((OUTER[0], DOORS[0] - DOOR / 2), (DOORS[0] + DOOR / 2, DOORS[1] - DOOR / 2),
              (DOORS[1] + DOOR / 2, DOORS[2] - DOOR / 2), (DOORS[2] + DOOR / 2, OUTER[1]))


def piers(colour):
    """Twelve piers: four corners and two between the doors on each side."""
    lo, hi = OUTER
    rects = set()
    for a, b in PIER_SPANS:
        rects.add((a, lo, b - a, WALL))           # top wall
        rects.add((a, hi - WALL, b - a, WALL))    # bottom wall
        rects.add((lo, a, WALL, b - a))           # left wall
        rects.add((hi - WALL, a, WALL, b - a))    # right wall
    body = ''.join('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="3"/>' % r for r in sorted(rects))
    return '<g fill="%s">%s</g>' % (colour, body)


def star(cx, cy, r1, r2, n=12):
    pts = []
    for k in range(2 * n):
        r = r1 if k % 2 == 0 else r2
        a = -math.pi / 2 + k * math.pi / n
        pts.append('%.2f,%.2f' % (cx + r * math.cos(a), cy + r * math.sin(a)))
    return '<polygon points="%s"/>' % ' '.join(pts)


def streams(r0=23.0, r1=91.0):
    """Twelve straight streams from the centre, one through each door. Returns (axis, between) path data."""
    axis, between = [], []
    for k in range(12):
        a = math.radians(k * 30)
        d = 'M%.2f %.2f L%.2f %.2f' % (100 + r0 * math.sin(a), 100 - r0 * math.cos(a),
                                        100 + r1 * math.sin(a), 100 - r1 * math.cos(a))
        (axis if k % 3 == 0 else between).append(d)
    return ' '.join(axis), ' '.join(between)


def mark(sand=SAND, water=WATER, gold=GOLD, width=7.0):
    """The bara-dari: twelve piers, twelve doors, and from the gold star at its heart (the idea) twelve streams
    of water and air flow out through every door, in every direction, unhindered."""
    axis, between = streams()
    cap = 'fill="none" stroke-linecap="round"'
    return ('<path d="%s" stroke="%s" stroke-width="%g" %s/>' % (between, water, width * 0.85, cap)
            + '<path d="%s" stroke="%s" stroke-width="%g" %s/>' % (axis, water, width * 1.15, cap)
            + piers(sand)
            + '<g fill="%s">%s</g>' % (gold, star(100, 100, 16, 8.5)))


# ---------- the lettering (cap height 100) ----------

LETTERS = {
    'T': (70, 'M0 0 H70 M35 0 V100'),
    'W': (112, 'M0 0 L27 100 L56 22 L85 100 L112 0'),
    'E': (58, 'M58 0 H0 V100 H58 M0 50 H48'),
    'L': (54, 'M0 0 V100 H54'),
    'V': (78, 'M0 0 L39 100 L78 0'),
    'D': (78, 'M0 0 H28 C62 0 78 22 78 50 C78 78 62 100 28 100 H0 Z'),
    'O': (100, 'M50 0 C78 0 100 22 100 50 C100 78 78 100 50 100 C22 100 0 78 0 50 C0 22 22 0 50 0 Z'),
    'R': (68, 'M0 100 V0 H38 C56 0 66 12 66 27 C66 42 56 54 38 54 H0 M34 54 L68 100'),
    'S': (64, 'M61 15 C54 5 44 0 32 0 C15 0 4 10 4 26 C4 43 19 47 32 50 C46 53 62 58 62 75 C62 91 50 100 32 100 C17 100 6 94 0 83'),
    'I': (0, 'M0 0 V100'),
    'N': (78, 'M0 100 V0 L78 100 V0'),
    'A': (86, 'M0 100 L43 0 L86 100 M17 62 H69'),
    'C': (90, 'M88 20 C79 7 66 0 50 0 C22 0 0 22 0 50 C0 78 22 100 50 100 C66 100 79 93 88 80'),
    'G': (90, 'M88 20 C79 7 66 0 50 0 C22 0 0 22 0 50 C0 78 22 100 50 100 C70 100 88 86 88 62 V54 H52'),
    'M': (104, 'M0 100 V0 L52 64 L104 0 V100'),
    'H': (76, 'M0 0 V100 M76 0 V100 M0 50 H76'),
    'P': (64, 'M0 100 V0 H36 C54 0 64 12 64 28 C64 44 54 56 36 56 H0'),
    ' ': (34, ''),
}


def word(text, x, y, size, colour, weight=12.0, tracking=30.0):
    """Draws capitals with their top-left at (x, y), cap height = size. Returns (svg, width)."""
    s = size / 100.0
    parts = []
    cx = 0.0
    for ch in text:
        w, d = LETTERS[ch]
        if d:
            parts.append('<path transform="translate(%g %g) scale(%g)" d="%s"/>' % (x + cx * s, y, s, d))
        cx += w + tracking
    width = (cx - tracking) * s
    g = '<g fill="none" stroke="%s" stroke-width="%g" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (
        colour, weight, ''.join(parts))
    return g, width


def svg(w, h, body, title='Twelve Doors Interactive'):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" width="%g" height="%g" role="img" '
            'aria-label="%s"><title>%s</title>%s</svg>\n' % (w, h, w, h, title, title, body))


def scaled(body, s, dx=0.0, dy=0.0):
    return '<g transform="translate(%g %g) scale(%g)">%s</g>' % (dx, dy, s, body)


def lockup_horizontal(dark=False):
    ink = CREAM if dark else INK
    m = mark(SAND_LIGHT if dark else SAND, WATER_LIGHT if dark else WATER)
    # Lettering: TWELVE DOORS (big), INTERACTIVE (small, wide tracking) under it.
    top, top_w = word('TWELVE DOORS', 0, 0, 100, ink, weight=13)
    sub, sub_w = word('INTERACTIVE', 0, 0, 100, SAND_LIGHT if dark else SAND, weight=14, tracking=62)
    top_s = 0.62
    sub_s = top_w * top_s / sub_w
    text_x = 230
    body = scaled(m, 1.0)
    body += scaled(top, top_s, text_x, 52)
    body += scaled(sub, sub_s, text_x, 52 + 100 * top_s + 22)
    w = text_x + top_w * top_s + 20
    return svg(w, 200, body)


def lockup_stacked(dark=False):
    ink = CREAM if dark else INK
    m = mark(SAND_LIGHT if dark else SAND, WATER_LIGHT if dark else WATER)
    top, top_w = word('TWELVE DOORS', 0, 0, 100, ink, weight=13)
    sub, sub_w = word('INTERACTIVE', 0, 0, 100, SAND_LIGHT if dark else SAND, weight=14, tracking=62)
    width = 600.0
    top_s = (width - 40) / top_w
    sub_s = top_w * top_s / sub_w
    body = scaled(m, 1.4, width / 2 - 140, 0)
    body += scaled(top, top_s, 20, 300)
    body += scaled(sub, sub_s, 20, 300 + 100 * top_s + 24)
    h = 300 + 100 * top_s + 24 + 100 * sub_s + 20
    return svg(width, h, body)


def icon(bg=CREAM, dark=False):
    """The mark on a rounded tile: favicon, app/social avatar."""
    m = mark(SAND_LIGHT if dark else SAND, WATER_LIGHT if dark else WATER, width=9)
    return svg(200, 200, '<rect width="200" height="200" rx="44" fill="%s"/>%s' % (bg, scaled(m, 0.9, 10, 10)))


def mark_flow():
    """The hero mark: water keeps flowing out through the doors (stops for people who prefer less motion), and the
    colours follow the visitor's light or dark setting."""
    axis, between = streams()
    style = ('<style>'
             '.p{fill:%s}.w{stroke:%s}.g{fill:%s}'
             '.base{opacity:.28}'
             '.flow{stroke-dasharray:9 13;animation:flow 1.8s linear infinite}'
             '.star{transform-box:fill-box;transform-origin:center;animation:turn 60s linear infinite}'
             '@keyframes flow{to{stroke-dashoffset:-22}}'
             '@keyframes turn{to{transform:rotate(360deg)}}'
             '@media (prefers-color-scheme:dark){.p{fill:%s}.w{stroke:%s}}'
             '@media (prefers-reduced-motion:reduce){.flow,.star{animation:none}.flow{stroke-dasharray:none}.base{opacity:0}}'
             '</style>') % (SAND, WATER, GOLD, SAND_LIGHT, WATER_LIGHT)
    cap = 'fill="none" stroke-linecap="round"'
    body = style
    for cls in ('w base', 'w flow'):
        body += '<path class="%s" d="%s" stroke-width="%g" %s/>' % (cls, between, 7 * 0.85, cap)
        body += '<path class="%s" d="%s" stroke-width="%g" %s/>' % (cls, axis, 7 * 1.15, cap)
    body += piers('none').replace('<g fill="none">', '<g class="p">')
    body += '<g class="g">%s</g>' % star(100, 100, 16, 8.5).replace('<polygon', '<polygon class="star"')
    return svg(200, 200, body)


def jali():
    """A 96 px tile of twelve-pointed stars on a lattice, for faint backgrounds."""
    body = '<g fill="%s">' % INK
    for cx, cy in ((48, 48), (0, 0), (96, 0), (0, 96), (96, 96)):
        body += star(cx, cy, 14, 7.5)
    body += '</g><g stroke="%s" stroke-width="1.5" fill="none">' % INK
    body += '<path d="M0 48 H96 M48 0 V96 M0 0 L96 96 M96 0 L0 96"/>'
    body += '</g>'
    return svg(96, 96, body, 'pattern')


def social_card():
    """1200 x 630 link preview: the stacked logo on deep teal."""
    m = mark(SAND_LIGHT, WATER_LIGHT, width=7)
    top, top_w = word('TWELVE DOORS', 0, 0, 100, CREAM, weight=13)
    sub, sub_w = word('INTERACTIVE', 0, 0, 100, SAND_LIGHT, weight=14, tracking=62)
    top_s = 0.62
    sub_s = top_w * top_s / sub_w
    text_w = top_w * top_s
    x = (1200 - 230 - text_w) / 2
    tile = jali().split('<title>pattern</title>')[1].replace('</svg>', '').strip()
    body = '<rect width="1200" height="630" fill="#16302F"/>'
    body += '<defs><pattern id="j" width="96" height="96" patternUnits="userSpaceOnUse">%s</pattern></defs>' % tile
    body += '<rect width="1200" height="630" fill="url(#j)" opacity=".06" style="filter:invert(1)"/>'
    body += scaled(m, 1.0, x, 215)
    body += scaled(top, top_s, x + 230, 215 + 52)
    body += scaled(sub, sub_s, x + 230, 215 + 52 + 100 * top_s + 22)
    return svg(1200, 630, body)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('wrote', path)


if __name__ == '__main__':
    write('brand/mark.svg', svg(200, 200, mark()))
    write('brand/mark-dark.svg', svg(200, 200, mark(SAND_LIGHT, WATER_LIGHT)))
    write('brand/logo-horizontal.svg', lockup_horizontal())
    write('brand/logo-horizontal-dark.svg', lockup_horizontal(dark=True))
    write('brand/logo-stacked.svg', lockup_stacked())
    write('brand/logo-stacked-dark.svg', lockup_stacked(dark=True))
    write('brand/icon.svg', icon())
    write('brand/icon-dark.svg', icon(bg='#16302F', dark=True))
    write('assets/img/mark.svg', svg(200, 200, mark()))
    write('assets/img/logo-horizontal.svg', lockup_horizontal())
    write('assets/img/logo-horizontal-dark.svg', lockup_horizontal(dark=True))
    write('assets/img/favicon.svg', icon())
    write('assets/img/mark-flow.svg', mark_flow())
    write('assets/img/jali.svg', jali())
    write('brand/social-card.svg', social_card())
