import sys
import pygame
from Tamagotchi import Tamagotchi

# Inicjalizacja i ustawienia
tamagotchi = Tamagotchi()
pygame.init()
pygame.font.init()
SZEROKOSC, WYSOKOSC = 400, 450
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
zegar = pygame.time.Clock()

# Kolory      R   G  B
kolor_tla = (150, 150, 150)
KOLOR_CZERWONY = (255, 0, 0)
KOLOR_CZARNY = (0, 0, 0)
KOLOR_BIALY = (255, 255, 255)
KOLOR_ZIELONY = (0, 255, 0)
KOLOR_ZOLTY = (255, 255, 0)

# Czcionka
CZCIONKA = pygame.font.SysFont("Comic Sans", 20)


# Funkcja pomocnicza
def okresl_kolor(poziom):
    if poziom > 75:
        return KOLOR_ZIELONY
    if 30 <= poziom <= 75:
        return KOLOR_ZOLTY
    return KOLOR_CZERWONY


wesoly = pygame.image.load('tamagotchi/happy.jpg')
wesoly = pygame.transform.scale(wesoly, (150, 150))
neutralny = pygame.image.load('tamagotchi/neutral.jpg')
neutralny = pygame.transform.scale(neutralny, (150, 150))
smutny = pygame.image.load('tamagotchi/sad.jpg')
smutny = pygame.transform.scale(smutny, (150, 150))


# Główna pętla gry
koniec_gry = False
while koniec_gry is not True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                koniec_gry = True
        elif zdarzenie.type == pygame.QUIT:
            koniec_gry = True
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            if not tamagotchi.przegrana:
                if przycisk_nakarm.collidepoint(zdarzenie.pos):
                    tamagotchi.nakarm()
                elif przycisk_pobaw.collidepoint(zdarzenie.pos):
                    tamagotchi.pobaw_sie()
            elif tamagotchi.przegrana:
                if przycisk_restart.collidepoint(zdarzenie.pos):
                    tamagotchi = Tamagotchi()

    tamagotchi.aktualizuj()

    ekran.fill(kolor_tla)
    # Inferfejs
    ## pasek szczęścia
    kolor_szczescie = okresl_kolor(tamagotchi.poziom_szczescia)
    pygame.draw.rect(ekran, kolor_szczescie, pygame.Rect(50, 50, tamagotchi.poziom_szczescia*2, 20))
    tekst_szczescie = CZCIONKA.render("Poziom szczęścia", True, KOLOR_CZARNY)
    ekran.blit(tekst_szczescie, (50, 20))


    ## pasek głodu
    kolor_glod = okresl_kolor(tamagotchi.poziom_glodu)
    pygame.draw.rect(ekran, kolor_glod, pygame.Rect(50, 100, tamagotchi.poziom_glodu*2, 20))
    tekst_glod = CZCIONKA.render("Poziom głodu", True, KOLOR_CZARNY)
    ekran.blit(tekst_glod, (50, 70))


    ## przyciski Nakarm i Pobaw się
    przycisk_nakarm = pygame.Rect(215, 300, 150, 50)
    przycisk_pobaw = pygame.Rect(25, 300, 150, 50)
    pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_nakarm, 3)
    pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_pobaw, 3)

    ## tekst przycisków
    tekst_nakarm = CZCIONKA.render("Nakarm", True, KOLOR_CZARNY)
    tekst_pobaw = CZCIONKA.render("Pobaw się", True, KOLOR_CZARNY)
    ekran.blit(tekst_pobaw, (60, 310))
    ekran.blit(tekst_nakarm, (245, 310))

    ## interfejs końca gry
    if tamagotchi.przegrana:
        przycisk_restart = pygame.Rect(50, 380, 300, 50)
        pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_restart, 3)

        tekst_restart = CZCIONKA.render("Spróbuj jeszcze raz", True, KOLOR_CZARNY)
        ekran.blit(tekst_restart, (90, 390))




    nastroj = tamagotchi.poziom_glodu + tamagotchi.poziom_szczescia
    if nastroj > 120:
        ekran.blit(wesoly, (125, 135))
    elif nastroj > 60:
        ekran.blit(neutralny, (125, 135))
    else:
        ekran.blit(smutny, (125, 135))

    if tamagotchi.przegrana:
        tekst_koniec_gry = CZCIONKA.render("Koniec gry!", True, KOLOR_CZARNY)
        ekran.blit(tekst_koniec_gry, (SZEROKOSC//2-tekst_koniec_gry.get_width()//2,WYSOKOSC//2+25))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
