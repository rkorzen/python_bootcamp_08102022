# definiowanie prostej funkcji

def nazwa_funkcji():
    print("Coś sobie robię...")


def funkcja_z_1_arg(arg):
    print("Coś sobie robię z ...", arg)


def suma_trzech_liczb(a: int, b: int, c: int) -> int:
    return a + b + c

print(dir(suma_trzech_liczb))
print(suma_trzech_liczb.__annotations__)
# wywołanie funkcji


nazwa_funkcji()
funkcja_z_1_arg(1)
funkcja_z_1_arg(arg="cos tam")
wynik = suma_trzech_liczb(1, 2, 3)
print("w=", wynik)
suma_trzech_liczb("a", "B", "C")
# suma_trzech_liczb("a", 13, "C")
