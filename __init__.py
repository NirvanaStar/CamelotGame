#-*- coding: utf-8 -*-
#!/usr/bin/env python
bgImageFile = 'background.jpg'
bImageFile = 'board.jpg'

import pygame, copy, random, time
from pygame.locals import *
from sys import exit

#width of window
WINDOWWIDTH = 1024
#height of window
WINDOWHEIGHT = 768
#width of window
BOARDWIDTH = 8
#height of window
BOARDHEIGHT = 14
#size of each space
SPACE = 50

XMARGIN = int((WINDOWHEIGHT-BOARDWIDTH*SPACE)/2-20)
YMARGIN = int((WINDOWWIDTH-BOARDHEIGHT*SPACE)/2-50)

#define color
black = (0,0,0)
white = (255,255,255)
fontBg = (30,80,156)

lineColor = black
#color of board line
fontColor = white
#color of font
fontBackground = fontBg

EMPTY_SPACE = 'EMPTY_SPACE'
#color of font background

def main():
    global screen, bgImage, boardRect, font, bigFont
    pygame.init()
    
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Camelot Game")
    #font = pygame.font.Font('simsun.ttc', 16)
    #bigFont = pygame.font.Font('simsun.ttc', 32)
    
    bImage = pygame.image.load(bImageFile).convert()
    bImage = pygame.transform.smoothscale(bImage, (BOARDWIDTH*SPACE, BOARDHEIGHT*SPACE))
    boardRect = bImage.get_rect()
    boardRect.topleft = XMARGIN, YMARGIN
    
    bgImage = pygame.image.load(bgImageFile).convert()
    bgImage = pygame.transform.smoothscale(bgImage, (WINDOWWIDTH, WINDOWHEIGHT))

    bgImage.blit(bImage, boardRect)
    
    while True:
        mainBoard = getNewBoard()
        drawBoard(mainBoard)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        pygame.display.update()

def drawBoard(board):
    #set background of board
    screen.blit(bgImage, (0,0))
    
    m = 1
    for x in range(BOARDHEIGHT+1):
        xstart, ystart = boardRect.topleft
        
        ystart += (x*SPACE)
        
        if m == BOARDHEIGHT or m == 1:
             xstart = xstart + 3*SPACE
             xend = xstart+(BOARDWIDTH-3)*SPACE
             yend = ystart
             
        xstart = xstart + 3*SPACE
        xend = xstart+BOARDWIDTH*SPACE
        yend = ystart
        
        pygame.draw.line(screen, lineColor, (xstart, ystart), (xend, yend))
    
    
def getNewBoard():   
   return [[EMPTY_SPACE] * BOARDHEIGHT  for x in range(BOARDWIDTH)]

def runGame():
    return True
       
if __name__=='__main__':
    main()