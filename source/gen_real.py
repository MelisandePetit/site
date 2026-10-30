# Génère parts/realisations.html à partir de la liste des chantiers
P=[
 dict(s="colombieres",n=7,cov=1,cat="Isolation · Crépi",lieu="Versoix",adr="Chemin des Colombières",
  t="Surélévation d'une école",
  p="Isolation de la surélévation en laine de roche, puis finition en crépi minéral à la chaux.",
  bat="École, surélévation",trav="Isolation thermique par l'extérieur et crépi",mat="Laine de roche, crépi minéral à la chaux"),
 dict(s="cornillons",n=6,cov=3,cat="Isolation · Pierre",lieu="Pregny-Chambésy",adr="Chemin des Cornillons",
  t="Transformation et extension d'une villa",
  p="Isolation de la villa transformée et agrandie, avec une finition qui associe la pierre et le crépi.",
  bat="Villa, transformation et extension",trav="Isolation, finition pierre et crépi",mat=None),
 dict(s="grandes-communes",n=2,cov=2,cat="Rénovation énergétique",lieu="Onex",adr="Avenue des Grandes-Communes",
  t="Rénovation énergétique d'un grand immeuble",
  p="Isolation des édicules, puis reprise de la peinture et du crépi des façades et des balcons.",
  bat="Grand bâtiment de logements",trav="Isolation des édicules, peinture et crépi",mat=None),
 dict(s="degallier",n=4,cov=2,cat="Isolation · Crépi",lieu="Versoix",adr="Chemin Louis-Dégallier",
  t="Isolation d'un bâtiment neuf",
  p="Isolation complète des façades d'un bâtiment neuf, avec une finition en crépi dentelé.",
  bat="Bâtiment neuf",trav="Isolation et crépi",mat="Crépi dentelé"),
 dict(s="montagne",n=4,cov=1,cat="Façade ventilée",lieu=None,adr=None,
  t="Façade ventilée en briquettes",
  p="Réalisation d'une façade ventilée sur un immeuble de logements neuf, avec un parement en briquettes.",
  bat="Immeuble de logements neuf",trav="Façade ventilée",mat="Briquettes de parement"),
 dict(s="montbrillant",n=1,cov=1,cat="Ravalement · Isolation",lieu="Genève",adr="Chemin de Montbrillant",
  t="Ravalement d'un immeuble genevois",
  p="Dépose de l'ancien crépi, isolation en aérogel, un isolant très mince adapté aux façades existantes, puis nouveau crépi.",
  bat="Immeuble existant",trav="Dépose du crépi, isolation et nouveau crépi",mat="Isolant aérogel, crépi"),
 dict(s="peutasse",n=2,cov=2,cat="Isolation · Crépi",lieu="La Croix-de-Bosson",adr="Chemin de la Peutasse",
  t="Immeuble de logements neuf",
  p="Isolation des façades d'un bâtiment de logements neuf et finition en crépi.",
  bat="Bâtiment de logements neuf",trav="Isolation et crépi",mat=None),
 dict(s="pralet",n=4,cov=3,cat="Ravalement",lieu="Founex",adr="Chemin du Pralet",
  t="Ravalement de deux immeubles",
  p="Ravalement complet des façades de deux bâtiments de logements.",
  bat="Deux bâtiments de logements",trav="Ravalement de façade",mat=None),
 dict(s="pilotis",n=1,cov=1,cat="Isolation · Crépi",lieu="Corsier",adr="Chemin des Pilotis",
  t="Maison de deux logements",
  p="Isolation en laine minérale et finition en crépi taloché à l'ancienne.",
  bat="Maison de deux logements",trav="Isolation et crépi",mat="Laine minérale, crépi taloché à l'ancienne"),
]
ORDRE=["colombieres","cornillons","grandes-communes","degallier","peutasse","pralet","pilotis","montbrillant","montagne"]
P=sorted(P,key=lambda c:ORDRE.index(c["s"]))
cards=[]
for c in P:
    order=[c["cov"]]+[i for i in range(1,c["n"]+1) if i!=c["cov"]]
    photos="|".join(f'img/real-{c["s"]}-{i}.jpg' for i in order)
    cover=f'img/real-{c["s"]}-{c["cov"]}.jpg'
    nb=f'<span class="nb"><svg><use href="#i-photos"/></svg>{c["n"]} photos</span>' if c["n"]>1 else ''
    lieu=f'<span class="lieu"><svg><use href="#i-pin"/></svg>{c["lieu"]}</span>' if c["lieu"] else ''
    li=[]
    if c["lieu"]: li.append(("Lieu",c["lieu"]))
    li+= [("Bâtiment",c["bat"]),("Travaux",c["trav"])]
    if c["mat"]: li.append(("Matériaux",c["mat"]))
    ul="".join(f'<li><span><b>{k} :</b> {v}</span></li>' for k,v in li)
    alt=f'{c["t"]}{", "+c["lieu"] if c["lieu"] else ""}'
    cards.append(f'''        <article class="real">
          <button class="ph" type="button" data-photos="{photos}" aria-label="Voir les photos : {alt}"><img src="{cover}" alt="{alt}" loading="lazy"><span class="cat">{c["cat"]}</span>{nb}</button>
          <div class="corps">
            {lieu}
            <h2>{c["t"]}</h2>
            <p>{c["p"]}</p>
            <details>
              <summary>Les détails du chantier</summary>
              <ul>{ul}</ul>
            </details>
          </div>
        </article>''')
html=f'''  <!-- Titre de page -->
  <section class="page-head page-head--real on-dark">
    <div class="wrap">
      <span class="eyebrow">Nos réalisations</span>
      <h1>Nos derniers chantiers, en images et en détail.</h1>
      <p>Isolation, crépi, façade ventilée, ravalement… une sélection de chantiers réalisés autour de Genève, sur des maisons comme sur des immeubles.</p>
    </div>
  </section>

  <section class="reals">
    <div class="wrap">
      <div class="grille-r" id="grille-r">
{chr(10).join(cards)}
      </div>
    </div>
  </section>

  <!-- Visionneuse photos -->
  <dialog class="lb" id="lb" aria-label="Photos du chantier">
    <img alt="">
    <span class="lb-n"></span>
    <button class="lb-x" type="button" aria-label="Fermer">×</button>
    <button class="lb-p" type="button" aria-label="Photo précédente">‹</button>
    <button class="lb-s" type="button" aria-label="Photo suivante">›</button>
  </dialog>
  <script>
  (function(){{
    var lb=document.getElementById('lb'); if(!lb) return;
    var im=lb.querySelector('img'), n=lb.querySelector('.lb-n'), L=[], i=0, alt='';
    function show(){{ im.src=L[i]; im.alt=alt+' – photo '+(i+1); n.textContent=(i+1)+' / '+L.length; lb.classList.toggle('solo',L.length<2); }}
    function go(d){{ i=(i+d+L.length)%L.length; show(); }}
    document.querySelectorAll('.real .ph').forEach(function(b){{
      b.addEventListener('click',function(){{ L=b.dataset.photos.split('|'); i=0; alt=b.querySelector('img').alt; show(); lb.showModal(); }});
    }});
    lb.querySelector('.lb-x').onclick=function(){{ lb.close(); }};
    lb.querySelector('.lb-p').onclick=function(){{ go(-1); }};
    lb.querySelector('.lb-s').onclick=function(){{ go(1); }};
    lb.addEventListener('click',function(e){{ if(e.target===lb) lb.close(); }});
    lb.addEventListener('keydown',function(e){{ if(e.key==='ArrowLeft') go(-1); if(e.key==='ArrowRight') go(1); }});
    var x0=null; lb.addEventListener('touchstart',function(e){{ x0=e.touches[0].clientX; }},{{passive:true}});
    lb.addEventListener('touchend',function(e){{ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>40) go(dx<0?1:-1); x0=null; }});
  }})();
  </script>
'''
open("parts/realisations.html","w").write(html)
