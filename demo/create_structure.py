import os

def create_project_structure():
    folders = [
        "data",
        "docs",
        "models",
        "notebooks",
        "pipeline",
        "reports",
        "src",
        "utils"
    ]
    
    try:
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        
        # Erstelle die README.md Datei
        readme_path = "README.md"
        if not os.path.exists(readme_path):
            with open(readme_path, "w") as f:
                f.write("# Projektbeschreibung\n")
        
        print("Projektstruktur erfolgreich erstellt!")
    except Exception as e:
        print(f"Fehler: {e}")

# Beispiel für die Nutzung
create_project_structure()
