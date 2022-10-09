
suma_liczb = 0
ilosc_zapytan = 0

max_number = None
min_number = None


while True:
    dane = input("Podaj liczbę (lub k by zakończyć): ")

    if dane == "k":
        break

    dane = int(dane)
    suma_liczb  = suma_liczb + dane
    ilosc_zapytan += 1

    if max_number is None or dane > max_number:
        max_number = dane

    if min_number is None or dane < min_number:
        min_number = dane

print("Średnia wynosi", suma_liczb / ilosc_zapytan)
print("Max: ", max_number)
print("Min: ", min_number)