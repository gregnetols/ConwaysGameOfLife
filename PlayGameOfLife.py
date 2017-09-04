# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:16:20 2017

@author: Greg
"""

import numpy as np
import pygame, sys
import GOL

# Dictionary of game inputs
# GameInputs
gameInputs = {'height': 140,
              'length': 120,
              'width': 120,
              'boarderWidth': 2,
              'displayHeight': 100,
              'displayWidth':100,
              'totalGenerations':200,
              'startingLive': .5,
              'FPS': 10,
              'black': (0,0,0),
              'red': (255,0,0),
              'grey': (30,30,30),
              'cellSize': 10,
              'minSurvive': 2,
              'maxSurvive': 3,
              'minRebirth': 3,
              'maxRebirth': 3}

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

# setup window
window = pygame.display.set_mode(((gameInputs['displayWidth'] * gameInputs['cellSize']),
                                 (gameInputs['displayHeight'] * gameInputs['cellSize'])))
pygame.display.set_caption('Conway''s Game of Life')
window.fill(gameInputs['black'])

# initialize game of life board
board = GOL.initialize_board(gameInputs['width'], gameInputs['height'],  gameInputs['startingLive'])

# Main Loop
while True:

    # Check if user wants to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update board
    board = GOL.game_of_life_turn(board, gameInputs['minSurvive'], gameInputs['maxSurvive'], gameInputs['minRebirth'], gameInputs['maxRebirth'])

    # draw grid
    for x in range(0, (gameInputs['displayWidth'] * gameInputs['cellSize']), gameInputs['cellSize']):
        for y in range(0, (gameInputs['displayHeight'] * gameInputs['cellSize']), gameInputs['cellSize']):
            if board[x/gameInputs['cellSize']+(gameInputs['width']-gameInputs['displayWidth'])/2][y/gameInputs['cellSize']+(gameInputs['height']-gameInputs['displayHeight'])/2] == 1:
                pygame.draw.rect(window, gameInputs['red'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']])
            else:
                pygame.draw.rect(window, gameInputs['black'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']])
            pygame.draw.rect(window, gameInputs['grey'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']], 1)

    # redraw board
    pygame.display.update()

    # refresh frequency
    clock.tick(gameInputs['FPS'])

