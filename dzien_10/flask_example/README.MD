

jesli plik nazywa sie app.py

    $ flask run

jeśli plik nazywa sie inaczej - np main.py

linux / mac

    $ export FLASK_APP=main.py
    
windows:

    $ set FLASK_APP=main.py

i potem

    $ flask run

automatyczne odswieżanie serwera po zmianach kodu
przed uruchomieniem serwera - wterminalu w sesjie gdzie uruchamiamay apke

    $ set FLASK_ENV=development

