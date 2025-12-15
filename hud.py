import pygame
import const_variable as c
from healthbar import HealthBar
from score import Score

class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load('Images/hub_bg.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = c.display_height - self.rect.height
        self.health_bar = HealthBar()
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = c.display_height - self.health_bar.rect.height - 10
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)



    def update(self):
        self.score_group.update()