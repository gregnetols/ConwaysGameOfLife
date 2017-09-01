# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:16:20 2017

@author: Greg
"""

import numpy as np
np.set_printoptions(threshold=np.nan)
import random
import pygame, sys

#For non boarder cells, determines if a live cell lives or dies
#Inputs:
#   board - Game of Life board
#   X - X Position
#   Y -Y Position
def cell_survival(board, X, Y):
    liveNeighbors = 0
    for x in [X-1, X, X+1]:
        for y in [Y-1, Y, Y+1]:
            if ( x != X or y != Y ) and board[x,y] == 1:
                liveNeighbors = liveNeighbors + 1
    if liveNeighbors in [2,3]:
        return 1
    else:
        return 0
                

#For non boarder cells, determines if a dead cell comes to life
#Inputs:
#   board - Game of Life board
#   X - X Position
#   Y -Y Position 
def cell_birth(board, X, Y):
    liveNeighbors = 0
    for x in [X-1, X, X+1]:
        for y in [Y-1, Y, Y+1]:
            if ( x != X or y != Y ) and board[x,y] == 1:
                liveNeighbors = liveNeighbors + 1
    if liveNeighbors == 3 :
        return 1
    else:
        return 0
 
#Determines if a cell is in the non displayed boarder
#Inputs:
#   board - Game of Life board 
#   x - x position
#   y - y position
def on_boarder(board, x, y):
    if (x-1<=0) or (y-1<=0) or (x+1>=board.shape[0]) or (y+1>=board.shape[1]):
        return 1

#Determines what happens between each generation for cells in the boarder
#Inputs
#   board - Game of Life Board
#   x - x position
#   y - y position
def boarder_rules(board, x, y):
    return 0


#Initailize a Game of Life Board
#Inputs:
#   length - length of the board
#   height - height of the board
#   pLive - probability that a cell starts alive
def initialize_board(length, height, pLive):
    pDead = 1 - pLive
    board = np.random.choice([0,1], size=(length, height), p=[pDead, pLive])
    return board

#performes a turn of the game of life
#Inputs
#   board - a game of life board
#   boarderWidth - width of the boarder used to determine when to use boarder logic
def game_of_life_turn(board):
    newBoard = np.zeros((board.shape))
    for row in range(0, len(board[:, 0])):
        for col in range(0, len(board[0, :])):
            if on_boarder(board, row, col):
                newBoard[row, col] = boarder_rules(board, row, col)
            elif board[row, col] == 1:
                newBoard[row, col] = cell_survival(board, row, col)
            elif board[row, col] == 0:
                newBoard[row, col] = cell_birth(board, row, col)
    return newBoard

#Dictionary of game inputs
#Inputs
#   length - length of the board
#   width - width of the board
#   displayLength - displayed length of the board
#   diaplyWidth - dispalyed width of the board
#   totalGenerations - the total amount of board geneartions to iterate through
gameInputs = {'height': 120,
              'length': 120,
              'width': 120,
              'boarderWidth': 10,
              'displayHeight': 100,
              'displayWidth':100,
              'totalGenerations':200,
              'startingLive': .5,
              'FPS': 100,
              'black': (0,0,0),
              'red': (255,0,0),
              'grey': (30,30,30),
              'cellSize': 10}

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#setup window
window = pygame.display.set_mode(((gameInputs['displayWidth'] * gameInputs['cellSize']),
                                 (gameInputs['displayHeight'] * gameInputs['cellSize'])))
pygame.display.set_caption('Conway''s Game of Life')
window.fill(gameInputs['black'])

#initialize game of life board
board = initialize_board(gameInputs['width'], gameInputs['height'],  gameInputs['startingLive'])

#Main Loop
while True:

    #Check if user wants to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update board
    board = game_of_life_turn(board)

    #draw grid
    for x in range(0, (gameInputs['displayWidth'] * gameInputs['cellSize']), gameInputs['cellSize']):
        for y in range(0, (gameInputs['displayHeight'] * gameInputs['cellSize']), gameInputs['cellSize']):
            if board[x/gameInputs['cellSize']+gameInputs['boarderWidth']][y/gameInputs['cellSize']+gameInputs['boarderWidth']] == 1:
                pygame.draw.rect(window, gameInputs['red'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']])
            else:
                pygame.draw.rect(window, gameInputs['black'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']])
            pygame.draw.rect(window, gameInputs['grey'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']], 1)

    #redraw board
    pygame.display.update()

    #refresh frequency
    clock.tick(gameInputs['FPS'])

    

    

    
    