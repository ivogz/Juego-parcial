import pygame as pg
from interfaces.boton import Button
from interfaces.boton_menu import boton_menu

import herramientas as h
import constantes as c

class Selector_niveles():
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

        self.actualizar_img_botones()

        for boton in self.botones:
            boton.draw(self.pantalla)

        pg.display.update()

    def actualizar_img_botones(self):

        for boton in self.botones_nivel:
            if boton.activado == False:
                boton.image = h.boton_nivel_bloq
            else:
                if boton == self.boton_nivel_2:
                    boton.image = h.boton_nivel_2
                if boton == self.boton_nivel_3:
                    boton.image = h.boton_nivel_3
                if boton == self.boton_nivel_4:
                    boton.image = h.boton_nivel_4
                if boton == self.boton_nivel_5:
                    boton.image = h.boton_nivel_5

    def btn_nivel_1(self):
        if self.boton_nivel_1.activado == True:
            return self.boton_nivel_1.draw(self.pantalla)
    
    def btn_nivel_2(self):
        if self.boton_nivel_2.activado == True:
            return self.boton_nivel_2.draw(self.pantalla)

    def btn_nivel_3(self):
        if self.boton_nivel_3.activado == True:
            return self.boton_nivel_3.draw(self.pantalla)
    
    def btn_nivel_4(self):
        if self.boton_nivel_4.activado == True:
            return self.boton_nivel_4.draw(self.pantalla)
    
    def btn_nivel_5(self):
        if self.boton_nivel_5.activado == True:
            return self.boton_nivel_5.draw(self.pantalla)
        
    def btn_menu(self):
        return self.boton_menu.draw(self.pantalla)
    
    def activar_nivel(self, valor):
        
        nivel = valor

        match nivel:
            case 1:
                self.boton_nivel_1.activado = True
            case 2:
                self.boton_nivel_2.activado = True
            case 3:
                self.boton_nivel_3.activado = True
            case 4:
                self.boton_nivel_4.activado = True
            case 5:
                self.boton_nivel_5.activado = True