import sys
import pygame

# Inicjalizacja i ustawienia
pygame.init()
pygame.font.init()
SZEROKOSC, WYSOKOSC = 400, 450
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
zegar = pygame.time.Clock()

# Kolory      R   G  B
kolor_tla = (255, 0, 0)  # jasnoszary





""" ! ruszamy dopiero pod koniec zajęć !
wesoly = pygame.image.load('happy.jpg')
wesoly = pygame.transform.scale(wesoly, (150, 150))
neutralny = pygame.image.load('neutral.jpg')
neutralny = pygame.transform.scale(neutralny, (150, 150))
smutny = pygame.image.load('sad.jpg')
smutny = pygame.transform.scale(smutny, (150, 150))
"""

# Główna pętla gry
koniec_gry = False
while koniec_gry is not True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                koniec_gry = True
        elif zdarzenie.type == pygame.QUIT:
            koniec_gry = True
    ekran.fill(kolor_tla)


    """ ! ruszamy dopiero pod koniec zajęć !
    nastroj = tamagotchi.poziom_glodu + tamagotchi.poziom_szczescia
    if nastroj > 120:
        ekran.blit(wesoly, (125, 135))
    elif nastroj > 60:
        ekran.blit(neutralny, (125, 135))
    else:
        ekran.blit(smutny, (125, 135))
    """
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
