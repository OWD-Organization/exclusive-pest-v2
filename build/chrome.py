# -*- coding: utf-8 -*-
"""Cromo compartido por todas las paginas: head, barra de utilidad, nav,
barra de accion movil, CTA y footer. Una sola fuente para los 6 archivos."""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEL   = "+16026006746"
TELD  = "(602) 600-6746"
MAIL  = "hello@exclusivepest.co"

def head(title, desc, extra_css=""):
    """Reutiliza literalmente la hoja de estilos del home y le anade la de
    paginas internas, para que el sistema no pueda divergir."""
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    h = src[:src.index("</head>")]
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, count=1, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*(">)',
               lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = h.replace('EXCLUSIVE PEST SOLUTIONS , about page', 'EXCLUSIVE PEST SOLUTIONS')
    h = h.replace('EXCLUSIVE PEST SOLUTIONS , home, v2 "desert daylight"',
                  'EXCLUSIVE PEST SOLUTIONS\n   Sistema heredado del home v2 "desert daylight".')
    if extra_css:
        i = h.rindex("</style>")
        h = h[:i] + extra_css + h[i:]
    return h + "</head>\n"

def chrome_top(current=None):
    from navpatch import nav_links
    links = nav_links(current, home_anchors=False)
    return f'''<body>

<!-- ===================== UTILITY BAR ===================== -->
<div class="util">
  <div class="shell">
    <div class="util-right">
      <span><span class="stars" aria-hidden="true">★★★★★</span> 5.0 on Google</span>
      <span class="util-hours">Mon to Sat: 7:00 AM to 6:00 PM</span>
      <a class="util-tel" href="tel:{TEL}">{TELD}</a>
    </div>
  </div>
</div>

<!-- ===================== NAV ===================== -->
<header class="nav">
  <div class="shell">
    <a class="brand" href="index.html" aria-label="Exclusive Pest Solutions, inicio">
      <picture>
        <source srcset="build-assets/logo-word.webp" type="image/webp">
        <img src="build-assets/logo-word.png" alt="Exclusive Pest Solutions" width="560" height="127">
      </picture>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Abrir menú">
      <span class="nav-toggle-bars" aria-hidden="true"><i></i><i></i><i></i></span>
    </button>
{links}
    <a class="btn" href="#contact">Get your custom quote</a>
  </div>
</header>
'''

def crumbs(trail):
    """trail: lista de (texto, href o None). El ultimo es la pagina actual."""
    out = []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        if last:
            out.append(f'      <li aria-current="page">{label}</li>')
        else:
            out.append(f'      <li><a href="{href}">{label}</a></li>')
    return ('<!-- ===================== MIGAS ===================== -->\n'
            '<nav class="crumbs" aria-label="Breadcrumb">\n  <div class="shell">\n'
            '    <ol>\n' + "\n".join(out) + '\n    </ol>\n  </div>\n</nav>\n')

ACTIONBAR = f'''
<!-- ===================== BARRA DE ACCIÓN (solo móvil) ===================== -->
<div class="actionbar" role="group" aria-label="Acciones rápidas">
  <a class="actionbar-tel" href="tel:{TEL}" aria-label="Llamar al {TELD}">
    <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" fill="none"
         stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .3 1.9.6 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.5 2.8.6a2 2 0 0 1 1.7 2z"/>
    </svg>
  </a>
  <a class="btn actionbar-cta" href="#contact">Get your custom quote</a>
</div>
'''

SUN = '''  <svg class="sun" viewBox="0 0 200 200" aria-hidden="true">
    <g fill="none" stroke="#2d1c10" stroke-width="5" stroke-linecap="round">
      <path d="M100 8 V30"/><path d="M100 170 V192"/>
      <path d="M8 100 H30"/><path d="M170 100 H192"/>
      <path d="M35 35 L50 50"/><path d="M150 150 L165 165"/>
      <path d="M165 35 L150 50"/><path d="M50 150 L35 165"/>
    </g>
    <circle cx="100" cy="100" r="58" fill="#ffbf40" stroke="#2d1c10" stroke-width="5"/>
  </svg>
'''

def cactus(variant):
    return f'''  <picture class="cactus cactus--{variant}">
    <source srcset="build-assets/cactus-mark2.webp" type="image/webp">
    <img src="build-assets/cactus-mark2.png" alt="" width="520" height="737" loading="lazy" aria-hidden="true">
  </picture>
'''

OWL = '  <img class="hero-owl" src="build-assets/owl-mark.png" alt="" width="448" height="425" aria-hidden="true">\n'

DUNES = '''  <svg class="dunes" viewBox="0 0 1440 150" preserveAspectRatio="none" aria-hidden="true">
    <path d="M0 84 C180 30 300 108 480 72 C660 36 760 100 960 62 C1140 28 1290 84 1440 56 V150 H0 Z" fill="#ffbf40"/>
    <path d="M0 108 C200 68 340 126 540 98 C740 70 880 130 1080 92 C1250 62 1350 108 1440 88 V150 H0 Z" fill="#f67c16"/>
    <path d="M0 132 C240 112 420 146 660 128 C900 110 1080 148 1440 122 V150 H0 Z" fill="#2d1c10"/>
  </svg>
'''

def cta(heading, body, facts=None, creds=False):
    facts = facts or [("Working hours", "Mon to Sat, 7 AM to 6 PM"),
                      ("Sunday", "Emergency service"),
                      ("AZ Dept. of Ag", "License #10150"),
                      ("Google rating", "5.0 ★★★★★")]
    rows = "\n".join(f'      <div class="cta-fact"><span>{a}</span><b>{b}</b></div>' for a, b in facts)
    cr = ''
    return f'''
<!-- ===================== CTA ===================== -->
<section class="cta pad" id="contact">
  <div class="shell cta-grid">
    <div class="stack reveal" style="--s:1.4rem">
      <div>
        <span class="tag tag--paper">Ready to start</span>
        <h2>{heading}</h2>
      </div>
      <div class="prose" style="max-width:52ch">
        <p>{body}</p>
      </div>
      <div class="hero-actions">
        <a class="btn btn--lg btn--paper" href="tel:{TEL}">Call {TELD}</a>
        <a class="btn-link" style="border-bottom-color:var(--c-ink)" href="mailto:{MAIL}">{MAIL}</a>
      </div>{cr}
    </div>
    <div class="cta-facts reveal" style="--d:100ms">
{rows}
    </div>
  </div>
</section>
'''

FOOTER = f'''
<!-- ===================== FOOTER ===================== -->
<footer class="foot">
  <div class="shell foot-top">
    <div>
      <h2>Phoenix Valley's premier pest control, built around your home, your family, and the desert we share.</h2>
      <span class="foot-lic">AZ Dept. of Agriculture License #10150</span>
    </div>
    <div>
      <h3>Valley Pest Alerts</h3>
      <p>Get seasonal tips for Phoenix Valley homes.</p>
      <form class="foot-news" onsubmit="return false">
        <label for="nl" style="font-weight:900;font-size:var(--step--2);letter-spacing:var(--tr-label);text-transform:uppercase;color:var(--c-sky)">Email</label>
        <input id="nl" type="email" name="email" placeholder="you@example.com" autocomplete="email" required>
        <button class="btn btn--gold" type="submit">Subscribe</button>
      </form>
    </div>
  </div>
  <div class="shell foot-grid">
    <div>
      <h3>Quick Links</h3>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="index.html#services">Services</a></li>
        <li><a href="index.html#process">Our Process</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </div>
    <div>
      <h3>Our Services</h3>
      <ul>
        <li><a href="scorpion-control.html">Scorpion Control</a></li>
        <li><a href="general-pest-control.html">General Pest Control</a></li>
        <li><a href="ant-control.html">Ant Control</a></li>
        <li><a href="general-pest-control.html#safe">Garden-Safe Treatments</a></li>
        <li><a href="general-pest-control.html#method">IPM Programs</a></li>
      </ul>
    </div>
    <div>
      <h3>Working Hours</h3>
      <ul>
        <li>Monday to Saturday: 7:00 AM to 6:00 PM</li>
        <li>Sunday: Emergency Service Available</li>
      </ul>
    </div>
    <div>
      <h3>Contact</h3>
      <ul>
        <li>Call Us<br><a href="tel:{TEL}">{TELD}</a></li>
        <li>Email Us<br><a href="mailto:{MAIL}">{MAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="shell foot-legal">
    <span>© 2026 Exclusive Pest Solutions. All Rights Reserved.</span>
    <span class="sep"><a href="privacy-policy.html">Privacy Policy</a></span>
    <span><a href="terms-of-service.html">Terms of Service</a></span>
    <span>Made by <a href="https://outworkemdigital.com/" target="_blank" rel="noopener noreferrer">Outwork'em Digital</a></span>
  </div>
</footer>
'''

def scripts():
    """Todos los scripts de cierre del home, no solo el ultimo: rindex dejaba
    fuera el menu movil y el observador de reveals."""
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    i = src.index("</footer>")
    return src[src.index("<script>", i):]

def nodash(s):
    return (s.replace("—", ",").replace("–", ",")
             .replace(" ,", ",").replace(",,", ","))
