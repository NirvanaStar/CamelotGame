"""
Created on Apr 3, 2015

@author: Xing
"""

BG_IMAGE_FILE = 'background.jpg'
BOARD_IMAGE_FILE = 'board.jpg'

#width of window
WINDOW_WIDTH = 1024

#height of window
WINDOW_HEIGHT = 768

#width of window
BOARD_WIDTH = 8

#height of window
BOARD_HEIGHT = 14

#size of each space
SPACE = 50
EMPTY_SPACE = 'EMPTY_SPACE'

XMARGIN = int((WINDOW_HEIGHT - BOARD_WIDTH * SPACE) / 2 - 60)
YMARGIN = int((WINDOW_WIDTH - BOARD_HEIGHT * SPACE) / 2 - 120)

#define color
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (96,96,96)
FONT_BG = (30,80,156)

#color of board line
LINE_COLOR = BLACK

#color of font
FONT_COLOR = WHITE

#color of font background
FONT_BACKGROUND = FONT_BG

WHITE_TILE = 'WHITE_TILE'
BLACK_TILE = 'BLACK_TILE'

FPS = 10

#For display
screen = 0
main_clock = 0