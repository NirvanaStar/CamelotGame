# -*- coding: utf-8 -*-

'''
Created on Apr 3, 2015

@author: Xing
'''

import constant, display
import pygame, copy, random, time
from pygame.locals import *
from sys import exit

class Board(object):

    def __init__(self):
        self.main_board = []
        constant.screen = display.display_set_mode(constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT)
        display.display_set_caption("Camelot Game")

        #initial font
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", 16)
        self.big_font = pygame.font.SysFont('arial', 32)

        #initial background and chess board
        self.board_image = pygame.image.load(constant.BOARD_IMAGE_FILE).convert()
        self.board_image = pygame.transform.smoothscale(self.board_image, (constant.BOARD_WIDTH * constant.SPACE,
                                                                 constant.BOARD_HEIGHT * constant.SPACE))
        self.board_rect = self.board_image.get_rect()
        self.board_rect.topleft = constant.XMARGIN, constant.YMARGIN

        self.bg_image = pygame.image.load(constant.BG_IMAGE_FILE).convert()
        self.bg_image = pygame.transform.smoothscale(self.bg_image, (constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT))

        self.bg_image.blit(self.board_image, self.board_rect)

        constant.main_clock = pygame.time.Clock()
    
    #create board
    def get_new_noard(self):
        return [[constant.EMPTY_SPACE] * constant.BOARD_HEIGHT  for x in range(constant.BOARD_WIDTH)]
    
    def reset_board(self, board):
        #set each space is empty
        for x in range(constant.BOARD_WIDTH):
            for y in range(constant.BOARD_HEIGHT):
                board[x][y] = constant.EMPTY_SPACE
        
        #initial cheess
        board[0][1] = constant.WHITE_TILE
              
    def draw_board(self):
        #draw line of board
                
        for x in range(constant.BOARD_HEIGHT + 1):
            xstart, ystart = self.board_rect.topleft
            ystart += (x * constant.SPACE)
           
            xend = xstart + constant.BOARD_WIDTH * constant.SPACE
            yend = ystart
            pygame.draw.line(constant.screen, constant.GRAY, (xstart, ystart), (xend, yend))
            
        for y in range(constant.BOARD_WIDTH + 1):
            xstart, ystart = self.board_rect.topleft
            xstart += (y * constant.SPACE)
            
            yend = ystart + constant.BOARD_HEIGHT * constant.SPACE
            xend = xstart
                
            pygame.draw.line(constant.screen, constant.GRAY, (xstart, ystart), (xend, yend))
        
        for x in range(constant.BOARD_HEIGHT + 1):
            xstart1, ystart = self.board_rect.topleft
            xstart2 = xstart1
            ystart += (x * constant.SPACE)
            
            if x < 4:
                xstart1 = xstart1 + ((-1) * x + 3) * constant.SPACE
                xstart2 = xstart2 + (x + 5) * constant.SPACE
                xend1 = xstart1 + constant.SPACE
                xend2 = xstart2 - constant.SPACE
                yend = ystart
                
            elif x > 10:
                xstart1 = xstart1 + (x - 11) * constant.SPACE
                xstart2 = xstart2 + ((-1) * x + 19) * constant.SPACE
                xend1 = xstart1 + constant.SPACE
                xend2 = xstart2 - constant.SPACE
                yend = ystart
            
            else:
                continue
                
            pygame.draw.line(constant.screen, constant.LINE_COLOR, (xstart1, ystart), (xend1, yend))
            pygame.draw.line(constant.screen, constant.LINE_COLOR, (xstart2, ystart), (xend2, yend))
            
        for y in range(constant.BOARD_WIDTH + 1):
            xstart, ystart1 = self.board_rect.topleft
            ystart2 = ystart1
            xstart += (y * constant.SPACE)
            
            if y == 0 or y == 8:
                ystart1 = ystart1 + 3 * constant.SPACE
                yend1 = ystart1 + 8 * constant.SPACE
                xend = xstart
                pygame.draw.line(constant.screen, constant.LINE_COLOR, (xstart, ystart1), (xend, yend1))
                continue
            
            if y > 0 and y < 4:
                ystart1 = ystart1 + ((-1) * y + 3) * constant.SPACE
                ystart2 = ystart2 + (y + 10) * constant.SPACE
                yend1 = ystart1 + constant.SPACE
                yend2 = ystart2 + constant.SPACE
                xend = xstart
                
            elif y > 4 and y < 8:
                ystart1 = ystart1 + (y - 5) * constant.SPACE
                ystart2 = ystart2 + ((-1) * y + 18) * constant.SPACE
                yend1 = ystart1 + constant.SPACE
                yend2 = ystart2 + constant.SPACE
                xend = xstart
            
            else:
                continue
                
            pygame.draw.line(constant.screen, constant.LINE_COLOR, (xstart, ystart1), (xend, yend1))
            pygame.draw.line(constant.screen, constant.LINE_COLOR, (xstart, ystart2), (xend, yend2))
            
        #draw chess
        for x in range(constant.BOARD_WIDTH):
            for y in range(constant.BOARD_HEIGHT):
                center_x, center_y = self.translate_board_to_pixel(x,y)
                
                if self.main_board[x][y] == constant.WHITE_TILE:
                    tile_color = constant.WHITE
                    pygame.draw.circle(constant.screen, tile_color, (center_x, center_y), int(constant.SPACE / 2) - 4)
                    
                elif self.main_board[x][y] == constant.BLACK_TILE:
                    tile_color = constant.BLACK
                    pygame.draw.circle(constant.screen, tile_color, (center_x, center_y), int(constant.SPACE / 2) - 4)
        
    def translate_board_to_pixel(self, x,y):
        return int(constant.XMARGIN) + x * constant.SPACE + int(constant.SPACE / 2), \
               int(constant.YMARGIN) + y * constant.SPACE + int(constant.SPACE / 2)

    def enter_player_tile(self):
        show_text = self.font.render('Choose ''Black'' or White', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
        show_rect = show_text.get_rect()
        show_rect.center = int(constant.WINDOW_WIDTH / 2), int(constant.WINDOW_HEIGHT / 2)

        white_text = self.big_font.render('Black', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
        white_rect = white_text.get_rect()
        white_rect.center = int(constant.WINDOW_WIDTH / 2) - constant.SPACE * 2, \
                            int(constant.WINDOW_HEIGHT / 2) + constant.SPACE

        black_text = self.big_font.render('White', True, constant.FONT_COLOR, constant.FONT_BACKGROUND)
        black_rect = black_text.get_rect()
        black_rect.center = int(constant.WINDOW_WIDTH / 2) + constant.SPACE * 2, \
                            int(constant.WINDOW_HEIGHT / 2) + constant.SPACE

        display.display_who_is_first(show_text, show_rect, white_text, white_rect, black_text, black_rect)
