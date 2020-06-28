

# This function finds the next index in the Sudoku
# (a list of lists) that contains a zero. If a zero
# still remains on the board it returns the index 
# in the form row, column and if there are no zeros left
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



# Performs a seearch through every column and row
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
# the back tracking algorithm
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
# on different sudoku boards by uncommenting
# the different sudokus below. The difficulty
# increases the further down the sudokus are.

sudoku = [
         [7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


'''
sudoku = [
         [6, 0, 0, 5, 0, 0, 9, 0, 0],
         [8, 0, 1, 6, 0, 4, 2, 7, 0],
         [0, 0, 0, 0, 7, 2, 6, 0, 0],
         [0, 0, 0, 0, 8, 1, 7, 0, 4],
         [0, 0, 4, 0, 3, 0, 1, 0, 0],
         [0, 5, 0, 0, 0, 9, 0, 2, 3],
         [0, 0, 0, 0, 0, 6, 0, 0, 0],
         [0, 6, 0, 0, 0, 0, 4, 0, 0],
         [0, 0, 0, 3, 4, 0, 5, 0, 6]
]
'''

'''
sudoku = [
         [0, 0, 6, 0, 0, 0, 1, 0, 0],
         [2, 0, 0, 7, 0, 0, 3, 0, 0],
         [0, 5, 3, 0, 0, 0, 0, 4, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 3, 1, 0, 8, 0, 0, 2, 0],
         [8, 0, 0, 0, 0, 0, 0, 9, 4],
         [0, 0, 0, 5, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0, 0, 6],
         [9, 6, 2, 0, 0, 0, 0, 0, 0]
]
'''

'''
sudoku = [
         [0, 0, 0, 0, 0, 0, 2, 0, 0],
         [0, 8, 0, 0, 0, 7, 0, 9, 0],
         [6, 0, 2, 0, 0, 0, 5, 0, 0],
         [0, 7, 0, 0, 6, 0, 0, 0, 0],
         [0, 0, 0, 9, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 4, 0],
         [0, 0, 5, 0, 0, 0, 6, 0, 3],
         [0, 9, 0, 4, 0, 0, 0, 7, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
]
'''


if solveSudoku(sudoku):
    printSudoku(sudoku)
else:
    print("This sudoku has no solution")



