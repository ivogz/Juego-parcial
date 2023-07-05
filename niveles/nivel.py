import pygame as pg
import random

import constantes as c
import herramientas as h

from modo import * 

from clases.player import Player
from clases.plataforma import Plataforma, Mini_isla
from clases.flores_powerup import Flor_vida, Flor_azul, Flor_verde, Flor_negra, Flor_lila
from clases.enemigo import Enemigo, Diablito
from clases.score import Score
from clases.boss import Boss

# from clases.proyectiles import Proyectiles

class Nivel():
    def __init__(self,
                pantalla,
                all_sprites,
                lista_plataformas,
                lista_flores,
                lista_enemigos,
                player_proyectiles,
                lista_enemigos_proyectiles,
                fondo, piso):
        
        self.pantalla = pantalla
        self.fondo = fondo
        self.piso = piso

        self.all_sprites = all_sprites
        self.plataformas = lista_plataformas
        self.enemigos = lista_enemigos
        self.flores = lista_flores
        self.player_proyectiles = player_proyectiles
        self.enemigos_proyectiles = lista_enemigos_proyectiles

        self.player = Player(lista_plataformas, player_proyectiles, all_sprites)
        self.all_sprites.add(self.player)

        self.max_flores = 2

        self.score = Score(25)
        self.all_sprites.add(self.score)

        self.plataforma_base = Plataforma(c.ANCHO // 2, c.ALTO - 52 , pg.Rect(0,0, c.ANCHO, 20))
        self.plataformas.add(self.plataforma_base)
        self.all_sprites.add(self.plataforma_base)

        ### BANDERA PERMITE EL ACCESO AL NIVEL
        self.acceso = False

        #### colision_player
        self.player_ultimo_tiempo = 0
        self.player_tiempo_cooldown = 500

        ### ENEMIGOS
        self.cantidad_enemigos = 5

    def detectar_colision_flores(self):
        colision_flor = pg.sprite.spritecollide(self.player, self.flores, True)
        if colision_flor: 
            for flower in colision_flor:
                if isinstance(flower, Flor_vida):
                    if self.player.salud <= 3:
                        self.player.salud += 1
                elif isinstance(flower, Flor_azul):
                    self.player.escudo = True
                elif isinstance(flower, Flor_negra):
                    self.player.recibir_daño()
                elif isinstance(flower, Flor_verde):
                    self.score.puntuacion += 50
    
    def comprobar_plataforma_tiene_flor(self):

        for plataforma in self.plataformas:
            colision = pg.sprite.spritecollide(plataforma, self.flores, False)
            if not colision:
                plataforma.tiene_flor = False 

    def creacion_flores(self):

        flores_disponibles = [Flor_verde, Flor_vida, Flor_negra, Flor_azul, Flor_lila]

        contador_flores = 0
        probabilidad_creacion = 0.002

        plataforma_aleatoria =  random.choice(self.plataformas.sprites())
        flor = random.choice(flores_disponibles)

        if len(self.flores) < self.max_flores and random.random() < probabilidad_creacion and plataforma_aleatoria.tiene_flor == False:
            nueva_flor = flor(plataforma_aleatoria)
            self.flores.add(nueva_flor)
            self.all_sprites.add(nueva_flor)

            plataforma_aleatoria.tiene_flor = True
            contador_flores += 1
    
    def detectar_colision_enemigo_player(self):
        tiempo_actual = pg.time.get_ticks()

        colision = pg.sprite.spritecollide(self.player, self.enemigos, False)
        if colision and tiempo_actual - self.player_ultimo_tiempo >= self.player_tiempo_cooldown:
            if self.player.escudo == False:
                self.player.salud -= 1
            elif self.player.escudo == True:
                self.player.escudo = False
            self.player_ultimo_tiempo = pg.time.get_ticks()

    def detectar_colision_proyectil_player(self):
        colision = pg.sprite.spritecollide(self.player, self.enemigos_proyectiles, True)
        if colision:
            self.player.recibir_daño()


    def crear_enemigos(self, cantidad_enemigos):
        if len(self.enemigos) < cantidad_enemigos:
            diablito = Diablito(self.player)
            self.enemigos.add(diablito)
            self.all_sprites.add(diablito)

    def detectar_daño_a_enemigos(self):
        daño_a_enemigo = pg.sprite.groupcollide(self.enemigos, self.player_proyectiles, False, True)

        for enemigo, proyectiles in daño_a_enemigo.items():
            if proyectiles:
                enemigo.salud -= 1
                if enemigo.salud <= 0:
                    self.score.aumentar_score()
                    enemigo.kill()
    
    def dibujar_hitboxes(self):
        if get_mode() == True:
            for sprite in self.all_sprites:
                pg.draw.rect(self.pantalla, c.GRIS , sprite, 2)

    def activar_nivel(self):
        self.acceso = True

    def spawn_boss(self):
            boss = Boss(self.player, self.enemigos_proyectiles, self.all_sprites)
            self.all_sprites.add(boss)
            self.enemigos.add(boss)

    def update(self):



        self.pantalla.blit(self.fondo, (0,0))
        self.pantalla.blit(self.piso, (0,c.ALTO -90))

        self.detectar_colision_enemigo_player()
        self.comprobar_plataforma_tiene_flor()
        self.detectar_colision_flores()
        self.detectar_daño_a_enemigos()

        self.crear_enemigos(self.cantidad_enemigos)
        self.creacion_flores()

        self.all_sprites.update()


