import pygame
import const_variable as c
from bullet import Bullet
from hud import HUD

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('Images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.display_width // 2
        self.rect.y = c.display_height - self.rect.height * 2.6
        self.bullets = pygame.sprite.Group()
        self.shoot_snd = pygame.mixer.Sound('snd_effects./player_bullet.ogg')
        self.shoot_snd.set_volume(0.1)
        self.hp = 3
        self.hud = HUD()
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.lives = 3
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 10
        
    def update(self):
        self.bullets.update()
        self.hud_group.update()
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.display_width - self.rect.width:
            self.rect.x = c.display_width - self.rect.width
        self.rect.y += self.vel_y

    def shoot(self):
        self.shoot_snd.play()
        new_bullet = Bullet()
        new_bullet.rect.midbottom = self.rect.midtop
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.hp = 0
        
        print(self.hp)

    def death(self):
        self.lives -= 1
        if self.lives <= 0:
            self.lives = 0
        self.hp = 3
