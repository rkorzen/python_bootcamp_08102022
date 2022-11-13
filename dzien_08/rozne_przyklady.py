import pprint
import random

lista = ["A", "B", "C", "D"]

print(random.random())
print(random.randint(1, 3))
print(random.randrange(start=10, step=10, stop=200))
print(random.choice(lista))
print(random.choices(lista, k=2))

print(help(random.choices))