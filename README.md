# twelvedoorsinteractive.com

The studio website for Twelve Doors Interactive: plain HTML and CSS, no build step, no cookies, no trackers.

| Path | Page |
| --- | --- |
| `/` | Studio home: hero, games, the story of the name, contact |
| `/farmoff/` | FarmOff! game page: trailer, features, screenshots, support email |
| `/farmoff/privacy/` | FarmOff! privacy policy (the URL for Google Play and the in-game Privacy button) |
| `/farmoff/online.json` | The FarmOff! online off switch (see the game's Docs/OnlineSwitch.md) |
| `/privacy/` | Website privacy note |
| `/404.html` | "This door leads nowhere" |
| `brand/` | Logo files and the scripts that draw them (see Brand below) |

Preview locally: `python -m http.server 8417` in this folder, then open http://localhost:8417.

## Hosting: GitHub Pages, with the domain at Cloudflare

**Recommendation:** host on **GitHub Pages** and register the domain at **Cloudflare Registrar**.

- **GitHub Pages:** free, very reliable for static sites, automatic HTTPS, and you already use GitHub. Every push publishes.
- **Cloudflare Registrar:** sells .com at cost (about $10–11 a year, no markup at renewal) and includes free
  WHOIS privacy, DNS and free **email forwarding** (so hello@twelvedoorsinteractive.com reaches your Gmail).
- *Alternative:* Cloudflare Pages instead of GitHub Pages: equally free and stable, one dashboard for everything.
  Either is fine; GitHub Pages keeps the site next to your code.

### Steps

1. **Buy the domain** at https://dash.cloudflare.com → Domain Registration → Register Domains → `twelvedoorsinteractive.com`.
2. **Create a GitHub repository**, e.g. `twelvedoors-site` (public: GitHub Pages is free for public repos), and push
   this folder to its `main` branch.
3. **Turn on Pages:** repository → Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.
   The `CNAME` file already names the custom domain.
4. **Verify the domain with GitHub** (stops anyone else claiming it): your GitHub profile → Settings → Pages →
   Add a domain → it gives a TXT record to add in Cloudflare DNS.
5. **Point the domain at GitHub** in Cloudflare → DNS (set each record to **DNS only**, grey cloud, so GitHub can
   issue the HTTPS certificate):

   | Type | Name | Value |
   | --- | --- | --- |
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | AAAA | @ | 2606:50c0:8000::153 |
   | AAAA | @ | 2606:50c0:8001::153 |
   | AAAA | @ | 2606:50c0:8002::153 |
   | AAAA | @ | 2606:50c0:8003::153 |
   | CNAME | www | `<your-github-username>.github.io` |

6. Back in repository → Settings → Pages: wait for the DNS check to pass, then tick **Enforce HTTPS** (can take up to an hour).
7. **Email:** Cloudflare → Email → Email Routing → add `hello@twelvedoorsinteractive.com` forwarding to your Gmail.
   To *send* as that address from Gmail, add it under Gmail → Settings → Accounts → "Send mail as"
   (needs an SMTP service; Zoho Mail's free plan or Google Workspace at about $7/month both work).

## After the site is live

- In the game: set `Consent.PolicyUrl` to `https://twelvedoorsinteractive.com/farmoff/privacy/` and
  `OnlineSwitch.Url` to `https://twelvedoorsinteractive.com/farmoff/online.json`, then rebuild.
- Fill in `[LAUNCH DATE]` in `farmoff/privacy/index.html` on launch day.
- **app-ads.txt:** published with the AdMob publisher ID (pub-7351099896560940). Put `https://twelvedoorsinteractive.com`
  as the **website** in the Play Console listing so AdMob can find it.
- When the game is on Google Play, swap the "Coming soon" button on `/farmoff/` for the store link (and Google's
  official badge from https://play.google.com/intl/en_us/badges/ if you like; follow its brand rules).
- Flip the online switch by editing `farmoff/online.json` and pushing: takes effect in about a minute.

## Brand

The mark is a bara-dari ("twelve doors": bara = twelve, dari = doors) seen from above: twelve piers, three doors in each wall, and from a gold twelve-pointed star
at the centre, twelve streams flowing out through every door. It comes from the Bara-dari of Kamran Mirza on the
Ravi in Lahore, a twelve-doored summer pavilion: air, water and ideas moving in every direction, unhindered.

Everything is drawn in code, including the lettering (hand-built monoline capitals, so no font licence applies):

```bash
python brand/src/logo.py            # writes the SVGs
python brand/src/assets.py SHOTS    # renders PNGs (needs Microsoft Edge and Pillow); SHOTS = folder of game captures
```

| File | Use |
| --- | --- |
| `brand/logo-horizontal(-dark).svg` / `brand/png/logo-horizontal(-dark)-2000.png` | Website header, documents, email signature |
| `brand/logo-stacked(-dark).svg` / `brand/png/logo-stacked(-dark)-1200.png` | Splash screens, posters, square spaces |
| `brand/mark.svg` / `brand/png/mark-1024.png` | The mark alone |
| `brand/png/icon-1024.png`, `icon-dark-1024.png` | Profile pictures (YouTube, X, TikTok), Play Console developer icon |
| `brand/png/social-card-1200x630.png` | Link previews, social banners |

Colours:

| Name | Hex | Role |
| --- | --- | --- |
| Sandstone | `#B4553A` (light `#E58A68`) | The piers; "INTERACTIVE" |
| Ravi teal | `#17707A` (light `#4FB3B8`) | The streams; links and buttons |
| Gold | `#D9A23A` | The star at the heart |
| Ink | `#2B2118` | Text |
| Cream | `#F7EFDF` | Light background |
| Deep teal | `#16302F` | Dark background |

Keep clear space around the mark of at least one pier's width, don't recolour the streams and piers to the same
colour, and use the dark versions on dark backgrounds.

Note: the FarmOff! trailer and its poster were made before the latest farmer-face update; re-record them when convenient.
