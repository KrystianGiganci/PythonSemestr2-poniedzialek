import pygame
import random
import time
from Kierunek import Kierunek
from Waz import Waz
from Jablko import Jablko
from Segment import Segment

# szerokość i wysokość ekranu
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

# stworzenie tla
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))

# ustawienia
pygame.init()
# obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

# Wąż
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
event_timer = 200
pygame.time.set_timer(PORUSZ_WEZEM, event_timer)

# jabłka
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_w or zdarzenie.key == pygame.K_UP:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_s or zdarzenie.key == pygame.K_DOWN:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_a or zdarzenie.key == pygame.K_LEFT:
                waz.zmien_kierunek(Kierunek.LEWO)
            if zdarzenie.key == pygame.K_d or zdarzenie.key == pygame.K_RIGHT:
                waz.zmien_kierunek(Kierunek.PRAWO)
            if zdarzenie.key == pygame.K_o:
                event_timer += 10
                pygame.time.set_timer(PORUSZ_WEZEM, event_timer)
            if zdarzenie.key == pygame.K_p:
                event_timer -= 10
                pygame.time.set_timer(PORUSZ_WEZEM, event_timer)

        elif zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem is not None:
        # print("Mniam niam mniam")
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka.add(jablko)

    # rysowanie tła
    ekran.blit(tlo, (0, 0))
    # rysowanie glłowy węża
    ekran.blit(waz.obraz, waz.rect)
    # rysowanie jablek
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)
    # rysowanie semgentów
    for segment in waz.segmenty:
        ekran.blit(segment.obraz, segment.pozycja)

    # spradzenie czy gra sie skonczyla
    if waz.sprawdz_kolizje():
        gra_dziala = False

    pygame.display.flip()
    zegar.tick(30)

time.sleep(3)
pygame.quit()
