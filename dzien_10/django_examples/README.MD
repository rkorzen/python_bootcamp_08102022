
## instalcja

pip install django

##  django-admin

jeśli mamy folder w ktorym chcemy miec projekt to w tym folderze wydajemy polecenie:


    django-admin startproject <nazwa-wasza> .

jeśli chcemy utworzy pełną strukturę - wraz z folderem projektu:

    django-admin startproject <nazwa-wasza>

struktura

    .
    ├── README.MD
    ├── <nazwa-wasza>
    │     ├── __init__.py
    │     ├── asgi.py
    │     ├── settings.py
    │     ├── urls.py
    │     └── wsgi.py
    ├── db.sqlite3
    └── manage.py

uruchamiamy:

    python manage.py runserver



