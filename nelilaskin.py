"""nelilaskin"""
VALINTA = (input("Valitse operaatio (+, -, *, /): "))
if VALINTA == "+":
    try:
        LUKU_1 = float(input("Anna luku 1: "))
        LUKU_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Tulos: ", LUKU_1 + LUKU_2)
elif VALINTA == "-":
    try:
        LUKU_1 = float(input("Anna luku 1: "))
        LUKU_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Tulos: ", LUKU_1 - LUKU_2)
elif VALINTA == "*":
    try:
        LUKU_1 = float(input("Anna luku 1: "))
        LUKU_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Tulos: ", LUKU_1 * LUKU_2)
elif VALINTA == "/":
    try:
        LUKU_1 = float(input("Anna luku 1: "))
        LUKU_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if LUKU_2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")
        else:
            print("Tulos: ", LUKU_1 / LUKU_2)
else:
    print("Operaatiota ei ole olemassa")
