import pygame # modul betarhálása
import random

WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
BLACK = [0,0,0]
xd = [WHITE,RED,GREEN,BLUE,BLACK]

pygame.init() #modul inicionilázása

screen = pygame.display.set_mode((600,300))  #képernyő méret
pygame.display.set_caption("szinek.exe")
mennyen_e = True
RGB = []
for szam in range(0,3):
  szin = random.randint(0,255)
  RGB.append(szin)


velet_background = random.choice(xd)
while mennyen_e:
  for event in pygame.event.get(): # inputok a felhasználotol
    if event.type == pygame.QUIT:
      mennyen_e = False

    if pygame.KEYDOWN == event.type:
      if event.key == pygame.K_r:
        velet_background = RED
      if event.key == pygame.K_g:
        velet_background = GREEN
      if event.key == pygame.K_b:
        velet_background = BLUE
      if event.key == pygame.K_w:
        velet_background = WHITE

      
      

  screen.fill(velet_background)

  pygame.display.update()



pygame.quit()