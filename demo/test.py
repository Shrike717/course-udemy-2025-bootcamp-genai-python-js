import csv

# Schreiben einer CSV-Datei
with open("daten.csv", "w", newline="") as file:
    writer = csv.writer(file)  # Erstellt einen CSV-Writer
    writer.writerow(["Name", "Alter", "Stadt"])  # Kopfzeile
    writer.writerow(["Alice", 30, "Berlin"])
    writer.writerow(["Bob", 25, "München"])

# Lesen einer CSV-Datei
with open("daten.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Gibt jede Zeile als Liste aus

# Schreiben als Dictionary
with open("personen.csv", "w", newline="") as file:
    fieldnames = ["Name", "Alter", "Stadt"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Schreibt die Kopfzeile
    writer.writerow({"Name": "Charlie", "Alter": 35, "Stadt": "Hamburg"})
    writer.writerow({"Name": "Dana", "Alter": 28, "Stadt": "Köln"})

# Lesen als Dictionary
with open("personen.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], "-", row["Alter"], "-", row["Stadt"])
