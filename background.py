import pygame
import random
import const_variable as c
from star import Star

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.Surface(c.display_size)
        self.color = (0, 0, 30)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1, 20)

    def update(self):
        self.stars.update()
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = random.randrange(1, 20)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1

