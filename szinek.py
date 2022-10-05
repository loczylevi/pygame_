import pygame
import random
szinek = ['yellow','red','white','purple','brown','green','blue',"black"]
index = random.randint(0,7)
pygame.init()

kijelzo = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("Barokkos_Szinek.exe")
futattas = True
while futattas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            futattas = False
    kijelzo.fill(szinek[index])
    pygame.display.update()

pygame.quit()