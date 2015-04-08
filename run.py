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
    game_screen = constant.gameScreen()
    font = pygame.font.SysFont("arial", 16)
    
    while True:
        b.main_board = b.get_new_noard()
        b.reset_board(b.main_board)
        display.display_screen(game_screen.screen, b.bg_image)
        b.draw_board()
        player_tile, computer_tile = b.enter_player_tile()
        
        if player_tile == constant.WHITE_TILE:
            turn = player_tile
        else:
            turn = computer_tile

        
        new_game = font.render('restart', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
        new_game_rect = new_game.get_rect()
        new_game_rect.topright = constant.WINDOW_WIDTH - 10, 10

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        display.display_update()