
print()
print("A")
print("A", 1, 2, 3, 4, 5)
print("A", 1, 2, 3, 4, 5, "-")
print("A", 1, 2, 3, 4, 5, sep="-")
print(help(print))

def my_print(*args, sep=" "):
    if not args:
        print()
    else:
        print(sep.join([str(i) for i in args]))

my_print()
my_print("A")
my_print("A", 1, 2, 3, 4, 5)
my_print("A", 1, 2, 3, 4, 5, "-")
my_print("A", 1, 2, 3, 4, 5, sep="-")