import pygame as pg

from setup import PANTALLA

import constantes as c

class Cronometro (pg.sprite.Sprite):
    def __init__ (self):

        self.tiempo_inicio = 0
        self.cronometro_activo = True

        self.tiempo_transcurrido = 0

        self.fuente  =pg.font.Font(None, 48)

    def pausa_despausa(self):
        self.cronometro_activo = not self.cronometro_activo

    def reiniciar(self):
        self.tiempo_transcurrido = 0
        self.tiempo_inicio = pg.time.get_ticks()

    def obtener_tiempo(self):
        return str(self.tiempo_transcurrido // 1000)
    
    def update(self):

        if self.cronometro_activo:
            self.tiempo_transcurrido = pg.time.get_ticks() - self.tiempo_inicio
        # else:
        #     self.tiempo_transcurrido = 0


        texto = self.fuente.render(str(self.tiempo_transcurrido // 1000), True, c.BLANCO)
        PANTALLA.blit(texto, (c.ANCHO // 2 - texto.get_width() // 2, 30 - texto.get_height() // 2))
