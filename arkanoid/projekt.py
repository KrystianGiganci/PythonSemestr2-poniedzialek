import pygame
from Platforma import Platforma
from Kulka import Kulka

# wysokość i szerokość ekranu
SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

# ustawienia pygame
pygame.init()

# obiekty ekranu, zegara i tła
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

    # wyświetlanie tła
    ekran.blit(obraz_tla, (0, 0))

    # wyświetlanie platformy i kulki
    ekran.blit(platforma.obraz, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
