import pygame as pg
from interfaces.boton import Button

import herramientas as h

class Intro():
    def __init__(self, pantalla):
    
        self.fondo = h.mapa_intro
        self.pantalla = pantalla

        ### CREO LAS INSTANCIAS DE LOS BOTONES ###
        self.boton_play = Button(640, 200, h.boton_play, 1)
        self.boton_settings = Button(640,  350, h.boton_settings, 1)
        self.boton_exit = Button(640,  500, h.boton_exit, 1)
        self.boton_ranking = Button(900,  500, h.boton_ranking, 1)


        ## AGREGO TODOS LOS BOTONES A LA LISTA
        self.botones = [self.boton_play, self.boton_settings, self.boton_exit, self.boton_ranking]

    def update(self):

        self.pantalla.blit(self.fondo, (0,0))

        for boton in self.botones:
            boton.draw(self.pantalla)

        pg.display.update()

    def btn_play(self):
        return self.boton_play.draw(self.pantalla)
    
    def btn_settings(self):
        return self.boton_settings.draw(self.pantalla)

    def btn_exit(self):
        return self.boton_exit.draw(self.pantalla)
    
    def btn_ranking(self):
        return self.boton_ranking.draw(self.pantalla)
