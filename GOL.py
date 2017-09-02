# -*- coding: utf-8 -*-
"""
Created on Sun Sep 02 21:16:20 2017

@author: Greg
"""

import numpy as np


# For non boarder cells, determines if a live cell lives or dies
# Inputs:
#   board - Game of Life board
#   x - x position
#   y - y position
# Returns: 1 stays alive 0 if it should die
def cell_survival(board, x, y):
    liveNeighbors = 0
    for X in [x-1, x, x+1]:
        for Y in [y-1, y, y+1]:
            if ( X != x or Y != y ) and board[X,Y] == 1:
                liveNeighbors = liveNeighbors + 1
    if liveNeighbors in [2,3]:
        return 1
    else:
        return 0


# For non boarder cells, determines if a dead cell comes to life
# Inputs:
#   board - Game of Life board
#   x - x position
#   y - y position
# Returns: 1 if a dead cell comes back to life 0 otherwise
def cell_birth(board, x, y):
    liveNeighbors = 0
    for X in [x-1, x, x+1]:
        for Y in [y-1, y, y+1]:
            if ( Y != x or Y != y ) and board[X,Y] == 1:
                liveNeighbors = liveNeighbors + 1
    if liveNeighbors == 3 :
        return 1
    else:
        return 0


# Determines if a cell is in the non displayed boarder
# Inputs:
#   board - Game of Life board
#   x - x position
#   y - y position
# Returns: 1 if a cell is on the boarder 0 otherwise
def on_boarder(board, x, y):
    return (x-1<=0) or (y-1<=0) or (x+1>=board.shape[0]) or (y+1>=board.shape[1])


# Determines what happens to cells on the boarder
# Inputs:
#   board - Game of Life Board
#   x - x position
#   y - y position
# Returns: 0
def boarder_rules(board, x, y):
    return 0


# Initialize a Game of Life Board
# Inputs:
#   length - length of the board
#   height - height of the board
#   pLive - probability that a cell starts alive
# Returns a new game of life board
def initialize_board(length, height, pLive):
    pDead = 1 - pLive
    board = np.random.choice([0,1], size=(length, height), p=[pDead, pLive])
    return board


# Performs a turn of the game of life
# Inputs
#   board - a game of life board
# Returns the next iteration of a game of life board
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

