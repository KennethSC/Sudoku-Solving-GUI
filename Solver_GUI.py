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

        while menu:
            menuFont = pygame.font.Font('freesansbold.ttf', 25)
            line = menuFont.render('                                                                       ', True ,WHITE, BLACK)
            textRect = line.get_rect()
            textRect.center = (543//2, 334//2)
            window.blit(line, textRect)
            pygame.display.update()

            line1 = menuFont.render('                           Welcome!                           ', True, WHITE, BLACK)
            textRect1 = line1.get_rect()
            textRect1.center = (543//2, 380//2)
            window.blit(line1,textRect1)
            pygame.display.update()

            line8 = menuFont.render('                                                                       ', True ,WHITE, BLACK)
            textRect8 = line.get_rect()
            textRect8.center = (543//2, 431//2)
            window.blit(line8, textRect8)
            pygame.display.update()

            line2 = menuFont.render('      To change sudoku boards, press        ', True, WHITE, BLACK)
            textRect2 = line2.get_rect()
            textRect2.center = (543//2, 483//2)
            window.blit(line2,textRect2)
            pygame.display.update()

            line3 = menuFont.render('     any number key (1-9). To solve that      ', True, WHITE, BLACK)
            textRect3 = line3.get_rect()
            textRect3.center = (543 // 2, 533 // 2)
            window.blit(line3,textRect3)
            pygame.display.update()

            line4 = menuFont.render('              board, press the spacebar.           ', True, WHITE, BLACK)
            textRect4 = line4.get_rect()
            textRect4.center = (543 // 2, 583 // 2)
            window.blit(line4,textRect4)
            pygame.display.update()

            line5 = menuFont.render('                                                                       ', True, WHITE, BLACK)
            textRect5 = line5.get_rect()
            textRect5.center = (543 // 2, 633 // 2)
            window.blit(line5,textRect5)
            pygame.display.update()

            line6 = menuFont.render('            Press any key to continue.             ', True, WHITE, BLACK)
            textRect6 = line6.get_rect()
            textRect6.center = (543 // 2, 683 // 2)            
            window.blit(line6,textRect6)
            pygame.display.update()

            line7 = menuFont.render('                                                                       ', True ,WHITE, BLACK)
            textRect7 = line.get_rect()
            textRect7.center = (543//2, 733//2)
            window.blit(line7, textRect7)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    menu = False
                    break


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

