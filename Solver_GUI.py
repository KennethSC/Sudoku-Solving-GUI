'''
Run this file in the same directory
as SudokuImport.py
'''
import pygame
import time
from SudokuImport import *

pygame.init()
pygame.font.init()

FPS = 30
speed = None
FPSCLOCK = pygame.time.Clock()

class SudoBoard():

    def __init__(self, row, col, height, width, screen):
        self.row = row
        self.col = col
        self.cells = None 
        self.height = height
        self.width = width
        self.instance = None
        self.screen = screen

    def update_instance(self):
        self.instance = [[self.cells[i][j].value for j in range(self.col)] for i in range(self.row)]

    def draw(self):
        gap = self.width / 9 
        # Draw Grid Lines
        for i in range(self.row+1):
            if i == 3 or i == 0 or i == 6:
                pygame.draw.line(self.screen, BLACK, (0, i*gap), (self.width, i*gap), 5)
                pygame.draw.line(self.screen, BLACK, (i * gap, 0), (i * gap, self.height), 5)
            else:
                pygame.draw.line(self.screen, BLACK, (0, i*gap), (self.width, i*gap), 1)
                pygame.draw.line(self.screen, BLACK, (i * gap, 0), (i * gap, self.height), 1)
        
        for i in range(self.row):
            for j in range(self.col):
                self.cells[i][j].fill_In(self.screen)

        pygame.draw.line(self.screen, BLACK, (0, 9*gap), (self.width, 9*gap), 15)
        pygame.draw.line(self.screen, BLACK, (9 * gap, 0), (9 * gap, self.height), 5)


    def changeBoard(self,boardNum):
        self.cells = [[Cell(boardNum[i][j], i, j, self.height, self.width) for j in range(self.col)] for i in range(self.row)]
        self.update_instance()
        pygame.display.update()


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


    def SudokuSolveGUI(self, speed):
        status = False

        row, col = findZeros(self.instance)

        if row == -1 and col == -1:
            status = True
            return status

        for i in range(1, 10):
            if validMove(self.instance, row, col, i):
                self.instance[row][col] = i
                self.cells[row][col].value = i
                self.cells[row][col].draw_change(self.screen, True)
                self.update_instance()
                pygame.display.update()
                pygame.time.delay(speed)

                status = self.SudokuSolveGUI(speed)
                if status:
                    return True

                self.instance[row][col] = 0
                self.cells[row][col].value = 0
                self.update_instance()
                self.cells[row][col].draw_change(self.screen, False)
                pygame.display.update()
                pygame.time.delay(speed)

        return status


class Cell:

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def fill_In(self, screen):
        fnt = pygame.font.SysFont("sfnsdisplayblackitalicotf", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, BLACK)
            screen.blit(text, (x+5, y+5))
        elif (self.value != 0):
            text = fnt.render(str(self.value), 1, BLUE)
            screen.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))


    def draw_change(self, screen, g=True):
        fnt = pygame.font.SysFont("sfnsdisplayblackitalicotf", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(screen, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap/ 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def drawButton(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont("comicsans", 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


    def checkBlue(self, pos):
        if self.isOver(pos):
            self.color = (0, 122, 199)
        else:
            self.color = BLUE


    def updateBoard(self, bo, pos, velocity, boardNum):
        global speed

        if self.isOver(pos):
            speed = velocity
            bo.changeBoard(boardNum)


def main():
    global FPS, FPSCLOCK, speed

    window = pygame.display.set_mode((543, 640))
    pygame.display.set_caption("Sudoku Solver Via the Backtracking Algorithm")
    board = SudoBoard(9, 9, 540, 540, window)
    board.changeBoard(board1)
    board.update_instance()

    Button1 = button(BLUE, 0, 543, 80, 50, 'Board 1')
    Button2 = button(BLUE, 80, 543, 80, 50, 'Board 2')
    Button3 = button(BLUE, 160, 543, 80, 50, 'Board 3')
    Button4 = button(BLUE, 240, 543, 80, 50, 'Board 4')
    Button5 = button(BLUE, 320, 543, 80, 50, 'Board 5')
    Button6 = button(BLUE, 0, 590, 80, 50, 'Board 6')
    Button7 = button(BLUE, 80, 590, 80, 50, 'Board 7')
    Button8 = button(BLUE, 160, 590, 80, 50, 'Board 8')
    Button9 = button(BLUE, 240, 590, 80, 50, 'Board 9')
    Solve = button(GREEN, 404, 540, 137, 100, 'SOLVE') 
    Clear = button(RED, 320, 590, 80, 50, 'CLEAR') 

    run = True

    while run:

        window.fill((255,255,255))
        board.draw()

        Button1.drawButton(window, BLACK)
        Button2.drawButton(window, BLACK)
        Button3.drawButton(window, BLACK)
        Button4.drawButton(window, BLACK)
        Button5.drawButton(window, BLACK)
        Button6.drawButton(window, BLACK)
        Button7.drawButton(window, BLACK)
        Button8.drawButton(window, BLACK)
        Button9.drawButton(window, BLACK)
        Solve.drawButton(window, BLACK)
        Clear.drawButton(window, BLACK)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        for event in pygame.event.get():
            MousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if Solve.isOver(MousePos):

                    if speed == 1 or speed == 2 or speed == 3:
                        board.SudokuSolveGUI(350)
                        
                    elif speed == 4:
                        board.SudokuSolveGUI(200)
                
                    elif speed == 9:
                        board.SudokuSolveGUI(80)
                        
                    else:
                        board.SudokuSolveGUI(90)
                        
                if Clear.isOver(MousePos):
                    board.ClearBoard(speed)

                Button1.updateBoard(board, MousePos, 1, board1)
                Button2.updateBoard(board, MousePos, 2, board2)
                Button3.updateBoard(board, MousePos, 3, board3)
                Button4.updateBoard(board, MousePos, 4, board4)
                Button5.updateBoard(board, MousePos, 5, board5)
                Button6.updateBoard(board, MousePos, 6, board6)
                Button7.updateBoard(board, MousePos, 7, board7)
                Button8.updateBoard(board, MousePos, 8, board8)
                Button9.updateBoard(board, MousePos, 9, board9)
    

            if event.type == pygame.MOUSEMOTION:
                if Solve.isOver(MousePos):
                    Solve.color = (0, 100, 0)
                else:
                    Solve.color = GREEN

                if Clear.isOver(MousePos):
                    Clear.color = (139, 0, 0)
                else:
                    Clear.color = RED

                Button1.checkBlue(MousePos)
                Button2.checkBlue(MousePos)
                Button3.checkBlue(MousePos)
                Button4.checkBlue(MousePos)
                Button5.checkBlue(MousePos)
                Button6.checkBlue(MousePos)
                Button7.checkBlue(MousePos)
                Button8.checkBlue(MousePos)
                Button9.checkBlue(MousePos)


main()
pygame.quit()
