# -*- coding: utf-8 -*-
"""Verificacion de una pagina: HTML, dashes, enlaces, assets, contraste,
desbordes y tamanos de texto, en escritorio y en movil real via iframe."""
import subprocess, re, html, os, sys
f = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
d = os.getcwd()
S = "/tmp/claude-1000/-home-jusevelez-Work-OWD-design-exploration/0d057a6c-97fd-4e44-acbe-de2e5bf58043/scratchpad"
raw = open(f, encoding="utf-8").read()

print(f"### {f}  {len(raw)//1024} KB")
print("  em/en dash:", raw.count("—"), raw.count("–"))
from html.parser import HTMLParser
void = {"meta","link","img","br","hr","input","source","path","circle"}
st, bad = [], []
class P(HTMLParser):
    def handle_starttag(s, t, a):
        if t not in void: st.append(t)
    def handle_endtag(s, t):
        if t in void: return
        if st and st[-1] == t: st.pop()
        else: bad.append(t)
P().feed(raw)
print("  HTML sin cerrar:", st or "ninguno", " desemparejados:", bad or "ninguno")
miss = [a for a in sorted(set(re.findall(r'(?:src|srcset)="(build-assets/[^"]+)"', raw)))
        if not os.path.exists(a)]
print("  assets ausentes:", miss or "ninguno")
lnk = sorted(set(re.findall(r'href="([a-z0-9][a-z0-9.#-]*)"', raw)))
ids = set(re.findall(r'id="([a-z0-9-]+)"', raw))
brk = []
for h in lnk:
    if h.startswith("#"):
        if h[1:] not in ids: brk.append(h)
    elif ".html" in h:
        if not os.path.exists(h.split("#")[0]): brk.append(h)
print("  enlaces rotos:", brk or "ninguno")

body = raw.replace(' loading="lazy"', "")
i = body.find("<!-- Feedbucket")
if i >= 0:
    j = body.index("</script>", i) + 9
    body = body[:i] + body[j:]

PROBE = r'''
<script>setTimeout(function(){
 var NL=String.fromCharCode(10),o=[],D=document,Wn=window,R=D.documentElement;
 var cv=D.createElement('canvas');cv.width=cv.height=1;var cx=cv.getContext('2d',{willReadFrequently:true});var ch={};
 function rgb(c){if(ch[c])return ch[c];cx.fillStyle='#000';cx.fillRect(0,0,1,1);cx.fillStyle=c;cx.fillRect(0,0,1,1);var p=cx.getImageData(0,0,1,1).data;return ch[c]=[p[0],p[1],p[2]]}
 function lin(c){c/=255;return c<=0.03928?c/12.92:Math.pow((c+0.055)/1.055,2.4)}
 function L(c){var r=rgb(c);return 0.2126*lin(r[0])+0.7152*lin(r[1])+0.0722*lin(r[2])}
 function bgEl(e){while(e&&e!==R){var c=getComputedStyle(e).backgroundColor;if(c&&c!=='rgba(0, 0, 0, 0)'&&!/,\s*0\)$/.test(c))return e;e=e.parentElement}return D.body}
 function rat(a,b){var l1=L(a),l2=L(b);return (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05)}
 function pth(e){var p=[];while(e&&e!==D.body){p.unshift(e.tagName.toLowerCase()+(e.className&&e.className.split?'.'+String(e.className).trim().split(/\s+/)[0]:''));e=e.parentElement}return p.slice(-2).join('>')}
 o.push('alto '+R.scrollHeight+'  desborda '+(R.scrollWidth>R.clientWidth)+' ('+R.scrollWidth+'/'+R.clientWidth+')');
 o.push('secciones '+D.querySelectorAll('section').length+'  h1 '+D.querySelectorAll('h1').length+'  h2 '+D.querySelectorAll('h2').length+'  h3 '+D.querySelectorAll('h3').length+'  details '+D.querySelectorAll('details').length);
 var bi=[];D.querySelectorAll('img').forEach(function(i){if(!i.complete||i.naturalWidth===0)bi.push(i.currentSrc||i.src)});
 o.push('imagenes '+D.querySelectorAll('img').length+'  fallidas '+(bi.length?bi.join(','):'0'));
 var sm=[];D.querySelectorAll('body *').forEach(function(e){if(!e.children.length&&e.textContent.trim()){var s=parseFloat(getComputedStyle(e).fontSize);if(s<12)sm.push(pth(e)+':'+s)}});
 o.push('texto <12px: '+(sm.length?sm.slice(0,4).join(', '):'ninguno'));
 var ov=[];D.querySelectorAll('body *').forEach(function(e){var cs=getComputedStyle(e);if(cs.position!=='static')return;var r=e.getBoundingClientRect();if(r.width&&r.right>R.clientWidth+1)ov.push(pth(e)+'='+Math.round(r.right))});
 o.push('elementos fuera de ancho: '+(ov.length?ov.slice(0,4).join(' | '):'ninguno'));
 var seen={},fail=[],worst=99,wd='';
 D.querySelectorAll('body *').forEach(function(e){
   if(e.children.length||!e.textContent.trim())return;
   var cs=getComputedStyle(e),fs=parseFloat(cs.fontSize),fw=parseInt(cs.fontWeight)||400;
   if(cs.display==='none'||cs.visibility==='hidden')return;
   var lg=(fs>=24)||(fs>=18.66&&fw>=700),be=bgEl(e),b=getComputedStyle(be).backgroundColor;
   var k=cs.color+'|'+b+'|'+(lg?'L':'N');if(seen[k])return;seen[k]=1;
   var r=rat(cs.color,b),need=lg?3:4.5;
   if(r<worst){worst=r;wd=r.toFixed(2)+' ('+(lg?'grande':'normal')+' '+Math.round(fs)+'px) '+pth(e)}
   if(r<need)fail.push(r.toFixed(2)+'/'+need+' '+Math.round(fs)+'px '+pth(e)+' "'+e.textContent.trim().slice(0,28)+'"');
 });
 o.push('contraste: '+Object.keys(seen).length+' pares, fallos AA '+fail.length+'  |  mas bajo en uso '+wd);
 fail.forEach(function(x){o.push('   FALLA '+x)});
 var pre=D.createElement('pre');pre.id='PP';pre.textContent=o.join(NL);
 (Wn.parent&&Wn.parent!==Wn?Wn.parent.document.body:D.body).appendChild(pre);
},5500);</script>'''

if W <= 500:
    open(f"{d}/_t.html","w",encoding="utf-8").write(body.replace("</body>", PROBE+"</body>"))
    open(f"{S}/_h.html","w").write(
      f'<style>html,body{{margin:0}}iframe{{width:{W}px;height:14000px;border:0;display:block}}</style>'
      f'<iframe src="file://{d}/_t.html"></iframe>')
    target, win = f"{S}/_h.html", W+20
else:
    open(f"{d}/_t.html","w",encoding="utf-8").write(body.replace("</body>", PROBE+"</body>"))
    target, win = f"{d}/_t.html", W

out = subprocess.run(["google-chrome","--headless=new","--disable-gpu","--no-sandbox",
  "--allow-file-access-from-files","--force-color-profile=srgb",
  f"--window-size={win},1200","--virtual-time-budget=28000","--dump-dom",f"file://{target}"],
  capture_output=True, text=True).stdout
m = re.search(r'<pre id="PP">(.*?)</pre>', out, re.S)
print(f"  --- render {W}px ---")
for l in (html.unescape(m.group(1)).strip().split("\n") if m else ["sin salida"]):
    print("   ", l)
os.remove(f"{d}/_t.html")
