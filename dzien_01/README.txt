# Podstawy

## Polecenia OS

- mkdir
- cd <nazwa>
- cd ..

## Instalacja Pythona

- https://www.python.org/

## Ogólnie o językach programowania

### Język Maszynowy

### Assemblery

mnemoniki - ADD

### Języki wyższego poziomu

- kompilowane

kod źródowy jest kompilowany

- interpretowane

- JIT - Just in Time

## Python

- język interpretowany, skryptowy, ogólnego zastosowania
- typowany silnie
- typowany dynamicznie
- bogata społeczność 
- bogata biblioteka narzędzi


### pip - manager pakietów

pip install ipython


### przydatne funkcje na poczatku

- help
- dir

help() -  interatykwna pomoc

help(print)
help(1)
help("str")  - dokumentacja obiektu

dir() -  wyświetlenie nazw z biężącej przestrzeni nazw, zasięgu (scope)
dir("napis")  - zwraca liste atrybutów i metod danego obiektu


### podstawowe typy

#### int - integer, liczby całkowite

Operacje: + - / * 
// -  dzielenie całkowite
% - reszta z dzielenia - dzielenie modulo
** - potęgowanie


##### system binarny

dwie cyfry = 1, 0

0d = 0b
1d = 1b
2d = 10b = 1 * 2 ** 1 + 0 * 2 ** 0

212d = 2 * 10**2  + 1 * 10**1  + 2 * 10 ** 0 = 11010100b


0b11 - liczba przedstawiona binarnie
0o11 - liczba ósemkowa
0x11 - liczba szesnatkowa


#### bool

wartości
False
True

operatory logiczne:
and, or, not


operatory porównania:
==
>
<
>=
<=
!=


#### float

#### complex


#### str - napis

dir("jakis napis")

#####

"%s == %d" % ("x", 10)

 "{} == {}".format("x", 10)
 "{a} == {b}".format(a="x", b=10)

najnowsza forma:
 f"{a:30} == {b:5.2f}"

'''
wiele
linijek
'''

"""
a
b
"""

f"""
{x}
"""




paragon:

nazwa waga cena
dla 3 produktów 
+ wiersza podsumowania


pomidory     10.00 kg   60.50 PLN
ogórki        5.00 kg    9.99 PLN
ser edamski   1.10 kg   17.25 PLN


### Zmienne (i STAŁE)

nazwy składają się z liter, cyfr i znaku podkreslenia
Możemy używac polskie znaki - ale lepiej tegonie robić
Najlepiej pisać kod po angielsku

źle - niezgodne z konwencja:
somevariable
someVariable
SomeVariable

dobrze:
some_variable

PEP8
https://peps.python.org/pep-0008/


### zad

Napisz program, który pobierze od użytkownika dane i wyliczy jego współczynnik BMI

### Zadanie

Napisz program, który obluczy koszty przejazdu z miasta A do B


Miasta A: Warszawa
Miasto B: Gdańsk
Dystans Warszawa-Gdańsk: 420
Cena paliwa: 7.25
Spalanie na 100 km: 10

Koszt przejazdu Warszawa-Gdańsk to 304.50 PLN
