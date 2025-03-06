import pygame # modul betarhálása

pygame.init() #modul inicionilázása

screen = pygame.display.set_mode((600,300))  #képernyő méret
pygame.display.set_caption("Diablo_4.exe")
mennyen_e = True
while mennyen_e:
  for event in pygame.event.get(): # inputok a felhasználotol
    if event.type == pygame.QUIT:
      mennyen_e = False

  pygame.display.update()



pygame.quit()