from dataclasses import dataclass
from typing import List

import requests

headers = {
    "Accept": "application/json"
}


@dataclass
class Rate:
    currency: str
    code: str
    bid: float
    ask: float


def get_rates():
    data = requests.get(
        "http://api.nbp.pl/api/exchangerates/tables/C",
        headers=headers
    )
    return [Rate(**d) for d in data.json()[0]["rates"]]


def print_shorts(rates: List[Rate]):
    print("Dostępne waluty:")
    print(", ".join([r.code for r in rates]))


def ask_user_for_choices():
    short = input("Jaką walutę chcesz kupic? ")
    how_many = input(f"Ile chcesz kupic {short}? ")
    return short, int(how_many)


def calculate(rates: List[Rate], short: str, how_many: int):
    rate = [r for r in rates if r.code == short][0]

    # rate = []
    # for r in rates:
    #     if r.code == short:
    #         rate.append(r)
    # rate = rate[0]
    #
    # rate = None
    # for r in rates:
    #     if r.code == short:
    #         rate = r
    #
    result = how_many * rate.ask
    return result


def main():
    rates = get_rates()
    print_shorts(rates)
    short, how_many = ask_user_for_choices()
    result = calculate(rates, short, how_many)
    print(f"Koszt to {result} PLN")


if __name__ == "__main__":
    main()
