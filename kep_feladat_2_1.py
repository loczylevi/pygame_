"""
2.1 Feladat - Plan
A letölthető mappában lévő repülőgépek közül válassz egyet, és ez mozgjon a játékablakan balról jobbra! A repülőgép ne tudja elhagyni a játékablakot!
"""

import pygame

WIDTH, HEIGHT = 800, 400  # width = X , height = y
BG_COLOR = (140, 137, 246)
PLANE_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
plane_surf = pygame.image.load('img/Fly_1.png').convert_alpha()
plane_x = 0  # width = X , height = y
plane_y = 200 # width = X , height = y
mehet_e = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    if plane_x >= 650:
        plane_x = 650
        mehet_e = False
    if mehet_e:
        plane_x += PLANE_SPEED
    screen.blit(plane_surf, (plane_x, plane_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
