from setup import *
import pygame as pg, sys

import herramientas as h
import constantes as c

from niveles.nivel_1 import Nivel_1
from niveles.nivel_2 import Nivel_2
from niveles.nivel_3 import Nivel_3
from niveles.nivel_4 import Nivel_4
from niveles.nivel_5 import Nivel_5

from interfaces.intro import Intro
from interfaces.selector_de_niveles import Selector_niveles
from interfaces.settings import Settings
from interfaces.menu_pause import Menu_pause

from modo import *

class GameState():
    def __init__(self):

        self.state = "intro"
        self.state_actual = None

        self.interfaz_intro = Intro(PANTALLA)
        self.selector_niveles = Selector_niveles(PANTALLA)
        self.interfaz_settings = Settings(PANTALLA)
        self.menu_pause = Menu_pause(PANTALLA)

        self.nivel_uno = Nivel_1()
        self.nivel_uno.activar_nivel()
        self.nivel_dos = Nivel_2()
        self.nivel_tres = Nivel_3()
        self.nivel_cuatro = Nivel_4()
        self.nivel_cinco = Nivel_5()
        self.nivel_cinco.activar_nivel()

        self.bandera_pause = False
        self.bandera_boss_5 = False

    def intro(self):


        for event in pg.event.get():
            self.cerrar_con_cruz(event)

        if self.interfaz_intro.btn_play():
            self.state = "selector de niveles"

        if self.interfaz_intro.btn_settings():
            self.state = "settings"

        if self.interfaz_intro.btn_exit():
            pg.quit()
            sys.exit()

        ## PONER OBJETOS EN PANTALLA
        self.interfaz_intro.update()
        pg.display.update()

    def settings(self):

        for event in pg.event.get():
            self.cerrar_con_cruz(event)

        if self.selector_niveles.btn_menu():
            self.state = "intro"

        self.interfaz_settings.update()
        pg.display.update()

    def selector_de_niveles(self):

        if self.nivel_uno.acceso == True:
            self.selector_niveles.activar_nivel(1)
        if self.nivel_dos.acceso == True:
            self.selector_niveles.activar_nivel(2)
        if self.nivel_tres.acceso == True:
            self.selector_niveles.activar_nivel(3)
        if self.nivel_cuatro.acceso == True:
            self.selector_niveles.activar_nivel(4)
        if self.nivel_cinco.acceso == True:
            self.selector_niveles.activar_nivel(5)

        for event in pg.event.get():
            self.cerrar_con_cruz(event)


        if self.selector_niveles.btn_nivel_1():
            self.state = "nivel_1"
            self.recrear_nivel()
            
        elif self.selector_niveles.btn_nivel_2():
            self.state = "nivel_2"
            if self.nivel_dos.acceso == True:
                self.recrear_nivel()
                self.nivel_dos.activar_nivel()
            else: self.recrear_nivel()

        elif self.selector_niveles.btn_nivel_3():
            self.state = "nivel_3"
            if self.nivel_tres.acceso == True:
                self.recrear_nivel()
                self.nivel_tres.activar_nivel()
            else: self.recrear_nivel()

        elif self.selector_niveles.btn_nivel_4():
            self.state = "nivel_4"
            if self.nivel_cuatro.acceso == True:
                self.recrear_nivel()
                self.nivel_cuatro.activar_nivel()
            else: self.nivel_cuatro = Nivel_4()

        elif self.selector_niveles.btn_nivel_5():
            self.state = "nivel_5"
            if self.nivel_cinco.acceso == True:
                self.recrear_nivel()
                self.nivel_cinco.activar_nivel()
            else: self.nivel_cinco = Nivel_5()

        elif self.selector_niveles.btn_menu():
            self.state = "intro"

        self.selector_niveles.update()
        pg.display.update()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        
        elif self.state == "selector de niveles":
            self.selector_de_niveles()

        elif self.state == "settings":
            self.settings()

        elif self.state == "nivel_1":
            self.state_actual = self.nivel_uno
            self.main_game()
            if self.state_actual.score.puntuacion >= 30:
                self.nivel_dos.activar_nivel()
                self.state = "nivel_2"

        elif self.state == "nivel_2":
            self.state_actual = self.nivel_dos
            self.main_game()
            if self.state_actual.score.puntuacion >= 30:
                self.nivel_tres.activar_nivel()
                self.state = "nivel_3"

        elif self.state == "nivel_3":
            self.state_actual = self.nivel_tres
            self.main_game()
            if self.state_actual.score.puntuacion >= 30:
                self.nivel_cuatro.activar_nivel()
                self.state = "nivel_4"

        elif self.state == "nivel_4":
            self.state_actual = self.nivel_cuatro
            self.main_game()
            if self.state_actual.score.puntuacion >= 30:
                self.nivel_cinco.activar_nivel()
                self.state = "nivel_5"

        elif self.state == "nivel_5":
            
            self.state_actual = self.nivel_cinco
            self.main_game()
            if self.state_actual.score.puntuacion >= 20 and self.bandera_boss_5 == False:
                self.state_actual.spawn_boss()
                self.bandera_boss_5 = True

    def main_game(self):

        clock.tick(c.FPS)

        for event in pg.event.get():
            self.cerrar_con_cruz(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F12:
                    cambiar_modo()
                elif event.key == pg.K_ESCAPE:
                    self.pause()

        self.comprobar_pause()

        self.state_actual.update()

        if self.state_actual.player.salud == 0:
            PANTALLA.fill(c.GRIS)
            PANTALLA.blit(h.game_over, (320,180))
            pg.display.update()
            pg.time.delay(5000)
            self.state = "intro"
            
        if get_mode() == True:
            for sprite in self.state_actual.all_sprites:
                pg.draw.rect(PANTALLA, c.GRIS , sprite, 2)

        pg.display.update()
        

######################################################################

        ####### FUNCIONES ####

    def cerrar_con_cruz(self, event):
        if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def comprobar_pause(self):

        while self.bandera_pause:

            for event in pg.event.get():
                self.cerrar_con_cruz(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.pause()

            if self.menu_pause.btn_play_pausa():
                self.pause()
            elif self.menu_pause.btn_menu_pausa():
                self.pause()
                self.state = "intro"
                pg.time.delay(200)
            elif self.menu_pause.btn_replay_pausa():
                self.pause()
                self.recrear_nivel()

            self.menu_pause.update()
            pg.display.update()

    
    def pause(self):
        self.bandera_pause = not self.bandera_pause

    def recrear_nivel(self):
        if self.state == "nivel_1":
            self.nivel_uno = Nivel_1()
        elif self.state == "nivel_2":
            self.nivel_dos = Nivel_2()
        elif self.state == "nivel_3":
            self.nivel_tres == Nivel_3()
        elif self.state == "nivel_4":
            self.nivel_tres == Nivel_4()
        elif self.state == "nivel_5":
            self.nivel_tres == Nivel_5()
