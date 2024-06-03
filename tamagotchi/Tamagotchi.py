class Tamagotchi:
    def __init__(self) -> None:
        self.maks_poziom = 100
        self.poziom_glodu = 50
        self.poziom_szczescia = 50
        self.przegrana = False

    def nakarm(self):
        self.poziom_glodu += 10
        if self.poziom_glodu > self.maks_poziom:
            self.poziom_glodu = self.maks_poziom

    def pobaw_sie(self):
        self.poziom_szczescia += 10
        self.poziom_szczescia = min(self.poziom_szczescia, self.maks_poziom)

    def aktualizuj(self):
        if self.przegrana:
            return

        self.poziom_glodu -= 0.1
        self.poziom_szczescia -= 0.1

        # sprawdzamy czy nastąpił koniec gry
        if self.poziom_szczescia <= 0 or self.poziom_glodu <= 0:
            self.przegrana = True
