import pygame, os
import pygame.freetype

# Global variables

# Main window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Colors
BG_COLOR = pygame.Color('grey12')
ACCENT_COLOR = (27, 35, 43)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (80, 80, 155)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

# Text Fonts
pygame.freetype.init()
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts", "Jellee-Bold.ttf")
font_size = 64
game_font = pygame.freetype.Font(font_path, font_size)
#game_font = pygame.font.Font('freesansbold.ttf', 32) 


