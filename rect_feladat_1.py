"""
1. Feladat
Fejleszd tovább a videó második részében elkészített -
és a Példák részben letölthető - kódot úgy, hogy amikor a madár ismét eléri a képernyő jobb szélét, újra megfordul,
 és így repül tovább. Tehát a madár folyamatosan repked a képernyő két széle között mindig a megfelelő irányba nézve!
"""

import pygame

WIDTH, HEIGHT = 800, 400  # width = X , height = y
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bird_surf = pygame.image.load('img/bird1.png').convert_alpha()

bird_rect = bird_surf.get_rect(midleft=(0, HEIGHT / 2))  # a kép köré irunk egy négyzetet
pygame.display.set_caption("Megbolondult_madar.exe")
mehet_e = True
running = True
elore = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    if bird_rect.right < WIDTH and elore:
        bird_rect.left += BIRD_SPEED
    elif bird_rect.right == WIDTH:
        elore = False
        bird_surf = pygame.image.load('img/bird1back.png').convert_alpha()
        bird_rect = bird_surf.get_rect(midright=(WIDTH - 1 , HEIGHT / 2))
    if elore == False:
        bird_rect.left -= BIRD_SPEED
        #print(f"{bird_rect.left}")
    if bird_rect.left <= 0:
        elore = True
        bird_surf = pygame.image.load('img/bird1.png').convert_alpha()
        bird_rect = bird_surf.get_rect(midleft=(0, HEIGHT / 2))


    screen.blit(bird_surf, bird_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
