import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_IMAGE

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Параметры размера
        self.width = 200  # Увеличен в 2 раза от предыдущего (было 30)
        self.height = 100  # Увеличен в 2 раза от предыдущего (было 20)
        
        try:
            # Загрузка и масштабирование с сохранением пропорций
            original_image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
            orig_width, orig_height = original_image.get_size()
            scale_factor = min(self.width/orig_width, self.height/orig_height)
            self.image = pygame.transform.smoothscale(
                original_image, 
                (int(orig_width*scale_factor), int(orig_height*scale_factor))
            )
        except:
            # Запасной вариант - зеленый треугольник
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, (0, 255, 0), 
                              [(self.width//2, 0), 
                               (0, self.height), 
                               (self.width, self.height)])
            print(f"Ошибка загрузки изображения: {PLAYER_IMAGE}")

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        
        # Сбалансированная скорость
        self.speed = 10  # Оптимально для нового размера
        self.shoot_cooldown = 180
        self.last_shot = pygame.time.get_ticks()

    def update(self, keys):
        # Плавное движение с проверкой границ
        new_x = self.rect.x
        new_y = self.rect.y
        
        if keys[pygame.K_LEFT]: new_x -= self.speed
        if keys[pygame.K_RIGHT]: new_x += self.speed
        if keys[pygame.K_UP]: new_y -= self.speed
        if keys[pygame.K_DOWN]: new_y += self.speed

        # Проверка границ
        self.rect.x = max(0, min(new_x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(new_y, SCREEN_HEIGHT - self.rect.height))

    def can_shoot(self):
        return pygame.time.get_ticks() - self.last_shot > self.shoot_cooldown

    def shoot(self):
        self.last_shot = pygame.time.get_ticks()
        return True