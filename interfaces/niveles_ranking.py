import pygame as pg
from interfaces.boton import Button
from interfaces.boton_menu import boton_menu

import herramientas as h
import constantes as c

class Niveles_ranking():
    def __init__(self, pantalla):
    
        self.fondo = h.mapa_intro
        self.pantalla = pantalla

        ### CREO LAS INSTANCIAS DE LOS BOTONES ###

        self.boton_nivel_1 = Button(320, 250, h.boton_nivel_1, 1)
        self.boton_nivel_2 = Button(640, 350, h.boton_nivel_2, 1)
        self.boton_nivel_3 = Button(980,  250, h.boton_nivel_3, 1)
        self.boton_nivel_4 = Button(426,  520, h.boton_nivel_4, 1)
        self.boton_nivel_5 = Button(854,  520, h.boton_nivel_5, 1) 
        self.boton_menu = boton_menu

        ## AGREGO TODOS LOS BOTONES A LA LISTA
        self.botones_nivel = [self.boton_nivel_1, self.boton_nivel_2, self.boton_nivel_3, self.boton_nivel_4, self.boton_nivel_5]
        self.botones = [self.boton_nivel_1, self.boton_nivel_2, self.boton_nivel_3, self.boton_nivel_4, self.boton_nivel_5, self.boton_menu]

    def update(self):

        self.pantalla.blit(self.fondo, (0,0))

        for boton in self.botones:
            boton.draw(self.pantalla)

        pg.display.update()


    def btn_nivel_1(self):
            return self.boton_nivel_1.draw(self.pantalla)
    
    def btn_nivel_2(self):
            return self.boton_nivel_2.draw(self.pantalla)

    def btn_nivel_3(self):
            return self.boton_nivel_3.draw(self.pantalla)
    
    def btn_nivel_4(self):
            return self.boton_nivel_4.draw(self.pantalla)
    
    def btn_nivel_5(self):
            return self.boton_nivel_5.draw(self.pantalla)
        
    def btn_menu(self):
        return self.boton_menu.draw(self.pantalla)
    