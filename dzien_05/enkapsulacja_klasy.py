class Sejf:

    def __init__(self, dane, haslo):
        self.haslo = haslo
        self.dane = dane
    
    def pobieranie_danych(self, haslo):
        if haslo == self.haslo:
            return self.dane
        else:
            self._zniszczenie_danych()
            return None

    def _zniszczenie_danych(self):
        self.dane = None
        self.haslo = None

