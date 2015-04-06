'''
Created on Apr 3, 2015

@author: Xing
'''

import board, constant, display
import pygame, copy, random, time
from pygame.locals import *
from sys import exit

def start_play():
    pygame.init()

    b = board.Board()

    while True:
        b.main_board = b.get_new_noard()
        b.reset_board(b.main_board)
        display.display_screen(constant.screen, b.bg_image)
        b.draw_board()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        display.display_upadte()