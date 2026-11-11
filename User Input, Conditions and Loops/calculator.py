# DIT IS DE VERANDERING VOOR DE GITHUB_OPDRACHT!!!
try:

    getal1 =int(input("geef een getal 1 in: "))
    getal2 = int(input("geef een getal 2 in: "))

    berekening = input("geef een berekening in (+,-,/,*): ")

    if berekening == "+":
        print(getal1 + getal2)
    elif berekening == "-":
        print(getal1 - getal2)
    elif berekening == "/":
        print(getal1 / getal2)
    elif berekening == "*":
        print(getal1 * getal2)
    else:
        print("ongeldige berekening ")

except ValueError:
    print("geef een getal in")
except ZeroDivisionError:
    print("deelbaar door nul is niet toegestaan:")

# DIT IS DE VERANDERING VOOR DE GITHUB_OPDRACHT!!!
