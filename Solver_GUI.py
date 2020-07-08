#Run this file in the same directory as SudokuImport.py

import pygame
from SudokuImport import *

pygame.init()
pygame.font.init()

FPS = 30
speed = 1
FPSCLOCK = pygame.time.Clock()


class SudoBoard():

    def __init__(self, row, col, height, width, screen):
        self.row = row
        self.col = col
        self.height = height
        self.width = width
        self.screen = screen
        self.cells = None 
        self.instance = None


    # Draws Sudoku Board
    def draw_Sudo_Board(self):
        space = self.width / self.row 

        for i in range(self.row):
            if i == 3 or i == 0 or i == 6:
                pygame.draw.line(self.screen, BLACK, (0, i * space), (self.width, i * space), 5)
                pygame.draw.line(self.screen, BLACK, (i * space, 0), (i * space, self.height), 5)
            else:
                pygame.draw.line(self.screen, BLACK, (0, i * space), (self.width, i * space), 1)
                pygame.draw.line(self.screen, BLACK, (i * space, 0), (i * space, self.height), 1)
        
        # Fills in the cells of the board
        # with the numbers of specified board
        for i in range(self.row):
            for j in range(self.col):
                self.cells[i][j].fill_In(self.screen)

        # Draws the bottom line thicker to 
        # seperate the board from the buttons
        pygame.draw.line(self.screen, BLACK, (0, 9 * space), (self.width, 9 * space), 15)
        pygame.draw.line(self.screen, BLACK, (9 * space, 0), (9 * space, self.height), 5)


    # Changes to the specified board
    def changeBoard(self,boardNum):
        self.cells = [[Cell(boardNum[i][j], i, j, self.height, self.width) for j in range(self.col)] for i in range(self.row)]
        self.update_Board_Instance()
        pygame.display.update()


    # Updates the board when a change is made 
    def update_Board_Instance(self):
        self.instance = [[self.cells[i][j].value for j in range(self.col)] for i in range(self.row)]


    # Clears the board back to its original state
    def ClearBoard(self, BoardNum):
        if BoardNum == 1:
            self.changeBoard(board1)
        elif BoardNum == 2:
            self.changeBoard(board2)
        elif BoardNum == 3:
            self.changeBoard(board3)
        elif BoardNum == 4:
            self.changeBoard(board4)
        elif BoardNum == 5:
            self.changeBoard(board5)
        elif BoardNum == 6:
            self.changeBoard(board6)
        elif BoardNum == 7:
            self.changeBoard(board7)
        elif BoardNum == 8:
           self.changeBoard(board8)
        else:
            self.changeBoard(board9)


    # Visualizes backtracking algorithm
    # on the screen
    def SudokuSolveGUI(self, speed):
        status = False
        row, col = findZeros(self.instance)

        if row == -1 and col == -1:
            status = True
            return status

        for i in range(1, 10):
            if validMove(self.instance, row, col, i):
                self.cells[row][col].value = i
                self.cells[row][col].new_Entry(self.screen, True, LIGHT_GREEN)

                self.update_Board_Instance()
                pygame.display.update()
                pygame.time.delay(speed)

                status = self.SudokuSolveGUI(speed)
                if status:
                    return True

                self.cells[row][col].value = 0
                self.cells[row][col].new_Entry(self.screen, False, RED)

                self.update_Board_Instance()
                pygame.display.update()
                pygame.time.delay(speed)

        return status



class Cell:

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.tempVal = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    # Fills in each cell with the appropriate value
    # according to the specified sudoku board
    def fill_In(self, screen):
        numFont = pygame.font.SysFont("sfnsdisplayblackitalicotf", 42)

        space = self.width / 9
        x = self.col * space
        y = self.row * space

        if self.tempVal != 0 and self.value == 0:
            num = numFont.render(str(self.tempVal), 1, BLACK)
            screen.blit(num, (x, y))

        elif self.value:
            num = numFont.render(str(self.value), 1, BLUE)
            screen.blit(num, (x + 17, y + 3))


    # Updates the board when a new entry is placed
    # or when a zero is placed while the algorithm is running
    def new_Entry(self, screen, valid, color):
        numFont = pygame.font.SysFont("sfnsdisplayblackitalicotf", 42)

        space = self.width / 9
        x = self.col * space
        y = self.row * space
        coordinates = (x, y, space, space)

        pygame.draw.rect(screen, WHITE, coordinates, 0)

        num = numFont.render(str(self.value), 1, BLACK)
        screen.blit(num, (x + 17, y + 3))

        if valid:
            pygame.draw.rect(screen, color, coordinates, 6)
        else:
            pygame.draw.rect(screen, color, coordinates, 6)


class button():

    def __init__(self, color, x, y, width, height, message):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.message = message

    # Draws the button onto the pygame window
    def make_Button(self, screen, border, txtSize):
        if border != None:
            pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2 ,self.width + 4, self.height + 4), 0)
            
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.message != None:
            txt = pygame.font.SysFont("sfnsdisplayblackitalicotf", txtSize)
            message = txt.render(self.message, 1, BLACK)
            screen.blit(message, (self.x + (self.width/2 - message.get_width()/2), self.y + (self.height/2 - message.get_height()/2)))


    # Checks if the mouse is over specified button
    def if_Hovering(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            else:
                return False


    # Makes the button color a darker shade if mouse is over the button
    def change_Button_Color(self, pos, newCol, defaultCol):
        if self.if_Hovering(pos):
            self.color = newCol
        else:
            self.color = defaultCol
    

    # If a button to change boards was pressed, then it switches to that board
    # and sets the new speed to solve that specific board
    def if_Clicked(self, sudoBoard, pos, velocity, boardNum):
        global speed

        if self.if_Hovering(pos):
            speed = velocity
            sudoBoard.changeBoard(boardNum)


def main():
    global FPS, FPSCLOCK, speed

    # Intitialize pygame window and Sudoku board
    window = pygame.display.set_mode((543, 640))
    pygame.display.set_caption("Sudoku Solver Via the Backtracking Algorithm")
    board = SudoBoard(9, 9, 540, 540, window)
    board.changeBoard(board1)
    board.update_Board_Instance()

    # Initialize buttons
    Button1 = button(BLUE, 0, 543, 80, 50, 'Board 1')
    Button2 = button(BLUE, 80, 543, 80, 50, 'Board 2')
    Button3 = button(BLUE, 160, 543, 80, 50, 'Board 3')
    Button4 = button(BLUE, 240, 543, 80, 50, 'Board 4')
    Button5 = button(BLUE, 320, 543, 80, 50, 'Board 5')
    Button6 = button(BLUE, 0, 590, 80, 50, 'Board 6')
    Button7 = button(BLUE, 80, 590, 80, 50, 'Board 7')
    Button8 = button(BLUE, 160, 590, 80, 50, 'Board 8')
    Button9 = button(BLUE, 240, 590, 80, 50, 'Board 9')
    Solve = button(GREEN, 404, 543, 137, 96, 'SOLVE') 
    Clear = button(RED, 320, 590, 80, 50, 'CLEAR') 

    run = True

    while run:

        # Draw out the Sudoku Board with a white background
        window.fill(WHITE)
        board.draw_Sudo_Board()

        # Draw buttons onto screen
        Button1.make_Button(window, BLACK, 17)
        Button2.make_Button(window, BLACK, 17)
        Button3.make_Button(window, BLACK, 17)
        Button4.make_Button(window, BLACK, 17)
        Button5.make_Button(window, BLACK, 17)
        Button6.make_Button(window, BLACK, 17)
        Button7.make_Button(window, BLACK, 17)
        Button8.make_Button(window, BLACK, 17)
        Button9.make_Button(window, BLACK, 17)
        Solve.make_Button(window, BLACK, 21)
        Clear.make_Button(window, BLACK, 17)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        for event in pygame.event.get():
            # Gets the current position of the mouse
            MousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Checks if the solve button was pressed
                if Solve.if_Hovering(MousePos):

                    if speed == 1 or speed == 2 or speed == 3 or speed == 4:
                        board.SudokuSolveGUI(350)
                    elif speed == 9:
                        board.SudokuSolveGUI(80)
                    else:
                        board.SudokuSolveGUI(100)
                        
                # Checks if Clear button was pressed
                if Clear.if_Hovering(MousePos):
                    board.ClearBoard(speed)
                
                # Checks if user pressed button to change boards
                Button1.if_Clicked(board, MousePos, 1, board1)
                Button2.if_Clicked(board, MousePos, 2, board2)
                Button3.if_Clicked(board, MousePos, 3, board3)
                Button4.if_Clicked(board, MousePos, 4, board4)
                Button5.if_Clicked(board, MousePos, 5, board5)
                Button6.if_Clicked(board, MousePos, 6, board6)
                Button7.if_Clicked(board, MousePos, 7, board7)
                Button8.if_Clicked(board, MousePos, 8, board8)
                Button9.if_Clicked(board, MousePos, 9, board9)
    
            if event.type == pygame.MOUSEMOTION:

                # Checks if mouse is hovering over each button
                Clear.change_Button_Color(MousePos, (139, 0, 0), RED)
                Solve.change_Button_Color(MousePos, (0, 100, 0), GREEN)
                
                Button1.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button2.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button3.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button4.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button5.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button6.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button7.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button8.change_Button_Color(MousePos, DARK_BLUE, BLUE)
                Button9.change_Button_Color(MousePos, DARK_BLUE, BLUE)


if __name__ == '__main__':
    main()
    pygame.quit()
