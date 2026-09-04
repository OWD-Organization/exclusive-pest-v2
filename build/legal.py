# -*- coding: utf-8 -*-
"""Genera las dos paginas legales leyendo el contenido del scrape, para que el
texto sea literal. Solo se cambia el envoltorio por el sistema neobrutalista."""
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome as C
from services import INNER, page as _page

ROOT = C.ROOT

def parse(src):
    """Devuelve (toc, bloques). toc: [(id, etiqueta)]. bloques: [(tipo, contenido)]."""
    s = open(os.path.join(ROOT, "scrape", "html", src), encoding="utf-8").read()
    s = re.sub(r"<(script|style|svg)\b[^>]*>.*?</\1>", "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)

    # el contador de la lista pone el numero, asi que se quita del texto
    toc = [(m.group(1),
            re.sub(r"^\d+\.\s*", "",
                   " ".join(H.unescape(re.sub(r"<[^>]+>", "", m.group(2))).split())))
           for m in re.finditer(r'<a href="#([^"]+)" class="toc-link">(.*?)</a>', s, re.S)]

    # el cuerpo empieza en la primera h2 con id y termina antes del footer
    i = s.index('<h2 id="')
    j = s.rfind("<footer")
    body = s[i:j if j > i else len(s)]

    # el bloque de contacto son <a> y <p> sueltos dentro de divs, no los captura
    # el barrido general: se extrae aparte para no perder telefono ni correo
    contact = []
    ci = body.rfind('<h2 id="contact"')   # el parrafo de entrada no es igual en las dos
    if ci > 0:
        seg = body[ci:]
        for m in re.finditer(r'<p class="text-xs[^"]*"[^>]*>(.*?)</p>\s*(?:<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>|<p[^>]*>(.*?)</p>)',
                             seg, re.S):
            lab = " ".join(H.unescape(re.sub(r"<[^>]+>", "", m.group(1))).split())
            val = " ".join(H.unescape(re.sub(r"<[^>]+>", "", m.group(3) or m.group(4) or "")).split())
            href = m.group(2)
            if lab and val:
                contact.append((lab, val, href))

    blocks = []
    for m in re.finditer(r"<(h2|h3|h4|p|ul|ol)\b([^>]*)>(.*?)</\1>", body, re.S):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        if tag in ("ul", "ol"):
            items = [" ".join(H.unescape(re.sub(r"<[^>]+>", "", li)).split())
                     for li in re.findall(r"<li\b[^>]*>(.*?)</li>", inner, re.S)]
            items = [x for x in items if x]
            if items:
                blocks.append(("ul", items))
            continue
        # conservar <strong>/<b>/<a> como marcado utilizable
        t = re.sub(r"</?(strong|b)>", lambda x: "<b>" if not x.group(0).startswith("</") else "</b>", inner)
        t = re.sub(r'<a\s+href="(mailto:[^"]+|tel:[^"]+|https?://[^"]+)"[^>]*>(.*?)</a>',
                   r'<a href="\1">\2</a>', t, flags=re.S)
        t = re.sub(r"<(?!/?(b|a)\b)[^>]+>", "", t)
        t = " ".join(H.unescape(t).split())
        if not t:
            continue
        if contact and tag == "p" and t in [c[0] for c in contact] + [c[1] for c in contact]:
            continue
        hid = re.search(r'id="([^"]+)"', attrs)
        # los ids del original chocan con los del cromo (por ejemplo #contact
        # es tambien el CTA), asi que se prefijan
        hid = "sec-" + hid.group(1) if hid else None
        blocks.append((tag, (hid, t)))
    if contact:
        blocks.append(("contact", contact))
    return toc, blocks

def render(toc, blocks):
    out = []
    for tag, val in blocks:
        if tag == "contact":
            rows = []
            for lab, v, href in val:
                inner = f'<a href="{href}">{v}</a>' if href else v
                rows.append(f'          <div><span>{lab}</span><b>{inner}</b></div>')
            out.append('      <div class="contact-card">\n' + "\n".join(rows) + "\n      </div>")
            continue
        if tag == "ul":
            out.append("      <ul>\n" + "\n".join(f"        <li>{x}</li>" for x in val) + "\n      </ul>")
        else:
            hid, txt = val
            idattr = f' id="{hid}"' if hid else ""
            if tag == "h2":
                if out:
                    out.append('      <hr class="legal-rule">')
                out.append(f"      <h2{idattr}>{txt}</h2>")
            elif tag in ("h3", "h4"):
                out.append(f"      <h3{idattr}>{txt}</h3>")
            else:
                out.append(f"      <p{idattr}>{txt}</p>")
    toc_html = "\n".join(f'        <li><a href="#sec-{i}">{l}</a></li>' for i, l in toc)
    return "\n".join(out), toc_html

def build(src, fn, title, meta_desc, h1, kick, intro, dates, note, crumb):
    toc, blocks = parse(src)
    prose, toc_html = render(toc, blocks)
    dates_html = "\n".join(f"      <li>{d}</li>" for d in dates)
    body = f'''<!-- ===================== HERO ===================== -->
<section class="hero hero--page hero--legal" id="top">
{C.SUN}  <div class="shell">
    <div class="stack reveal" style="--s:1.35rem;max-width:60rem">
      <p style="margin:0"><span class="hero-kick">{kick}</span></p>
      <h1>{h1}</h1>
      <p class="prose" style="font-size:var(--step-1);line-height:1.5;max-width:70ch">{intro}</p>
      <ul class="legal-meta" style="margin-top:0.5rem">
{dates_html}
      </ul>
    </div>
  </div>
{C.DUNES}</section>
{C.ACTIONBAR}
<!-- ===================== TEXTO LEGAL ===================== -->
<section class="band band--paper pad">
  <div class="shell legal-grid">
    <nav class="toc reveal" aria-label="On this page">
      <h2>On This Page</h2>
      <ol>
{toc_html}
      </ol>
    </nav>
    <div class="legal reveal" style="--d:100ms">
      <div class="legal-note" style="margin-top:0;margin-bottom:clamp(2rem,3.5vw,2.75rem)">
        <b>Please note</b>
        {note}
      </div>
{prose}
    </div>
  </div>
</section>
''' + C.cta("Questions about this document?",
            "Call us or send an email and a real person at Exclusive Pest Solutions will answer. "
            "Phoenix Valley, Maricopa and Pinal County.",
            creds=False)
    out = (C.head(title, meta_desc, INNER)
           + C.chrome_top(None)
           + body + C.FOOTER + "\n" + C.scripts())
    out = C.nodash(out)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(out)
    return fn, len(out), len(toc), len(blocks)

print(build("privacy-policy.html", "privacy-policy.html",
  "Privacy Policy | Exclusive Pest Solutions",
  "How Exclusive Pest Solutions collects, uses, shares and protects your information when you "
  "visit our site, request an estimate or receive pest control service in the Phoenix Valley.",
  "Privacy Policy", "Legal",
  "How Exclusive Pest Solutions collects, uses, shares, and protects your information when you "
  "visit our website, request an estimate, or receive pest control service in the Phoenix Valley.",
  ["Effective Date: August 14, 2026", "Last Updated: August 14, 2026"],
  "This Privacy Policy is provided for general informational purposes and does not constitute "
  "legal advice. Please review it with qualified counsel before relying on it for compliance purposes.",
  [("Home", "index.html"), ("Privacy Policy", None)]))

print(build("terms-of-service.html", "terms-of-service.html",
  "Terms of Service | Exclusive Pest Solutions",
  "The terms that govern pest control service from Exclusive Pest Solutions in the Phoenix "
  "Valley: estimates, scheduling, service plans, payment, guarantee and pesticide safety.",
  "Terms of Service", "Legal",
  "The terms that govern your use of this website and the pest control services provided by "
  "Exclusive Pest Solutions across the Phoenix Valley.",
  ["Effective Date: August 14, 2026", "Last Updated: August 14, 2026"],
  "These Terms of Service are provided for general informational purposes and do not constitute "
  "legal advice. Please review them with qualified counsel before relying on them.",
  [("Home", "index.html"), ("Terms of Service", None)]))
