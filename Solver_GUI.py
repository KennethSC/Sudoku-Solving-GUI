import pygame
import pygame_menu
import time
from SudokuBoards import *

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
        #self.update_instance()
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




class Cube:
    #rows = 9
    #cols = 9

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



def main():
    global FPS, FPSCLOCK


    window = pygame.display.set_mode((543, 543))
    pygame.display.set_caption("Sudoku Solver Via the Backtracking Algorithm")
    board = SudoBoard(9, 9, 540, 540, window)
    board.changeBoard(board1)
    run = True
    menu = True
    

    while run:

        window.fill((255,255,255))
        board.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                #    board.SudokuSolveGUI()

                if event.key == pygame.K_1:
                    board.changeBoard(board1)
                    pygame.display.update()
                
                if event.key == pygame.K_2:
                    board.changeBoard(board2)
                    pygame.display.update()

                if event.key == pygame.K_3:
                    board.changeBoard(board3)
                    pygame.display.update()

                if event.key == pygame.K_4:
                    board.changeBoard(board4)
                    pygame.display.update()

                if event.key == pygame.K_5:
                    board.changeBoard(board5)
                    pygame.display.update()

                if event.key == pygame.K_6:
                    board.changeBoard(board6)
                    pygame.display.update()

                if event.key == pygame.K_7:
                    board.changeBoard(board7)
                    pygame.display.update()

                if event.key == pygame.K_8:
                    board.changeBoard(board8)
                    pygame.display.update()

                if event.key == pygame.K_9:
                    board.changeBoard(board9)
                    pygame.display.update()

    

main()
pygame.quit()

