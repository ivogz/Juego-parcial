import pygame as pg
from clases.all_sprites import *

from setup import *

import herramientas as h
import constantes as c



#FONDO
fondo = pg.image.load(map_1)
fondo = pg.transform.scale(fondo, c.TAMAÑO_PANTALLA)

### SE CREAN TODAS LAS PLATAFORMAS
isla_1 = Mini_isla(c.ANCHO//4, c.ALTO//2, pg.Rect(0,0, c.ANCHO//2, 40), h.isla1)
isla_2 = Mini_isla(1000, 500, pg.Rect(0,0, 150, 20), h.isla1)
isla_3 = Mini_isla(130, 500, pg.Rect(0,0, 150, 20), h.isla1)
isla_4 = Mini_isla(130, 180, pg.Rect(0,0, 150, 20), h.isla1)
isla_5 = Mini_isla(1000, 180, pg.Rect(0,0, 150, 20), h.isla1)


#     #Añado las plataformas a todas las plataformas
all_plataformas.add(isla_1)
all_plataformas.add(isla_2)
all_plataformas.add(isla_3)
all_plataformas.add(isla_4)
all_plataformas.add(isla_5)
# all_plataformas.add(plataforma_base)

#     #añado todas las plataformas a todos los sprites
for plataforma in all_plataformas:
    all_sprites.add(plataforma)


def level_1():
    
    PANTALLA.blit(fondo, (0,0))
    PANTALLA.blit(piso_map_1, (0,c.ALTO -90))
    
    # acercar_enemigos(player.rect , all_enemigos)
    crear_enemigos(5)
    creacion_flores(2)
    
    all_sprites.update() 