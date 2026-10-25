import base64, re, subprocess, sys
import os
FONT=os.environ.get('MANROPE_TTF','manrope.ttf')  # Manrope variable font (OFL), from fonts.google.com/specimen/Manrope
MARK='data:image/png;base64,'+base64.b64encode(open('mark-source.png','rb').read()).decode()
def text(s, x, top, size, weight, color, anchor='start'):
    svg=subprocess.run(['hb-view',f'--font-file={FONT}',f'--variations=wght={weight}',f'--font-size={size}','--margin=0','--background=FFFFFF00',f'--foreground={color.lstrip("#")}','--output-format=svg',s],capture_output=True,text=True,check=True).stdout
    w=float(re.search(r'width="([\d.]+)"',svg).group(1)); h=float(re.search(r'height="([\d.]+)"',svg).group(1))
    if anchor=='middle': x-=w/2
    if anchor=='end': x-=w
    uri='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
    return f'<image x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{h:.1f}" xlink:href="{uri}"/>'
DEFS='<defs><filter id="white" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1 0"/></filter></defs>'
def phone(px, py, app='Consular appointments', host='apps.partner.example', heading='Book an appointment', button='Add to my plans'):
    g=[f'<g transform="translate({px},{py})">',
    '<rect width="360" height="620" rx="48" fill="#0b2a66"/>','<rect x="14" y="14" width="332" height="592" rx="36" fill="#F4F7FC"/>',
    '<rect x="14" y="14" width="332" height="78" rx="36" fill="#FFFFFF"/>','<rect x="14" y="56" width="332" height="36" fill="#FFFFFF"/>',
    '<line x1="14" y1="92" x2="346" y2="92" stroke="#D8DEEA" stroke-width="2"/>',
    '<path d="M40 46 l14 14 M54 46 l-14 14" stroke="#172033" stroke-width="4" stroke-linecap="round"/>',
    '<rect x="68" y="38" width="30" height="30" rx="8" fill="#003893"/>',f'<image x="71" y="41" width="24" height="24" filter="url(#white)" xlink:href="{MARK}"/>',
    text(app,108,36,15,800,'#172033'),'<circle cx="112" cy="70" r="5" fill="#157347"/>',text(host,122,61,13,500,'#5f6b80'),
    '<line x1="296" y1="53" x2="310" y2="53" stroke="#172033" stroke-width="4" stroke-linecap="round"/>',
    '<circle cx="330" cy="45" r="2.6" fill="#172033"/><circle cx="330" cy="53" r="2.6" fill="#172033"/><circle cx="330" cy="61" r="2.6" fill="#172033"/>',
    text(heading,38,114,24,800,'#0b2a66'),text('Signed in with SabiVida',38,150,15,500,'#5f6b80'),
    '<rect x="38" y="186" width="284" height="84" rx="18" fill="#FFFFFF" stroke="#D8DEEA" stroke-width="2"/>','<rect x="56" y="204" width="48" height="48" rx="12" fill="#DCE6F7"/>',
    '<rect x="118" y="210" width="150" height="14" rx="7" fill="#172033" opacity="0.85"/>','<rect x="118" y="234" width="104" height="12" rx="6" fill="#5f6b80" opacity="0.5"/>',
    '<rect x="38" y="286" width="284" height="84" rx="18" fill="#FFFFFF" stroke="#D8DEEA" stroke-width="2"/>','<rect x="56" y="304" width="48" height="48" rx="12" fill="#FFF3BF"/>',
    '<rect x="118" y="310" width="130" height="14" rx="7" fill="#172033" opacity="0.85"/>','<rect x="118" y="334" width="120" height="12" rx="6" fill="#5f6b80" opacity="0.5"/>',
    '<rect x="38" y="396" width="284" height="60" rx="30" fill="#F7D116"/>',text(button,180,411,18,800,'#172033','middle'),
    '<rect x="38" y="476" width="284" height="104" rx="18" fill="#FFFFFF" stroke="#D8DEEA" stroke-width="2"/>',
    '<rect x="56" y="496" width="180" height="12" rx="6" fill="#5f6b80" opacity="0.35"/>','<rect x="56" y="520" width="240" height="12" rx="6" fill="#5f6b80" opacity="0.25"/>',
    '</g>']
    return '\n'.join(g)
def canvas(w,h,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{DEFS}<clipPath id="c"><rect width="{w}" height="{h}"/></clipPath><g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="#003893"/><rect x="88" width="96" height="10" fill="#F7D116"/>{body}</g></svg>'
def lockup(x,y,s=1):
    return f'<image x="{x}" y="{y}" width="{76*s:.0f}" height="{76*s:.0f}" filter="url(#white)" xlink:href="{MARK}"/>'+text('SabiVida',x+92*s,y+14*s,40*s,800,'#FFFFFF')
def write(name,svg,w,h):
    open(name+'.svg','w').write(svg); subprocess.run(['rsvg-convert','-w',str(w),'-h',str(h),name+'.svg','-o',name+'.png'],check=True); print('wrote',name+'.png')
# Profile banner 1600x520
write('banner',canvas(1600,520,'\n'.join([lockup(88,104),text('Mini apps',84,196,92,800,'#FFFFFF'),
  text('Your service, inside the app Cape Verdean',88,326,34,500,'#FFFFFF'),text('families use to run their homes.',88,370,34,500,'#FFFFFF'),
  text('Invited partners · Consent first · Visible trust',88,436,26,700,'#F7D116'),phone(1130,56)])),1600,520)
# Social previews 1280x640
for repo,title,l1,l2,app,host,heading,button in [
  ('partner-kit','Partner kit','Guide, protocol and SDK to build','a SabiVida mini app.','Consular appointments','apps.partner.example','Book an appointment','Add to my plans'),
  ('first-app','First app','A starter page and server that verify','SabiVida sign-in and suggest plan steps.','Your first app','your-app.example','Hello, member','Add to my plans'),
  ('registry','Partner registry','The public list of genuine','SabiVida partner apps.','Consular appointments','apps.partner.example','Is this app genuine?','Listed in the registry'),
  ('first-app-react','First app · React','React, Vite and TypeScript, with','SabiVida sign-in and a local stand-in.','Your first app','your-app.example','Hello, member','Add to my plans'),
  ('first-app-next','First app · Next.js','Next.js App Router and TypeScript,','with SabiVida sign-in on your server.','Your first app','your-app.example','Hello, member','Add to my plans'),
  ('first-app-vue','First app · Vue','Vue, Vite and TypeScript, with','SabiVida sign-in and a local stand-in.','Your first app','your-app.example','Hello, member','Add to my plans'),
  ('first-app-solid','First app · Solid','Solid, Vite and TypeScript, with','SabiVida sign-in and a local stand-in.','Your first app','your-app.example','Hello, member','Add to my plans')]:
    write('social-'+repo,canvas(1280,640,'\n'.join([lockup(88,120),text(title,84,212,84,800,'#FFFFFF'),
      text(l1,88,338,32,500,'#FFFFFF'),text(l2,88,380,32,500,'#FFFFFF'),
      text('github.com/sabivida-mini-apps/'+repo,88,460,24,700,'#F7D116'),phone(840,64,app,host,heading,button)])),1280,640)
