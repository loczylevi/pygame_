import pygame
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

WIDTH, HEIGHT = 800, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pityu_karakter = pygame.image.load('img/proba.png').convert_alpha()

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
        pityu_y += 2
        pityu_x += 2
    pygame.display.update()
    clock.tick(60)
pygame.quit()
