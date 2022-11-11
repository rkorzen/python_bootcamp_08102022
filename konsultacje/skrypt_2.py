#        0  1  2  3
lista = [1, 2, 3, 4, 3, 3, 3, 3]
lista2 = [1, 2, 3, "a", (1, 2), [1, 2, 3, ["b", "c"]]]
tupla2 = (1, 2, 3, "a", (1, 2), [1, 2, 3, ["b", "c"]])

print(lista[0])

print(dir(lista[0]))
print(dir(lista))

x = print(1 + 10)
print(x)

# 'append', 'clear', 'copy',  'extend', , 'insert', 'pop', 'remove', 'reverse', 'sort'
# 'index', 'count' - te metody sa także w krotce, napisie

print(lista.count(3))
print(lista2)
print(tupla2)

print(lista2[5])
print(tupla2[5])

el = lista2[5]
print(el[3])

print(lista2[5][3])
print(lista2[5][3][0])
#     [1, 2, 3, ['b', 'c']][3]
#               ['b', 'c'][0]
#                'b'

# print(el_we)

lista2[0] = 10
lista2[0] += 1

lista2[5][2] += 1
print(lista2)

lista2[5][3][1] += "d"
print(lista2)

lista2[5][3][1] = lista2[5][3][1] + "d"
pusta_lista = []
slownik = {}

slownik = {"a": ["Adam", "Alojzy"], "b": ["Bartek"]}
print(slownik)

print(slownik["a"])

slownik["a"].append("Anna")

print(slownik)

print(slownik["a"])
print(slownik["a"][2])
slownik["a"][2] = "Anastazja"
print(slownik)

slownik["a"][2] += "Anna"
print(slownik)

slownik["a"][2] *= 2
slownik["a"][2] = slownik["a"][2] * 2
print(slownik)

slownik["c"] = ["Cecylia"]
print(slownik)

print(lista2)
# lista2[61] = 11 # nie moge ustawiac na nieistniejacym indexie

lista2.append(11)
print(lista2)
print(lista2[6])

slownik["b"].append("Bartek")
print(slownik)
print(list(set([1, 1, 1, 1])))
slownik["b"] = list(set(slownik["b"] ))
print(slownik)

a = [1, 1, 1, 1]
b = set(a)
c = list(b)

d = list(set([2, 3, 2, 3]))
print(tuple(d))


print(list(slownik))

print(slownik.keys())
print(slownik.values())

print("a" in slownik)
print("Adam" in slownik)

print("Adam" in slownik.values())

print(slownik.items())

imie = "Adam"
print(imie.lower()[0])
print(slownik[imie.lower()[0]])
print(imie in slownik[imie.lower()[0]])

# print(slownik["k"])
if "k" in slownik:
    print(slownik["k"])

print(slownik.get("k"))
print(slownik.get("k", ""))


print(slownik.get("a"))  # slownik["a"]
print(slownik.get("a", "dsdsdsd"))

print(help(slownik.get))


imie = "Adam"
print(imie.lower())
print(imie.lower()[0])  # "adam"[0]

c = [
    1,
    2,
    3,
    "4"
    "5"
]
print(c)

print(
    "a"
    "b"
    "c"
)

print([
    1,
    2,
    3,
])

x = (1 + 2)
print(x, type(x))

x = (1 + 2,)
print(x, type(x))

print(dir(slownik))
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
print(dir(lista2))
[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


print(len(slownik))
print(len(lista2))

# print(help(slownik.update))
#
# print(help(lista2.extend))

dane = [("d", ["Danuta", "Dorota"])]

slownik.update(dane)
print(slownik)


slownik.update({"e": ["Eliza", "Ela"]})
print(slownik)

print(dict(list(reversed(slownik.items()))))

z = {10, 1, "z", "a"}
print(len(z))
print(2 in z)
print(z)
for el in z:
    print(el)

print(2 in z)

print(dir(z))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print()
print(a & b)
print(a.intersection(b))
print()
print(a - b)
print(b - a)
print(a ^ b)

"sdsd"
b"sdsd"