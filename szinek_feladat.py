
"""
1. Feladat
Egészítsd ki a "Példák" fülön elérhető második kódot úgy, hogy a 'b' billentyű lenyomására kék (blue),
 az 'y' gomb lenyomására sárga (yellow) legyen az ablak háttérszíne, és az ablak címe mutassa az éppen
 aktuális háttérszín RGB értékét ilyen módon: "Az ablak háttérszínének RGB értéke: (0, 255, 0)"
"""


import pygame
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
piros = (255, 0, 0)
zold = (0, 255, 0)
kek = (0, 0, 255)
sarga = (255, 255, 0)
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
                pygame.display.set_caption(f"Piros RGB{piros}")
            elif event.key == pygame.K_g:
                hatter = zold
                pygame.display.set_caption(f"Zold RGB{zold}")
            elif event.key == pygame.K_b:
                hatter = kek
                pygame.display.set_caption(f"Kék RGB{kek}")
            elif event.key == pygame.K_y:
                hatter = sarga
                pygame.display.set_caption(f"Sárga RGB{sarga}")

    kijelzo.fill(hatter)
    pygame.display.update()

pygame.quit()
