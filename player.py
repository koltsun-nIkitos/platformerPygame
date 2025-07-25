import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, PLAYER_SPEED, PLAYER_COLOR

class Player:
    def __init__(self, x=None, y=None):
        self.x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
        self.y = SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2
        self.speed = PLAYER_SPEED
        self.size = PLAYER_SIZE
        self.color = PLAYER_COLOR 

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.size:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))