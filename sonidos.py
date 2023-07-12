import pygame as pg
import constantes as c

### AMBIENTEE ###
sonido_fondo = pg.mixer.Sound("assets\Sonidos\sonido_fondo.mp3")
sonido_pausa = pg.mixer.Sound("assets\Sonidos\pausa.mp3")
sonido_juego = pg.mixer.Sound("assets\Sonidos\sonido_juego.mp3")
sonido_fondo2 = pg.mixer.Sound("assets\Sonidos\musica_fondo.wav")

lista_sonidos = [sonido_fondo, sonido_pausa, sonido_juego]


#### EFECTOS ###

sonido_perder_vida = pg.mixer.Sound("assets\Sonidos\perder_vida_player.wav")
sonido_muerte_diablo = pg.mixer.Sound("assets\Sonidos\muerte_diablo.wav")
sonido_muerte_player = pg.mixer.Sound("assets\Sonidos\muerte_player.wav")
sonido_disparo_player = pg.mixer.Sound("assets\Sonidos\disparo_player.wav")
sonido_muerte_boss = pg.mixer.Sound("assets\Sonidos\muerte_boss.wav")


lista_efectos_sonidos = [sonido_perder_vida, sonido_muerte_diablo, sonido_muerte_player, sonido_disparo_player, sonido_muerte_boss]




#############

sonido_fondo.set_volume(0.1)

# def apagar_sonidos_menos(sonido_no_apagar:str):
#     '''fondo, juego, pausa'''
#     global lista_sonidos
#     if sonido_no_apagar == "fondo":
#         for sonido in lista_sonidos:
#             if sonido == sonido_fondo:
#                 sonido.play(-1)
#             else: sonido.stop()
#     elif sonido_no_apagar == "juego":
#         for sonido in lista_sonidos:
#             if sonido == sonido_juego:
#                 sonido.play(-1)
#             else: sonido.stop()
#     elif sonido_no_apagar == "pausa":
#         for sonido in lista_sonidos:
#             if sonido == sonido_pausa:
#                 sonido.play(-1)
#             else: sonido.stop()
#     for sonido in lista_sonidos:
#         sonido.set_volume(0.5)