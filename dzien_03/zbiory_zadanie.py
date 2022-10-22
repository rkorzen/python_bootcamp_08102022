"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych
przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami
parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
iloczynu.

"""

liczby_parzyste_od_0_do_100 = set(range(0, 101, 2))

liczby = set()

while True:
    liczba = input("Podaj liczbę lub k by zakończyc: ")
    if liczba == "k":
        break
    # liczba = int(liczba)
    try:
        liczby.add(int(liczba))
    except ValueError:
        print("Zła wartośc!!! Wpisz liczbę całkowitą lub literę 'k'")

print(f"Unikalnych liczb: {len(liczby)}")
print(f"Z czego parzystych od 0 do 100: {len(liczby & liczby_parzyste_od_0_do_100)}")

