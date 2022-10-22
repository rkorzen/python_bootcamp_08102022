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


print(dir(litery))
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print("keys", litery.keys())
print("values", litery.values())
print("items", litery.items())


for klucz in litery:
    print(klucz)


sx = dict([('a', 1), ('b', 5), ('c', 1), ('e', 1)])
print(sx)

sy = dict(a=1, b=5, c=1, e=1)
print(sy)

# czy wszystko może by wartością i kluczem?
# wartości - tak dowolne

# klucze - obiekty hashowalne - z dużym przybliżeniem możemy uznac ze chodzi o obiekty niemutowalne


d = {(1, 2): 1}

# hash - "unikalna", stałą reprezentacja - wyliczana na podstawie zawartości.
# rodzaj sumy kontrolnej.
# stałe - w sensie życia sesji interpretera

# klucze - unikalne, hashowalne

print(help(dict.pop))

klucze = [1, 2, 3]

d = dict.fromkeys(klucze, 10)
print(d)

print(d.pop(1))
print(d)

print(d.popitem())
print(d)


for k, v in litery.items():
    print(k, v)

for k in litery:
    print(k, litery[k])

print(litery.items())


# tworzenie
s = dict()
s = {1: "a", 2: "b"}

# pobieranie
s[1]
# modyfikacja
s[1] = "c"

# usuwanie
# s.pop(1)

del s[1]
print(s)