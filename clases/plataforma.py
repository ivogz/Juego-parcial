import pygame as pg
import constantes as c
import herramientas as h
from setup import PANTALLA

class Plataforma(pg.sprite.Sprite):
    def __init__(self, x_inicial, y_inicial, rectangulo):
        super().__init__()

        self.rect = rectangulo
        self.rect.centery = y_inicial
        self.rect.centerx = x_inicial
        self.tiene_flor = False


class Mini_isla(Plataforma):
    def __init__(self, x_inicial, y_inicial, rectangulo, imagen):
        super().__init__(x_inicial, y_inicial, rectangulo)

        self.image = imagen
        self.image = pg.transform.scale(self.image, (self.rect.width, self.rect.height))

    def update(self,):
        PANTALLA.blit(self.image, self.rect)


