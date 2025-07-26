from screen_manager import ScreenManager
from settings import *
import pygame

def main():
    pygame.init()
    screen = ScreenManager()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        running = screen.handle_events()
        screen.draw()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()