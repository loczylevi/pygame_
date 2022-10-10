"""
2. Feladat - Plan
A letölthető mappában lévő repülőgépek közül válassz egyet,
és ez mozgjon a játékablakan balról jobbra! Amikor a repülőgép eléri a képernyő valemelyik szélét,
forduljon meg, és repüljön az ellenkező irányba!
"""

import pygame

WIDTH, HEIGHT = 800, 400  # width = X , height = y
BG_COLOR = (140, 137, 246)
PLANE_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
plane_surf = pygame.image.load('img/Fly_1.png').convert_alpha()
plane_rect = plane_surf.get_rect(midleft=(0, HEIGHT / 2))  # a kép köré irunk egy négyzetet
pygame.display.set_caption("Megbolondult_Boeing_737.exe")
mehet_e = True
running = True
elore = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    if plane_rect.right < WIDTH and elore:
        plane_rect.left += PLANE_SPEED
    elif plane_rect.right == WIDTH:
        elore = False
        plane_surf = pygame.image.load('img/Fly_1.png').convert_alpha()
        plane_surf = pygame.transform.flip(plane_surf, True, False)           # ezzel forditjuk meg a képet!!!!!!
        plane_rect = plane_surf.get_rect(midright=(WIDTH - 1 , HEIGHT / 2))
    if elore == False:
        plane_rect.left -= PLANE_SPEED
        #print(f"{bird_rect.left}")
    if plane_rect.left <= 0:
        elore = True
        plane_surf = pygame.image.load('img/Fly_1.png').convert_alpha()
        plane_rect = plane_surf.get_rect(midleft=(0, HEIGHT / 2))


    screen.blit(plane_surf, plane_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
