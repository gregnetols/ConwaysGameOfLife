# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:16:20 2017

@author: Greg
"""

import numpy as np
np.set_printoptions(threshold=np.nan)
import random
import pygame

#For non boarder cells, determines if a live cell lives or dies
#Inputs:
#   board - Game of Life board
#   X - X Position
#   Y -Y Position
def cell_survival(board, X, Y):
    liveNeighbors = 0
    for x in [X-1, X, X+1]:
        for y in [Y-1, Y, Y+1]:
            if x != X and y != Y and board[x,y] == 1:
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
            if x != X and y != Y and board[x,y] == 1:
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
#   displayLength - displayed length of the board
#   diaplyWidth - dispalyed width of the board
def in_boarder(board, boarderWidth, X, Y):
    if X >= boarderWidth and X <= len(board[0,:]) - boarderWidth:
        return 1
    if Y >=  boarderWidth and Y <= len(board[:,0]) - boarderWidth:
        return 1
    return 0

#Determines what happens between each generation for cells in the boarder
#Inputs
#   board - Game of Life Board
#   X - X Position
#   Y -Y Position
def boarder_rules(board, X, Y):
    if random.random() < .5:
        return 0
    else:
        return board[X,Y]

#Initailize a Game of Life Board
#Inputs:
#   length - length of the board
#   width - width of the board
#   pLive - porbablity that a cell starts alive
def initialize_board(length, width, pLive):
    pDead = 1 - pLive
    board = np.random.choice([0,1], size=(length, width), p=[pDead, pLive])
    return board


#Dictionary of game inputs
#Inputs
#   length - length of the board
#   width - width of the board
#   displayLength - displayed length of the board
#   diaplyWidth - dispalyed width of the board
#   totalGenerations - the total amount of board geneartions to iterate through
gameInputs = {'length': 10,
              'width': 10,
              'boarderWidth': 3,
              'totalGenerations': 25,
              'startingLive': .5}


def main():
    board = initialize_board(gameInputs['length'], gameInputs['width'], gameInputs['startingLive'])
    
    currentGeneration = 0
    while( currentGeneration < gameInputs['totalGenerations']):
        print(currentGeneration)
        for row in [0, gameInputs['length'] - 1]:
            for col in [0, gameInputs['width'] - 1]:
                if in_boarder(board, gameInputs['boarderWidth'], row, col ):
                    board[row,col] = boarder_rules(board, row, col)
                elif board[row, col] == 1:
                    board[row,col] = cell_survival(board, row, col)
                else:
                    board[row,col] = cell_birth(board, row, col)
                    
        currentGeneration = currentGeneration + 1
        print(board)
    
def test():
    board = np.zeros((10,10))
    
    for x in range (0, 9):
        print(1)
        for y in range (0, 9):
            board[x,y] = in_boarder(board, 3, x, y)

    print(board)
    
test()
    

    
    