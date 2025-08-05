import os
import re

# Directory di partenza con i markdown
input_dir = r"C:\Users\HP\Desktop\New_tarocchi_read\frontend\des_a_m_1carta"
# Directory di destinazione per gli HTML
output_dir = r"C:\Users\HP\Desktop\New_tarocchi_read\frontend\tarocchi"

# Assicurati che la cartella di destinazione esista
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(input_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Estrai titolo H2 dalla prima riga tipo "## Il Matto – L’Inizio del Viaggio"
        title_match = re.search(r"^##\s+(.*)", content, re.MULTILINE)
        if title_match:
            full_title = title_match.group(1).strip()
        else:
            full_title = os.path.splitext(filename)[0]

        # Genera slug SEO-friendly per il file
        # Usa solo la prima parola significativa del titolo per il nome
        # es: "Il Matto – ..." -> "0-matto" se il file originale inizia con numero
        base_name = os.path.splitext(filename)[0]
        slug = base_name.lower().replace(" ", "-")

        # Converti markdown in HTML base (qui semplice: titoli -> <h2>, <h3>)
        # Si può usare markdown2 per conversione completa
        html_body = content

        # Converti titoli
        html_body = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r"^### (.*)$", r"<h3>\1</h3>", html_body, flags=re.MULTILINE)

        # Converti liste markdown
        html_body = re.sub(r"^- (.*)$", r"<li>\1</li>", html_body, flags=re.MULTILINE)
        # Raggruppa liste <ul>
        html_body = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", html_body, count=1, flags=re.DOTALL)

        # Template HTML SEO-friendly
        html_template = f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title} - Significato e Interpretazione nei Tarocchi</title>
  <meta name="description" content="Scopri il significato dell'Arcano {full_title} nei tarocchi: simbolismo, interpretazioni esoteriche e meditazioni spirituali.">
  <link rel="canonical" href="https://tuodominio.com/tarocchi/{slug}">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{full_title}",
    "description": "Interpretazione esoterica dell'Arcano {full_title} nei tarocchi: significato, simbolismo e meditazione.",
    "author": {{
      "@type": "Person",
      "name": "Il tuo nome o pseudonimo"
    }},
    "datePublished": "2025-08-05"
  }}
  </script>
  <style>
    body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; }}
    img {{ max-width: 100%; height: auto; display: block; margin: 20px auto; }}
    h1, h2, h3 {{ color: #333; }}
    nav a {{ margin-right: 15px; }}
  </style>
</head>
<body>
  <header>
    <h1>{full_title}</h1>
    <img src="/frontend/cards_arcani_maggiori/{slug}.jpg" alt="{full_title} - Arcano dei Tarocchi">
  </header>
  <main>
    {html_body}
  </main>
  <nav>
    <a href="/tarocchi">← Torna a tutti gli Arcani Maggiori</a>
  </nav>
</body>
</html>
"""

        # Salva file HTML
        output_path = os.path.join(output_dir, slug + ".html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_template)

        print(f"Creato: {output_path}")
