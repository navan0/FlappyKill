import pygame
import random
pygame.init()

disPlay_height = 800
disPlay_width = 600
black = (0,0,0)
white = (255,255,255)
guns = False
xB = (disPlay_width * 0.15)
yB = (disPlay_height * .5)
bChange = 0
xG = (disPlay_width * .9)
yG = (disPlay_height * .4)
gravity = 3
velocity = 0
crashed = False
d = {}

disPlay = pygame.display.set_mode((disPlay_height,disPlay_width))
pygame.display.set_caption('FlappyKill')
clock = pygame.time.Clock()
birdImg = pygame.image.load('bird.png')
bg = pygame.image.load("bg.png")
gunImg = pygame.image.load('gun.png')
# ran = random.randint(1,3)

def bird(x,y):
    disPlay.blit(birdImg,(x,y))

def gun(x,y):

    disPlay.blit(gunImg,(x,y))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        pressed = pygame.key.get_pressed()


    disPlay.blit(bg, (0, 0))
    velocity =gravity
    yB += velocity
    xG += -4
    # disPlay.fill(bg)
    bird(xB,yB)
    if guns:
        gun(xG,yG)

    if xG < -150:
        guns = False
        xG = (disPlay_width * 1.3)
        yG = (200 + 7*10)

    if yB > 550:
        yB=550

    if yB < 0:
        yB=0


    if pressed[pygame.K_SPACE]:
        yB += -14
    if pressed[pygame.K_l]:
        guns = True
        #xG = (disPlay_width * 1)



    print(xG,yB)

    pygame.display.update()
    clock.tick(600)
    # print(xG)

pygame.quit()
