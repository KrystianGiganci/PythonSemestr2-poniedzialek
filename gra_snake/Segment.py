import pygame
import copy


class Segment(pygame.sprite.Sprite):
    def __init__(self, kolor, pozycja):
        super().__init__()
        self.obraz = pygame.image.load("images/segment.png")
        self.pozycja = pygame.Rect(-32, -32, 32, 32)
        self.ostatania_pozycja = None

    def przesun(self, nowa_pozycja):
        self.ostatania_pozycja = copy.deepcopy(self.pozycja)
        self.pozycja = copy.deepcopy(nowa_pozycja)
