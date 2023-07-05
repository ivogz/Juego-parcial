import pygame as pg

import constantes as c
import herramientas as h
from setup import PANTALLA

from modo import * 

from niveles.nivel import Nivel

from clases.plataforma import Plataforma, Mini_isla



class Nivel_2(Nivel):
    def __init__(self):
        # Se crean todos los grupos
        all_sprites = pg.sprite.Group()
        all_plataformas = pg.sprite.Group()
        player_proyectiles = pg.sprite.Group()
        all_flowers = pg.sprite.Group()
        all_proyectiles_enemigos = pg.sprite.Group()
        all_enemigos = pg.sprite.Group()
        all_textos = pg.sprite.Group()


        #FONDO
        fondo = pg.image.load(h.map_2)
        fondo = pg.transform.scale(fondo, c.TAMAÑO_PANTALLA)
        piso = h.piso_map_2

        ### SE CREAN TODAS LAS PLATAFORMAS
        isla_1 = Mini_isla(c.ANCHO//2, c.ALTO//2 + 150, pg.Rect(0,0, 200, 40), h.isla1)
        isla_2 = Mini_isla(c.ANCHO//2, c.ALTO//2, pg.Rect(0,0, 200, 40), h.isla1)
        isla_3 = Mini_isla(c.ANCHO//2, c.ALTO//2 - 150, pg.Rect(0,0, 200, 40), h.isla1)
        isla_4 = Mini_isla(1100, 500, pg.Rect(0,0, 150, 20), h.isla1)
        isla_5 = Mini_isla(180, 500, pg.Rect(0,0, 150, 20), h.isla1)
        isla_6 = Mini_isla(180, 180, pg.Rect(0,0, 150, 20), h.isla1)
        isla_7 = Mini_isla(1100, 180, pg.Rect(0,0, 150, 20), h.isla1)


        #Añado las plataformas a todas las plataformas
        all_plataformas.add(isla_1, isla_2, isla_3, isla_4, isla_5, isla_6, isla_7)

        #añado todas las plataformas a todos los sprites
        for plataforma in all_plataformas:
            all_sprites.add(plataforma)

        super().__init__(PANTALLA, all_sprites, all_plataformas, all_flowers, all_enemigos, player_proyectiles, all_proyectiles_enemigos, fondo, piso)

        self.cantidad_enemigos = 6