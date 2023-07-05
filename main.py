from setup import *
import pygame as pg, sys
import constantes as c

from modo import *
from game_state import GameState

game_state = GameState()

running = True
    
while running:

    game_state.state_manager()