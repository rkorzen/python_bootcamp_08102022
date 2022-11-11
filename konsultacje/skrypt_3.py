"""
to jest docstring
"""

#
# lista = [1, 2, 3, 4, 5]
#
# lista[0]
# lista.append(6)
#
# print(lista)
#
# print(lista.pop())
# print(lista)
#
# print(lista.pop())
# print(lista)
#
# print(help(lista.pop))
#
# print(lista.pop(0))
# [1, 2, 3]
# [1, 2]
# [2, 3]
# # kolejka
# # first in  first out
#
# # stos
# # last in firist out
#
# str
# tuple
# frozenset
#
# list
#
# set  # nie ma kolejnosci. Unikalne
# dict # pary wartosci. Unikalne klucze
#
# print(dir(str))
# print(help(str.upper))
#
# 1 in {1, 2}  # add
# 1 in (1, 2)
# 1 in [1, 2]
# 1 in {1: 2, 2: 3}
# 1 in "123"
# 1 in frozenset([1, 2, 3])
#
# # funkcje

def nazwa_funkcji():  # sygnatura funkcji
    # ciało funkcji
    # 1 / 0
    return 10

print(nazwa_funkcji)
print(dir(nazwa_funkcji))
print(nazwa_funkcji.__dict__)

nazwa_funkcji.xxx = 10
nazwa_funkcji.__name__ = "zespsulem"
print(nazwa_funkcji.__name__)
print(nazwa_funkcji.__dict__)

print(dir())
print(__file__)
print(__package__)
print(__name__)

print(__doc__)

nazwa_funkcji.__dict__ = {"x": "kukułka"}
print(nazwa_funkcji())

def suma(a, b):
    # print(a + b)
    return a + b

wynik = suma(1, 3)

print(wynik)

# suma(1, 2, 3)

def foo():
    return 1, 2, 3
    print("jestem poza funkcja")

print(foo())


def bar(x):
    if x > 10:
        return x ** 2
    return x ** 0.5

# def bar(x):
#     result = x ** 2
#     if x < 10:
#         result = x ** 0.5
#     return result


def bar(x):
    if x > 10:
        return x ** 2
    else:
        return x ** 0.5


print(bar(11))

print(bar(4))

print(help(bar(1))) # help(1)


print([1, 2, 3].append(4))

x = [1, 2, 3]
print(x)
print(x.append(4))
print(x)

print(x.pop())
print(x)

def increment(x, step=1):
    return x + step

print(increment(10, 1))
print(increment(10))
print(increment(10, 10)) # -> 20
print(increment(10, step=10)) # -> 20
print(increment(x=10, step=10)) # -> 20
print(increment(step=5, x=11)) # -> 16 # zamiana kolejnosci jest mozliwa
print(increment(x=1, step=4))


def suma(a, b, cast_to_float=False):
    result = a + b
    if cast_to_float:   # if 0
        result = float(result)
    return result

print(suma(1, 2))  # cast_to_float = False
print(suma(1, 2, True))  # cast_to_float = False
print(suma(1, 2, 0))  # cast_to_float = False
print(suma(1, 2, 1))  # cast_to_float = False

print(suma(1, 2, cast_to_float=True))  # cast_to_float = False

def suma(a, b, *, cast_to_float=False, cast_to_str=False):
    result = a + b
    if cast_to_float:   # if 0
        result = float(result)
    if cast_to_str is True:
        result = str(result)
    return result

print(suma(1, 2, cast_to_float=True))
print(suma(1, 2, cast_to_float=1))
x = suma(1, 2, cast_to_str=True)
print(x, type(x))


print(1,2,3,4,5,True,"-", ";")


def suma(a, b, *reszta_argumentow, cast_to_float=False): # zwykle *args
    print(reszta_argumentow)
    result = a + b
    for el in reszta_argumentow:
        result += el
    if cast_to_float:
        result = float(result)
    return result

# print(suma(1))
print(suma(1, 2))
print(suma(1, 2, 1, 2, 4,))
print(suma(1, 2, 10))
print(suma(1, 2, 10, 10, 10, 10))
print(suma(1, 2, 10, 10, 10, 10, cast_to_float=True))
