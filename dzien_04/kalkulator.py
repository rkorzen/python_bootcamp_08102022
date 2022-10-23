"""

Napisz program, który będzie realizował proste działania matematyczne.

$ python kalkulator.py

> Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: 1
> Podaj liczbę 1: 2
> Podaj liczbę 2: 3
Wynik to: 5

"""

def kalkulator() -> int:
    # print("Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]:")
    operacja = input("Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]:")
    a = int(input("Podaj liczbę 1"))
    b = int(input("Podaj liczbę 2"))

    if operacja == "1":
        print(a + b)
    elif operacja == "2":
        print(a - b)
    elif operacja == "3":
        print(a * b)
    elif operacja == "4":
        print(a / b)


kalkulator()