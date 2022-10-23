
a = 1  # a jest w przestrzeni globalnej

def foo():
    print("a widziane z funkcji foo", a)
    b = 2  # b jest w przestrzeni lokalnej funkcji foo
    print(locals())

def foo2():
    # global a
    a = 2  # tworzę a w przestrzeni lokalnej
    print("a widziane z funkcji foo2", a)
    print(locals())


foo()
foo2()
print("a widziane z głownego modułu", a)
# print(b) # b nie ma w przestrzeni globalnej