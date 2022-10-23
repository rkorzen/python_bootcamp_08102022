def add(a, b, *args, c=1, d=2, **kwargs):
    print("kwargs", kwargs)
    print(args, type(args))
    return a + b + sum(args)


# add()
add(1, 2)
add(1, 2, 3, 4, 5, e=11, f=22)

a, b, *c = 1, 2, 3, 4, 5, 6, 7
print(a, b, c)

lista = (1, 2, 3, 4, 5, 6)
# add(10, 20, lista)
add(10, 20, *[1, 2, 3, 4, 5, 6])
add(10, 20, *lista)
add(10, 20, 1, 2, 3, 4, 5, 6)


def hello(name="Ada", age=22):
    print(name, age)

dane = dict(name="GGGG", age=333)

hello(**dane)



