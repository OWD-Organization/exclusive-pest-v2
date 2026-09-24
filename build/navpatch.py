# -*- coding: utf-8 -*-
"""Inserts the Services submenu CSS, JS and markup into index.html and
about.html. Generated pages inherit it because chrome.head() copies the
index.html stylesheet and chrome.scripts() copies its scripts."""
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = """
/* NAV-SUB:CSS:START */
/* =========================================================
   NAV , Services submenu
   ========================================================= */
.nav-sub-wrap{position:relative;display:flex;align-items:center}
.nav-sub-toggle{
  display:inline-flex;align-items:center;gap:0.42em;
  font:inherit;font-weight:700;letter-spacing:var(--tr-nav);
  color:inherit;background:none;border:0;
  padding:0.35em 0;margin:0;cursor:pointer;
  border-bottom:3px solid transparent;
  transition:color 140ms var(--ease-out-expo);
}
.nav-sub-toggle:hover{border-bottom-color:var(--c-orange)}
.nav-sub-toggle .chev{
  width:0.72em;height:0.72em;flex:0 0 auto;
  transition:rotate 190ms var(--ease-out-expo);
}
.nav-sub-toggle.is-current{border-bottom-color:var(--c-orange)}
.nav-sub-toggle[aria-expanded="true"]{color:var(--c-orange-deep);border-bottom-color:var(--c-orange)}
.nav-sub-toggle[aria-expanded="true"] .chev{rotate:180deg}

.nav-sub{
  position:absolute;top:calc(100% + 0.9rem);left:-0.8rem;z-index:70;
  min-width:15.5rem;
  background:var(--c-paper);
  border:var(--bd-hard);border-radius:var(--r);
  box-shadow:-6px 6px 0 var(--c-ink);
  padding:0.42rem;
  display:grid;gap:0.12rem;
}
.nav-sub a{
  display:grid;grid-template-columns:1.45rem 1fr;gap:0.7rem;align-items:center;
  padding:0.68em 0.75em;border-radius:calc(var(--r) - 3px);
  border-bottom:0;text-decoration:none;
  font-weight:800;font-size:var(--step--1);line-height:1.25;
  transition:background-color 130ms var(--ease-out-expo);
}
.nav-sub a:hover,.nav-sub a:focus-visible{background:var(--c-gold-pale);border-bottom:0}
.nav-sub a[aria-current]{background:var(--c-gold)}
.nav-sub a svg{width:1.45rem;height:1.45rem;color:var(--c-orange-deep)}
.nav-sub a[aria-current] svg{color:var(--c-ink)}
/* with JS the panel starts collapsed; without JS it stays visible and usable */
.js .nav-sub{display:none}
.js .nav-sub-wrap[data-open="true"] .nav-sub{display:grid}

/* on desktop it opens on plain hover, no click needed; the click handler
   (further down) stays only as a fallback for keyboards and hybrid
   touch screens, where :hover doesn't fire */
@media (min-width:48.0625rem){
  /* invisible bridge over the gap between the button and the panel: without it,
     the pointer loses hover while crossing that gap and the panel closes
     before it gets there */
  .nav-sub-wrap::after{
    content:"";position:absolute;left:0;right:0;top:100%;height:0.9rem;
  }
  .js .nav-sub-wrap:hover .nav-sub,
  .js .nav-sub-wrap:focus-within .nav-sub{display:grid}
  .js .nav-sub-wrap:hover .nav-sub-toggle,
  .js .nav-sub-wrap:focus-within .nav-sub-toggle{color:var(--c-orange-deep);border-bottom-color:var(--c-orange)}
  .js .nav-sub-wrap:hover .nav-sub-toggle .chev,
  .js .nav-sub-wrap:focus-within .nav-sub-toggle .chev{rotate:180deg}
}

@media (max-width:48rem){
  /* in the mobile column the submenu lives inside the menu itself */
  .nav-sub-wrap{width:100%;display:block}
  .nav-sub-toggle{
    width:100%;justify-content:space-between;
    padding:0.85em 0.25em;font-size:var(--step-0);
    border-bottom:var(--bd-hair);
  }
  .nav-sub-toggle .chev{width:0.9em;height:0.9em}
  .nav-sub{
    position:static;min-width:0;
    background:transparent;border:0;border-bottom:var(--bd-hair);
    border-radius:0;box-shadow:none;
    padding:0.35rem 0 0.6rem 0.25rem;
  }
  .nav-sub a{font-size:var(--step--1);padding:0.6em 0.5em}
}
/* NAV-SUB:CSS:END */
"""

JS = """
<script data-nav-sub="1">
/* Services submenu: a real button, keyboard included. Without JS the panel
   stays visible and the links remain reachable */
(function(){
  var wrap = document.querySelector('.nav-sub-wrap');
  if (!wrap) return;
  var btn = wrap.querySelector('.nav-sub-toggle');
  function set(open){
    wrap.setAttribute('data-open', open ? 'true' : 'false');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  set(false);
  btn.addEventListener('click', function(e){
    e.preventDefault();
    set(wrap.getAttribute('data-open') !== 'true');
  });
  document.addEventListener('click', function(e){
    if (!wrap.contains(e.target)) set(false);
  });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && wrap.getAttribute('data-open') === 'true'){ set(false); btn.focus(); }
  });
  wrap.querySelectorAll('.nav-sub a').forEach(function(a){
    a.addEventListener('click', function(){ set(false); });
  });
})();
</script>"""

ICONS = {
 "scorpion": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4"/>'
             '<path d="M12 1.6v2.4M12 20v2.4M1.6 12h2.4M20 12h2.4"/></svg>',
 "ant":      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<circle cx="6" cy="5.5" r="2.4"/><circle cx="6" cy="18.5" r="2.4"/>'
             '<circle cx="18" cy="12" r="2.4"/>'
             '<path d="M6 7.9v8.2M8.2 6.8l7.6 3.9M8.2 17.2l7.6-3.9"/></svg>',
 "general":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M12 2.4 21 7l-9 4.6L3 7l9-4.6Z"/><path d="M3 12.2l9 4.6 9-4.6"/>'
             '<path d="M3 17.2l9 4.6 9-4.6"/></svg>',
}

SUB = [("Scorpion Control", "scorpion-control.html", "scorpion"),
       ("Ant Control",      "ant-control.html",      "ant"),
       ("General Pest Control", "general-pest-control.html", "general")]

def nav_links(current=None, home_anchors=False):
    """current: home|about|scorpion|ant|general|process|reviews|contact|None"""
    pre = "" if home_anchors else "index.html"
    def h(frag): return f"{pre}#{frag}" if not home_anchors else f"#{frag}"
    cur = lambda k: ' aria-current="page"' if k == current else ""
    subs = "\n".join(
      f'        <a href="{href}"{cur(key)}>{ICONS[key]}<span>{label}</span></a>'
      for label, href, key in SUB)
    is_cur = " is-current" if current in ("scorpion", "ant", "general") else ""
    home = "index.html" if not home_anchors else "#home"
    return f'''    <nav class="nav-links" id="nav-links" aria-label="Main">
      <a href="{home}"{cur("home")}>Home</a>
      <a href="about.html"{cur("about")}>About</a>
      <div class="nav-sub-wrap">
        <button class="nav-sub-toggle{is_cur}" type="button" aria-expanded="false" aria-controls="nav-sub">
          Services
          <svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"
               stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 9l7 7 7-7"/></svg>
        </button>
        <div class="nav-sub" id="nav-sub">
{subs}
        </div>
      </div>
      <a href="{h("process")}"{cur("process")}>Process</a>
      <a href="{h("reviews")}"{cur("reviews")}>Reviews</a>
      <a href="#contact"{cur("contact")}>Contact</a>
    </nav>'''

CSS_RE = re.compile(r"/\* NAV-SUB:CSS:START \*/.*?/\* NAV-SUB:CSS:END \*/\n?", re.S)
JS_RE  = re.compile(r'<script data-nav-sub="1">.*?</script>\n?', re.S)

def patch(fn, current, home_anchors):
    p = os.path.join(ROOT, fn)
    s = open(p, encoding="utf-8").read()
    css_block = CSS.strip("\n") + "\n"
    # CSS: if a marked block already exists (from an earlier run) it's
    # replaced whole, so CSS changes reach pages that were already patched;
    # otherwise it's inserted before the stylesheet closes
    if CSS_RE.search(s):
        s = CSS_RE.sub(css_block, s, count=1)
    else:
        i = s.rindex("</style>")
        s = s[:i] + CSS + s[i:]
    # JS: same rule, marked by the data-nav-sub attribute
    js_block = JS.strip("\n") + "\n"
    if JS_RE.search(s):
        s = JS_RE.sub(js_block, s, count=1)
    else:
        i = s.rindex("</body>")
        s = s[:i] + js_block + s[i:]
    # nav markup
    s = re.sub(r' *<nav class="nav-links".*?</nav>', nav_links(current, home_anchors), s, count=1, flags=re.S)
    open(p, "w", encoding="utf-8").write(s)
    return fn

if __name__ == "__main__":
    print(patch("index.html", "home", True))
    print(patch("about.html", "about", False))
