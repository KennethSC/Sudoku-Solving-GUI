import pygame

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
RED = (255, 0, 0)
GREEN = (51, 165, 50)
BLUE = (51, 153, 255)

# These are all the different sudoku boards that 
# you can use in the GUI and in SudokuSolver.py.
# Feel free to test and add any other Sudoku boards.
# They vary in difficulty with board1 being the easiest 
# and board5 being the hardest

board1 = [
         [0, 2, 0, 0, 5, 3, 7, 4, 8],
         [0, 5, 0, 1, 0, 6, 0, 2, 0],
         [9, 3, 7, 2, 8, 4, 0, 1, 6],
         [5, 0, 3, 8, 0, 2, 1, 6, 4],
         [4, 0, 0, 0, 6, 0, 0, 0, 7],
         [6, 1, 8, 3, 4, 7, 2, 5, 9],
         [0, 0, 9, 0, 0, 5, 0, 7, 0],
         [0, 4, 5, 0, 0, 8, 3, 9, 2],
         [0, 6, 1, 7, 2, 9, 4, 0, 0]
]

board2 = [
         [0, 9, 8, 6, 4, 1, 0, 3, 7],
         [0, 0, 7, 8, 0, 0, 9, 4, 6],
         [0, 3, 6, 0, 0, 9, 8, 2, 0],
         [8, 5, 9, 2, 3, 6, 1, 7, 0],
         [0, 0, 0, 0, 9, 8, 3, 5, 2],
         [3, 0, 0, 1, 0, 7, 6, 9, 8],
         [0, 6, 0, 0, 1, 0, 4, 0, 5],
         [9, 0, 5, 7, 6, 4, 0, 1, 0],
         [0, 0, 4, 3, 8, 5, 0, 0, 9]
]

board3 = [
         [2, 6, 0, 0, 0, 3, 0, 1, 5],
         [4, 7, 0, 0, 0, 0, 0, 0, 8],
         [5, 8, 1, 0, 0, 4, 7, 6, 3],
         [0, 3, 0, 4, 8, 9, 0, 7, 0],
         [0, 0, 6, 0, 0, 2, 8, 3, 0],
         [0, 0, 8, 3, 1, 0, 0, 0, 0],
         [6, 9, 0, 0, 0, 8, 0, 0, 7],
         [3, 0, 0, 0, 9, 0, 2, 0, 0],
         [0, 1, 0, 5, 0, 0, 0, 9, 6]
]


board4 = [
         [0, 2, 7, 5, 0, 1, 9, 8, 4],
         [0, 1, 3, 0, 0, 9, 2, 0, 0],
         [0, 0, 4, 0, 0, 7, 6, 0, 0],
         [0, 7, 5, 4, 0, 0, 8, 3, 2],
         [3, 0, 0, 0, 1, 8, 7, 0, 0],
         [0, 0, 8, 0, 5, 0, 1, 0, 0],
         [0, 3, 6, 1, 8, 5, 0, 0, 9],
         [0, 0, 0, 0, 0, 0, 3, 7, 0],
         [9, 8, 0, 3, 0, 0, 0, 0, 0]
]


board5 = [
         [3, 0, 2, 0, 0, 7, 9, 4, 0],
         [4, 0, 5, 9, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 4, 5, 0, 0],
         [8, 9, 0, 0, 0, 2, 0, 0, 0],
         [0, 2, 7, 0, 8, 1, 0, 6, 9],
         [1, 6, 3, 0, 5, 9, 0, 0, 7],
         [7, 0, 8, 0, 0, 0, 0, 0, 2],
         [2, 0, 9, 6, 7, 3, 0, 1, 0],
         [0, 5, 0, 2, 0, 0, 0, 0, 4]
]


board6 = [
         [4, 0, 0, 8, 0, 1, 0, 0, 0],
         [0, 0, 6, 3, 4, 0, 8, 0, 0],
         [9, 8, 1, 2, 0, 0, 0, 3, 0],
         [7, 4, 0, 1, 0, 2, 0, 5, 8],
         [0, 0, 2, 0, 9, 0, 0, 4, 3],
         [3, 0, 8, 7, 0, 4, 2, 0, 1],
         [1, 0, 3, 4, 0, 0, 5, 0, 0],
         [8, 6, 0, 0, 0, 5, 0, 0, 4],
         [5, 0, 0, 0, 8, 0, 0, 0, 0]
]

board7 = [
         [8, 0, 1, 0, 4, 9, 0, 5, 0],
         [6, 0, 0, 0, 3, 1, 0, 0, 0],
         [0, 0, 0, 8, 2, 7, 6, 0, 3],
         [3, 0, 6, 2, 1, 0, 7, 4, 0],
         [0, 0, 0, 0, 0, 6, 8, 0, 0],
         [2, 0, 4, 7, 0, 0, 0, 0, 0],
         [4, 0, 5, 0, 0, 0, 3, 0, 8],
         [7, 0, 3, 0, 8, 0, 4, 2, 0],
         [0, 0, 8, 0, 7, 4, 0, 6, 1]
]


board8 = [
         [4, 0, 0, 8, 0, 1, 0, 0, 0],
         [0, 0, 6, 3, 4, 0, 8, 0, 0],
         [9, 8, 1, 2, 0, 0, 0, 3, 0],
         [7, 4, 0, 1, 0, 2, 0, 5, 8],
         [0, 0, 2, 0, 9, 0, 0, 4, 3],
         [3, 0, 8, 7, 0, 4, 2, 0, 1],
         [1, 0, 3, 4, 0, 0, 5, 0, 0],
         [8, 6, 0, 0, 0, 5, 0, 0, 4],
         [5, 0, 0, 0, 8, 0, 0, 0, 0]
]

board9 = [
         [5, 0, 0, 0, 3, 0, 4, 0, 7],
         [3, 0, 2, 6, 0, 0, 9, 0, 0],
         [0, 0, 7, 0, 4, 0, 0, 8, 0],
         [0, 2, 6, 0, 0, 0, 8, 0, 1],
         [0, 0, 0, 7, 6, 0, 0, 4, 0],
         [4, 7, 0, 0, 0, 0, 2, 0, 0],
         [2, 1, 0, 0, 0, 0, 7, 0, 0],
         [0, 0, 4, 0, 0, 6, 5, 0, 0],
         [0, 0, 0, 0, 9, 7, 0, 3, 0]
]



# Below are helper functions that are used in
# the GUI as well as two functions from 
# SudokuSolver.py that are also used in the GUI.


# This function finds the next index in the Sudoku
# (a list of lists) that contains a zero. If a zero
# still remains on the board it returns the index 
# in the form (row, column) and if there are no zeros left
# then it returns -1, -1
def findZeros(sudoku):
    check = False

    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                check = True
                break
        if check:
            break


    if check:
        return i, j
    else:
        return -1, -1
    

# Performs a search through every column and row
# of the sudoku to see if num is a valid
# number to place at the indice sudoku[x][y].
# Returns True if its a valid move, false otherwise
def validMove(sudoku, x, y, num):
    for i in range(len(sudoku)):
        if sudoku[x][i] == num:
            return False

    for j in range(len(sudoku)):
        if sudoku[j][y] == num:
            return False

    for k in range(0,3):
        for l in range(0,3):
            if sudoku[((x//3) * 3) + k][((y//3) * 3) + l] == num:
                return False

    return True

