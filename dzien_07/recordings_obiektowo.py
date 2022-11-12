import sys
import json

class Record:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


def get_file_name():
    file_name = "recordings.json"
    if len(sys.argv ) > 1:
        file_name = sys.argv[1]
    return file_name


def add_record(recordings):
    # tytul: The Wall
    # artysta: Pink Floyd
    # rok wydania: 1979

    title = input("tytuł: ")
    artist = input("artysta: ")
    year = input("rok wydania: ")

    record = Record(
        title=title,
        artist=artist,
        year=year
    )

    recordings.append(record)

def show_records(recordings):
    max_artist_len = get_longest(recordings, 'artist')
    max_title_len = get_longest(recordings, 'title')
    for i, rec in enumerate(recordings, start=1):
        print(f"- [{i}] {rec.artist:{max_artist_len}} - {rec.title:{max_title_len}} ({rec.year})")

def get_recordings(file_name):
    try:
        with open(file_name) as f:
            recordings = json.load(f)
            recordings = [Record(**d) for d in recordings]
            print(recordings)
    except FileNotFoundError:
        recordings = []

    return recordings

def main():
    file_name = get_file_name()
    recordings = get_recordings(file_name)
    while True:

        option = input("Co chcesz zrobić? [d - dodaj, w - wypisz, q - zakończ] ")

        if option == "d":
            add_record(recordings)
            # poberanie danych
            # zapis
        elif option == "w":
            show_records(recordings)
            # odczyt
            # wypisanie danych
        elif option == "q":
            print(f"Koniec sesji. Dane zapisane w {file_name}")
            with open(file_name, "w") as f:
                json.dump([x.__dict__ for x in recordings], f)
            break

def get_longest(collection, key):
    """

    :param collection: list of dicts [{"artist": "xxx","title": "xssdfwdf"}, ...]
    :param key: key from dict ex: 'artist'
    :return: int - len of longest value for key in dicts from collection
    """
    # dane = []
    # for d in collection:
    #     dane.append(len(d[key]))
    # return max(dane)
    if collection:
        return max([len(getattr(d, key)) for d in collection])


if __name__ == "__main__":

    main()
    # recordings = [
    #     {"title": "aa", "artist": "bb", "year": 1980},
    #     {"title": "adddddsda sdsd", "artist": "bbdsdsd sdsdsdsd", "year": 2021},
    # ]
    # show_records(recordings)
    # print(get_recordings("recordings.json"))
    #
    # class Record:
    #     def __init__(self, title, artist, year):
    #         self.title = title
    #         self.artist = artist
    #         self.year = year
    #
    # d =  {"title": "aa", "artist": "bb", "year": 1980}
    # # title="aa", artist="bb", year=1980
    # print(**d)
    # print(title="aa")
    # d = dict(title="aa", artist="bb", year=1980)
    # r = Record(**d)
    # print(r, r.__dict__)
    # # [<__main__.Record object at 0x10cd97d30>]