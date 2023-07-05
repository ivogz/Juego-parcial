import pygame as pg
import random

import herramientas as h
import constantes as c

from setup import PANTALLA

class Flor(pg.sprite.Sprite):
    def __init__(self, plataforma, imagen):
        super().__init__()

        
        self.image = imagen  
        self.rect = self.image.get_rect()
        self.image.set_colorkey(c.BLANCO)
        self.rect.bottom = plataforma.rect.top + 2
        self.rect.left = plataforma.rect.x + random.randrange(plataforma.rect.width - self.rect.width)

    def update(self):
        PANTALLA.blit(self.image, self.rect)

class Flor_azul(Flor):
    def __init__(self, plataforma):
        super().__init__(plataforma, h.planta_azul)
        

class Flor_vida(Flor):
    
    def __init__(self, plataforma):
        super().__init__(plataforma, h.planta_vida)
        

class Flor_verde(Flor):
    def __init__(self, plataforma):
        super().__init__(plataforma, h.planta_verde)
        

class Flor_negra(Flor):
    def __init__(self, plataforma):
        super().__init__(plataforma, h.planta_negra)
        

class Flor_lila(Flor):
    def __init__(self, plataforma):
        super().__init__(plataforma, h.planta_lila)
        


