# SUDOKUUUUUU
import pygame
import time
pygame.init()
pygame.font.init()
pygame.display.set_caption("Sudoku")



WIDTH,HEIGHT = 600,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
path = "PyGame\\Sudoku\\"
icon = pygame.image.load(path+"spiel.png")
pygame.display.set_icon(icon)
gameclock = pygame.time.Clock()
click = False
clicked = False

grid = [[]]
def main_menu():
    global clicked
    global click
    run = True
    mainfont = pygame.font.SysFont(None,28)
    titlefont = pygame.font.SysFont(None,128)
    title=titlefont.render("SUDOKU",1,(30,30,30))
    create_puzzle_label = mainfont.render("Create custom puzzle",1,(0,0,0))
    play_user_label = mainfont.render("Play your puzzles",1,(0,0,0))
    play_random_label = mainfont.render("Play random 9x9 puzzle",1,(0,0,0))
    create_puzzle_label = mainfont.render("Create custom Puzzle",1,(0,0,0))
    load_saved_game_label = mainfont.render("Load saved game",1,(0,0,0))
    exit_label = mainfont.render("Exit",1,(0,0,0))
    lx,ly = 0,0
      
    while run:
        
        SCREEN.fill((255,255,255))
        SCREEN.blit(title,(WIDTH/2-title.get_width()/2,10+title.get_height()))
        mx,my = pygame.mouse.get_pos()
        cpborder_1 = pygame.Rect(WIDTH/2-127,HEIGHT*0.4+3,254,49)
        pygame.draw.rect(SCREEN,(0,0,0),cpborder_1)
        cpbutton_1 = pygame.Rect(WIDTH/2-125,HEIGHT*0.4+5,250,45)
        if cpbutton_1.collidepoint((mx,my)):
            pygame.draw.rect(SCREEN,(150,190,225),cpbutton_1)
            if click:
                pygame.draw.rect(SCREEN,(140,170,225),cpbutton_1)

        else:
            pygame.draw.rect(SCREEN,(255,255,255),cpbutton_1)
        SCREEN.blit(create_puzzle_label,(WIDTH/2-create_puzzle_label.get_width()/2,HEIGHT*0.4+create_puzzle_label.get_height()))
        cpborder_2 = pygame.Rect(WIDTH/2-127,HEIGHT*0.4+3+50,254,49)
        pygame.draw.rect(SCREEN,(0,0,0),cpborder_2)
        cpbutton_2 = pygame.Rect(WIDTH/2-125,HEIGHT*0.4+55,250,45)
        
        if cpbutton_2.collidepoint((mx,my)):
            
            pygame.draw.rect(SCREEN,(150,190,225),cpbutton_2)
            if click:
                pygame.draw.rect(SCREEN,(140,170,225),cpbutton_2)
        else:
            pygame.draw.rect(SCREEN,(255,255,255),cpbutton_2)
        SCREEN.blit(play_user_label,(WIDTH/2-play_user_label.get_width()/2,HEIGHT*0.4+50+play_user_label.get_height()))
        cpborder_3 = pygame.Rect(WIDTH/2-127,HEIGHT*0.4+3+100,254,49)
        pygame.draw.rect(SCREEN,(0,0,0),cpborder_3)
        cpbutton_3 = pygame.Rect(WIDTH/2-125,HEIGHT*0.4+105,250,45)
        if cpbutton_3.collidepoint((mx,my)):
            pygame.draw.rect(SCREEN,(150,190,225),cpbutton_3)
            if click:
                pygame.draw.rect(SCREEN,(140,170,225),cpbutton_3)
        else:
            pygame.draw.rect(SCREEN,(255,255,255),cpbutton_3)
        SCREEN.blit(play_random_label,(WIDTH/2-play_random_label.get_width()/2,HEIGHT*0.4+100+play_random_label.get_height()))
        cpborder_4 = pygame.Rect(WIDTH/2-127,HEIGHT*0.4+3+150,254,49)
        pygame.draw.rect(SCREEN,(0,0,0),cpborder_4)
        cpbutton_4 = pygame.Rect(WIDTH/2-125,HEIGHT*0.4+155,250,45)
        if cpbutton_4.collidepoint((mx,my)):
            pygame.draw.rect(SCREEN,(150,190,225),cpbutton_4)
            if click:
                pygame.draw.rect(SCREEN,(140,170,225),cpbutton_4)

        else:
            pygame.draw.rect(SCREEN,(255,255,255),cpbutton_4)
        SCREEN.blit(load_saved_game_label,(WIDTH/2-load_saved_game_label.get_width()/2,HEIGHT*0.4+150+play_random_label.get_height()))
        cpborder_5 = pygame.Rect(WIDTH/2-127,HEIGHT*0.4+3+200,254,49)
        pygame.draw.rect(SCREEN,(0,0,0),cpborder_5)
        cpbutton_5 = pygame.Rect(WIDTH/2-125,HEIGHT*0.4+205,250,45)
        if cpbutton_5.collidepoint((mx,my)):
            pygame.draw.rect(SCREEN,(150,190,225),cpbutton_5)
            if click:
                pygame.draw.rect(SCREEN,(140,170,225),cpbutton_5)
        else:
            pygame.draw.rect(SCREEN,(255,255,255),cpbutton_5)
        #Menu Functionality
        if cpbutton_1.collidepoint((lx,ly)):
            create_sudoku()
        elif cpbutton_2.collidepoint((lx,ly)):
            exit()
        elif cpbutton_3.collidepoint((lx,ly)):
            exit()
        elif cpbutton_4.collidepoint((lx,ly)):
            exit()
        elif cpbutton_5.collidepoint((lx,ly)):
            exit()
        


        SCREEN.blit(exit_label,(WIDTH/2-exit_label.get_width()/2,HEIGHT*0.4+200+play_random_label.get_height()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
                lx,ly = pygame.mouse.get_pos()
                
            

        pygame.display.update()
        gameclock.tick(60)
        

main_menu()

# Basic Requirements

# User Story: As a user I want to be able to input a valid starting sudoku board.

#     This can be done in pieces (one box/row/column at a time) or all at once.

# User Store: As a user I want to be able to choose to use the most recent starting board.

#     Board can be hard-coded initially to help you get started, since the focal point of this project is the implementation of minimax. This will also streamline testing, as it won’t be necessary to manually input a board each you run the program.

# User Story: As a user I want to be able to quit the program or go again after each cycle.
# Additional Challenges

# Intermediate Challenge

# User Story: As a user I want to be able to switch between 4x4, 9x9 and 16x16 configurations.

# Advanced Challenge

#User Story: As a user I want the program to save the output, in addition to printing to console, so that it can be preserved and accessed separately.