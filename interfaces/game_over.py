import pygame as pg
from interfaces.boton import Button

import herramientas as h

class Game_Over():
    def __init__(self, pantalla):
    
        self.pantalla = pantalla

        ### CREO LAS INSTANCIAS DE LOS BOTONES ###
        self.boton_play_pausa = Button(640, 200, h.boton_play_pausa, 1)
        self.boton_replay_pausa = Button(640,  350, h.boton_replay_pausa, 1)
        self.boton_menu_pausa = Button(640,  500, h.boton_menu_pausa, 1)


        ## AGREGO TODOS LOS BOTONES A LA LISTA
        self.botones = [self.boton_play_pausa, self.boton_replay_pausa, self.boton_menu_pausa]

    def update(self):

        for boton in self.botones:
            boton.draw(self.pantalla)

        pg.display.update()

    def btn_play_pausa(self):
        return self.boton_play_pausa.draw(self.pantalla)
    
    def btn_replay_pausa(self):
        return self.boton_replay_pausa.draw(self.pantalla)

    def btn_menu_pausa(self):
        return self.boton_menu_pausa.draw(self.pantalla)