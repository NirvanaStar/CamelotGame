'''
Created on Apr 3, 2015

@author: Xing
'''

import constant
import pygame, copy, random, time
from pygame.locals import *
from sys import exit

def display_set_mode(width, height):
    return pygame.display.set_mode((width, height))

def display_set_caption(text):
    pygame.display.set_caption(text)

def display_screen(screen, image):
    screen.blit(image, (0,0))
         
def display_upadte():
    pygame.display.update()    

def display_who_is_first():
    while True:
        #check_for_quit()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                center_x, center_y = event.pos
                if black_rect.collidepoint((center_x, center_y)):
                    return [constant.BLACK_TILE, constant.WHITE_TILE]
                elif white_rect.collidepoint((center_x, center_y)):
                    return [constant.WHITE_TILE, constant. BLACK_TILE]

        constant.screen.blit(show_text, show_rect)
        constant.screen.blit(black_text, black_rect)
        constant.screen.blit(white_text, white_rect)
        pygame.display.update()
        mainClock.tick(FPS)