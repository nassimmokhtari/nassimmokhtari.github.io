import os
import bibtexparser
from datetime import datetime

# Modèle Markdown
MD_TEMPLATE = """---
title: "{title}"
collection: publications
category: manuscripts
permalink: /publication/{permalink}
excerpt: "{excerpt}"
date: {date}
venue: "{venue}"
bibtexurl: "{bibtexurl}"
citation: "{citation}"
---
{content}
"""


def generate_md_from_bib(bib_file, output_dir, base_url=""):
    """
    Génère des fichiers Markdown à partir d'un fichier BibTeX.

    Arguments:
    - bib_file: chemin vers le fichier .bib
    - output_dir: dossier de sortie pour les fichiers .md
    - base_url: URL de base pour slides, PDF et BibTeX si disponible
    """
    os.makedirs(output_dir, exist_ok=True)

    with open(bib_file, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for entry in bib_database.entries:
        temp_db = bibtexparser.bibdatabase.BibDatabase()
        temp_db.entries = [entry]

        # Convertit en texte BibTeX
        bibtex_text = bibtexparser.dumps(temp_db)

        filename = f"{entry.get('ID')}.bib"
        filepath = os.path.join("files", filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(bibtex_text)

        title = entry.get('title', 'No Title').replace('{', '').replace('}', '')
        year = entry.get('year', datetime.today().year)
        journal = entry.get('journal', entry.get('booktitle', 'Unknown Venue'))
        authors = entry.get('author', 'Unknown Author')
        doi = entry.get('doi', '')
        url = entry.get('url', '')
        slidesurl = entry.get('slidesurl', '')  # optionnel, peut être ajouté dans le BibTeX
        paperurl = url
        bibtex_filename = f"{title.lower().replace(' ', '-')}.bib"

        citation = f"{authors} ({year}). &quot;{title}.&quot; <i>{journal}</i>."
        excerpt = f"Publication titled '{title}' by {authors}."
        content = f"This is the full content for the paper '{title}'."
        permalink = f"{year}-{title.lower().replace(' ', '-')}"

        md_content = MD_TEMPLATE.format(
            title=title,
            permalink=permalink,
            excerpt=excerpt,
            date=f"{year}-01-01",  # par défaut, on prend le 1er janvier si pas de date complète
            venue=journal,
            slidesurl=slidesurl,
            paperurl=paperurl,
            bibtexurl=f"{base_url}/{bibtex_filename}",
            citation=citation,
            content=content
        )

        filename = f"{entry.get('ID')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"Fichier généré : {filepath}")


# Exemple d'utilisation
if __name__ == "__main__":
    generate_md_from_bib("publications.bib", "_publications", base_url="https://nassimmokhtari.github.io/files")
