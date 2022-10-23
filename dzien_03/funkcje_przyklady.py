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

# positional aguments

# def sum(a, b, c)

# keyword arguments (step)

# def increment(value, step=1)
def increment(value: int, step: int = 1) -> int:
    return value + step

print(increment(5, 2))
print(increment(5))
print(increment(value=5, step=2))
print(increment(step=5, value=1))
print(increment(5, step=2))