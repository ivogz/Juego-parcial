import pygame as pg
import random


import constantes as c

from clases.proyectiles import Proyectiles

from clases.player import Player
from clases.plataforma import Plataforma, Mini_isla
from clases.flores_powerup import Flor_vida, Flor_azul, Flor_verde, Flor_negra, Flor_lila
from clases.enemigo import Enemigo, Diablito
from clases.score import Score
# from clases.proyectiles import Proyectiles

# Se crean todos los grupos
all_sprites = pg.sprite.Group()
all_plataformas = pg.sprite.Group()
player_proyectiles = pg.sprite.Group()
all_flowers = pg.sprite.Group()
all_proyectiles_enemigos = pg.sprite.Group()
all_enemigos = pg.sprite.Group()
all_textos = pg.sprite.Group()


# Crear la plataforma base
plataforma_base = Plataforma(0, c.ALTO - 52 , pg.Rect(0,0, c.ANCHO, 20))
all_plataformas.add(plataforma_base)

# Crear el jugador
player = Player(all_plataformas, player_proyectiles,all_sprites)
#Añade el jugador a todos los sprites
all_sprites.add(player)

# CREAR TEXTO SCORE
score = Score(25)
all_textos.add(score)
all_sprites.add(score)



# FUNCION PARA LA CREACION ALEATORIA DE FLORES EN EL ESCENARIO
def creacion_flores(max_flores):
    global all_plataformas
    global all_sprites
    global all_flowers

    flores_disponibles = [Flor_verde, Flor_vida, Flor_negra, Flor_azul, Flor_lila]

    contador_flores = 0
    probabilidad_creacion = 0.002

    plataforma_aleatoria =  random.choice(all_plataformas.sprites())
    flor = random.choice(flores_disponibles)

    if len(all_flowers) < max_flores and random.random() < probabilidad_creacion and plataforma_aleatoria.tiene_flor == False:
        nueva_flor = flor(plataforma_aleatoria)
        all_flowers.add(nueva_flor)
        all_sprites.add(nueva_flor)

        plataforma_aleatoria.tiene_flor = True
        contador_flores += 1

def comprobar_plataforma_tiene_flor():

    for plataforma in all_plataformas:
        colision = pg.sprite.spritecollide(plataforma, all_flowers, False)
        if not colision:
            plataforma.tiene_flor = False 

#DETECTA LA COLISION CON LAS FLORES Y ACTIVA UN POWERUP
def detectar_colision_flores():
    colision_flor = pg.sprite.spritecollide(player, all_flowers, True)
    if colision_flor: 
        for flower in colision_flor:
            if isinstance(flower, Flor_vida):
                if player.salud <= 3:
                    player.salud += 1
            elif isinstance(flower, Flor_azul):
                player.escudo = True
            elif isinstance(flower, Flor_negra):
                player.recibir_daño()
            elif isinstance(flower, Flor_verde):
                score.puntuacion += 50

def detectar_daño_a_enemigos():
    daño_a_enemigo = pg.sprite.groupcollide(all_enemigos, player_proyectiles, False, True)

    for enemigo, proyectiles in daño_a_enemigo.items():
        if proyectiles:
            enemigo.salud -= 1
            if enemigo.salud <= 0:
                score.aumentar_score()
                enemigo.kill()



ultimo_tiempo = 0
tiempo_cooldown = 500
def detectar_colision_enemigo_player(player, lista_enemigos):
    tiempo_actual = pg.time.get_ticks()
    global ultimo_tiempo 
    global tiempo_cooldown

    colision = pg.sprite.spritecollide(player, lista_enemigos, False)
    if colision and tiempo_actual - ultimo_tiempo >= tiempo_cooldown:
        if player.escudo == False:
            player.salud -= 1
        elif player.escudo == True:
            player.escudo = False
        ultimo_tiempo = pg.time.get_ticks()

def crear_enemigos(cantidad_enemigos):
    if len(all_enemigos) < cantidad_enemigos:
        diablito = Diablito(player)
        all_enemigos.add(diablito)
        all_sprites.add(diablito)
