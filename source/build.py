import os,re,shutil
P=lambda n: open(f"parts/{n}").read()
HEAD='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap">
'''
def header(active,devis='#devis'):
    cur=lambda k:' aria-current="page"' if k==active else ''
    return f'''<header class="header" id="top">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="NG Façades, accueil"><img src="img/logo-couleur.svg" alt="NG Façades"></a>
    <nav class="nav" id="nav" aria-label="Menu principal">
      <a href="index.html"{cur("accueil")}>Accueil</a>
      <a href="services.html"{cur("services")}>Nos services</a>
      <a href="realisations.html"{cur("realisations")}>Nos réalisations</a>
      <a class="btn btn-primary" href="{devis}">Demander un devis</a>
    </nav>
    <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
'''
footer=P("footer.html").replace('href="#top"','href="index.html"').replace('href="#histoire"','href="index.html#histoire"').replace('href="#services"','href="services.html"').replace('<a href="#">Nos réalisations</a>','<a href="realisations.html">Nos réalisations</a>')
home=P("home.html")
ids=["isolation","crepi","pierre","brique","peinture","entretien","facade-ventilee","carbonatation"]
it=iter(ids)
home=re.sub(r'<a class="card" href="#services">',lambda m:f'<a class="card" href="services.html#{next(it)}">',home)
home=home.replace('<a class="btn btn-ghost all" href="#services">','<a class="btn btn-ghost all" href="services.html">')
PAGES={
 "index":dict(title="NG Façades – Accueil",desc="NG Façades : création, rénovation et isolation de façades à Genève et à Lausanne. Visite sur place et devis gratuits.",active="accueil",label="page d'accueil",css="",main=home+P("deroule.html")),
 "services":dict(title="NG Façades – Nos services",desc="Isolation, crépi, pierre, brique, peinture, entretien, façade ventilée et protection anti-carbonatation : les services de NG Façades à Genève et à Lausanne.",active="services",label="page Nos services",css=P("pagehead.css")+P("services-b.css"),main=P("services-b.html")+P("deroule.html")),
 "realisations":dict(title="NG Façades – Nos réalisations",desc="Découvrez des chantiers de façades réalisés par NG Façades : isolation, crépi, peinture, façade ventilée et entretien.",active="realisations",label="page Nos réalisations · chantiers d'exemple",css=P("pagehead.css")+P("realisations.css"),main=P("realisations.html")),
 "mentions-legales":dict(title="NG Façades – Mentions légales",desc="Mentions légales et politique de confidentialité du site NG Façades.",active="",label="page Mentions légales et confidentialité",css=P("legal.css"),main=P("legal.html"),contact=False,note="passages surlignés à compléter"),
}
def page(k):
    p=PAGES[k]
    top=f'<title>{p["title"]}</title>\n<meta name="description" content="{p["desc"]}">\n{HEAD}<style>\n{P("style.css")}{p["css"]}</style>\n'
    body=f'''
{P("sprite.html")}
<div class="maquette">Maquette · {p["label"]} · {p.get("note","photos génériques à remplacer")}</div>

{header(p["active"], "#devis" if p.get("contact",True) else "index.html#devis")}
<main>
{p["main"]}{P("contact.html") if p.get("contact",True) else ""}</main>

{footer if p.get("contact",True) else footer.replace('href="#devis"','href="index.html#devis"')}
<a class="whatsapp" href="https://wa.me/41782302841" target="_blank" rel="noopener" aria-label="Nous écrire sur WhatsApp"><svg><use href="#i-wa"/></svg></a>

<script>
{P("script.js")}</script>
'''
    return top,body
full=lambda t,b:'<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+t+'</head>\n<body>'+b+'</body>\n</html>\n'
ART="../art"; OUT="/mnt/user-data/outputs/site-web/maquette-accueil"
os.makedirs(OUT+"/img",exist_ok=True)
for k in PAGES:
    t,b=page(k)
    open(f"{OUT}/{k}.html","w").write(full(t,b))
    if k=="index": open(f"{ART}/ngfacades-accueil.html","w").write(t+b)
    else:
        open(f"{ART}/{k}.html","w").write(full(t,b))
        if k=="services": open(f"{ART}/ngfacades-services-b.html","w").write(t+b)
used=set(re.findall(r'img/[\w\-.]+', "".join(open(f"{OUT}/{k}.html").read() for k in PAGES)))
for f in os.listdir(OUT+"/img"): os.remove(OUT+"/img/"+f)
for u in sorted(used): shutil.copy(f"{ART}/{u}", f"{OUT}/{u}")
print(sorted(used))

# ---- Version en ligne (dépôt GitHub) : sans bandeau maquette, non référencée
import sys
SITE="/home/claude/site"
if os.path.isdir(SITE):
    os.makedirs(SITE+"/img",exist_ok=True)
    for k in PAGES:
        t,b=page(k)
        b=re.sub(r'<div class="maquette">.*?</div>\n\n','',b)
        t=t.replace('<meta name="description"','<meta name="robots" content="noindex, nofollow">\n<meta name="description"')
        b=b.replace("Maquette : l'envoi du formulaire sera branché lors de la mise en ligne.","Le formulaire n'est pas encore actif. En attendant, appelez-nous ou écrivez-nous par e-mail.")
        open(f"{SITE}/{k}.html","w").write(full(t,b))
    for u in sorted(used): shutil.copy(f"{ART}/{u}", f"{SITE}/{u}")
    open(SITE+"/robots.txt","w").write("User-agent: *\nDisallow: /\n")
    open(SITE+"/.nojekyll","w").write("")
