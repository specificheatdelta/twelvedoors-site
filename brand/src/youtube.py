"""YouTube channel art for Twelve Doors Interactive.

    python brand/src/youtube.py   -> brand/youtube/ (banner 2560x1440, profile 800x800, watermark 150x150)

The banner keeps everything important inside YouTube's safe area (the middle 1546x423), which is all that shows on
phones; the jali pattern fills the rest for TVs and wide screens.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import logo as L  # noqa: E402
import render  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, 'brand', 'youtube')
DEEP = '#16302F'


def banner():
    W, H = 2560, 1440
    tile = L.jali().split('<title>pattern</title>')[1].replace('</svg>', '').strip()
    body = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, DEEP)
    body += '<defs><pattern id="j" width="96" height="96" patternUnits="userSpaceOnUse">%s</pattern></defs>' % tile
    body += '<rect width="%d" height="%d" fill="url(#j)" opacity=".07" style="filter:invert(1)"/>' % (W, H)
    # A soft band behind the safe area so the logo reads on any device.
    body += '<rect x="0" y="%d" width="%d" height="%d" fill="%s" opacity=".55"/>' % ((H - 423) // 2, W, 423, '#0f2322')
    mark = L.mark(L.SAND_LIGHT, L.WATER_LIGHT, width=7)
    top, top_w = L.word('TWELVE DOORS', 0, 0, 100, L.CREAM, weight=13)
    sub, sub_w = L.word('INTERACTIVE', 0, 0, 100, L.SAND_LIGHT, weight=14, tracking=62)
    tag, tag_w = L.word('GAMES WITH OPEN DOORS', 0, 0, 100, L.GOLD, weight=12, tracking=34)
    top_s = 0.78
    sub_s = top_w * top_s / sub_w
    mark_s = 1.5
    block_w = 200 * mark_s + 40 + top_w * top_s
    x = (W - block_w) / 2
    y = (H - 300) / 2 - 20
    body += L.scaled(mark, mark_s, x, y)
    tx = x + 200 * mark_s + 40
    body += L.scaled(top, top_s, tx, y + 50)
    body += L.scaled(sub, sub_s, tx, y + 50 + 100 * top_s + 26)
    tag_s = 0.3
    body += L.scaled(tag, tag_s, (W - tag_w * tag_s) / 2, y + 300 + 14)
    return L.svg(W, H, body)


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'banner.svg'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(banner())
    render.render(os.path.join(OUT, 'banner.svg'), os.path.join(OUT, 'banner_2560x1440.png'), 2560, 1440)
    render.render(os.path.join(ROOT, 'brand', 'icon-dark.svg'), os.path.join(OUT, 'profile_800.png'), 800, 800)
    render.render(os.path.join(ROOT, 'brand', 'icon.svg'), os.path.join(OUT, 'profile_light_800.png'), 800, 800)
    render.render(os.path.join(ROOT, 'brand', 'mark-dark.svg'), os.path.join(OUT, 'watermark_150.png'), 150, 150)


if __name__ == '__main__':
    main()
