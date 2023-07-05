import pygame as pg

import constantes as c
import herramientas as h
from setup import PANTALLA

from modo import * 

from niveles.nivel import Nivel

from clases.plataforma import Plataforma, Mini_isla



class Nivel_3(Nivel):
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
        fondo = pg.image.load(h.map_3)
        fondo = pg.transform.scale(fondo, c.TAMAÑO_PANTALLA)
        piso = h.piso_map_3

        ### SE CREAN TODAS LAS PLATAFORMAS
        isla_1 = Mini_isla(0, c.ALTO * 1/4 , pg.Rect(0,0, 500, 40), h.isla1)
        isla_2 = Mini_isla(c.ANCHO, c.ALTO * 1/4, pg.Rect(0,0, 500, 40), h.isla1)
        isla_3 = Mini_isla(c.ANCHO//2, c.ALTO//2 - 80, pg.Rect(0,0, 200, 20), h.isla1)
        isla_4 = Mini_isla(c.ANCHO, 500, pg.Rect(0,0, 900, 30), h.isla1)
        isla_5 = Mini_isla(0, 500, pg.Rect(0,0, 900, 30), h.isla1)



        #Añado las plataformas a todas las plataformas
        all_plataformas.add(isla_1, isla_2, isla_3, isla_4, isla_5)

        #añado todas las plataformas a todos los sprites
        for plataforma in all_plataformas:
            all_sprites.add(plataforma)

        super().__init__(PANTALLA, all_sprites, all_plataformas, all_flowers, all_enemigos, player_proyectiles, all_proyectiles_enemigos, fondo, piso)

        self.cantidad_enemigos = 7