import pygame, sys
from pygame.locals import *
pygame.init()
import time

FPS = 50
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1200, 700), 0, 32)
pygame.display.set_caption('REINFORCEMENT LEARNING (Discrete Mathematics) - Football Analytics (footRein)')
# set up the colors
BLACK = ( 0,0,0)
WHITE = (255, 255, 255)
RED= (255,0,0)
GREEN = ( 0, 255,0)
BLUE = ( 0,0, 255)

# draw on the surface object
def boarddisplay():
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, GREEN, (20, 20, 1160, 660))
    pygame.draw.rect(DISPLAYSURF, BLUE, (20, 250, 20, 200))
    pygame.draw.rect(DISPLAYSURF, BLUE, (1160, 250, 20, 200))
    pygame.draw.rect(DISPLAYSURF, WHITE, (598, 0, 4, 700))
    pygame.draw.ellipse(DISPLAYSURF, WHITE, (500, 200, 200, 300))
    pygame.draw.rect(DISPLAYSURF, WHITE, (20, 20, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (1160, 20, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (20, 660, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (1160, 660, 20, 20))
    pygame.draw.circle(DISPLAYSURF, RED, (600, 350), 10, 10)
    return



#Define team A
TEAMA_goalkeeper = pygame.image.load('images/players/TeamAk.png')
TEAMA_goalkeeper = pygame.transform.scale(TEAMA_goalkeeper, (30, 30))

TEAMA_one = pygame.image.load('images/players/teamA1.png')
TEAMA_one = pygame.transform.scale(TEAMA_one, (30, 30))

TEAMA_two = pygame.image.load('images/players/teamA2.png')
TEAMA_two = pygame.transform.scale(TEAMA_two, (30, 30))

TEAMA_three = pygame.image.load('images/players/teamA3.png')
TEAMA_three = pygame.transform.scale(TEAMA_three, (30, 30))

TEAMA_four = pygame.image.load('images/players/teamA4.png')
TEAMA_four = pygame.transform.scale(TEAMA_four, (30, 30))

TEAMA_five = pygame.image.load('images/players/teamA5.png')
TEAMA_five = pygame.transform.scale(TEAMA_five, (30, 30))

TEAMA_six = pygame.image.load('images/players/teamA6.png')
TEAMA_six = pygame.transform.scale(TEAMA_six, (30, 30))

TEAMA_seven = pygame.image.load('images/players/teamA7.png')
TEAMA_seven = pygame.transform.scale(TEAMA_seven, (30, 30))

TEAMA_eight = pygame.image.load('images/players/teamA8.png')
TEAMA_eight = pygame.transform.scale(TEAMA_eight, (30, 30))

TEAMA_nine = pygame.image.load('images/players/teamA9.png')
TEAMA_nine = pygame.transform.scale(TEAMA_nine, (30, 30))

TEAMA_ten = pygame.image.load('images/players/teamA10.png')
TEAMA_ten = pygame.transform.scale(TEAMA_ten, (30, 30))


#define team B
TEAMB_goalkeeper = pygame.image.load('images/players/TeamBk.png')
TEAMB_goalkeeper = pygame.transform.scale(TEAMB_goalkeeper, (30, 30))

TEAMB_one = pygame.image.load('images/players/teamB1.png')
TEAMB_one = pygame.transform.scale(TEAMB_one, (30, 30))

TEAMB_two = pygame.image.load('images/players/teamB2.png')
TEAMB_two = pygame.transform.scale(TEAMB_two, (30, 30))

TEAMB_three = pygame.image.load('images/players/teamB3.png')
TEAMB_three = pygame.transform.scale(TEAMB_three, (30, 30))

TEAMB_four = pygame.image.load('images/players/teamB4.png')
TEAMB_four = pygame.transform.scale(TEAMB_four, (30, 30))

TEAMB_five = pygame.image.load('images/players/teamB5.png')
TEAMB_five = pygame.transform.scale(TEAMB_five, (30, 30))

TEAMB_six = pygame.image.load('images/players/teamB6.png')
TEAMB_six = pygame.transform.scale(TEAMB_six, (30, 30))

TEAMB_seven = pygame.image.load('images/players/teamB7.png')
TEAMB_seven = pygame.transform.scale(TEAMB_seven, (30, 30))

TEAMB_eight = pygame.image.load('images/players/teamB8.png')
TEAMB_eight = pygame.transform.scale(TEAMB_eight, (30, 30))

TEAMB_nine = pygame.image.load('images/players/teamB9.png')
TEAMB_nine = pygame.transform.scale(TEAMB_nine, (30, 30))

TEAMB_ten = pygame.image.load('images/players/teamB10.png')
TEAMB_ten = pygame.transform.scale(TEAMB_ten, (30, 30))



#Define the teamA players default position
playerakeep = (40, 330)
playera1 = (140, 100)
playera2 = (140, 250)
playera3 = (140, 400)
playera4 = (140, 550)
playera5 = (340, 150)
playera6 = (340, 300)
playera7 = (340, 450)
playera8 = (500, 350)
playera9 = (550, 300)
playera10 = (550, 400)


#Define the teamB players default position
playerbkeep = (1130, 330)
playerb1 = (1030, 100)
playerb2 = (1030, 250)
playerb3 = (1030, 400)
playerb4 = (1030, 550)
playerb5 = (830, 150)
playerb6 = (830, 300)
playerb7 = (830, 450)
playerb8 = (750, 350)
playerb9 = (650, 300)
playerb10 = (650, 400)



def displayDefaultA():
    #randomly display players A within enclosed position x, y, xwidth, ywidth
    DISPLAYSURF.blit(TEAMA_goalkeeper, playerakeep)
    DISPLAYSURF.blit(TEAMA_one, playera1)
    DISPLAYSURF.blit(TEAMA_two, playera2)
    DISPLAYSURF.blit(TEAMA_three, playera3)
    DISPLAYSURF.blit(TEAMA_four, playera4)
    DISPLAYSURF.blit(TEAMA_five, playera5)
    DISPLAYSURF.blit(TEAMA_six, playera6)
    DISPLAYSURF.blit(TEAMA_seven, playera7)
    DISPLAYSURF.blit(TEAMA_eight, playera8)
    DISPLAYSURF.blit(TEAMA_nine, playera9)
    DISPLAYSURF.blit(TEAMA_ten, playera10)
    return


def displayDefaultB():
    #randomly display players A within enclosed position x, y, xwidth, ywidth
    DISPLAYSURF.blit(TEAMB_goalkeeper, playerbkeep)
    DISPLAYSURF.blit(TEAMB_one, playerb1)
    DISPLAYSURF.blit(TEAMB_two, playerb2)
    DISPLAYSURF.blit(TEAMB_three, playerb3)
    DISPLAYSURF.blit(TEAMB_four, playerb4)
    DISPLAYSURF.blit(TEAMB_five, playerb5)
    DISPLAYSURF.blit(TEAMB_six, playerb6)
    DISPLAYSURF.blit(TEAMB_seven, playerb7)
    DISPLAYSURF.blit(TEAMB_eight, playerb8)
    DISPLAYSURF.blit(TEAMB_nine, playerb9)
    DISPLAYSURF.blit(TEAMB_ten, playerb10)
    return


nextTeam = 'Team A'

count = 0


while True:
    #display board
    boarddisplay()
    
    #display player A
    displayDefaultA()
    
    #display player B
    displayDefaultB()
    
    
    
    
    
    
    


    pygame.display.update()
    fpsClock.tick(FPS)
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

