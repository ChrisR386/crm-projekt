kunden = {}  # Kunden werden hier als Dictionary gespeichert

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

def kunde_hinzufuegen():
    print("\n--- Kunden hinzufügen ---")
    name = input("Name des Kunden: ")
    email = input("E-Mail des Kunden: ")
    telefon = input("Telefonnummer des Kunden: ")

    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return

    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")

# Nur zum Testen (danach wieder auskommentieren!)
kunde_hinzufuegen()
kunden_anzeigen()