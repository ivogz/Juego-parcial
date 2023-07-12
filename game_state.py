from setup import *
import pygame as pg, sys
import json

import herramientas as h
import constantes as c
import sonidos as s

from niveles.nivel_1 import Nivel_1
from niveles.nivel_2 import Nivel_2
from niveles.nivel_3 import Nivel_3
from niveles.nivel_4 import Nivel_4
from niveles.nivel_5 import Nivel_5

from interfaces.intro import Intro
from interfaces.selector_de_niveles import Selector_niveles
from interfaces.settings import Settings
from interfaces.menu_pause import Menu_pause
from interfaces.next_level import Next_level
from interfaces.niveles_ranking import Niveles_ranking
from interfaces.ranking import Ranking

from modo import *

class GameState():
    def __init__(self):

        self.state = "intro"
        self.state_actual = None

        self.interfaz_intro = Intro(PANTALLA)
        self.selector_niveles = Selector_niveles(PANTALLA)
        self.selector_de_ranking = Niveles_ranking(PANTALLA)
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

        self.next_level = Next_level(PANTALLA)
        self.ranking_tabla = Ranking()

        ## sonido
        self.sonido_fondo_actual = None

    def intro(self):

        s.sonido_fondo.play()

        for event in pg.event.get():
            self.cerrar_con_cruz(event)

        if self.interfaz_intro.btn_play():
            self.state = "selector de niveles"

        if self.interfaz_intro.btn_settings():
            self.state = "settings"

        if self.interfaz_intro.btn_ranking():
            self.state = "ranking"

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

        if self.interfaz_settings.btn_volume_mas():
            for sonido in s.lista_sonidos:
                volumen = sonido.get_volume()
                nuevo_volumen = volumen + 0.1
                sonido.set_volume(nuevo_volumen)

        if self.interfaz_settings.btn_volume_menos():
            for sonido in s.lista_sonidos:
                volumen = sonido.get_volume()
                nuevo_volumen = volumen - 0.1
                sonido.set_volume(nuevo_volumen)

        if self.interfaz_settings.btn_volume_mute():
            for sonido in s.lista_sonidos:
                volumen = sonido.get_volume()
                if volumen == 0:
                    sonido.set_volume(1)
                else: sonido.set_volume(0)


        self.interfaz_settings.update()
        pg.display.update()

    def ranking(self,nivel):

        for event in pg.event.get():
            self.cerrar_con_cruz(event)

        if self.selector_niveles.btn_menu():
            self.state = "intro"

        self.ranking_tabla.update(nivel)
        pg.display.update()

    def selector_ranking(self):

        for event in pg.event.get():
            self.cerrar_con_cruz(event)

        if self.selector_de_ranking.btn_menu():
            self.state = "intro"

        if self.selector_de_ranking.btn_nivel_1():
            self.state = "ranking_1"
            
        elif self.selector_de_ranking.btn_nivel_2():
            self.state = "ranking_2"

        elif self.selector_de_ranking.btn_nivel_3():
            self.state = "ranking_4"

        elif self.selector_de_ranking.btn_nivel_4():
            self.state = "ranking_4"

        elif self.selector_de_ranking.btn_nivel_5():
            self.state = "ranking_5"
        

        self.selector_de_ranking.update()
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
            self.interior_state("nivel_1", self.nivel_uno)
            
        elif self.selector_niveles.btn_nivel_2():
            self.interior_state("nivel_2", self.nivel_dos)

        elif self.selector_niveles.btn_nivel_3():
            self.interior_state("nivel_3", self.nivel_tres)

        elif self.selector_niveles.btn_nivel_4():
            self.interior_state("nivel_4", self.nivel_cuatro)

        elif self.selector_niveles.btn_nivel_5():
            self.interior_state("nivel_5", self.nivel_cinco)

        elif self.selector_niveles.btn_menu():
            self.state = "intro"

        self.selector_niveles.update()
        pg.display.update()

    def interior_state(self, state, nivel):
        self.state = state
        if nivel.acceso == True:
            self.recrear_nivel()
            nivel.activar_nivel()
        else: nivel.recrear_nivel()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
            self.aplicar_sonido_fondo(s.sonido_fondo)
        
        elif self.state == "selector de niveles":
            self.selector_de_niveles()
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "settings":
            self.settings()
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "ranking":
            self.selector_ranking()
            self.aplicar_sonido_fondo(s.sonido_fondo)
        
        elif self.state == "ranking_1":
            self.ranking(1)
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "ranking_2":
            self.ranking(2)
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "ranking_3":
            self.ranking(3)
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "ranking_4":
            self.ranking(4)
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "ranking_5":
            self.ranking(5)
            self.aplicar_sonido_fondo(s.sonido_fondo)

        elif self.state == "nivel_1":
            self.aplicar_sonido_fondo(s.sonido_juego)
            self.controlador_nivel(self.nivel_uno, "nivel_2", 75, self.nivel_dos)

        elif self.state == "nivel_2":
            self.aplicar_sonido_fondo(s.sonido_juego)
            self.controlador_nivel(self.nivel_dos, "nivel_3", 100, self.nivel_tres)

        elif self.state == "nivel_3":
            self.aplicar_sonido_fondo(s.sonido_juego)
            self.controlador_nivel(self.nivel_tres, "nivel_4", 150, self.nivel_cuatro)

        elif self.state == "nivel_4":
            self.aplicar_sonido_fondo(s.sonido_juego)
            self.controlador_nivel(self.nivel_cuatro, "nivel_5", 200, self.nivel_cinco)

        elif self.state == "nivel_5":
            self.aplicar_sonido_fondo(s.sonido_juego)
            self.state_actual = self.nivel_cinco
            self.main_game()
            
            if self.state_actual.score.puntuacion >= 100 and self.state_actual.bandera_boss_5 == False:
                self.state_actual.spawn_boss()
                self.state_actual.bandera_boss_5 = True

            if self.state_actual.bandera_boss_5 == True:    
                if self.state_actual.boss.salud == 0:
                    self.state_actual.boss.kill()
                    self.ganar()

    def controlador_nivel(self, state_actual, state_siguiente:str, puntuacion_p_pasar:int, nivel_siguiente):
        self.state_actual = state_actual
        self.main_game()
        if self.state_actual.score.puntuacion >= puntuacion_p_pasar:
            nivel_siguiente.activar_nivel()
            self.next_level.guardar_score("ivo", self.state_actual.cronometro.obtener_tiempo(), self.obtener_nivel_int())
            self.next_level.update()
            
            self.state = state_siguiente

    def ganar(self):
        PANTALLA.fill(c.GRIS)
        PANTALLA.blit(h.ganaste_img, (180,180))
        pg.display.update()
        pg.time.delay(5000)
        self.state = "intro"

    def main_game(self):

        clock.tick(c.FPS)

        for event in pg.event.get():
            self.cerrar_con_cruz(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F12:
                    cambiar_modo()
                elif event.key == pg.K_ESCAPE:
                    self.pause()
                elif event.key == pg.K_y:
                    self.state_actual.score.puntuacion += 50

        self.comprobar_pause()

        self.state_actual.update()

        if self.state_actual.player.salud == 0:
            s.sonido_muerte_player.play()
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

            self.aplicar_sonido_fondo(s.sonido_pausa)

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
            self.nivel_tres = Nivel_3()
        elif self.state == "nivel_4":
            self.nivel_cuatro = Nivel_4()
        elif self.state == "nivel_5":
            self.nivel_cinco = Nivel_5()

    def aplicar_sonido_fondo(self, sonido):

        if sonido != self.sonido_fondo_actual:
            if self.sonido_fondo_actual != None:
                self.sonido_fondo_actual.stop()
            
            sonido.play(-1)

        self.sonido_fondo_actual = sonido 

    def obtener_nivel_int(self):
        if self.state == "nivel_1":
            return "1"
        elif self.state == "nivel_2":
            return "2"
        elif self.state == "nivel_3":
            return "3"
        elif self.state == "nivel_4":
            return "4"
        elif self.state == "nivel_5":
            return "5"

    # def leer_ranking(self, nivel):

    #     ranking = True
    #     lista_ranking = []
    #     primera_altura = 200
    #     pos = 1
    #     fuente = pg.font.Font(None, 36)

    #     while ranking:
    #         PANTALLA.fill(c.NEGRO)
    #         try:
    #             with open(f"Ranking\level_{nivel}.json", encoding='utf-8') as f:
    #                 data = json.load(f)
    #                 for dicc in data:
    #                     lista_ranking.append(dicc)
    #         except:
    #             print("HUBO UN ERROR CON LOS RANKING")

    #         try:
    #             for dicc in lista_ranking:
    #                 texto = f"{pos} - {dicc['Nombre']} completado en {dicc['tiempo']}"

    #                 superficie_texto = fuente.render(texto, True, c.BLANCO)
    #                 PANTALLA.blit(superficie_texto, (460, primera_altura + 100))
    #         except:
    #             print("NO HAY RANKING")

    #         pg.display.update()