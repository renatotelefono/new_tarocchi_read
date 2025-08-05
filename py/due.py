import os

# Directory dei file HTML
directory = r"C:\Users\HP\Desktop\New_tarocchi_read\frontend\tarocchi"

# Dizionario di traduzione basato sui nomi file reali
translation = {
    "fool": "matto",
    "magician": "mago",
    "high_priestess": "papessa",
    "empress": "imperatrice",
    "emperor": "imperatore",
    "hierophant": "papa",
    "lovers": "amanti",
    "chariot": "carro",
    "strength": "forza",
    "hermit": "eremita",
    "wheel_of_fortune": "ruota",
    "justice": "giustizia",
    "hanged_man": "appeso",
    "death": "morte",
    "temperance": "temperanza",
    "devil": "diavolo",
    "tower": "torre",
    "star": "stella",
    "moon": "luna",
    "sun": "sole",
    "judgement": "giudizio",
    "world": "mondo"
}

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        old_path = os.path.join(directory, filename)
        name_no_ext = os.path.splitext(filename)[0]  # es: "00_fool"
        
        # Divide numero e nome
        parts = name_no_ext.split("_", 1)
        if len(parts) == 2:
            num, name_en = parts
            # Mantieni underscore per nomi composti
            name_en = name_en.lower()
            
            # Trova la traduzione
            new_name = translation.get(name_en)
            if new_name:
                new_filename = f"{num}_{new_name}.html"
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
                print(f"Rinominato: {filename} → {new_filename}")
            else:
                print(f"Nessuna traduzione trovata per: {filename}")
