import pygame as pg
import constantes as c
from setup import PANTALLA

class Proyectiles(pg.sprite.Sprite):
    def __init__(self, lista_animacion, x, y, velocidad_en_x, velocidad_en_y):
        super().__init__()

        self.animacion = lista_animacion
        self.image = lista_animacion[0]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.velocidad_y = velocidad_en_y
        self.velocidad_x = velocidad_en_x
        
        # Animación
        self.contador_animacion = 0
        self.animacion_cooldown = 280  # Cooldown de 5 segundos en milisegundos
        self.ultimo_update = 0  # Tiempo del último update en milisegundos

    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        if self.rect.bottom < 0 or self.rect.bottom > c.ANCHO or self.rect.top < 0 or self.rect.top > c.ALTO:
            self.kill()

        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - self.ultimo_update >= self.animacion_cooldown:
            self.contador_animacion += 1
            self.ultimo_update = tiempo_actual

        if self.contador_animacion < len(self.animacion):
            PANTALLA.blit(self.animacion[self.contador_animacion], self.rect)

        if self.contador_animacion >= len(self.animacion) - 1:
            self.contador_animacion = 0

