# funkcje

# zmienna reprezentujaca kwadrat
# kwadrat = 2  # bok kwadratu

# kwadrat reprezentuje lista. Na indeksie 0 jest bok
# a na indeksie 1 jest kolor
# kwadrat = [2, "czerwony"]  # bok kwadratu

kwadrat = {
    "bok": 2,
    "kolor": "czerwony"
}

kw2 = {
    "bok": 4,
    "kolor": "czarny"
}

kwadrat["bok"]

def obwod(kwadrat): # bok to argument funkcji
    """Zwraca obwod kwadratu o boku `bok`

    kwadrat: słownik zawierajaca klucz - bok
    """
    bok = kwadrat["bok"]  # do wybierania zawsze nawiasy []
    # w nawiasie albo pozycja - jeśli to jest lista, str, tupla
    # albo klucz jeśli to jest słownil
    return bok * 4

def pole(kwadrat):
    bok = kwadrat["bok"]
    return bok ** 2



# printy pokazuja cos uzytkownikowi

print(obwod(kwadrat))  # wywołuje z argumentem kwadrat
print(pole(kwadrat))

print(pole(kw2))


# napiszmy testy - oparte o assert
# to są przypadki testowe
assert obwod({"bok": 2, "kolor": "czerwony"}) == 8
assert obwod({"bok": 3, "kolor": "zólty"}) == 12
assert obwod({"bok": 10,"kolor":  "niebieski"}) == 40
assert obwod({"bok": 0, "kolor": "czarny"}) == 0
# assert obwod(-1) == ? to taka decyzja biznesowa
# czy rzucac wyjatek czy cos innego...

# czyli tutaj też stosujemy slowniki
# TODO: poprawic testy
# assert pole([2, "czerwony"]) == 4
# assert pole([3, "zólty"]) == 9
# assert pole([10, "niebieski"]) == 100
# assert pole([0, "czarny"]) == 0


