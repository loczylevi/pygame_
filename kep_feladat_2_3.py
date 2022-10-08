"""
2.3 Feladat - Plan
A letölthető fájlok között találsz egy háttérképet is. Töltsd be azt is!

"""

import pygame

WIDTH, HEIGHT = 800, 400  # width = X , height = y
PLANE_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
plane_surf = pygame.image.load('img/Fly_1.png').convert_alpha()
bg = pygame.image.load("img/BG.png").convert_alpha()
plane_x = 0  # width = X , height = y
plane_y = 200 # width = X , height = y
mehet_e = True
running = True
szamlalo = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if plane_x >= 800:
        plane_x = -200
        szamlalo += 1
        #mehet_e = False
    if mehet_e and szamlalo < 2:
        plane_x += PLANE_SPEED
    screen.blit(bg, (0, 0))
    screen.blit(plane_surf, (plane_x, plane_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
