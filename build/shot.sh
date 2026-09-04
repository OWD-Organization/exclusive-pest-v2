#!/bin/bash
# uso: shot.sh archivo.html ancho alto etiqueta
cd "/home/jusevelez/Work/OWD/design-exploration/exclusive pest"
S=/tmp/claude-1000/-home-jusevelez-Work-OWD-design-exploration/0d057a6c-97fd-4e44-acbe-de2e5bf58043/scratchpad
python3 -c "
s=open('$1',encoding='utf-8').read().replace(' loading=\"lazy\"','')
i=s.find('<!-- Feedbucket')
if i>=0:
    j=s.index('</script>',i)+9; s=s[:i]+s[j:]
open('_s.html','w',encoding='utf-8').write(s)"
if [ "$2" -le 500 ]; then
  cat > $S/_hs.html <<EOF
<style>html,body{margin:0}iframe{width:$2px;height:$3px;border:0;display:block}</style>
<iframe src="file://$PWD/_s.html"></iframe>
EOF
  google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --allow-file-access-from-files \
    --force-color-profile=srgb --window-size=$(($2+20)),$3 --virtual-time-budget=28000 \
    --screenshot=$S/$4.png "file://$S/_hs.html" 2>&1 | grep -ic written
else
  google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --allow-file-access-from-files \
    --force-color-profile=srgb --window-size=$2,$3 --virtual-time-budget=28000 \
    --screenshot=$S/$4.png "file://$PWD/_s.html" 2>&1 | grep -ic written
fi
rm -f _s.html
