
import pygame as pg
import random

import herramientas as h
import constantes as c
import sonidos as s

from clases.proyectiles import Proyectiles

from setup import PANTALLA

class Boss(pg.sprite.Sprite):
    def __init__(self, player, lista_proyectiles, all_sprites):
        super().__init__()

        self.acciones = h.cerebro_animacion
        self.rect = self.acciones[0].get_rect()
        self.borde_superior, self.borde_inferior, self.borde_izquierdo, self.borde_derecho = h.crear_bordes(self.rect)

        self.rect.x = c.ANCHO/2  
        self.rect.y = 0
        self.velocidad = 4

        #### SELF LISTA_PROYECT #####
        self.lista_proyectiles = lista_proyectiles
        self.all_sprites = all_sprites

        ###### MOVIMIENTO ######
        self.player = player
        self.probabilidad_movimiento = 0.5
        self.current_time = 0
        self.cooldown_animacion = 5000
        self.ultimo_tiempo = 0

        self.i = 0
        self.cond = True

        self.salud = 25

    def update(self):
        if self.salud > 91: i = 0
        elif self.salud > 78: i = 1
        elif self.salud > 65: i = 2
        elif self.salud > 52: i = 3
        elif self.salud > 39: i = 4
        elif self.salud > 26: i = 5
        elif self.salud > 13: i = 6
        elif self.salud > 0: i = 0

        self.current_time = pg.time.get_ticks()

        if self.current_time - self.ultimo_tiempo >= self.cooldown_animacion:
            self.i = random.randint(0, 1)
            self.ultimo_tiempo = self.current_time
        PANTALLA.blit(self.acciones[self.i], self.rect)
        PANTALLA.blit(h.lista_barra_de_vida_boss[i], (250,0))
        self.shoot()


        self.rect.x += self.velocidad

        if self.rect.right >= c.ANCHO:
            self.velocidad = -4
        elif self.rect.left <= 0:
            self.velocidad = 4

    def shoot(self):
        if self.rect.x == self.player.rect.centerx:
            for i in range(8):
                x = self.rect.centerx + random.randint(-20, 20)  # Posición x aleatoria
                y = self.rect.y  # Posición y del Boss
                proyectil = Proyectiles(h.cerebro_shoot, x, y, 0, 3)
                self.lista_proyectiles.add(proyectil)
                self.all_sprites.add(proyectil)

    def recibir_daño(self):
        self.salud -= 1
        if self.salud == 0:
            s.sonido_muerte_boss.play()
            pg.time.delay(200)


