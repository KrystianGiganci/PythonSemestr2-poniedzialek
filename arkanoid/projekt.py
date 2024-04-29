import pygame
from Platforma import Platforma
from Kulka import Kulka

# wysokość i szerokość ekranu
SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
ZYCIA = 3

# ustawienia pygame
pygame.init()
pygame.font.init()

# obiekty czcionki, ekranu, zegara i tła
czcionka = pygame.font.SysFont("Comic Sans MS", 24)
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('arkanoid/images/background.png')

# tworzymy platforme i kulke
platforma = Platforma()
kulka = Kulka()

# główna pętla
gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # sterowanie platformą
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)

    kulka.aktualizuj(platforma)
    platforma.aktualizuj()

    if kulka.przegrana:
        ZYCIA -= 1
        if ZYCIA <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    # wyświetlanie tła
    ekran.blit(obraz_tla, (0, 0))

    # wyświetlanie platformy i kulki
    ekran.blit(platforma.obraz, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)

    # wyświetlanie liczby żyć
    tekst = czcionka.render(f'Pozostałe życia: {ZYCIA}', False, (255, 181, 33))
    ekran.blit(tekst, (16, 16))

    pygame.display.flip()
    zegar.tick(30)
# ---------------------------------

pygame.quit()
