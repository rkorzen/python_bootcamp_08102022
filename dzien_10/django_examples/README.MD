
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



## Migracje

### wykonanie:

    python manage.py migrate

### utworzenie migracji:

    python manage.py makemigrations

### podejrzenie stanu wykonania

    python manage.py showmigrations

## Query

    Book.objects.all()
    Book.objects.first()
    Book.objects.last()
    Book.objects.get(id=1)
    Book.objects.get(title="Pan Tadeusz")
    Book.objects.get(title__iexact="pan tadeusz")
    Book.objects.filter(title__iendswith="tadeusz")

