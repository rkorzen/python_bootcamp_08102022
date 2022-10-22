# przypomniene

lista = [1, 2, 3, 4, "a"]
tupla = ("a", "b")


print(tupla[1])

# słownik

pusty_slownik = {}
pusty_slownik_2 = dict()

# dodawanie wartosci

litery = {}
litery["a"] = 1

print(litery)

litery = {'a': 1, "b": 2}

print(litery["b"])
litery["b"] = 3
print(litery["b"])

# litery od b - czasem tak sie mowi
litery["b"] = litery["b"] + 1
litery["b"] += 1

print(litery["b"])

# print(litery["c"])  # KeyError: 'c'

litery["c"] = 0
litery["c"] += 1

try:
    print(litery["d"])
except KeyError as e:
    print("Nie ma takiego klucza")
    print(e, type(e))


print(litery.get("d", 0))

# litery["d"] = 10
print("xxxx", litery)
litery.get("d", 1000) + 1
print(litery)
# powyższa linijka to skrót dla czegoś takiego

if "e" in litery:
    litery["e"] += 1
else:
    litery["e"] = 0

# inna możliwa forma

try:
    litery["e"] += 1
except:
    litery["e"] = 0

