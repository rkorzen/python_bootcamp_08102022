

def funkcja(*args):
    print(args)

lista = [1,2,3]
funkcja(*lista)

funkcja(1, 2, 3, 4, 5)

def funkcja2(**kwargs):
    print(kwargs)

funkcja2(k=1, j=2)

d = {"k": 1, "j": 2}

funkcja2(**d)

print(getattr(d, 'values'))

class Foo:
    a = 1
    b = 2

x = Foo()
y = Foo()

print(x.a, y.a)
Foo.a = 10

print(x.a, y.a)



x.a = 100

print(x.a, y.a)


print(x.__dict__)

