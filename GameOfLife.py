# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:16:20 2017

@author: Greg
"""

import numpy as np
np.set_printoptions(threshold=np.nan)
import random

#For non boarder cells, determines if a live cell lives or dies
#Inputs:
#   board - Game of Life board
#   X - X Position
#   Y -Y Position
def cell_survival(board, X, Y):
    liveNeighbors = 0
    for x in [X-1, X, X+1]:
        for y in [Y-1, Y, Y+1]:
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
                liveNeighbors = liveNeighbors + 1
    if liveNeighbors == 3 :
        return 1
    else:
        return 0
 
#Determines if a cell is in the non displayed boarder
#Inputs:
#   board - Game of Life board 
#   length - length of the board
#   width - width of the board
def in_boarder(board, boarderWidth, X, Y):
    inBoarder = 0
    if X < boarderWidth:
        inBoarder = 1
    if Y < boarderWidth:
        inBoarder = 1
    if X >= len(board[:,0]) - boarderWidth:
        inBoarder = 1
    if Y >= len(board[0,:]) - boarderWidth:
        inBoarder = 1
    return inBoarder

#Determines what happens between each generation for cells in the boarder
#Inputs
#   board - Game of Life Board
#   X - X Position
#   Y -Y Position
def boarder_rules(board, X, Y):
    return 0


#Initailize a Game of Life Board
#Inputs:
#   length - length of the board
#   width - width of the board
#   pLive - porbablity that a cell starts alive
def initialize_board(length, width, pLive):
    pDead = 1 - pLive
    board = np.random.choice([0,1], size=(length, width), p=[pDead, pLive])
    return board

#performes a turn of the game of life
#Inputs
#   board - a game of life board
#   boarderWidth - width of the boarder used to determine when to use boarder logic
def game_of_life_turn(board, boarderWidth):
    newBoard = np.zeros((board.shape))
    for row in range(0, len(board[:, 0])):
        for col in range(0, len(board[0, :])):
            if in_boarder(board, boarderWidth, row, col):
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
gameInputs = {'length': 125,
              'width': 125,
              'boarderWidth': 3,
              'totalGenerations':200,
              'startingLive': .5,
              'FPS': 5,
              'black': (0,0,0),
              'red': (255,0,0),
              'grey': (30,30,30),
              'cellSize': 10}

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#setup window
window = pygame.display.set_mode((((gameInputs['length'] - 2*gameInputs['boarderWidth']) * gameInputs['cellSize']),
                                 ((gameInputs['width'] - 2*gameInputs['boarderWidth']) * gameInputs['cellSize'])))
pygame.display.set_caption('Conway''s Game of Life')
window.fill(gameInputs['black'])

#initialize game of life board
board = initialize_board(gameInputs['length'], gameInputs['width'], gameInputs['startingLive'])

#Main Loop
while True:

    #Check if user wants to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update board
    board = game_of_life_turn(board, gameInputs['boarderWidth'])

    #draw grid
    for x in range(0, ((gameInputs['length'] - gameInputs['boarderWidth']) * gameInputs['cellSize']), gameInputs['cellSize']):
        for y in range(0, ((gameInputs['width'] - gameInputs['boarderWidth']) * gameInputs['cellSize']), gameInputs['cellSize']):
            if board[x/gameInputs['cellSize']+gameInputs['boarderWidth']][y/gameInputs['cellSize']+gameInputs['boarderWidth']] == 1:
                pygame.draw.rect(window, gameInputs['red'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']])
            else:
                pygame.draw.rect(window, gameInputs['black'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']])
            pygame.draw.rect(window, gameInputs['grey'], [x, y, gameInputs['cellSize'], gameInputs['cellSize']], 1)

    #redraw board
    pygame.display.update()

    #refresh frequency
    clock.tick(gameInputs['FPS'])

    

    

    
    