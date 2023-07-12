import pygame as pg
from interfaces.boton import Button
from interfaces.boton_menu import boton_menu

import herramientas as h
import sonidos as s

class Settings():
    def __init__(self, pantalla):
    
        self.fondo = h.mapa_intro
        self.pantalla = pantalla

        ### CREO LAS INSTANCIAS DE LOS BOTONES ###
        self.boton_volume_mute = Button(640, 280, h.boton_volume_mute, 1)
        self.boton_volume_mas = Button(960,  280, h.boton_volume_mas, 1)
        self.boton_volume_menos = Button(320,  280, h.boton_volume_menos, 1)
        self.boton_menu = boton_menu

        self.boton_volume_mute_effects = Button(640, 500, pg.transform.scale(h.boton_volume_mute, (80, 80)), 1)
        self.boton_volume_mas_effects = Button(960,  500, pg.transform.scale(h.boton_volume_mas, (80, 80)), 1)
        self.boton_volume_menos_effects = Button(320,  500, pg.transform.scale(h.boton_volume_menos, (80, 80)), 1)


        ## AGREGO TODOS LOS BOTONES A LA LISTA
        self.botones = [self.boton_volume_mute, self.boton_volume_mas, self.boton_volume_menos, self.boton_menu, self.boton_volume_mas_effects, self.boton_volume_menos_effects, self.boton_volume_mute_effects]

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
    
    ###   EFECTOS   ###
    
    def btn_volume_mute_effects(self):
        return self.boton_volume_mute_effects.draw(self.pantalla)
    
    def btn_volume_mas_effects(self):
        return self.boton_volume_mas_effects.draw(self.pantalla)
    
    def btn_volume_menos_effects(self):
        return self.boton_volume_menos_effects.draw(self.pantalla)