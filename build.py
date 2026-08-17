import base64, os

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")

def b64(path, mime="image/jpeg"):
    with open(path, "rb") as f:
        data = f.read()
    return f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"

LOGO_IMG = b64(os.path.join(ASSETS, "logo", "stella-logo.png"), mime="image/png")

WORKS = [
    dict(num="01", slug="01", title="ITEM2022", sub="SHIMADZU",
         model="c32366b25c664ec8903557372eee8d13", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#SHIMADZU"]),
    dict(num="02", slug="02", title="jeca - copy", sub="DAIKEN / Synergy Link",
         model="c68832aae54541bdaad3b77da9826dae", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#DAIKEN"]),
    dict(num="03", slug="03", title="fooma", sub="LION",
         model="d02e0e352a6043bc8ba55334413a8ea7", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#LION"]),
    dict(num="04", slug="04", title="cp+", sub="TAMRON",
         model="4450715b0f514712963cb593a67ce010", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#TAMRON"]),
    dict(num="05", slug="05", title="CP+2024_1 - copy", sub="",
         model="b7385fc8c67f44729cddeeb583a0caa7", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN"]),
    dict(num="06", slug="06", title="A - copy", sub="NABTESCO",
         model="366a918d94bd483993a38859355334f3", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#NABTESCO"]),
    dict(num="07", slug="07", title="RTJ2024_A", sub="",
         model="2598df9e31f54b00b5b9c1af85ae8dbe", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN"]),
    dict(num="08", slug="08", title="JOA2025_A2 - copy", sub="ASAHI KASEI",
         model="cf6d8c5e0d1c4cb4a5e64332d12d2ee0", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#ASAHI KASEI"]),
    dict(num="09", slug="09", title="iRex2025_jissi_02_A", sub="",
         model="ec2f36775ca643c29b953fba74864d83", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN"]),
    dict(num="10", slug="10", title="EVS_jissi_1", sub="SUBARU",
         model="709248d857ef4704a8ba2e15a037b23a", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#SUBARU"]),
    dict(num="11", slug="11", title="AEE2025_B", sub="SUBARU",
         model="804bc70baad04b86a295007b6aa1a3a2", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#SUBARU"]),
    dict(num="12", slug="12", title="BJ_A", sub="GS YUASA",
         model="dc8463f3a42347bdba4290f83581bebc", available=True,
         tags=["#EXHIBITION BOOTH", "#3D DESIGN", "#GS YUASA"]),
]

# attach prev/next among available (clickable) works only, in listed order
avail = [w for w in WORKS if w["available"]]
for i, w in enumerate(avail):
    w["prev"] = avail[i-1] if i > 0 else None
    w["next"] = avail[i+1] if i < len(avail)-1 else None

CSS_JS_HEAD = """<link rel="stylesheet" href="style.css">
"""

HEADER = f"""<div class="top-bar"></div>
<header class="site-header">
  <a class="logo-link" href="index.html"><img class="logo-img" src="{LOGO_IMG}" alt="stella / Design Division Designer 吉田智広 Tomohiro Yoshida"></a>
  <a class="home-link" href="index.html">ALL WORKS</a>
</header>
"""

BACK_TO_TOP = """<a href="index.html" class="back-to-top" title="TOPへ戻る" aria-label="TOPへ戻る">
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 19V5M12 5L5 12M12 5L19 12" stroke="#26261F" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</a>
"""

def render_list():
    cards = []
    for w in WORKS:
        thumb_path = os.path.join(ASSETS, "thumb", f"{w['slug']}.jpg")
        img = b64(thumb_path)
        if w["available"]:
            cards.append(f"""
        <a class="card" href="work-detail-{w['slug']}.html">
          <span class="num">{w['num']}</span>
          <div class="card-media"><img src="{img}" alt="{w['title']}" loading="lazy"></div>
        </a>""")
        else:
            cards.append(f"""
        <a class="card is-disabled" href="#" aria-disabled="true">
          <span class="num">{w['num']}</span>
          <div class="card-media"><img src="{img}" alt="{w['title']}" loading="lazy"></div>
        </a>""")
    cards_html = "".join(cards)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>works | STELLA</title>
{CSS_JS_HEAD}</head>
<body>
{HEADER}
<div class="page-title"><h1>works</h1></div>
<div class="works-wrap">
  <div class="works-grid">{cards_html}
  </div>
</div>
<script src="script.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_detail(w):
    top_path = os.path.join(ASSETS, "render", f"{w['slug']}-top.jpg")
    hero_path = os.path.join(ASSETS, "render", f"{w['slug']}-hero.jpg")
    top_img = b64(top_path)
    hero_img = b64(hero_path)

    renders_html = f"""<div class="render-box"><img src="{top_img}" alt="{w['title']}"></div>
<div class="render-box"><img src="{hero_img}" alt="{w['title']}"></div>"""

    if w["available"]:
        model_html = f"""<div class="media-box"><iframe title="{w['title']}" frameborder="0"
        allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true"
        allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking
        execution-while-out-of-viewport execution-while-not-rendered web-share
        src="https://sketchfab.com/models/{w['model']}/embed?autostart=1&autospin=0.15&transparent=1&password=stella"></iframe></div>"""
        notice = ""
    else:
        model_html = ""
        notice = '<div class="notice">この案件の3Dモデルは準備中です。公開までしばらくお待ちください。</div>'

    tags_html = "".join(f"<span>{t}</span>" for t in w["tags"])

    prev_link = f'<a href="work-detail-{w["prev"]["slug"]}.html">← Prev</a>' if w.get("prev") else '<span class="disabled">← Prev</span>'
    next_link = f'<a href="work-detail-{w["next"]["slug"]}.html">Next →</a>' if w.get("next") else '<span class="disabled">Next →</span>'

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{w['title']} | STELLA WORKS</title>
{CSS_JS_HEAD}</head>
<body>
{HEADER}
<div class="page-title"><h1>works</h1></div>
<div class="detail-frame-wrap">
  <div class="detail-frame">
    <div class="frame-head">
      <span class="num">works {w['num']}</span>
      <h1>{w['title']}</h1>
    </div>
    {renders_html}
    {model_html}
  </div>
</div>
<div class="detail-body">
  <div class="tags">{tags_html}</div>
  {notice}
  <dl class="credits">
    <div><dt>Design</dt><dd>T.Y (Stella Corp.)</dd></div>
    <div><dt>Client</dt><dd>{w['sub'] if w['sub'] and w['sub'] != 'Coming soon' else '—'}</dd></div>
    <div><dt>Category</dt><dd>Exhibition Booth</dd></div>
  </dl>
</div>
<div class="detail-foot">
  <div class="pager">{prev_link}{next_link}</div>
  <a class="all-works-link" href="index.html">ALL WORKS</a>
</div>
{BACK_TO_TOP}
<script src="script.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, f"work-detail-{w['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    render_list()
    for w in WORKS:
        render_detail(w)
    print("built", len(WORKS)+1, "pages")
