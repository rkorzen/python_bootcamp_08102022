from modul_a import hello_world
# import waluty

from waluty import headers

# print(waluty.headers)
print(headers)
hello_world()

class Square:
    a = 1 # atrybut klasowy

if __name__ == "__main__":
    s = Square()  # instancja, obiekt danej klasy
    s2 = Square()
    print(s.a)
    print(s2.a)

    Square.a = 10  # tu ustawiam dla całej klasy

    print(s.a)
    print(s2.a)

    s.a = 20  # ustawiam dla instancji - dla konkretnego obiektu
    s.__class__.a

    print(s.a)
    print(s.__class__.a)
    print(s2.a)

