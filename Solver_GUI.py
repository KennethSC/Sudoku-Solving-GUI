import pygame
import time
from SudokuImport import *

pygame.init()
pygame.font.init()

FPS = 30
FPSCLOCK = pygame.time.Clock()
BLUE = (51, 153, 255)
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)


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

        pygame.draw.line(self.screen, BLACK, (0, 9*gap), (self.width, 9*gap), 5)
        pygame.draw.line(self.screen, BLACK, (9 * gap, 0), (9 * gap, self.height), 5)



    def changeBoard(self,boardNum):
        self.cells = [[Cube(boardNum[i][j], i, j, self.height, self.width) for j in range(self.col)] for i in range(self.row)]


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



class Cube:

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
        screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)



def main():
    global FPS, FPSCLOCK

    window = pygame.display.set_mode((543, 543))
    pygame.display.set_caption("Sudoku Solver Via the Backtracking Algorithm")
    board = SudoBoard(9, 9, 540, 540, window)
    board.changeBoard(board1)
    board.update_instance()
    run, check = True, True
    speed = 1

    while run:

        window.fill((255,255,255))
        board.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        while check:
            Intro(window)
            check = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if speed == 1 or speed == 2 or speed == 3:
                        VizStart = time.time()
                        board.SudokuSolveGUI(300)
                        VizElapsed = (time.time() - VizStart)
                    elif speed == 4:
                        VizStart = time.time()
                        board.SudokuSolveGUI(100)
                        VizElapsed = (time.time() - VizStart)
                    else:
                        VizStart = time.time()
                        board.SudokuSolveGUI(90)
                        VizElapsed = (time.time() - VizStart)

                    if int(VizElapsed) == 0:
                        Error = True
                        while Error:
                            boardError(window)
                            Error = False
                    else:
                        Go = True
                        while Go:
                            DisplayStats(window, VizElapsed)
                            Go = False

                if event.key == pygame.K_1:
                    speed = 1
                    board.changeBoard(board1)
                    board.update_instance()
                    pygame.display.update()
                
                if event.key == pygame.K_2:
                    speed = 2
                    board.changeBoard(board2)
                    board.update_instance()
                    pygame.display.update()

                if event.key == pygame.K_3:
                    speed = 3
                    board.changeBoard(board3)
                    board.update_instance()
                    pygame.display.update()

                if event.key == pygame.K_4:
                    speed = 4
                    board.changeBoard(board4)
                    board.update_instance()
                    pygame.display.update()

                if event.key == pygame.K_5:
                    speed = 5
                    board.changeBoard(board5)
                    board.update_instance()
                    pygame.display.update()


main()
pygame.quit()

