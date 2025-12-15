import pygame
import const_variable as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('Images/enemy1.png').convert_alpha()
        self.is_destoyed = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.display_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('snd_effects/hit_snd.ogg')
        self.snd_hit.set_volume(0.1)
        self.hp = 3
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3, 8)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            self.hp -= 1
            if self.hp <=0:
                self.kill()
                self.is_invincible = True
                self.is_destroyed = True
                self.rect.x = self.rect.x - 32
                self.rect.y = self.rect.y - 32
    def destroy(self):
        self.kill()