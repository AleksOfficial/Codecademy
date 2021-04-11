import pygame
import random
import math
import os
import time
import math
from pygame import mixer
pygame.font.init()
pygame.init()
#Event -> Anything that happens in that window, even movement of a mouse

#set_mode((width -> x,height -> y))
#Screen & Background
mainpath=""
WIDTH,HEIGHT = 1200,700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
mixer.music.load(mainpath+"gameassets\\sounds\\Background.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)


#Gameassets n stuff
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(mainpath+"gameassets\\icons\\transport.png")
pygame.display.set_icon(icon)
background = pygame.image.load(mainpath+"gameassets\\background\\space.jpg")



#ShipAssets Enemies:
shippath = "gameassets\icons"
Enemy_image_class1 = pygame.image.load(os.path.join((mainpath+shippath),"Enemy_Spacefighter1.png"))
Enemy_image_class2_right = pygame.image.load(os.path.join((mainpath+shippath),"Enemy_Spacefighter2_right.png"))
Enemy_image_class2_left = pygame.image.load(os.path.join((mainpath+shippath),"Enemy_Spacefighter2_left.png"))
Enemy_image_class3 = pygame.image.load(os.path.join((mainpath+shippath),"Enemy_Spacefighter3.png"))
Enemy_image_class4 = pygame.image.load(os.path.join((mainpath+shippath),"Enemy_Spacefighter4.png"))
Enemy_image_class5 = pygame.image.load(os.path.join((mainpath+shippath),"Enemy_Spacefighter5.png"))

#Player
playerImg = pygame.image.load(mainpath+"gameassets\\icons\\X_Wing_smaller.png")
x_coordinate = 0
y_coordinate = 0

#Powerups
Infinite_shield_img= pygame.image.load(os.path.join((mainpath+shippath),"Powerup1.png"))
Infinite_damage_img= pygame.image.load(os.path.join((mainpath+shippath),"Powerup2.png"))
bomb_img= pygame.image.load(os.path.join((mainpath+shippath),"Powerup3.png"))
regenerate_health_img= pygame.image.load(os.path.join((mainpath+shippath),"Powerup4.png"))

#Laserbolt_enemy
Enemy_Laserbolt_Img1 = pygame.image.load(mainpath+"gameassets\\icons\\Enemy_Laserbolt1.png")
Enemy_Laserbolt_Img2 = pygame.image.load(mainpath+"gameassets\\icons\\Enemy_Laserbolt2.png")
Enemy_Laserbolt_Img4 = pygame.image.load(mainpath+"gameassets\\icons\\Enemy_Laserbolt4.png")



#Laserbolt_player
soundpath = "gameassets\sounds"
Player_Laserbolt_Img = pygame.image.load(mainpath+"gameassets\\icons\\Player_Laserbolt.png")
Player_LaserboltY_change = 10
Player_Laserbolt_state = "ready"

#sounds
Player_lasersounds = [mixer.Sound(os.path.join((mainpath+soundpath),"x_wing_laser{}.wav".format(x))) for x in range(1,11)]
Enemy_Laserbolt_sounds1 = [mixer.Sound(os.path.join((mainpath+soundpath),"ion_shot{}.wav".format(x))) for x in range(1,4)]
Enemy_Laserbolt_sounds2_4 = [mixer.Sound(os.path.join((mainpath+soundpath),"tie_laser{}.wav".format(x))) for x in range(1,16)]
Hit_sounds = [mixer.Sound(os.path.join((mainpath+soundpath),"hit{}.wav".format(x))) for x in range(1,13)]
Shield_sounds = [mixer.Sound(os.path.join((mainpath+soundpath),"shield_hit{}.wav".format(x))) for x in range(1,8)]
Explosion_sounds = [mixer.Sound(os.path.join((mainpath+soundpath),"Explosion {}.wav".format(x))) for x in range(1,14)]
damage_critical = mixer.Sound(os.path.join((mainpath+soundpath),"damage_critical.wav"))
Destroyer_sounds = [mixer.Sound(os.path.join((mainpath+soundpath),"Destroyer{}.wav".format(x))) for x in range(1,4)]
powerup_sound = mixer.Sound(os.path.join((mainpath+soundpath),"powerupsound.wav"))
bomb_sound = mixer.Sound(os.path.join((mainpath+soundpath),"bomb.wav"))
class Powerup:
    powerups = {
                1:Infinite_shield_img,
                2:Infinite_damage_img,
                3:bomb_img,
                4:regenerate_health_img
    }
    def __init__(self,x,y,class_powerup):
        self.x = x
        self.y = y
        self.img = self.powerups[class_powerup]
        self.mask = pygame.mask.from_surface(self.img)
        self.class_powerup = class_powerup
        self.speed = 1.5
        
    def move(self):
        self.y += self.speed
    
    def get_width(self):
        return self.img.get_width()   
    
    def get_height(self):
        return self.img.get_height()
    def draw(self,window):
        window.blit(self.img, (self.x,self.y))

        

class Ship:
    COOLDOWN = 0
    def __init__(self,x,y,class_of_craft=0,shield = 0,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.shield = shield
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.class_of_craft = class_of_craft
        self.speed = 0
        self.damage = 0
        self.laserspeed = 0
        
        
    def hit(self,amount):
        if self.shield >0:
            self.shield -= amount
            if amount==2:
                self.shield = 0
            if self.class_of_craft == 0:
                Shield_sounds[random.randint(0,len(Shield_sounds)-1)].play()
        else:
            if amount==2:
                self.speed = self.speed /2
                if self.ionize_counter<=0:
                    self.ionize_counter = 0
                self.ionize_counter +=500
                if self.powerup_timer >300:
                    self.powerup_timer-=300
                else:
                    self.powerup_timer = 1
            self.health-= amount
            if self.class_of_craft == 0:
                Hit_sounds[random.randint(0,len(Hit_sounds)-1)].play()
            else:
                global score
                score +=10
    def draw(self,window):
        window.blit(self.ship_img, (self.x,self.y))
        for laser in self.lasers:
            laser.draw(window)
            
    def move_lasers(self,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move()
            if laser.off_screen(HEIGHT):
                if laser in self.lasers:
                    self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.isCollision(obj):
                        obj.hit(self.damage)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        if obj.health <=0:
                            objs.remove(obj)
                            global score
                            score +=100
                            Explosion_sounds[random.randint(0,len(Explosion_sounds)-1)].play()
        
    def cooldown(self):
        if self.cool_down_counter>0:
            if self.COOLDOWN >= self.cool_down_counter:
                self.COOLDOWN =0
            elif self.COOLDOWN >0:
                self.COOLDOWN+=1
            
    
    def shoot(self):
        if self.COOLDOWN == 0:
            if self.y > 0:
                if self.class_of_craft == 0:
                    if self.switch:
                        laser = Laser((self.x-7),self.y,self.laserspeed ,self.laser_img)
                        self.switch = False
                        self.lasers.append(laser)
                        self.COOLDOWN = 1
                    else:
                        laser = Laser((self.x+40),self.y,self.laserspeed ,self.laser_img)
                        self.switch = True
                        self.lasers.append(laser)
                        self.COOLDOWN = 1
                elif self.class_of_craft in [2,4]:
                    laser = Laser(self.x+10,self.y+5,self.laserspeed ,self.laser_img)
                    self.lasers.append(laser)
                    self.COOLDOWN = 1
                
                elif self.class_of_craft in [1]:
                    laser = Laser(self.x+random.choice([5,25]),self.y+5,self.laserspeed ,self.laser_img)
                    self.lasers.append(laser)
                    self.COOLDOWN = 1
                
                elif self.class_of_craft in [3]:
                    laser = Laser(self.x+50,self.y+10,self.laserspeed ,self.laser_img)
                    self.lasers.append(laser)
                    self.COOLDOWN = 1
    
    def get_width(self):
        return self.ship_img.get_width()   
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, class_of_craft=0, shield=100, health=100):
        super().__init__(x, y, class_of_craft=class_of_craft, shield=shield, health=health)
        self.ship_img = playerImg
        self.switch = True
        self.laser_img = Player_Laserbolt_Img
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.max_shield = shield
        self.speed = 12
        self.cool_down_counter = 7
        self.laserspeed = -15
        self.damage = 50
        self.shieldcounter = 0
        self.ionized = False
        self.ionize_counter = 250
        self.bomb_ready = True
        self.bombing = False
        self.powerup_timer = -1
        self.powerups = []
    
    def draw(self,window):
        super().draw(window)
        if not self.health <=0:
            self.healthbar(window)
        if not self.shield<=0:
            self.shieldbar(window)
        if self.powerup_timer>0:
            self.powerup_bar(window)
    
    def healthbar(self,window):
        pygame.draw.rect(window,(255,0,0),(self.x,self.y + self.ship_img.get_height() + 10,self.ship_img.get_width(),10))
        pygame.draw.rect(window,(0,255,0),(self.x,self.y + self.ship_img.get_height() + 10,self.ship_img.get_width()*(self.health/self.max_health),10))
    def shieldbar (self,window):
        pygame.draw.rect(window,(0,0,150),(self.x,self.y + self.ship_img.get_height() + 23,self.ship_img.get_width(),10))
        pygame.draw.rect(window,(0,0,255),(self.x,self.y + self.ship_img.get_height() + 23,self.ship_img.get_width()*(self.shield/self.max_shield),10))
    def powerup_bar (self,window):
        pygame.draw.rect(window,(255,255,255),(WIDTH-25,HEIGHT*0.3,10,HEIGHT*0.6*self.powerup_timer/600))
        

class Enemy(Ship):
    
    def __init__(self, x, y, class_of_craft=0, shield=0, health=100):
        Class_map = {
                1:(Enemy_image_class1,Enemy_Laserbolt_Img1),
                2:(Enemy_image_class2_right,Enemy_Laserbolt_Img2),
                3:(Enemy_image_class3,Enemy_Laserbolt_Img4),
                4:(Enemy_image_class4,Enemy_Laserbolt_Img2),
                5:(Enemy_image_class5,None)
    }
        super().__init__(x, y, class_of_craft=class_of_craft, shield=shield, health=health)
        if self.class_of_craft == 1:
            self.ship_img,self.laser_img = Class_map[1]
            self.shield = 50
            self.health = 200
            self.speed = 1
            self.cool_down_counter = 150
            self.laserspeed = 5
            self.damage = 2
        if self.class_of_craft == 2:
            self.ship_img,self.laser_img = Class_map[2]
            self.health = 200
            self.speed = 12
            self.cool_down_counter = 30
            self.laserspeed = 10
            self.damage = 13
        if self.class_of_craft == 3:
            self.ship_img,self.laser_img = Class_map[3]
            self.health = 500
            self.shield = 100
            self.speed = 0.5
            self.cool_down_counter = 100
            self.laserspeed = 4
            self.damage = 30
            
        if self.class_of_craft == 4:
            self.ship_img,self.laser_img = Class_map[4]
            self.speed = 2
            self.health = 200
            self.cool_down_counter = 15
            self.laserspeed = 8
            self.damage = 10
        if self.class_of_craft == 5:
            self.ship_img,self.laser_img = Class_map[5]
            self.speed = 2
            self.health = 150
        self.mask = pygame.mask.from_surface(self.ship_img)
        
            
        
    def move(self):
        if self.class_of_craft ==1:
            self.y += self.speed   
        if self.class_of_craft == 2:
            self.x+=self.speed
            if self.x >WIDTH-10-64:
                self.x = WIDTH-10-64
                self.y +=45
                self.speed =-11
                self.ship_img =Enemy_image_class2_left
            if self.x <10:
                self.x = 10
                self.y +=60
                self.speed =11
                self.ship_img =Enemy_image_class2_right
        if self.class_of_craft == 3:
            self.y+=self.speed
        if self.class_of_craft == 4:
            if self.y < HEIGHT*0.1:
                self.y += self.speed
        if self.class_of_craft == 5:
            self.y+=self.speed
            
class Laser:
    def __init__(self,x,y,speed,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.speed = speed
        self.xspeed = 0 
        self.yspeed = 0
        if self.img == Player_Laserbolt_Img:
            Player_lasersounds[random.randint(0,len(Player_lasersounds)-1)].play()
        if self.img == Enemy_Laserbolt_Img4:
            Destroyer_sounds[random.randint(0,len(Destroyer_sounds)-1)].play()
        if self.img == Enemy_Laserbolt_Img1:
            Enemy_Laserbolt_sounds1[random.randint(0,len(Enemy_Laserbolt_sounds1)-1)].play()
            self.rotate_laser()
        elif self.img == Enemy_Laserbolt_Img2:
            Enemy_Laserbolt_sounds2_4[random.randint(0,len(Enemy_Laserbolt_sounds2_4)-1)].play()
            self.rotate_laser()

    
    def rotate_laser(self):
        try:
            global x_coordinate
            global y_coordinate
            distance = math.sqrt(math.pow(x_coordinate-self.x,2)+math.pow(y_coordinate-self.y,2))
            angle = math.atan((self.x-x_coordinate)/(self.y-y_coordinate))*180/math.pi
            self.img=pygame.transform.rotate(self.img,angle)
            self.yspeed =(self.speed/distance)* (self.y-y_coordinate)*-1
            self.xspeed =(self.speed/distance)* (self.x-x_coordinate)*-1
        except:
            self.yspeed = self.speed
            self.xspeed = 0
        
        
    
    def draw(self,window):
        window.blit(self.img,(self.x,self.y))
    
    def move(self):
        if self.xspeed == 0:
            self.y+=self.speed
        else:
            self.y+=self.yspeed
            self.x+=self.xspeed            
    
    def off_screen(self,height):
        return not(self.y<height and self.y >=0)
    
    def isCollision(self,obj):
        return collide(obj,self)         
            
def collide(obj1,obj2):
    offset_x = int(round(obj2.x - obj1.x))
    offset_y = int(round(obj2.y - obj1.y))    
    check = obj1.mask.overlap(obj2.mask,(offset_x,offset_y))
    if check != None:
        return True #returns a Tuple (x,y) or None

def main_menu():
    run =True
    main_font =pygame.font.SysFont("comicsansms",64)
    while run:
        screen.blit(background,(0,0))
        title = main_font.render("Press Any Key to start :D",1,(255,255,255))
        screen.blit(title,(WIDTH/2-title.get_width()/2,HEIGHT*0.6))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                score = 0
                main()  
        pygame.display.update()
         
        
score = 0
# Game Loop
def main():
    level = 0
    lives = 3
    global score
    score = 0
    distance = 0
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    main_font =pygame.font.SysFont("comicsansms",32)
    wave_length = 0
    enemies = []
    powerups = []
    lost = False
    lost_count = 0
    lost_font = pygame.font.SysFont("comicsansms",64)
    powerup_spawn = 0
    
    
    player_ship = Player(100,HEIGHT-120)
    powerup_sound_bool = False
    
    def redraw_window():
        screen.blit(background,(0,0))
        lives_label = main_font.render("Level: {}".format(level),1,(255,255,255))
        level_label = main_font.render("Lives: {}".format(lives),1,(255,255,255))
        score_label = main_font.render("Score: {}".format(score),1,(255,255,255))
        if player_ship.bomb_ready:
            bomb_label = main_font.render("Bomb is ready",1,(0,155,0))
            screen.blit(bomb_label,(WIDTH/2-bomb_label.get_width()/2,HEIGHT-10-bomb_label.get_height()))
        remaining_enemies = main_font.render("Remaining Enemies: {}".format(len(enemies)),1,(255,255,255))
        for enemy in enemies:
            enemy.draw(screen)
        for powerup in powerups:
            powerup.draw(screen)
        screen.blit(lives_label,(10,10))
        screen.blit(level_label,(WIDTH - level_label.get_width()-10,10))
        screen.blit(score_label,(10,HEIGHT-10-score_label.get_height()))
        screen.blit(remaining_enemies,(WIDTH-remaining_enemies.get_width()-10,HEIGHT-10-remaining_enemies.get_height()))
        player_ship.draw(screen)
        if lost:
            lost_label = lost_font.render("You Lost! :(",1,(255,255,255))
            screen.blit(lost_label,((WIDTH/2 - lost_label.get_width()/2),HEIGHT*0.6))
        pygame.display.update()
        
    while running:
        clock.tick(FPS)
        redraw_window()
        if lives <0 or player_ship.health <=0:
            lost = True
            lost_count +=1
        if lost:
            if lost_count> FPS*5:
                running = False
            else:
                continue
            
        #check if powerups are collected
        if len(player_ship.powerups) == 1:
            if player_ship.powerups[0] == 1:
                    player_ship.max_shield = 999999
                    player_ship.shield = 999999
            elif player_ship.powerups[0] ==2:
                player_ship.damage = 999999 
        elif len(player_ship.powerups)>=2:
            player_ship.damage = 999999 
            player_ship.max_shield = 999999
            player_ship.shield = 999999
            
        #check if powerups are over
        if player_ship.powerup_timer <= 0:
            if powerup_sound_bool:
                damage_critical.play()
                powerup_sound_bool = False
            
            if player_ship.ionized:
                if len(player_ship.powerups)==1:
                    if player_ship.powerups[0] == 1:
                        player_ship.max_shield = player_ship.max_health
                        player_ship.shield = player_ship.max_shield
                elif len(player_ship.powerups)>1:
                    player_ship.max_shield = player_ship.max_health
                    player_ship.shield = player_ship.max_shield
            else:
                player_ship.max_shield = player_ship.max_health
                player_ship.shield = 0
            player_ship.powerups = []
            player_ship.damage = 50 + level
            

        
        player_ship.powerup_timer -=1   
        
        if len(enemies) == 0:
            level+=1
            wave_length +=2
            for i in range(wave_length):
                distance +=15
                enemy = Enemy(random.randrange(50,WIDTH-100),random.randrange(-500-distance,-50),random.choice([1,2,3,4,5]))
                enemies.append(enemy)
            distance = 0
            player_ship.shield = player_ship.max_shield
            player_ship.speed = 12
            player_ship.ionize_counter = 0
            player_ship.damage +=wave_length
        player_ship.ionize_counter-=1
        if player_ship.ionize_counter <=0:
            player_ship.ionized = True
        else:
            player_ship.ionized = False
        if player_ship.ionized:
           player_ship.speed =12 
        powerup_spawn = random.randint(0,60000//wave_length)
        if powerup_spawn == 15:
            powerup = Powerup(random.randrange(15,WIDTH-150),0,random.randint(1,4))
            powerups.append(powerup)

            
        global x_coordinate
        x_coordinate = player_ship.x
        global y_coordinate 
        y_coordinate = player_ship.y
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_ship.x -player_ship.speed >0:
            player_ship.x -=player_ship.speed
        if keys[pygame.K_RIGHT] and player_ship.x + player_ship.speed +player_ship.get_width() < WIDTH:
            player_ship.x += player_ship.speed
        if keys[pygame.K_UP] and player_ship.y - player_ship.speed >0:
            player_ship.y -= player_ship.speed
        if keys[pygame.K_DOWN] and player_ship.y +player_ship.speed +player_ship.get_height()+50 < HEIGHT:
            player_ship.y += player_ship.speed
        if keys[pygame.K_SPACE]:
            player_ship.shoot()
        if keys[pygame.K_LSHIFT]:
            if player_ship.bomb_ready:
                player_ship.bombing = True
        if keys[pygame.K_ESCAPE]:
            paused = True
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        paused = False
                paused_label = main_font.render("Paused",1,(255,255,255))
                screen.blit(paused_label,(WIDTH/2-paused_label.get_width()/2,HEIGHT/2-paused_label.get_height()/2))
                pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Player_Laserbolt_state = "fire"
        for powerup in powerups[:]:
            powerup.move()
            if powerup.y +powerup.get_height()>HEIGHT:
                if powerup in powerups:
                    powerups.remove(powerup)
            elif collide(powerup,player_ship):
                powerup_sound.play()
                if powerup.class_powerup == 1 or powerup.class_powerup == 2:
                    if len(player_ship.powerups)<2:
                        player_ship.powerups.append(powerup.class_powerup)
                    powerup_sound_bool=True
                    player_ship.powerup_timer = 600
                elif powerup.class_powerup == 3:
                    player_ship.bomb_ready = True
                elif powerup.class_powerup == 4:
                    player_ship.max_health +=50
                    player_ship.health = player_ship.max_health
                    player_ship.max_shield +=50
                    player_ship.shield = player_ship.max_shield 
                powerups.remove(powerup)  
                
                
        for enemy in enemies[:]:
                enemy.move()
                enemy.move_lasers([player_ship])
                if enemy.y + enemy.get_height()>HEIGHT:
                    lives -=1
                    enemies.remove(enemy)
                elif collide(enemy,player_ship):
                    player_ship.hit(20)
                    enemies.remove(enemy)
                    Explosion_sounds[random.randint(0,len(Explosion_sounds)-1)].play()
                enemy.shoot()
        if player_ship.bombing:
            bomb_sound.play()
            for enemy in enemies[:]:
                if enemy in enemies:
                    enemy.hit(999999)
                    score+=100
                    if enemy.health <=0:
                        enemies.remove(enemy)          
                        Explosion_sounds[random.randint(0,len(Explosion_sounds)-1)].play()             
                    
            player_ship.bombing = False
            player_ship.bomb_ready = False
        player_ship.move_lasers(enemies)
        
        
main_menu()
