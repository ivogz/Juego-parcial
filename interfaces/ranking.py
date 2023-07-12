import pygame as pg
import json 

import constantes as c

from setup import PANTALLA

from interfaces.boton_menu import boton_menu

class Ranking():
    def __init__(self):
        self.lista_ranking = []
        self.primera_altura = 200
        self.pos = 1
        self.fuente = pg.font.Font(None, 36)

    def update(self, nivel):

        PANTALLA.fill(c.NEGRO)
        try:
            with open(f"Ranking\level_1.json", encoding='utf-8') as f:
                data = json.load(f)
                for dicc in data:
                    self.lista_ranking.append(dicc)
        except:
            print("HUBO UN ERROR CON LOS RANKING")

        try:
            for dicc in self.lista_ranking:
                print (dicc)
                texto = f"{self.pos} - {dicc['Nombre']} completado en {dicc['tiempo']}"

                superficie_texto = self.fuente.render(texto, True, c.BLANCO)
                PANTALLA.blit(superficie_texto, (460, self.primera_altura + 100))
        except:
            print("NO HAY RANKING")

        

        boton_menu.draw(PANTALLA)
        pg.display.update()

    def btn_menu(self):
        return self.boton_menu.draw(self.pantalla)