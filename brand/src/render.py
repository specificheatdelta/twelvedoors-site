"""Renders SVGs to PNG with headless Microsoft Edge (no extra Python packages needed).

    python brand/src/render.py in.svg out.png WIDTH HEIGHT [background]

The SVG is scaled to fit the box. Background defaults to transparent.
"""
import os
import subprocess
import sys
import tempfile
import time

EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'


def render(svg_path, png_path, w, h, background='transparent', fit=True):
    with open(svg_path, encoding='utf-8') as f:
        svg = f.read()
    style = 'width:100%;height:100%;' if fit else ''
    svg = svg.replace('<svg ', '<svg style="%s" preserveAspectRatio="xMidYMid meet" ' % style, 1)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;width:%dpx;height:%dpx;'
            'background:%s;overflow:hidden}</style></head><body>%s</body></html>' % (w, h, background, svg))
    tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8')
    tmp.write(html)
    tmp.close()
    out = os.path.abspath(png_path)
    if os.path.exists(out):
        os.remove(out)
    profile = os.path.join(tempfile.gettempdir(), 'td-render-edge')
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--no-first-run', '--user-data-dir=' + profile, '--hide-scrollbars', '--default-background-color=00000000',
                    '--force-device-scale-factor=1', '--window-size=%d,%d' % (w, h), '--screenshot=' + out,
                    'file:///' + tmp.name.replace('\\', '/')], check=True, capture_output=True)
    # Edge hands the job to a background process and returns early, so wait for the file to land.
    deadline = time.time() + 30
    while time.time() < deadline and not (os.path.exists(out) and os.path.getsize(out) > 0):
        time.sleep(0.2)
    time.sleep(0.3)
    os.unlink(tmp.name)
    if not os.path.exists(out):
        raise SystemExit('Edge did not write ' + out)
    print('rendered', png_path)


if __name__ == '__main__':
    a = sys.argv
    render(a[1], a[2], int(a[3]), int(a[4]), a[5] if len(a) > 5 else 'transparent')
