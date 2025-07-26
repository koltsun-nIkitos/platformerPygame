import pygame
import os
from settings import *
from ui_components import TextInput, TextLabel
from player import Player

class ScreenManager:
    def __init__(self):
        # Инициализация экрана
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Звёздный защитник")
        
        # Шрифты
        try:
            self.main_font = pygame.font.Font(FONT_PATH, 24)
            self.small_font = pygame.font.Font(FONT_PATH, 20)
        except:
            self.main_font = pygame.font.SysFont('Arial', 24)
            self.small_font = pygame.font.SysFont('Arial', 20)

        # Состояния игры
        self.state = "tutorial"  # tutorial → name_input → game
        
        # UI компоненты
        self.name_input = TextInput(
            SCREEN_WIDTH//2 - 200, 
            SCREEN_HEIGHT//2, 
            400, 40, 
            self.main_font
        )
        self.title_label = TextLabel("ЗВЁЗДНЫЙ ЗАЩИТНИК", self.main_font, BLUE)
        self.exit_label = TextLabel("ВЫХОД (ESC)", self.main_font, RED)
        
        # Текст обучения
        self.tutorial_lines = [
            "Управление кораблем:",
            "← → ↑ ↓ - движение",
            "ПРОБЕЛ - стрельба",
            "",
            "Собирайте сферы для улучшений",
            "",
            "Нажмите ЛЮБУЮ КЛАВИШУ чтобы начать"
        ]

        # Игровые объекты
        self.player = Player()
        self.all_sprites = pygame.sprite.Group(self.player)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if self.state == "tutorial":
                    self.state = "name_input"
                elif self.state == "name_input":
                    if event.key == pygame.K_RETURN and self.name_input.text:
                        self.state = "game"
                    else:
                        self.name_input.handle_event(event)
                elif event.key == pygame.K_ESCAPE:
                    return False
                elif self.state == "game" and event.key == pygame.K_SPACE:
                    if self.player.can_shoot():
                        self.player.shoot()
                        # Здесь будет создание пули

        # Управление кораблем
        if self.state == "game":
            self.player.update(keys)
            
        return True

    def draw_tutorial(self):
        """Отрисовка экрана обучения"""
        self.screen.fill(BLACK)
        
        # Заголовок
        title = self.main_font.render("ОБУЧЕНИЕ", True, GREEN)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 50))

        # Текст обучения
        for i, line in enumerate(self.tutorial_lines):
            text = self.small_font.render(line, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 150 + i*35))

    def draw_name_input(self):
        """Отрисовка экрана ввода имени"""
        self.screen.fill(BLACK)
        
        # Инструкция
        prompt = self.main_font.render("ВВЕДИТЕ ВАШЕ ИМЯ:", True, GREEN)
        self.screen.blit(prompt, (SCREEN_WIDTH//2 - prompt.get_width()//2, SCREEN_HEIGHT//2 - 50))
        
        # Поле ввода
        self.name_input.draw(self.screen)
        
        # Подсказка
        hint = self.small_font.render("Нажмите ENTER чтобы начать", True, BLUE)
        self.screen.blit(hint, (SCREEN_WIDTH//2 - hint.get_width()//2, SCREEN_HEIGHT//2 + 70))

    def draw_game_ui(self):
        """Отрисовка игрового интерфейса"""
        self.screen.fill(BLACK)
        
        # Все игровые объекты
        self.all_sprites.draw(self.screen)
        
        # UI элементы
        self.title_label.draw(self.screen, 20, 20)
        self.exit_label.draw(self.screen, 
                          SCREEN_WIDTH - self.exit_label.font.size(self.exit_label.text)[0] - 20,
                          20)

    def clear(self):
        self.screen.fill(BLACK)

    def update(self):
        pygame.display.flip()

    def draw(self):
        """Основной метод отрисовки"""
        self.clear()
        
        if self.state == "tutorial":
            self.draw_tutorial()
        elif self.state == "name_input":
            self.draw_name_input()
        elif self.state == "game":
            self.draw_game_ui()
        
        self.update()