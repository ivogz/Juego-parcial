import pygame as pg
from interfaces.boton import Button
from interfaces.boton_menu import boton_menu

import herramientas as h

class Settings():
    def __init__(self, pantalla):
    
        self.fondo = h.mapa_intro
        self.pantalla = pantalla

        ### CREO LAS INSTANCIAS DE LOS BOTONES ###
        self.boton_volume_mute = Button(640, 360, h.boton_volume_mute, 1)
        self.boton_volume_mas = Button(960,  360, h.boton_volume_mas, 1)
        self.boton_volume_menos = Button(320,  360, h.boton_volume_menos, 1)
        self.boton_menu = boton_menu


        ## AGREGO TODOS LOS BOTONES A LA LISTA
        self.botones = [self.boton_volume_mute, self.boton_volume_mas, self.boton_volume_menos, self.boton_menu]

    def update(self):

        self.pantalla.blit(self.fondo, (0,0))

        for boton in self.botones:
            boton.draw(self.pantalla)

        pg.display.update()

    def btn_menu(self):
        return self.boton_menu.draw(self.pantalla)
    
    def btn_volume_mute(self):
        return self.boton_volume_mute.draw(self.pantalla)
    
    def btn_volume_mas(self):
        return self.boton_volume_mas.draw(self.pantalla)
    
    def btn_volume_menos(self):
        return self.boton_volume_menos.draw(self.pantalla)