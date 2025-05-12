import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

catBx = 280
catBy = 220
directionB = 'up'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    #Cat A logic
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    #Cat B Logic
    if directionB == 'right':
        catBx += 5
        if catBx == 280:
            directionB = 'up'
    elif directionB == 'down':
        catBy += 5
        if catBy == 220:
            directionB = 'right'
    elif directionB == 'left':
        catBx -= 5
        if catBx == 10:
            directionB = 'down'
    elif directionB == 'up':
        catBy -= 5
        if catBy == 10:
            directionB = 'left'

    DISPLAYSURF.blit(catImg, (catBx, catBy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
