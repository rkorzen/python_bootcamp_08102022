from typing import Union, Tuple

"""

Napisz program, który będzie realizował proste działania matematyczne.

$ python kalkulator.py

> Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: 1
> Podaj liczbę 1: 2
> Podaj liczbę 2: 3
Wynik to: 5

"""


#

# def return_dict() -> dict[str, int]:
#     return {"a": 1}
# def get_data() -> Tuple[str, int, int]: # < 3.10

def get_data() -> tuple[str, int, int]:  # 3.10
    operacja = input("Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]:")
    a = int(input("Podaj liczbę 1"))
    b = int(input("Podaj liczbę 2"))
    return operacja, a, b

def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int or str:
    if b == 0:
        return "Nie dziel przez zero"
    return a / b


# def kalkulator(operacja: str, a: int, b: int) -> Union[int, str]: # < 3.10
def kalkulator(operacja: str, a: int, b: int) -> int or str:  # 3.10
    # print("Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]:")
    wynik = "Nieokreślona operacja"

    if operacja == "1":
        wynik = add(a, b)
    elif operacja == "2":
        wynik = sub(a, b)
    elif operacja == "3":
        wynik = mul(a, b)
    elif operacja == "4":
        wynik = div(a, b)
    return wynik


# kalkulator(operacja, a, b)
print(kalkulator("1", 3, 4))
