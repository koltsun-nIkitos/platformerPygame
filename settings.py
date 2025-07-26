import pygame
import os

# Настройки экрана
pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 40
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Пути
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
FONT_PATH = os.path.join(ASSETS_DIR, 'fonts', 'PressStart2P.ttf')

PLAYER_IMAGE = os.path.join(ASSETS_DIR, 'img', 'player.png')

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 20