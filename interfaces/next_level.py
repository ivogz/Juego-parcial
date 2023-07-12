import pygame as pg
import json

from interfaces.boton import Button

import herramientas as h
import constantes as c

from setup import PANTALLA

class Next_level():
    def __init__(self, pantalla, ):
    
        self.pantalla = pantalla

    def update(self):

        PANTALLA.fill(c.NEGRO)
        PANTALLA.blit(h.level_complete, (300,180))

        pg.display.update()

        pg.time.delay(3000)

    def guardar_score(self, usuario, tiempo, state):

        usuario = {
        "Nombre": usuario,
        "tiempo": tiempo
        }
        # JSON
        with open(f"Ranking/level_{state}.json", "a") as f:
            json.dump(usuario, f, indent = 4 , ensure_ascii=False)

        # TXT

        # with open(f"Ranking/level_{state}.txt", "a") as f:
        #     f.write(f"{usuario}; tiempo de {tiempo} segundos")

