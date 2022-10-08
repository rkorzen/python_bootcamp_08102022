miasto_a = input("Miasta A: ")
miasto_b = input("Miasta B: ")
dystans = int(input(f"Odległość pomiędzy {miasto_a}-{miasto_b}: "))
cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))

koszt = dystans * cena_paliwa / spalanie

print(f"Koszt podróży z {miasto_a} do {miasto_b} wynosi {koszt:.2f} PLN")