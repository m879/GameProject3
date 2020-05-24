#CREATING MULTIPLE IMAGE  
import pygame
import random
import math
from pygame import mixer
x=pygame.init()
#creating window
black=(0,0,0)
gamewindow=pygame.display.set_mode((1300,700))

#BACKGROUND
background=pygame.image.load("background.jpg")
pygame.display.set_caption("GAME--develop by MERAJ AHMED")
mixer.music.load("music.mp3")
mixer.music.play(-1)

img=pygame.image.load("ufo.png")
pygame.display.set_icon(img)

#player
playerimg=pygame.image.load("plane1.png")
playerX=0
playerY=0
playerY_change=0

heliimg=pygame.image.load("astro.png")
heliX=100
heliY=560
heliX_change=0
 
#ENEMY
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=5
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("ufo1.png"))
    enemyX.append(random.randint(0,1200))
    enemyY.append(random.randint(-5,0))
    enemyX_change.append(4)
    enemyY_change.append(10)

bullimg=[]
bullX=enemyX
bullY=[]
bullX_change=[]
bullY_change=[]
num_of_bull=5
for i in range(num_of_bull):
    bullimg.append(pygame.image.load("bullet4.png"))
    bullX.append(random.randint(0,664))
    bullY.append(random.randint(50,400))
    bullX_change.append(2)
    bullY_change.append(6)

#BULLET
#Ready=you cannot see the bullet on the screen
#Fire=the bullet is currently moving
bulletimg=pygame.image.load("BULLET2.png")
bulletX=0
bulletY=0
bulletX_change=60
bulletY_change=0
bullet_state="ready"

#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    gamewindow.blit(score,(x,y))


def player(x,y):
    gamewindow.blit(playerimg,(x,y))


def astronaut(x,y):
    gamewindow.blit(heliimg,(x,y))

def enemy(x,y,i):
    gamewindow.blit(enemyimg[i],(x,y))

def enbullet(x,y,i):
    gamewindow.blit(bullimg[i],(x,y))    

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    gamewindow.blit(bulletimg,(x+25,y+50))

def iscollision(bullX,bullY,bulletX,bulletY):
    distance=math.sqrt((math.pow(bullX-bulletX,2))+(math.pow(bullY-bulletY,2)))
    if distance<50:
        return True
    else:
        return False    


def gamecollision(bullX,bullY,heliX,heliY):
    distance=math.sqrt((math.pow(bullX-heliX,2))+(math.pow(bullY-heliY,2)))
    if distance<50:
        return True
    else:
        return False

#game specific variables
exit_game=False

#creating a game loop
while not exit_game:
    gamewindow.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                playerY_change=-8
            if event.key==pygame.K_DOWN:
                playerY_change=8

            if event.key==pygame.K_LEFT:
                heliX_change=-8
            if event.key==pygame.K_RIGHT:
                heliX_change=8
            

 
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    #get the current x coordinate of the spaceship    
                    bulletY=playerY
                    fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerY_change=0
                

    playerY+=playerY_change
    heliX+=heliX_change
    bullY[i]+=bullY_change[i]

#THIS IS USED TO MAKE BOUNDARIES
    if playerX <=0:    #lower limit of x-coordinate
        playerX=0
    elif playerX >=665:  #upper limit of x-coordinate--image size
        playerX=665

    if playerY <=0:   
        playerY=0
    elif playerY>=250: 
        playerY=250    

    if heliX>=1200:
        heliX=0  
      

    #ENEMY MOVEMENT
    for i in range(num_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <=200:    
            enemyX_change[i]=6
        elif enemyX[i] >= 1200: 
            enemyX_change[i]=-6
        
        enemy(enemyX[i],enemyY[i],i)

    for i in range(num_of_bull):
        bullY[i]+=bullY_change[i]
        if bullY[i]>=700:
            bullY[i]=10

        #COLLISION
        collision=iscollision(bullX[i],bullY[i],bulletX,bulletY)
        if collision:
            bulletY=560
            bullet_state="ready"
            score_value+=10
            bullX[i]=random.randint(0,1200)
            bullY[i]=random.randint(5,10)  

        collisions=gamecollision(bullX[i],bullY[i],heliX,heliY) 
        if collisions:
            exit_game=True
        enbullet(bullX[i],bullY[i],i)    

    
    #BULLET MOVEMENT
    if bulletX>=1200:
        bulletX=0
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletX+=bulletX_change


    player(playerX,playerY)
    astronaut(heliX,heliY)
    show_score(textX,textY)
    pygame.display.update()

pygame.quit()
quit()

