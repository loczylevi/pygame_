"""
1. Feladat
A videóban bemutatott kódot, amely a Példák részben leölthető,
alakítsd át úgy, hogy a téglalap csak a játékablak széléig mozgjon,
de azt ne hagyja el!
"""
import pygame

WIDTH, HEIGHT = 600, 300 #width = x height = y
BLUE = (0, 0, 255)
BG_COLOR = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect_pos_x = 10
rect_pos_y = 20

clock = pygame.time.Clock()
hozzaadni_szabad = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    if rect_pos_x >= 500 and rect_pos_y >= 210:
        rect_pos_x = 500
        rect_pos_y = 210
        hozzaadni_szabad = False

    if hozzaadni_szabad:
        rect_pos_x += 5
        rect_pos_y += 2

    rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

