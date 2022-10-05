import pygame

pygame.init()

kijelzo = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("Barokkos_Játék.exe")
futattas = True
while futattas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            futattas = False
    pygame.display.update()

pygame.quit()