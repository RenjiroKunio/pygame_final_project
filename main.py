import pygame
from player import Ship
import const_variable as c
from background import Background
from spawner import Spawner

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# Display
display = pygame.display.set_mode((c.display_size))
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# Items on screen
bg = Background()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = Spawner()

#Soundtrack
pygame.mixer.music.load('snd_effects/bg_music.ogg')
pygame.mixer.music.set_volume(.3)
pygame.mixer.music.play(loops=True)

pygame.font.init()

running = True
while running:
    #Tick Clock for Framerate
    clock.tick(fps)

    #Check for Key presses 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.vel_x = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.vel_x = 0
            elif event.key == pygame.K_d:
                player.vel_x = 0

    
    #Update all object states in memory
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()

    # Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible:
            player.get_hit()
        enemy[0].hp = 0
        enemy[0].get_hit()

    # Draw Objects on the screen
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)

    pygame.display.update()