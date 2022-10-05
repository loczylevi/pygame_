import pygame
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
print(red,green,blue)
pygame.init()

kijelzo = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("Barokkos_Szinek.exe")
futattas = True
while futattas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            futattas = False
    kijelzo.fill((red,green,blue))
    pygame.display.update()

pygame.quit()