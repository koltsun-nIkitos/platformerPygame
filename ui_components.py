import pygame
from settings import *

class TextInput:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text = ""
        self.active = True
        self.cursor_visible = True
        self.cursor_timer = 0
        self.max_length = 15

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < self.max_length:
                self.text += event.unicode
        return False

    def draw(self, screen):
        # Рамка поля ввода
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        
        # Текст
        text_surface = self.font.render(self.text, True, WHITE)
        text_x = self.rect.x + (self.rect.width - text_surface.get_width()) // 2
        screen.blit(text_surface, (text_x, self.rect.y + 5))

        # Мигающий курсор
        if self.active:
            self.cursor_timer = (self.cursor_timer + 1) % 60
            if self.cursor_timer < 30:
                cursor_x = text_x + text_surface.get_width() + 2
                pygame.draw.line(screen, WHITE, 
                               (cursor_x, self.rect.y + 5),
                               (cursor_x, self.rect.y + 35), 2)

class TextLabel:
    def __init__(self, text, font, color):
        self.text = text
        self.font = font
        self.color = color
        
    def draw(self, screen, x, y):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (x, y))