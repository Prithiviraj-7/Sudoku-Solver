import pygame
import sudoku_solver

pygame.init()

background_color = (0,0,0)
line_color =(255,255,255)
num_color = (143,0,255)
num_font = pygame.font.Font(None,48)

grid = [[0 for i in range(9)] for j in range(9)]

def print_grid():
    screen = pygame.display.set_mode([550,550])
    pygame.display.set_caption("SUDOKU SOLUTION")
    screen.fill(background_color)
    
    for i in range(10):
        if i%3 == 0:
            width = 4
        else:
            width = 2
        pygame.draw.line(screen,line_color,(50 + 50*i,50),(50 + 50*i,500),width)
        pygame.draw.line(screen,line_color,(50,50 + 50*i),(500, 50 + 50*i),width)
    pygame.display.update()

    for i in range(9):
        for j in range(9):
            if 0<grid[i][j]<10:
                value = num_font.render(str(grid[i][j]),True,num_color)
                screen.blit(value, ((j+1)*50 + 15,(i+1)*50 + 15))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def get_input(screen,pos):

    row = pos[1]//50
    col = pos[0]//50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if 48 <= event.key < 58:
                    grid[row-1][col-1] = event.key - 48
                    pygame.draw.rect(screen,background_color,(col*50 + 4,row*50 + 4,50 - 7,50 - 7))
                    value = num_font.render(str(event.key-48),True,num_color) 
                    screen.blit(value,(col*50 + 15,row*50 + 15))             
                    pygame.display.update()  
                    return
                return
                   
def input_grid():
    screen = pygame.display.set_mode([550,550])
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)

    for i in range(10):
        if i%3 == 0:
            width = 4
        else:
            width = 2
        pygame.draw.line(screen,line_color,(50 + 50*i,50),(50 + 50*i,500),width)
        pygame.draw.line(screen,line_color,(50,50 + 50*i),(500, 50 + 50*i),width)
    pygame.display.update()

    for i in range(9):
        for j in range(9):
            if 0<grid[i][j]<10:
                value = num_font.render(str(grid[i][j]),True,num_color)
                screen.blit(value, ((j+1)*50 + 15,(i+1)*50 + 15))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button ==1:
                pos = pygame.mouse.get_pos()
                get_input(screen,pos)                

input_grid()

if sudoku_solver.solve(grid):
    print_grid()
else:
    print("No Solution exists")
