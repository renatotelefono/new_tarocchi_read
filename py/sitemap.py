import os

# Directory dei file HTML
directory = r"C:\Users\HP\Desktop\New_tarocchi_read\frontend\tarocchi"

# URL base del tuo sito
base_url = "https://tuodominio.com/tarocchi/"

# File di output della sitemap
sitemap_path = r"C:\Users\HP\Desktop\New_tarocchi_read\frontend\sitemap.xml"

# Trova tutti i file HTML
files = [f for f in os.listdir(directory) if f.endswith(".html")]
files.sort()  # Ordina per numero

# Crea contenuto XML
sitemap_entries = []

# Aggiungi la pagina indice
sitemap_entries.append(f"  <url>\n    <loc>{base_url}index.html</loc>\n    <priority>1.0</priority>\n  </url>")

# Aggiungi tutte le carte
for f in files:
    sitemap_entries.append(f"  <url>\n    <loc>{base_url}{f}</loc>\n    <priority>0.8</priority>\n  </url>")

# Unisci tutto nel formato XML
sitemap_content = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
sitemap_content += "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
sitemap_content += "\n".join(sitemap_entries)
sitemap_content += "\n</urlset>"

# Salva la sitemap.xml
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Sitemap generata in: {sitemap_path}")
