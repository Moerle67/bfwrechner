from number import Number

def menue():
    print("Wähle aus")
    print("Dez -> Bin (1)")
    print("Bin -> Dez (2)")
    return input("Ende (0): ")

def deztobin():
    # Zufallszahl erstellen
    zahl1 = Number()
    # Erfolgszähler initialisieren
    anzahl = 1
    # Erste Abfrage
    tipp = input(f"{anzahl}. Binär für {zahl1}: ")
    # Endlosschleife bis "" eingegeben wird
    while tipp!="":
        # Abfrage, gegebenfalls "1" durch "I" ersetzen
        if tipp==zahl1.get_bin() or tipp.replace("1", "I")==zahl1.get_bin():
            # Treffer
            print("Richtig")
            # Neue Zahl bestimmen
            zahl1 = Number()
            anzahl += 1
        else:
            print("Falsch")
        tipp = input(f"{anzahl}. Binär für {zahl1}: ")

choice = menue()
while choice != "0":
    match choice:
        case "1":
            deztobin()
    choice = menue()