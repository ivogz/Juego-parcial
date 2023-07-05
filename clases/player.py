import pygame as pg
import time
import constantes as c
import herramientas as h
from clases.proyectiles import Proyectiles
from setup import PANTALLA






class Player(pg.sprite.Sprite):
    def __init__(self, grupo_plataformas, grupo_balas, grupo_all_sprites):
        super().__init__()
        self.image = h.player_quieto[0]
        self.rect = h.player_quieto[0].get_rect()
        self.rect.centerx = c.ANCHO // 2
        self.rect.bottom = c.ALTO - 50
        self.velocidad_x = 0

        self.borde_superior, self.borde_inferior, self.borde_izquierdo, self.borde_derecho = h.crear_bordes(self.rect)
        # self.rects = [self.rect, self.borde_superior, self.borde_inferior, self.borde_izquierdo, self.borde_derecho]

        ## control tiempo de animacion
        self.current_time = 0
        self.contador_pasos = 0
        self.animacion_cooldown = 280
        self.ultimo_update = 0
        self.ultima_direccion = "Derecha"

        ## gravedad / salto

        self.gravedad = 1
        self.potencia_salto = -19
        self.limite_velocidad_caida = 9
        self.esta_saltando = False
        self.esta_cayendo = False
        self.desplazamiento_y = 0
        self.cantidad_saltos = 2
        self.saltos_hechos = 0

        self.tiempo_ultimo_salto = 0
        self.salto_cooldown = 0.2

        ## Disparo
        self.tiempo_ultimo_disparo = 0
        self.disparo_cooldown = 0.2
        self.ultima_direccion_apuntada = "Derecha"

        # GRUPOS
        self.grupo_plataformas = grupo_plataformas
        self.grupo_balas = grupo_balas
        self.grupo_all_sprites = grupo_all_sprites

        # VIDA

        self.salud = 4
        self.escudo = False

    ##### ANIMACION DEL SPRITE ####

    def animar(self, acciones_personaje, pantalla, rectangulo_pj):

        self.current_time = pg.time.get_ticks()
        largo = len(acciones_personaje)
        if self.contador_pasos >= largo - 1:
            self.contador_pasos = 0

        if self.current_time - self.ultimo_update >= self.animacion_cooldown:
            self.contador_pasos += 1
            self.ultimo_update = self.current_time

        if self.contador_pasos <= largo:
            pantalla.blit(acciones_personaje[self.contador_pasos], rectangulo_pj)

    ### MOVIMIENTO DEL JUGADOR ###

    def caminar(self, velocidad: int, animacion):
        self.velocidad_x = velocidad
        if not self.esta_saltando:
            self.animar(animacion, PANTALLA, self.rect)
        self.rect.x += self.velocidad_x

    ## GRAVEDAD DEL JUGADOR

    def aplicar_gravedad(self, pantalla, accion, rectangulo_pj, lista_plataformas):

        if self.esta_saltando:
            self.animar(accion, pantalla, rectangulo_pj)
            rectangulo_pj.y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        for piso in lista_plataformas:
            if rectangulo_pj.colliderect(piso) and self.desplazamiento_y >= 0:
                self.esta_saltando = False
                self.saltos_hechos = 0
                rectangulo_pj.bottom = piso.rect.top + 1
                self.desplazamiento_y = 0
                break
            else:
                self.esta_saltando = True

    def recibir_daño(self):

        if self.escudo == False:
            self.salud -= 1
        elif self.escudo == True:
            self.escudo = False

    ## PROYECTIL 

    def Bala(self, velocidad_x, velocidad_y):
        ataque_distancia = Proyectiles(h.player_disparo, self.rect.centerx, self.rect.top, velocidad_x, velocidad_y)
        self.grupo_balas.add(ataque_distancia)
        self.grupo_all_sprites.add(ataque_distancia)



    ###### ACTUALIZACION PERSONAJE


    def update(self):

        PANTALLA.blit(h.lista_barra_de_vida[self.salud], (0,0))

        keys = pg.key.get_pressed()

        self.velocidad_x = 0

        if keys[pg.K_j]:
            tiempo_actual_disparo = time.time()
            if tiempo_actual_disparo - self.tiempo_ultimo_disparo > self.disparo_cooldown:
                if self.ultima_direccion_apuntada == "Arriba":
                    self.Bala(0, -4)
                elif self.ultima_direccion_apuntada == "Abajo":
                    self.Bala(0, 4)
                elif self.ultima_direccion_apuntada == "Derecha":
                    self.Bala(4, 0)
                elif self.ultima_direccion_apuntada == "Izquierda":
                    self.Bala(-4, 0)

                self.tiempo_ultimo_disparo = tiempo_actual_disparo

        if keys[pg.K_d]:  # DERECHA
            self.ultima_direccion = "Derecha"
            self.ultima_direccion_apuntada = "Derecha"

            if keys[pg.K_LSHIFT]:
                self.caminar(6, h.player_sprint_derecha)
            else:
                self.caminar(4, h.player_camina_derecha)

            if self.rect.right >= PANTALLA.get_width():
            # Si el personaje alcanza o supera el borde derecho de la pantalla,
            # ajustar su posición para que no salga de la pantalla
                self.rect.right = PANTALLA.get_width()

        elif keys[pg.K_a]:  # IZQUIERDA
            self.ultima_direccion = "Izquierda"
            self.ultima_direccion_apuntada = "Izquierda"

            if keys[pg.K_LSHIFT]:
                self.caminar(-6, h.player_sprint_izquierda)
            else:
                self.caminar(-4, h.player_camina_izquierda)

            if self.rect.left <= 0:
                # Si el personaje alcanza o supera el borde izquierdo de la pantalla,
                # ajustar su posición para que no salga de la pantalla
                self.rect.left = 0

        else:  # Quieto
            if not self.esta_saltando and self.ultima_direccion == "Derecha":
                self.animar(h.player_quieto, PANTALLA, self.rect)
            if not self.esta_saltando and self.ultima_direccion == "Izquierda":
                self.animar(h.player_quieto_izquierda, PANTALLA, self.rect)

        if keys[pg.K_w]:  # ARRIBA
            self.ultima_direccion_apuntada = "Arriba"

        elif keys[pg.K_s]:  # ABAJO
            self.ultima_direccion_apuntada = "Abajo"

        if keys[pg.K_SPACE]:
            tiempo_actual_salto = time.time()
            if tiempo_actual_salto - self.tiempo_ultimo_salto > self.salto_cooldown:
                self.tiempo_ultimo_salto = tiempo_actual_salto
                if self.saltos_hechos < self.cantidad_saltos:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.saltos_hechos += 1

        if self.ultima_direccion == "Derecha":
            self.aplicar_gravedad(PANTALLA, h.player_salto_derecha, self.rect, self.grupo_plataformas)
        elif self.ultima_direccion == "Izquierda":
            self.aplicar_gravedad(PANTALLA, h.player_salto_izquierda, self.rect, self.grupo_plataformas)
            

        if self.escudo == True:
            self.animar(h.player_barrier, PANTALLA, self.rect)

        ## MOVIMIENTO RECTS BORDES

        self.borde_superior, self.borde_inferior, self.borde_izquierdo, self.borde_derecho = h.crear_bordes(self.rect)

        # pg.draw.rect(PANTALLA, c.GRIS, self.borde_inferior, 2)
        # pg.draw.rect(PANTALLA, c.GRIS, self.borde_superior, 2)
        # pg.draw.rect(PANTALLA, c.GRIS, self.borde_izquierdo, 2)
        # pg.draw.rect(PANTALLA, c.GRIS, self.borde_derecho, 2)

