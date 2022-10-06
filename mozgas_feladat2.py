"""
2. Feladat
Rajzolj egy alakzatot a játékablak bal felső, egyet pedig a jobb felső sarkába.
 A két alakzat átlósan mozogjon lefelé, de egyik se hagyja el a játékablak területét!
"""


import pygame

WIDTH, HEIGHT = 600, 300 #width = x height = y
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BG_COLOR = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect_pos_x = 10
rect_pos_y = 20

circle_pos_x = 30
circle_pos_y = 500

clock = pygame.time.Clock()
hozzaadni_szabad = True
hozzaadni_szabad2 = True
running = True
#while True:
    #for sor in pygame.event.get():
        #print(sor)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    if rect_pos_x >= 500 and rect_pos_y >= 210:
        rect_pos_x = 500
        rect_pos_y = 210
        hozzaadni_szabad = False

    if circle_pos_x >= 250 and circle_pos_y >= 50:
        circle_pos_x = 250
        circle_pos_y = 50
        hozzaadni_szabad2 = False

    if hozzaadni_szabad:
        rect_pos_x += 5
        rect_pos_y += 2

    if hozzaadni_szabad2:
        #print(f"X: {circle_pos_x}")
        #print(f"Y: {circle_pos_y}")
        circle_pos_x += 5
        circle_pos_y -= 10

    rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)
    rect2 = pygame.Rect(circle_pos_y, circle_pos_x, 100, 50)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.draw.rect(screen, RED, rect2)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

