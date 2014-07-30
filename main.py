import random
import pygame
import sys
import time
from pygame.locals import *
from random import *



pygame.init()
fps = 30
dispWidth = 800
dispHeight = 600


#Larger cellSize
cellSize = 20

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bg = black

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

deadZones = []

def whatNext():
    for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None



def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = (int(dispWidth / 2), int(dispHeight / 2))
    setDisplay.blit(titleTextSurf, titleTextRect)
    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = (int(dispWidth / 2), int(dispHeight / 2) + 100)
    setDisplay.blit(typTextSurf, typTextRect)
    while whatNext() == None:
        pygame.display.update()
        fpsTime.tick()
    runGame()





def evilMove(evilGuy):
    evilCoords = []
    deadZones.append(evilCoords)
    

    randomMovex = randrange(-1,2)
    randomMovey = randrange(-1,2)
    
    newCell = {'x': evilGuy[0]['x']+randomMovex, 'y': evilGuy[0]['y']+randomMovey}
    # Limits
    if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth/cellSize or newCell['y'] > dispHeight/cellSize):
        
        newCell = {'x': dispWidth/(2*cellSize), 'y': dispHeight/(2*cellSize)}
    del evilGuy[-1]

    evilCoords.append(newCell['x'])
    evilCoords.append(newCell['y'])

    evilGuy.insert(0, newCell)

    
    
    
    

def runGame():
    global deadZones
    startx = 3
    starty = 3
    coords = [{'x': startx,'y': starty}]

    evilCoords1 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]
    evilCoords2 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]
    evilCoords3 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]
    evilCoords4 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]
    evilCoords5 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]
    evilCoords6 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]
    evilCoords7 = [{'x': dispWidth/(2*cellSize),'y': dispHeight/(2*cellSize)}]


    
    direction = RIGHT
    isAlive = 'yes'
    while True: # main game loop

        while isAlive == 'yes':
            deadZones = []
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        direction = LEFT
                    elif event.key == K_RIGHT:
                        direction = RIGHT
                    elif event.key == K_UP:
                        direction = UP
                    elif event.key == K_DOWN:
                        direction = DOWN
            # move the worm by adding a segment in the direction it is moving
            if direction == UP:
                newCell = {'x': coords[0]['x'], 'y': coords[0]['y'] - 1}
            elif direction == DOWN:
                newCell = {'x': coords[0]['x'], 'y': coords[0]['y'] + 1}
            elif direction == LEFT:
                newCell = {'x': coords[0]['x'] - 1, 'y': coords[0]['y']}
            elif direction == RIGHT:
                newCell = {'x': coords[0]['x'] + 1, 'y': coords[0]['y']}
            del coords[-1]

            coords.insert(0, newCell)
            setDisplay.fill(bg)

            
            evilMove(evilCoords1)
            evilMove(evilCoords2)
            evilMove(evilCoords3)
            evilMove(evilCoords4)
            evilMove(evilCoords5)
            evilMove(evilCoords6)
            evilMove(evilCoords7)


            currentPos = []
            currentPos = [newCell['x'],newCell['y']]

            for eachDeathCoord in deadZones:
                if eachDeathCoord == currentPos:
                    isAlive = 'no'

            
            drawCell(coords,white)
            drawCell(evilCoords1,red)
            drawCell(evilCoords2,red)
            drawCell(evilCoords3,red)
            drawCell(evilCoords4,red)
            drawCell(evilCoords5,red)
            drawCell(evilCoords6,red)
            drawCell(evilCoords7,red)
            
            pygame.display.update()
            fpsTime.tick(fps)





            if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth/cellSize or newCell['y'] > dispHeight/cellSize):
                isAlive = 'no'

        msgSurface('You Died')


def drawCell(coordinates,color):
    for coord in coordinates:

        x = coord['x'] * cellSize
        y = coord['y'] * cellSize

        makeCell = pygame.Rect(x, y, cellSize, cellSize)
        pygame.draw.rect(setDisplay, color, makeCell)


while True:
    global fpsTime, setDisplay
    
    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth, dispHeight))
    pygame.display.set_caption('controlling')
    runGame()
