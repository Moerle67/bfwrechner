from number import Number

def menue():
    print("Wähle aus")
    print("Dez -> Bin (1)")
    print("Bin -> Dez (2)")
    return input("Ende (0):")

def deztobin():
    zahl1 = Number()
    anzahl = 1
    tipp = input(f"{anzahl}. Binär für {zahl1}: ")
    while tipp!="":
        if tipp==zahl1.get_bin() or tipp.replace("1", "I")==zahl1.get_bin():
            print("Richtig")
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