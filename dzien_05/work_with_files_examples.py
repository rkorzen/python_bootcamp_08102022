# print(help(open))

f = open("data/emails.txt")
print(f)
f.close()

f = open("../README.md")

for i, line in enumerate(f, start=1):
    print(i, line, end="")
print()
print(f.closed)
f.close()
print()
print(f.closed)


with open("../README.md") as g:  #  context manager
    for i, line in enumerate(g, start=1):
        print(i, line, end="")

# ty wychodzę z context managera
print()
print(g.closed)
# tu zadziałął close

with open("aaaa.txt", "r") as f:
    f.write("\nAA\n")
    f.write("BB")

