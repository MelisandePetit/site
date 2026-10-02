# Fichiers de travail

Les pages du site (`index.html`, `services.html`, `realisations.html`, `mentions-legales.html`) sont fabriquées à partir des morceaux de ce dossier :

- `parts/` : les blocs communs (en-tête de page, contact, pied de page, styles) et le contenu de chaque page ;
- `gen_b.py` : génère le contenu de la page Nos services ;
- `build.py` : assemble les pages.

Pour modifier le site, on change un morceau dans `parts/`, puis on relance `build.py`. Les chemins de dossiers dans `build.py` sont à adapter à l'endroit où on travaille.
