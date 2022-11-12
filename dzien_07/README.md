## Rozgrzewka

### sys.argv

#### zadanie

Napisz program wczytujący plik z logami aktywności użytkowników
w systemie. Na podstawie wczytanych danych wyświetl informację o
sumarycznym czasie przebywania każdego użytkownika w systemie.
Przykład użycia:

    $ python read_logs.py logs.txt
    Czas przebywania w systemie:
    - user-1: 92 s
    - user-2: 51 s
    - user-3: 20 s

### Praca domowa z klas.

+  powtórka

## Moduły i paczki w Pythonie

#### zadanie

Utwórz następującą strukturę pakietów i modułów:

* główny pakiet `mathematica` 
* pakiet wewnętrzny `geometry`
* moduł `figures` w pakiecie geometry z funkcjami `square_area` oraz `triangle_area`
* pakiet wewnętrzny `algebra`
* moduł `matrices` w pakiecie `algebra` z funkcjami `add_matrices` i `sub_matrices`
* główny pakiet `tests`
* moduł `test_geometry` testujący funkcje geometryczne
* moduł `test_algebra` testujący funkcje algebraiczne

## Biblioteka standardowa

### os

    getcwd
    chdir

### Path
    
    path.exist
    path.mkdir(exist_ok=True)
    path.open

    
### Pickle, JSON


#### zadanie

Napisz program obsługujący bazę danych płyt winylowych
 
W bazie danych przechowuj dane takie tytuł, artysta, rok wydania

Skorzystaj z modułu `json`.

    Przykład użycia:
    $ python recordings.py
    
    Co chcesz zrobić? [d - dodaj, w - wypisz, q - zakończ] d
    
    tytul: The Man with the Horn    
    artysta: Miles Davis 
    Rok urodzenia: 1981

    Co chcesz zrobić? [d - dodaj, w - wypisz, q - zakończ] w

    Pracownicy:
    - [1] The Man with the Horn (1981)

    Co chcesz zrobić? [d - dodaj, w - wypisz, q - zakończ] d

    tytul: The Wall
    artysta: Pink Floyd 
    Rok urodzenia: 1979

    Co chcesz zrobić? [d - dodaj, w - wypisz, q - zakończ] w

    Pracownicy:
    - [1] Miles Davis - The Man with the Horn (1981)
    - [2] Pink Floyd  - The Wall              (1980)

    Co chcesz zrobić? [d - dodaj, w - wypisz, q - zakończ] q

    Koniec sesji. Dane zapisane w c://users/alx/muzyka/recordings.json

Opcje rozbudowy:

- Dodanie wyboru pliku źródłowego 
- Dodanie sortowania po tytule, artyście, roku w nodze wyświetlania

## re

### Wyrażenia regularne

### Metody

* `re.match`

* `re.findall`

Szukamy ile razy "AT"

```python
import re
text = "ATTAGAGACCTTAAGGATGAAAC"
print(re.findall("AT", text))

```

Wszystkie wystąpienia AT lub AC

```python
print(re.findall("A[TC]", text))

```

Pierwsze słowa

```python
target_string = """Szukam zawsze i wszędzie
Pierwszego co tylko będzie
Słowa bo boli głowa"""

# two groups enclosed in separate ( and ) bracket
result = re.findall(r"^\w+", target_string, re.MULTILINE)
```

ostatnie

```
result = re.findall(r"\w+$", target_string, re.MULTILINE)
```

* `re.search`

```python
import re

text = "ATTAGAGACCTTAAGGATGAAAC"


r = re.search("AT", text)
print(r.group())
print(r.groups)


r = re.search("AT", text)

print(r.groups())

```

    - `groups`

```python
    import re

    target_string = "The price of PINEAPPLE ice cream is 20"
    
    # two groups enclosed in separate ( and ) bracket
    result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)
    
    # Extract matching values of all groups
    print(result.groups())
    # Output ('PINEAPPLE', '20')
    
    # Extract match value of group 1
    print(result.group(1))
    # Output 'PINEAPPLE'
    
    # Extract match value of group 2
    print(result.group(2))
    # Output 20
```

#### zadanie

Napisz program znajdujący w dostarczonym pliku wszystkie
wystąpienia:
* kodów pocztowych - 12-123
* adresów email - test@email.com
* dat - 12 Jan 1990
Skorzystaj z modułu re.

## tkinter


Napisz program z graficznym interfejsem użytkownika (GUI) do
obliczania kosztów przejazdu na zadanym dystansie na podstawie
spalania samochodu oraz ceny paliwa.
Skorzystaj z modułu tkinter.


# PIP

## requests  / urllib.request

### Przykład 

API pogodowe

```python

import json
import urllib.request
from collections import namedtuple


MY_KEY = "BAEVLKZKT7EZHTJYCRXYSRDCR"

Weather = namedtuple('Weather', ['location', 'temperature', 'icon', 'humidity'])

def get_location_weather(city):
    with urllib.request.urlopen(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={MY_KEY}&contentType=json') as f:
        result = json.loads(f.read())#.decode('utf-8'))
        return Weather(
            location=result['resolvedAddress'],
            temperature=result['days'][0]['temp'],
            icon=result['days'][0]['icon'],
            humidity=result['days'][0]['humidity'],
        )


if __name__ == '__main__':

    weather = get_location_weather("Berlin")
    print(f'Pogoda w {weather.location}:')
    print(f'- temperatura: {weather.temperature:.2f}°C')
    print(f'- ikona: {weather.icon}')
    print(f'- wilgotność: {weather.humidity}%')

```

#### zadanie

Kalkulator NBP
