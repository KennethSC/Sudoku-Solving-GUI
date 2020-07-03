from SudokuImport import *

'''
This python script takes in a Sudoku board (a list of lists)
from the file SudokuImport.py and returns the formatted solved
sudoku board to the command line. Run this program in the same
directory as SudokuImport.py
'''

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
        


# Prints out the Sudoku board
# in a neat and readable way
# to the command line
def printSudoku(sudoku):
    print("\n")

    for i in range(len(sudoku)):
        row = ""
        if i == 3 or i == 6 or i == 0:
            print("-" * 25)

        for j in range(len(sudoku)):
            if j == 3 or j == 6 or j == 0:
                row += "| "

            row += str(sudoku[i][j]) + " "

        print(row + "|")


    print("-" * 25)
    print("\n")



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
            if sudoku[((x//3)*3)+k][((y//3)*3)+l] == num:
                return False

    return True



# Solves the sudoku board using 
# the Backtracking Algorithm
def solveSudoku(sudoku):
    status = False

    row, col = findZeros(sudoku)
    
    if row == -1 and col == -1:
        status = True
        return status

    for i in range(1, 10):
        if validMove(sudoku, row, col, i):
            sudoku[row][col] = i

            status = solveSudoku(sudoku)
            if status:
                return True

            sudoku[row][col] = 0

    return status



# You could try the solveSudoku function
# on different sudoku boards from the file 
# SudokuImports.py, just change the number of the board
# to any number from 1-9.The difficulty increases
# the further down the sudokus are. Make sure to 
# run this file in the same directory as SudokuBoards.py.

if solveSudoku(board4):
    printSudoku(board4)
else:
    print("This sudoku has no solution")



