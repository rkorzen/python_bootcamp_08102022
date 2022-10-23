"""

Napisz program, który będzie realizował proste działania matematyczne.

$ python kalkulator.py

> Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]: 1
> Podaj liczbę 1: 2
> Podaj liczbę 2: 3
Wynik to: 5

"""


def get_data() -> tuple[str, int, int]:  # 3.10
    operacja = input("Jaką operację chcesz wykona? [1-dodaj, 2-odejmowanie, 3-mnożenie, 4-dzielenie]:")
    a = int(input(f"Podaj liczbę 1"))
    b = int(input("Podaj liczbę 2"))
    return operacja, a, b



def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float or str:
    if b == 0:
        return "Nie dziel przez zero"
    return a / b


operations = {
    "1": add,
    "2": sub,
    "3": mul,
    "4": div
}


def kalkulator(operacja: str, a: int, b: int) -> int or str or float:  # 3.10
    try:
        wynik = operations[operacja](a, b)
    except KeyError:
        wynik = "Nieokreślona operacja"
    return wynik


if __name__ == "__main__":
    op, a, b = get_data()
    assert kalkulator("1", 3, 4) == "Nieokreślona operacja"
