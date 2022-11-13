from main import spalanie, koszt

def get_data():
    per_100 = float(input("Ile samochód pali na 100 km? "))
    dystans = float(input("Jaki dystans chcesz przejechac? "))
    koszt_litra = float(input("Jaki jest koszt litra paliwa? "))

    return per_100, dystans, koszt_litra

def main():
    per_100, dystans, koszta_litra = get_data()
    ile_spali = spalanie(per_100, dystans)
    koszt_calkowity = koszt(ile_spali, koszta_litra)

    print(f"Koszt przejazdu na dystansie {dystans} wyniesie {koszt_calkowity:.2f}")

if __name__ == "__main__":
    main()