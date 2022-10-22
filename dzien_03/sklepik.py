"""
Napisz program wyliczający kwotę należną za zakupiony towar na
podstawie podanej przez użytkownika wagi i nazwy produktu. Do
przechowywania informacji o cenie za kilogram danego produktu
użyj słownika. Wypisz wszystkie dostępne produkty w sklepie.

Przykład działania:

ver 1.

$ python sklepik.py

Witaj w warzywniaku.
Oferujemy:

- marchew: 3.00 PLN / kg
- ziemniaki: 5.00 PLN / kg
...

Co chcesz kupic? marchew
ile chcesz kupic - marchew? 2.5

Należy się: 7.50 PLN

Dziękujemy! Zapraszamy ponownie.


ver dalsze.

1. Umożliwienie zakupu większe ilości towarów (while True)
2. Stan magazynowy - żeby nie kupi więcje niż mamy
    a) powiększanie stanu
    b) dodawanie nowych produktów



"""

ceny = {
    "marchew": 2.5,
    "cebula": 2.2,
    "ziemniaki": 3.01
}

magazyn = {
    "marchew": 5,
    "cebula": 5,
    "ziemniaki": 5
}

print("Witaj w naszym Warzywniaku!")

while True:
    tryb = input("Rodzaj pracy: m-magazyn, k-kasa, z-zakończ")
    if tryb == "k":

        print("Oferujemy: ")
        print()

        for pr, cena in ceny.items():
            print(f" - {pr:30}: {cena:5.2f} PLN/kg")

        koszt = 0
        while True:
            produkt = input("Co chcesz kupic? (Enter by zakończyc)")
            if produkt == "":
                break
            waga = float(input(f"Ile chcesz kupic ({produkt}): "))

            if waga > magazyn[produkt]:
                print(f"Przepraszam mam tylko {magazyn[produkt]} kg {produkt}")
            else:
                koszt += waga * ceny[produkt]

        if koszt:
            print(f"Należy się: {koszt:.2f} PLN")
        else:
            print("Może innym razem ... ")
    elif tryb == "m":
        while True:
            produkt = input("Co chcesz dodac? (Enter by zakonczyc dodawanie)")
            if not produkt:
                break
            ile = int(input(f"Ile chces dodac {produkt}: "))
            magazyn[produkt] += ile  #  powiekszenie stanu

        print(magazyn)


