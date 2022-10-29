#
# print()
# print("A")
# print("A", 1, 2, 3, 4, 5)
# print("A", 1, 2, 3, 4, 5, "-")
# print("A", 1, 2, 3, 4, 5, sep="-")
# print(help(print))
#
# def my_print(*args, sep=" "):
#     if not args:
#         print()
#     else:
#         print(sep.join([str(i) for i in args]))
#
# my_print()
# my_print("A")
# my_print("A", 1, 2, 3, 4, 5)
# my_print("A", 1, 2, 3, 4, 5, "-")
# my_print("A", 1, 2, 3, 4, 5, sep="-")
#
#
# x,y = 1, 2
# f"{x} {y}"
#
# "{} {}".format(1, 2)
#
# "{a} {b}".format(a=1, b=2)



print("$a cos tam".replace("$a", "Ala"))



assert formatuj("$a $b $d") == "$a $b $d"
assert formatuj("$a $b $d", b=10) == "$a 10 $d"
assert formatuj("$a $b $d", a=1, b=2, c=20, d=30) == "1 2 30"
assert formatuj("$a $b", a=1, b=2, c=20, d=30) == "1 2"

# v2
assert formatuj("$a $b", "$a $d", a=1, b=2, c=20, d=30) == """1 2
1 30"""