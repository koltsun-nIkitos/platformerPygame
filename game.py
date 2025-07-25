import pygame
from player import Player
from config import FULLSCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from ui import TextInput

class Game:
    def __init__(self):
        pygame.init()
        
        if FULLSCREEN:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            SCREEN_WIDTH, SCREEN_HEIGHT = self.screen.get_size()
        else:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption("Моя Игра")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.running = False
        self.player_name = ""
        self.name_input = TextInput(
            x=SCREEN_WIDTH//2 - 150,
            y=SCREEN_HEIGHT//2 - 25,
            width=300,
            height=50
        )

    def show_name_input(self):
        input_active = True
        instruction_text = "Введите ваш никнейм и нажмите Enter:"
        font = pygame.font.Font(None, 36)
        
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                
                if self.name_input.handle_event(event):
                    self.player_name = self.name_input.text
                    return True

            self.screen.fill(BACKGROUND_COLOR)
            
            # Отрисовка инструкции
            text_surface = font.render(instruction_text, True, pygame.Color('white'))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            self.screen.blit(text_surface, text_rect)
            
            # Отрисовка поля ввода
            self.name_input.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
        return False

    def run(self):
        if not self.show_name_input():
            return
            
        self.running = True
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)

        print(self.player_name)
        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

    def _draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.player.draw(self.screen)
        pygame.display.flip()




