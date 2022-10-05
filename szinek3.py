import pygame
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
piros = (255, 0, 0)
zold = (0, 255, 0)
print(red,green,blue)
pygame.init()

kijelzo = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("Barokkos_Szinek.exe")
futattas = True
hatter = (blue,red,green)
while futattas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            futattas = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                hatter = piros
            elif event.key == pygame.K_g:
                hatter = zold

    kijelzo.fill(hatter)
    pygame.display.update()

pygame.quit()
