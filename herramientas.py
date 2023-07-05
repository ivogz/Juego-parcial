import pygame as pg
import constantes as c


def crear_bordes(rect_principal):

    '''
    return = borde superior, inferior, izquierdo, derecho.
    '''

    # Crear rectángulos en los bordes
    borde_superior = pg.Rect(rect_principal.left, rect_principal.top , rect_principal.width, 3)
    borde_inferior = pg.Rect(rect_principal.left, rect_principal.bottom -3, rect_principal.width, 3)
    borde_izquierdo = pg.Rect(rect_principal.left, rect_principal.top, 3, rect_principal.height)
    borde_derecho = pg.Rect(rect_principal.right - 3, rect_principal.top, 3, rect_principal.height)

    return borde_superior, borde_inferior, borde_izquierdo, borde_derecho


def reescalar_imagenes(lista_imagenes, ancho, alto):
    for lista in lista_imagenes:
        for i in range(len(lista)):
            lista[i] = pg.transform.scale(lista[i], (ancho, alto))

def reescalar_imagenes2(lista_imagenes, ancho, alto):
    for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pg.transform.scale(lista_imagenes[i], (ancho, alto))

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = [pg.transform.flip(imagen, flip_x, flip_y) for imagen in lista]

    return lista_girada



######################## MAPAS #################################


map_1 = "assets/Mapas/map1.jpg"
map_2 = "assets/Mapas/map2.jpg"
map_3 = "assets/Mapas/map3.jpg"
map_4 = "assets/Mapas/map4.jpg"
map_5 = "assets/Mapas/map5.jpg"

mapa_intro = pg.transform.scale(pg.image.load("assets/fondo_menu.jpg"), (c.ANCHO, c.ALTO))


#################### BOTONES #################################

## INTRO
boton_play = pg.image.load("assets/Menu/1.png")
boton_settings = pg.image.load("assets/Menu/2.png")
boton_exit = pg.image.load("assets/Menu/3.png")

## MENU
boton_menu = pg.transform.scale(pg.image.load("assets/Menu/boton_casa.png"), (80,80))

## VOLUMEN

boton_volume_mute = pg.transform.scale(pg.image.load("assets/Menu/volume_mute.png"), (180,180))
boton_volume_mas = pg.transform.scale(pg.image.load("assets/Menu/volume_mas.png"), (180,180))
boton_volume_menos = pg.transform.scale(pg.image.load("assets/Menu/volume_menos.png"), (180,180))

# SELECTOR NIVELES

boton_nivel_1 = pg.image.load("assets/Selector_niveles/1.png")
boton_nivel_2 = pg.image.load("assets/Selector_niveles/2.png")
boton_nivel_3 = pg.image.load("assets/Selector_niveles/3.png")
boton_nivel_4 = pg.image.load("assets/Selector_niveles/4.png")
boton_nivel_5 = pg.image.load("assets/Selector_niveles/5.png")
boton_nivel_bloq = pg.image.load("assets/Selector_niveles/bloq.png")

## PAUSA

boton_menu_pausa = pg.transform.scale(pg.image.load("assets/Menu/pausa/menu_pausa.png"), (240,90))
boton_replay_pausa = pg.transform.scale(pg.image.load("assets/Menu/pausa/replay_pausa.png"), (240,90))
boton_play_pausa = pg.transform.scale(pg.image.load("assets/Menu/pausa/play_pausa.png"), (240,90))

## GAME OVER ## 

game_over = pg.transform.scale(pg.image.load("assets/Menu/game_over.png"), (1105 / 2 , 673 / 2))


############################ PLATAFORMAS #########################

piso_map_1 = pg.image.load("assets/Plataformas_base/0.png")
piso_map_1 = pg.transform.scale(piso_map_1, (c.ANCHO, 90)) 
piso_map_2 = pg.image.load("assets/Plataformas_base/1.png")
piso_map_2 = pg.transform.scale(piso_map_2, (c.ANCHO, 90)) 
piso_map_3 = pg.image.load("assets/Plataformas_base/2.png")
piso_map_3 = pg.transform.scale(piso_map_3, (c.ANCHO, 90)) 
piso_map_4 = pg.image.load("assets/Plataformas_base/4.png")
piso_map_4 = pg.transform.scale(piso_map_4, (c.ANCHO, 90)) 
piso_map_5 = pg.image.load("assets/Plataformas_base/5.png")
piso_map_5 = pg.transform.scale(piso_map_5, (c.ANCHO, 90)) 


isla1 = pg.image.load("assets/Plataformas_islas\plataforma.png")



#################################### PLAYER #################################

player_quieto = [
        pg.image.load("assets/Player/idle/8.png"),
        pg.image.load("assets/Player/idle/9.png"),
        pg.image.load("assets/Player/idle/10.png"),
        pg.image.load("assets/Player/idle/11.png"),
        pg.image.load("assets/Player/idle/12.png"),
        pg.image.load("assets/Player/idle/13.png"),
        ]

player_quieto_izquierda = girar_imagenes(player_quieto, True, False)

player_camina_derecha = [
    pg.image.load("assets/Player/run/20.png"),
    pg.image.load("assets/Player/run/21.png"),
    pg.image.load("assets/Player/run/22.png"),
    pg.image.load("assets/Player/run/23.png"),
        ]

player_sprint_derecha = [
    pg.image.load("assets/Player/sprint/24.png"),
    pg.image.load("assets/Player/sprint/25.png"),
    pg.image.load("assets/Player/sprint/26.png"),
    pg.image.load("assets/Player/sprint/27.png"),
        ]

player_camina_izquierda = girar_imagenes(player_camina_derecha, True, False)

player_sprint_izquierda = girar_imagenes(player_sprint_derecha, True, False)

player_salto_derecha = [
        pg.image.load("assets/Player/salto/0.png"),
        pg.image.load("assets/Player/salto/1.png"),
        pg.image.load("assets/Player/salto/2.png"),
        pg.image.load("assets/Player/salto/3.png"),
        pg.image.load("assets/Player/salto/4.png")
        ]
player_salto_izquierda = girar_imagenes(player_salto_derecha,True, False)

player_animacion_disparo = [
        pg.image.load("assets/Player/patada_shoot/0.png"),
        pg.image.load("assets/Player/patada_shoot/1.png"),
        pg.image.load("assets/Player/patada_shoot/2.png"),
        pg.image.load("assets/Player/patada_shoot/3.png"),
        pg.image.load("assets/Player/patada_shoot/4.png")
]

player_animacion_disparo_izquierda = girar_imagenes(player_animacion_disparo, True, False)

player_disparo = [

    pg.image.load("assets/Player/shoot1/0.png"),
    pg.image.load("assets/Player/shoot1/1.png"),
    pg.image.load("assets/Player/shoot1/2.png"),
    pg.image.load("assets/Player/shoot1/3.png"),
    pg.image.load("assets/Player/shoot1/4.png"),
    pg.image.load("assets/Player/shoot1/5.png"),
    pg.image.load("assets/Player/shoot1/6.png"),
    pg.image.load("assets/Player/shoot1/7.png")
    # pg.image.load("assets/Player/shoot1/8.png"),
    # pg.image.load("assets/Player/shoot1/9.png"),
]

player_barrier = [
    
    pg.image.load("assets/Player/barrier/0.png"),
    pg.image.load("assets/Player/barrier/1.png"),
    pg.image.load("assets/Player/barrier/2.png"),
    pg.image.load("assets/Player/barrier/3.png")
]
reescalar_imagenes2(player_barrier, 48, 55)

lista_animaciones_player = [
                    player_camina_derecha,
                    player_sprint_derecha,
                    player_camina_izquierda,
                    player_sprint_izquierda,
                    player_quieto,
                    player_quieto_izquierda,
                    player_salto_derecha,
                    player_animacion_disparo,
                    player_animacion_disparo_izquierda,
                            ]

lista_animaciones = reescalar_imagenes(lista_animaciones_player, 48, 55)

            ###### BARRA DE VIDA #####

lista_barra_de_vida = [
    pg.image.load("assets/Player/barra_de_vida/0.png"),
    pg.image.load("assets/Player/barra_de_vida/1.png"),
    pg.image.load("assets/Player/barra_de_vida/2.png"),
    pg.image.load("assets/Player/barra_de_vida/3.png"),
    pg.image.load("assets/Player/barra_de_vida/4.png")
                        ]

lista_barra_de_vida_boss = [
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_0.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_1.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_2.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_3.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_4.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_5.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_6.png"),
    pg.image.load("assets/Enemigos/Boss/barra_de_vida_7.png")
]

reescalar_imagenes2(lista_barra_de_vida, 240, 60)
reescalar_imagenes2(lista_barra_de_vida_boss, 240, 60)


### PLANTAS

planta_vida = pg.image.load("assets/Plantas/0.png")
planta_azul = pg.image.load("assets/Plantas/1.png")
planta_verde = pg.image.load("assets/Plantas/2.png")
planta_negra = pg.image.load("assets/Plantas/3.png")
planta_lila = pg.image.load("assets/Plantas/4.png")
planta_marron = pg.image.load("assets/Plantas/5.png")

planta_vida = pg.transform.scale(planta_vida, (60, 80)) 
planta_azul = pg.transform.scale(planta_azul, (60, 80)) 
planta_verde = pg.transform.scale(planta_verde, (60, 80)) 
planta_negra = pg.transform.scale(planta_negra, (60, 80)) 
planta_lila = pg.transform.scale(planta_lila, (60, 80)) 
planta_marron = pg.transform.scale(planta_marron, (60, 80)) 

##### ENEMIGOS ####

diablito_sprite = pg.image.load("assets/Enemigos/Diablito/0.png")
diablito_sprite = pg.transform.scale(diablito_sprite, (45, 57))

cerebro_animacion = [
    pg.image.load("assets/Enemigos/Boss/0.png"),
    pg.image.load("assets/Enemigos/Boss/1.png")
]

reescalar_imagenes2(cerebro_animacion, 62*3, 62*3)

cerebro_shoot = [
    pg.image.load("assets/Enemigos/Boss/6.png"),
    pg.image.load("assets/Enemigos/Boss/7.png"),
    pg.image.load("assets/Enemigos/Boss/8.png"),
    pg.image.load("assets/Enemigos/Boss/9.png")
]
reescalar_imagenes2(cerebro_shoot, 42, 42)


############# SONIDOS #######
pg.mixer.init()

sonido_fondo = pg.mixer.Sound("assets\Sonidos\sonido_fondo.mp3")
sonido_pausa = pg.mixer.Sound("assets\Sonidos\pausa.mp3")
sonido_juego = pg.mixer.Sound("assets\Sonidos\sonido_juego.mp3")

lista_sonidos = [sonido_fondo, sonido_pausa, sonido_juego]


sonido_fondo.set_volume(0.1)

def apagar_sonidos_menos(sonido_no_apagar:str):
    global lista_sonidos
    if sonido_no_apagar == "fondo":
        for sonido in lista_sonidos:
            if sonido == sonido_fondo:
                sonido.play()
            else: sonido.stop()
    elif sonido_no_apagar == "juego":
        for sonido in lista_sonidos:
            if sonido == sonido_juego:
                sonido.play()
            else: sonido.stop()
    elif sonido_no_apagar == "pausa":
        for sonido in lista_sonidos:
            if sonido == sonido_pausa:
                sonido.play()
            else: sonido.stop()

