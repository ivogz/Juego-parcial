
import pygame as pg
import random

import herramientas as h
import constantes as c

from setup import PANTALLA

class Enemigo(pg.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.image = h.diablito_sprite
        self.rect = self.image.get_rect()
        self.borde_superior, self.borde_inferior, self.borde_izquierdo, self.borde_derecho = h.crear_bordes(self.rect)

        self.rect.x = random.choice([-40, c.ANCHO])  
        self.rect.y = random.randrange(-40, c.ALTO)
        self.velocidad = 0

        self.player = player
        self.probabilidad_movimiento = random.random()

        self.salud = 1

    def update(self):

        PANTALLA.blit(self.image, self.rect)

        if random.random() > self.probabilidad_movimiento:
            if self.player.rect.y > self.rect.y:
                self.rect.y += self.velocidad
            elif self.player.rect.y < self.rect.y:
                self.rect.y -= self.velocidad

            if self.player.rect.x > self.rect.x:
                self.rect.x += self.velocidad
            elif self.player.rect.x < self.rect.x:
                self.rect.x -= self.velocidad

        # if self.salud == 0:
        #     pass


class Diablito(Enemigo):
    def __init__(self, player):
        super().__init__(player)

        self.image = h.diablito_sprite
        self.velocidad = random.randrange(1,4)
        self.salud = 2


        






