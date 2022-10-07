"""
1. Feladat
Fejleszd tovább a videóban bemutatott - és a Példák részben letölthető - kódot úgy, hogy a madár ne repüljön ki a képernyő jobb oldalán!
"""

import pygame

WIDTH, HEIGHT = 800, 400  # width = X , height = y
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bird_surf = pygame.image.load('img/bird1.png').convert_alpha()
bird_x = 0  # width = X , height = y
bird_y = 200 # width = X , height = y
mehet_e = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    if bird_x >= 670:
        bird_x = 670
        mehet_e = False
    if mehet_e:
        bird_x += BIRD_SPEED
    screen.blit(bird_surf, (bird_x, bird_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
