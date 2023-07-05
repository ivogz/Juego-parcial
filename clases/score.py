import pygame as pg

import constantes as c

from setup import PANTALLA

class Score(pg.sprite.Sprite):
    def __init__(self, tamaño, ):
        super().__init__()

        self.puntuacion = 0

        self.fuente = pg.font.SysFont("serif", tamaño)
        self.surface = self.fuente.render(("Score: " + str(self.puntuacion)), True, c.BLANCO)
        self.rect = self.surface.get_rect()
        self.rect.midtop = (c.ANCHO - 60, 0)

    def update(self):
        self.surface = self.fuente.render(("Score: " + str(self.puntuacion)), True, c.BLANCO)
        PANTALLA.blit(self.surface, self.rect)

    def aumentar_score(self):
        self.puntuacion += 10

    def reducir_score(self):
        self.puntuacion -= 10