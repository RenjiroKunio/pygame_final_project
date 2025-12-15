import pygame
import const_variable as c

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar, self).__init__()
        self.image = pygame.image.load('Images/hp_bar1.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        pass