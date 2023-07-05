
import constantes as c
import pygame as pg
from herramientas import *



##########################################

# Este modulo inicia el display

##########################################

pg.init()
# pg.mixer.init()
# pg.mixer.music.set_volume(0.7)
clock = pg.time.Clock()

pg.display.set_caption("JUEGO")
PANTALLA = pg.display.set_mode(c.TAMAÑO_PANTALLA)

