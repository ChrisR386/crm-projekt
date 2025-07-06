import json
import re

# Globale Variable für Kundendaten
kunden = {}

# Konstanten
DATEINAME = "kunden.json"

def katalog_laden():
    """
    Lädt die Kundendaten aus der JSON-Datei in die globale Variable 'kunden'.

    Falls die Datei nicht existiert oder beschädigt ist, wird ein leerer Katalog gestartet.
    """
    global kunden
    try:
        with open(DATEINAME, "r", encoding="utf-8") as f:
            kunden = json.load(f)
        print(f"{len(kunden)} Kunden erfolgreich geladen.")
    except FileNotFoundError:
        print("Keine bestehende Datei gefunden. Starte mit leerem Kundenkatalog.")
    except json.JSONDecodeError:
        print("Fehler beim Laden der Datei. Datei ist beschädigt oder leer.")
    except Exception as e:
        print(f"Unerwarteter Fehler beim Laden: {e}")

def katalog_speichern():
    """
    Speichert die aktuelle Kundendatenbank in einer JSON-Datei.

    Gibt eine Erfolgsmeldung aus oder informiert bei Fehlern.
    """
    try:
        with open(DATEINAME, "w", encoding="utf-8") as f:
            json.dump(kunden, f, indent=4, ensure_ascii=False)
        print("Kundendaten erfolgreich gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der Daten: {e}")

def kunden_anzeigen():
    """
    Zeigt alle Kunden mit Name, E-Mail und Telefonnummer an.

    Gibt eine Meldung aus, wenn der Katalog leer ist.
    """
    if not kunden:
        print("Der Katalog ist leer.")
        return

    print("\n--- Deine Kundenliste ---")
    for name, details in kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def is_valid_email(email):
    """
    Prüft, ob die E-Mail-Adresse einem einfachen Regex-Muster entspricht.

    Args:
        email (str): Die zu überprüfende E-Mail-Adresse.

    Returns:
        bool: True, wenn gültig, sonst False.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_telefon(telefon):
    """
    Prüft, ob die Telefonnummer nur aus Ziffern besteht.

    Args:
        telefon (str): Die Telefonnummer als String.

    Returns:
        bool: True, wenn nur Ziffern, sonst False.
    """
    return telefon.isdigit()

def kunde_hinzufuegen():
    """
    Fragt den Benutzer nach Kundendaten, validiert sie und fügt den Kunden zum Katalog hinzu.

    Gibt Fehler aus, falls Name schon existiert oder Eingaben ungültig sind.
    """
    print("\n--- Kunden hinzufügen ---")
    name = input("Name des Kunden: ").strip()
    if not name:
        print("Fehler: Name darf nicht leer sein.")
        return

    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return

    email = input("E-Mail des Kunden: ").strip()
    if not is_valid_email(email):
        print("Fehler: Ungültiges E-Mail-Format.")
        return

    telefon = input("Telefonnummer des Kunden (nur Ziffern): ").strip()
    if not is_valid_telefon(telefon):
        print("Fehler: Telefonnummer darf nur Ziffern enthalten.")
        return

    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")

def kunde_suchen():
    """
    Sucht Kunden nach einem Suchbegriff in Name oder E-Mail (case-insensitive).

    Zeigt alle passenden Kunden an oder eine Meldung, wenn keine gefunden wurden.
    """
    print("\n--- Kunden suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff (Name oder E-Mail) ein: ").lower()
    gefundene_kunden = {}

    for name, details in kunden.items():
        if suchbegriff in name.lower() or suchbegriff in details.get('email', '').lower():
            gefundene_kunden[name] = details

    if not gefundene_kunden:
        print(f"Keine Kunden gefunden, die '{suchbegriff}' im Namen oder in der E-Mail enthalten.")
        return

    print(f"\n--- Gefundene Kunden für '{suchbegriff}' ---")
    for name, details in gefundene_kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_loeschen():
    """
    Löscht einen Kunden aus dem Katalog nach Namen, wenn bestätigt.

    Gibt Fehlermeldung aus, falls Kunde nicht gefunden wird.
    """
    print("\n--- Kunden löschen ---")
    name = input("Name des Kunden, der gelöscht werden soll: ").strip()

    if name not in kunden:
        print(f"Kunde '{name}' wurde nicht gefunden.")
        return

    bestaetigung = input(f"Bist du sicher, dass du '{name}' löschen möchtest? (ja/nein): ").lower()
    if bestaetigung == "ja":
        del kunden[name]
        print(f"Kunde '{name}' wurde gelöscht.")
    else:
        print("Löschen abgebrochen.")

def zeige_menue():
    """
    Zeigt das Hauptmenü mit allen Optionen an.
    """
    print("\n--- CRM Menü ---")
    print("1. Kunde hinzufügen")
    print("2. Kunden anzeigen")
    print("3. Kunde suchen")
    print("4. Kunde löschen")
    print("5. Speichern")
    print("6. Beenden")
    print("----------------")

def main():
    """
    Hauptfunktion, die das Programm steuert.

    Lädt den Katalog, zeigt das Menü und führt die Benutzerwahl aus,
    bis das Programm beendet wird.
    """
    katalog_laden()
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ").strip()

        if wahl == '1':
            kunde_hinzufuegen()
        elif wahl == '2':
            kunden_anzeigen()
        elif wahl == '3':
            kunde_suchen()
        elif wahl == '4':
            kunde_loeschen()
        elif wahl == '5':
            katalog_speichern()
        elif wahl == '6':
            print("Programm wird beendet. Bis bald!")
            katalog_speichern()
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
