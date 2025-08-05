import os

# Directory dei file HTML dei tarocchi
directory = r"C:\Users\HP\Desktop\New_tarocchi_read\frontend\tarocchi"

# Prende tutti i file HTML e li ordina per numero
files = [f for f in os.listdir(directory) if f.endswith(".html")]
files.sort()  # Assumiamo nomi tipo 00_matto.html, 01_mago.html

def pretty_name(filename):
    """Converte '00_matto.html' in '00 Matto' per i link di navigazione"""
    base = os.path.splitext(filename)[0]
    num, name = base.split("_", 1)
    return f"{num} {name.capitalize()}"

for i, filename in enumerate(files):
    filepath = os.path.join(directory, filename)
    
    # Determina file precedente e successivo (ciclo completo)
    prev_file = files[i-1] if i > 0 else files[-1]
    next_file = files[i+1] if i < len(files)-1 else files[0]

    # Leggi il contenuto del file
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Rimuovi eventuali vecchi blocchi di navigazione (opzionale)
    content = content.replace("</nav>", "").replace("<nav>", "")

    # Crea la barra di navigazione
    nav_html = f"""
  <nav>
    <a href="{prev_file}">← {pretty_name(prev_file)}</a> |
    <a href="index.html">Torna agli Arcani</a> |
    <a href="{next_file}">{pretty_name(next_file)} →</a>
  </nav>
</body>
</html>
"""

    # Sostituisci la chiusura </body></html> con la nuova navigazione
    new_content = content
    new_content = new_content.replace("</body>\n</html>", nav_html).replace("</body></html>", nav_html)

    # Sovrascrivi il file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Aggiornato: {filename} con link a {prev_file} e {next_file}")
