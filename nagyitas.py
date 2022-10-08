import pygame
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

WIDTH, HEIGHT = 800, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pityu_karakter = pygame.image.load('img/cuccmok2.png').convert_alpha()

pityu_karakter = pygame.transform.rotozoom(pityu_karakter, 0, 3)    # nagyitás!!! ---_-  pygame.transform.rotozoom(surface, forgatasi_szog, nagyitas_merteke) 

pityu_x = 0
pityu_y = 200

pygame.display.set_caption("Barkkos-Game.exe")
hatter = (blue,red,green)

running = True
mehet_e = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(hatter)
    screen.blit(pityu_karakter, (pityu_y, pityu_x))
    if pityu_x >= 250 and pityu_y >= 450:
        pityu_x = 250
        pityu_y = 450
        mehet_e = False
    if mehet_e:
        pityu_y += 1
        pityu_x += 1
    pygame.display.update()
    clock.tick(60)
pygame.quit()
