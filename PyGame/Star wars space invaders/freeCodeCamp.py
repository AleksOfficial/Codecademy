import pygame
import random
import math
import os
import time
from pygame import mixer

pygame.init()

#set_mode((width -> x,height -> y))
screen = pygame.display.set_mode((800,600))

#Event -> Anything that happens in that window, even movement of a mouse

#Gameassets n stuff
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Pygame\\gameassets\\icons\\transport.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Pygame\\gameassets\\background\\space.jpg")
mixer.music.load("Pygame\\gameassets\\sounds\\Background.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

#Player
playerImg = pygame.image.load("Pygame\\gameassets\\icons\\X_Wing_smaller.png")
playerX = 370
playerY = 480
playerX_change = 0

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Enemies
enemyImg = []
enemyX = []
enemyY =[]
enemyX_change = []
enemyY_change=[]
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Pygame\\gameassets\\icons\\Enemy_Spacefighter{}.png".format(random.randint(1,5))))
    enemyX.append(random.randint(0,700))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(10)


#Laserbolt_enemy
#Needs completion
Enemy_Laserbolt_Img = pygame.image.load("Pygame\\gameassets\\icons\\Enemy_Laserbolt.png")
Player_LaserboltX = 0
Player_LaserboltY = 480
Player_LaserboltX_change = 0
Player_LaserboltY_change = 10
Player_Laserbolt_state = "ready"
sound = True
Player_lasersound1 = mixer.Sound("pygame\\gameassets\\sounds\\Player_Laserbolt1.wav")
bullet_sound = 0 

#Laserbolt_player
# Ready -> You can't see the bullet on the screen
# Fire -> The bullet is currently moving
Player_Laserbolt_Img = pygame.image.load("Pygame\\gameassets\\icons\\Player_Laserbolt.png")
#Player_LaserboltX = 0
#Player_LaserboltY = 0
Player_LaserboltX_change = 0
Player_LaserboltY_change = 10
Player_Laserbolt_state = "ready"
sound = True
Player_lasersound1 = mixer.Sound("pygame\\gameassets\\sounds\\Player_Laserbolt1.wav")
bullet_sound = 0 

def show_score(x,y):
    score = font.render("Score : {}".format(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg, (x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
    
def fire_bullet(x,y):
    
    global Player_Laserbolt_state
    Player_Laserbolt_state = "fire"
    screen.blit(Player_Laserbolt_Img,(x-7,y-15))
    screen.blit(Player_Laserbolt_Img,(x+40,y-15))
    
def isCollision(enemyX,enemyY,boltx,bolty):
    distance = math.sqrt(math.pow(enemyX-(boltx-7),2)+math.pow(enemyY-bolty,2))
    distance2 = math.sqrt(math.pow(enemyX-(boltx+40),2)+math.pow(enemyY-bolty,2))
    if distance<27:
        return True
    if distance2 <27:
        return True
    else:
        return False

# Game Loop
running = True
Left_bool = False
Right_bool = False
Up_bool = False
down_bool = False

while running:
    screen.blit(background,(0,0))
    show_score(textX,textY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Left_bool = True
            if event.key == pygame.K_RIGHT:
                Right_bool = True
            if event.key == pygame.K_SPACE:
                #Player_lasersound1.play()
                Player_Laserbolt_state = "fire"
            if event.key == pygame.K_UP:
                Up_bool = True
            if event.key == pygame.K_DOWN:
                down_bool = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Left_bool = False
            if event.key == pygame.K_RIGHT:
                Right_bool = False
            if event.key == pygame.K_UP:
                Up_bool = False
            if event.key == pygame.K_DOWN:
                down_bool = False
    # RGB Values -> Changes the screen Color. it can also be an image
    #Movement of player
    if Left_bool:
        playerX -=5
    if Right_bool:
        playerX +=5
    if Up_bool:
        playerY -=5
    if down_bool:
        playerY += 5
    #Restriction of Boundaries
    if playerX <=0:
        playerX =0
    elif playerX >=736:
        playerX = 736
    for i in range(num_of_enemies):
        enemy(enemyX[i],enemyY[i],i)
        enemyX[i] += enemyX_change[i]
    
        if enemyX[i] <=0:
            enemyX_change[i] =2.5
            enemyY[i] += enemyY_change[i] 
        elif enemyX[i] >=736:
            enemyX_change[i] =-2.5
            enemyY[i] += enemyY_change[i]  
        
            #collision
        collision = isCollision(enemyX[i],enemyY[i],Player_LaserboltX,Player_LaserboltY)
        #print(collision)
        if collision:
            explosion = mixer.Sound("pygame\\gameassets\\sounds\\Explosion {}.wav".format(random.randint(1,13)))
            explosion.play()
            Player_LaserboltY = 480
            Player_Laserbolt_state = "ready"
            score_value+=10
            enemyX[i] = random.randint(0,700)
            enemyY[i] = random.randint(50,150)
    
    if Player_Laserbolt_state =="ready":
        Player_LaserboltX = 999
        Player_LaserboltY = 999
        sound = True
    
    #Bullet Movement
    if Player_LaserboltY <= 0:
        Player_LaserboltY=480
        Player_Laserbolt_state="ready"
        

    if Player_Laserbolt_state == "fire":
        if Player_LaserboltX>800:
            Player_LaserboltX = playerX
            Player_LaserboltY = playerY
        
        if sound:
            Player_lasersound1.play()
            sound = False
        fire_bullet(Player_LaserboltX,Player_LaserboltY)
        Player_LaserboltY -= Player_LaserboltY_change
    print(sound)

    player(playerX,playerY)
    pygame.display.update()