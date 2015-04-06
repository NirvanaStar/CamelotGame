'''
Created on Apr 3, 2015

@author: Xing
'''
import constant, board
import pygame, copy, random, time
from pygame.locals import *
from sys import exit

font = pygame.font.Font('MSYH.TTF', 16)
big_font = pygame.font.Font('MSYH.TTF', 32)

def enter_player_tile():
    show_text = font.render('Choose Black or White', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
    
    show_rect = show_text.get_rect()
    
    show_rect.center = int(constant.WINDOW_WIDTH / 2), int(constant.WINDOW_HEIGHT/2)
    
    white_text = big_font.render('Black', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
    white_rect = white_text.get_rect()
    white_rect.center = int(constant.WINDOW_WIDTH / 2) - constant.SPACE * 2, int(constant.WINDOW_HEIGHT / 2) + constant.SPACE * 2
    
    black_text = big_font.render('White', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
    black_rect = black_text.get_rect()
    black_rect.center = int(constant.WINDOW_WIDTH / 2) - constant.SPACE * 2, int(constant.WINDOW_HEIGHT / 2) + constant.SPACE * 2
    
    while True:
        check_for_quit()
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                center_x, center_y = event.pos
                if black_rect.collidepoint((center_x, center_y)):
                    return [constant.BLACK_TILE, constant.WHITE_TILE]
                elif white_rect.collidepoint((center_x, center_y)):
                    return [constant.WHITE_TILE, constant.BLACK_TILE]
        
        #screen.blit(show_text, show_rect)
        
def check_for_quit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
            pygame.quit()
            exit()