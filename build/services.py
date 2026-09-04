# -*- coding: utf-8 -*-
"""Genera las tres paginas de servicio. Todo el copy es literal del sitio
original; los guiones largos se sustituyen por coma o punto."""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome as C

ROOT = C.ROOT
INNER = open(os.path.join(ROOT, "build", "inner.css"), encoding="utf-8").read()

def cards(items, tight=False, note=None):
    out = []
    tone = ["", " card--gold", " card--sky", ""]
    for i, it in enumerate(items):
        tag  = f'\n        <span class="card-tag{it.get("tagmod","")}">{it["tag"]}</span>' if it.get("tag") else ""
        icon = (f'\n        <img class="card-icon" src="{it["icon"]}" alt="" width="360" height="360" '
                f'loading="lazy" aria-hidden="true">') if it.get("icon") else ""
        link = (f'\n        <a class="btn-link" style="font-size:var(--step--1);justify-self:start;'
                f'margin-top:0.3rem" href="{it["href"]}">{it["link"]}</a>') if it.get("link") else ""
        body = f'\n        <p>{it["body"]}</p>' if it.get("body") else ""
        d = f' style="--d:{i*70}ms"' if i else ""
        out.append(f'''      <article class="card{it.get("tone", tone[i % 4])} reveal"{d}>{icon}{tag}
        <h3>{it["h"]}</h3>{body}{link}
      </article>''')
    n = f'\n    <p class="cards-note reveal">{note}</p>' if note else ""
    return (f'    <div class="cards{" cards--tight" if tight else ""}">\n'
            + "\n".join(out) + f'\n    </div>{n}')

def steps(items):
    out = []
    for i, (h, p) in enumerate(items):
        d = f' style="--d:{i*70}ms"' if i else ""
        out.append(f'''      <li class="step reveal"{d}>
        <span class="step-num" aria-hidden="true">{i+1:02d}</span>
        <h4>{h}</h4>
        <p>{p}</p>
      </li>''')
    return '    <ol class="steps">\n' + "\n".join(out) + '\n    </ol>'

def areas(cities):
    return ('    <ul class="areas reveal">\n'
            + "\n".join(f'      <li>{c}</li>' for c in cities) + '\n    </ul>')

def faq(items):
    out = []
    for q, a in items:
        out.append(f'''      <details>
        <summary>{q}</summary>
        <div class="faq-a"><p>{a}</p></div>
      </details>''')
    return '    <div class="faq reveal">\n' + "\n".join(out) + '\n    </div>'

def head_block(tag, h2, lead=None, tagmod=""):
    l = f'\n      <p class="prose" style="margin-top:1.25rem">{lead}</p>' if lead else ""
    return (f'    <div class="section-head reveal">\n'
            f'      <span class="tag{tagmod}">{tag}</span>\n'
            f'      <h2>{h2}</h2>{l}\n    </div>')

def hero(kick, h1, paras, cta_label, plate, img, alt, w, h):
    ps = "\n".join(f'      <p class="prose"{" style=\"font-size:var(--step-1);line-height:1.5\"" if i==0 else ""}>{p}</p>'
                   for i, p in enumerate(paras))
    return f'''<!-- ===================== HERO ===================== -->
<section class="hero hero--page" id="top">
  <div class="shell">
    <div class="hero-grid">
      <div class="stack reveal" style="--s:1.35rem">
        <p style="margin:0"><span class="hero-kick">{kick}</span></p>
        <h1>{h1}</h1>
{ps}
        <p class="hero-rating"><span class="stars" aria-hidden="true">★★★★★</span> 5.0 on Google</p>
        <div class="hero-actions">
          <a class="btn btn--lg" href="#contact">{cta_label}</a>
          <a class="btn-link" href="tel:{C.TEL}">Call {C.TELD}</a>
        </div>
      </div>
      <div class="stack reveal" style="--d:120ms;--s:1.25rem">
        <div class="shot">
          <picture>
            <source srcset="{img.rsplit('.',1)[0]}.webp" type="image/webp">
            <img src="{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
          </picture>
        </div>
        <p style="margin:0"><span class="hero-plate">{plate}</span></p>
      </div>
    </div>
  </div>
{C.DUNES}</section>
'''

def page(fn, title, desc, crumb, body, current="services"):
    out = (C.head(title, desc, INNER)
           + C.chrome_top(current)
           + body
           + C.FOOTER + "\n" + C.scripts())
    out = C.nodash(out)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(out)
    return fn, len(out)
