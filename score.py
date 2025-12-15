import pygame
import const_variable as c 

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0 
        self.font_size = 40
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)

        self.x_pad = 20
        self.y_pad = 30
        self.image = self.font.render(str(f'score: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.display_width- self.rect.width - self.x_pad
        self.rect.y = c.display_height - self.rect.height - self.y_pad

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'score: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.display_width- self.rect.width - 20
        self.rect.y = c.display_height - self.rect.height -20