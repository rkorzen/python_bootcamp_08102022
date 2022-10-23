def second(x):
    return x[1]

sec = lambda x: x[1]
sec.__name__ = "sec"

print(second, sec)
print(second.__name__, sec.__name__)

lista = ["a5", "c0", "b1"]
print(sorted(lista, key=second))
print(sorted(lista, key=sec))
print(sorted(lista, key=lambda x: x[1]))


xxx = lambda x, y: print(x + y)
xxx(1, 2)
(lambda x, y: print(x + y))(1, 4)