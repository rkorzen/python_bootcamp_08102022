# Markdown  H1
## H2
### H3
#### H4
##### H5
###### H6

* Item 1
* Item 2


1. Item 1
2. Item 2

| A | B |
|---|---|
 | 1 | 2 |


```python
x = 1
print(x)

def foo(): print(10)

```

# Pycharm

## Przydatne skróty

* formatowanie kodu:

```commandline
ctrl + alt  + l  # (L - małe)
```

* dodanie lub usunięcie komentarza

```commandline
ctrl + /
```

# Python CD

## Pętla while

```python

while <warunek>:
    blok instrukcji


```
patrz przyklady_while.py


### zadanie 1 petla

Napisz program, który wypisze kwadraty 100 pierwszych liczb naturalnych.

### zadanie 2 while

Napisz program, który zapyta użytkownika o kolejne liczby i zwróci ich średnią

Podaj liczbę (lub k by zakończyć): 3
Podaj liczbę (lub k by zakończyć): 3
Podaj liczbę (lub k by zakończyć): 4
Podaj liczbę (lub k by zakończyć): 4
Podaj liczbę (lub k by zakończyć): k

Średnia wynosi: 3.5

Min: 3
Max: 4

### zadanie 2a while

Drukuj w pętli co drugą liczbę z zakresu 1-100

1
3
5

W pętli drukuj z tego zakrsu tylko liczby podzielne przez 7

### Zadanie 3 while

Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o wymiarach 10 x 10

Użytkownik wprowadza informacje o ruchu (góra, dół, lewo, prawo - np wasd)

Po ruchu otrzymuje informacje o tym czy jest bliżej czy dalej (ciepło zimno)

Wyjście poza plansze oznacza koniec gry - przegrana

Po znalezieniu skarbu wypisz liczbe ruchów wykorzystanych przez użytkownika

Dodatkowe modyfikacje:

- po wykonaniu wiekszej liczby krokow niz minimalna wartość x 2 umieśc skarb w innym miejscu
- z prawdopodobienstwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku


# SLACK -  zapisy

https://docs.google.com/document/d/1DGIIznTFFGNaXmac0pXAiUndnY1DFUWN5hd_TJbfdec/edit?usp=sharing


# Collections

Ogólnie - wprowadzamy nawiasy []
Pozwalają one wybierać z kolekcji określone elementy.

Elementy te okresla się na dwa sposoby - index, klucz
index - pozycja w kolekcji licznona liczbami calkowitymi od 0 w górę

## Napisy

"Ala ma kota"

Typ niemutowalny

Patrz kolekcje_przyklad.py


## Tupla - krotka

typ niemutowalny

(1, 2, 3, "a")


## lista

[]

[1, 2, 3, 2, 2, "a", 2.0]


### Zadanie

1. Utwórz tuple zawierająca 10 elemtów (mogą byc róznego typu)

printy:
- wybierz 2 element
- przedostatni
- od trzeciego do siódmego (włacznie)
- co trzeci element
- odwróć kolejnośc tupli

2. utwórz napis i powtórz te kroki

3. Utwórrz liste 10 elementowa

- dołącz element do listy                    # append
- wsadz nowy element przed 3 indexem         # insert(3, "x")
- zmien wartosc na indeksie 5                # lista[5] = 2
- zrzuć ostatnią wartość (pop)               # lista.pop()



### zadanie
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Użyj listy. Skorzystaj z funkcji: sum, len, min, max

x = []

x = list()


### zadanie

masz zadaną listę liczb - np [1, 2, 3, -1, -2, 10, 20, -400, 200, 24]

Napisz program zliczający występienia liczb dodatnich i ujemnych

