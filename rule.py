'''
Created on Apr 3, 2015

@author: Xing
'''
import constant, board
import pygame, copy, random, time
from pygame.locals import *
from sys import exit

        
def check_for_quit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
            pygame.quit()
            exit()