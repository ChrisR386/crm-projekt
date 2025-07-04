# Dein Kundenmanagement-System

# Dictionary zum Speichern der Kunden
# Schlüssel = Kundenname, Wert = weiteres Dictionary mit Details wie E-Mail und Telefon
kunden = {}

# Funktion zum Anzeigen aller Kunden
def kunden_anzeigen():
    if not kunden:
        print("Der Katalog ist leer.")
        return

    print("\n--- Deine Kundenliste ---")
    for name, details in kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

# Test (kannst du später entfernen oder einkommentieren)
kunden_anzeigen()
