"""Builds the site's raster files: favicons, the link-preview card, logo PNGs and the FarmOff! media.

    python brand/src/assets.py [SHOTS_DIR]

SHOTS_DIR holds FarmOff! captures from the game's DevCapture tool (t_lobby.png, t_promo-field.png, t_versus.png,
t_farmers.png). FarmOff! icon and trailer come from ../ArtDrops. Needs Pillow and Microsoft Edge (for SVG).
"""
import os
import shutil
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DROPS = os.path.join(os.path.dirname(ROOT), 'ArtDrops')
sys.path.insert(0, HERE)
import render  # noqa: E402


def p(*parts):
    path = os.path.join(ROOT, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def webp(src, dst, width=None, quality=82):
    img = Image.open(src).convert('RGB')
    if width and img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    img.save(dst, 'WEBP', quality=quality, method=6)
    print('wrote', os.path.relpath(dst, ROOT), img.size)


def main():
    # Favicons and app-style icons.
    render.render(p('brand', 'icon.svg'), p('assets', 'img', 'favicon-32.png'), 32, 32)
    render.render(p('brand', 'icon.svg'), p('assets', 'img', 'apple-touch-icon.png'), 180, 180)
    render.render(p('brand', 'icon.svg'), p('assets', 'img', 'icon-512.png'), 512, 512)
    # Link preview.
    render.render(p('brand', 'social-card.svg'), p('assets', 'img', 'og-image.png'), 1200, 630)

    # Logo PNGs for social profiles, the Play Console and press.
    render.render(p('brand', 'icon.svg'), p('brand', 'png', 'icon-1024.png'), 1024, 1024)
    render.render(p('brand', 'icon-dark.svg'), p('brand', 'png', 'icon-dark-1024.png'), 1024, 1024)
    render.render(p('brand', 'mark.svg'), p('brand', 'png', 'mark-1024.png'), 1024, 1024)
    render.render(p('brand', 'logo-horizontal.svg'), p('brand', 'png', 'logo-horizontal-2000.png'), 2000, 361)
    render.render(p('brand', 'logo-horizontal-dark.svg'), p('brand', 'png', 'logo-horizontal-dark-2000.png'), 2000, 361)
    render.render(p('brand', 'logo-stacked.svg'), p('brand', 'png', 'logo-stacked-1200.png'), 1200, 1050)
    render.render(p('brand', 'logo-stacked-dark.svg'), p('brand', 'png', 'logo-stacked-dark-1200.png'), 1200, 1050)
    shutil.copy(p('assets', 'img', 'og-image.png'), p('brand', 'png', 'social-card-1200x630.png'))

    # FarmOff! media.
    game = ('assets', 'img', 'farmoff')
    webp(os.path.join(DROPS, 'app_icon', 'icon_512.png'), p(*game, 'icon.webp'), 256, 90)
    webp(os.path.join(DROPS, 'video', 'card_title.png'), p(*game, 'trailer-poster.webp'), 1280)
    Image.open(os.path.join(DROPS, 'video', 'card_title.png')).convert('RGB').resize((1200, 675), Image.LANCZOS).save(
        p(*game, 'share.jpg'), quality=85)  # link previews: some apps don't read WebP
    shutil.copy(os.path.join(DROPS, 'video', 'farmoff_trailer_30s.mp4'), p('assets', 'video', 'farmoff-trailer.mp4'))
    print('copied trailer')
    shots = sys.argv[1] if len(sys.argv) > 1 else None
    if shots:
        for name in ('lobby', 'promo-field', 'versus', 'farmers'):
            webp(os.path.join(shots, 't_%s.png' % name), p(*game, '%s.webp' % name), 1600)


if __name__ == '__main__':
    main()
