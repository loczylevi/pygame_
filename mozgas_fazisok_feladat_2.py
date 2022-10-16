"""
2. Feladat - Robot
Készíts egy programot, amelyben a robot a képernyő középső harmadában jobbra-balra rohangál.
 A robot mindig a haladás irányába nézzen!
 A képek méretezését és tükrözését a kódban valósítsd meg! Válassz egy megfelelő háttérképet is!
"""
import pygame
import pygame as pygame

WIDTH, HEIGHT = 1200, 600
ROBOT_SPEED = 5
BG_COLOR = (140, 137, 246)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

robot_surf_1 = pygame.image.load('img/robot/Run_1.png').convert_alpha()
robot_surf_1 = pygame.transform.rotozoom(robot_surf_1, 0, 0.4)
robot_surf_2 = pygame.image.load('img/robot/Run_2.png').convert_alpha()
robot_surf_2 = pygame.transform.rotozoom(robot_surf_2, 0, 0.4)
robot_surf_3 = pygame.image.load('img/robot/Run_3.png').convert_alpha()
robot_surf_3 = pygame.transform.rotozoom(robot_surf_3, 0, 0.4)
robot_surf_4 = pygame.image.load('img/robot/Run_4.png').convert_alpha()
robot_surf_4 = pygame.transform.rotozoom(robot_surf_4, 0, 0.4)
robot_surf_5 = pygame.image.load('img/robot/Run_5.png').convert_alpha()
robot_surf_5 = pygame.transform.rotozoom(robot_surf_5, 0, 0.4)
robot_surf_6 = pygame.image.load('img/robot/Run_6.png').convert_alpha()
robot_surf_6 = pygame.transform.rotozoom(robot_surf_6, 0, 0.4)
robot_surf_7 = pygame.image.load('img/robot/Run_7.png').convert_alpha()
robot_surf_7 = pygame.transform.rotozoom(robot_surf_7, 0, 0.4)
robot_surf_8 = pygame.image.load('img/robot/Run_8.png').convert_alpha()
robot_surf_8 = pygame.transform.rotozoom(robot_surf_8, 0, 0.4)

robot_surf = [robot_surf_1, robot_surf_2, robot_surf_3, robot_surf_4, robot_surf_5, robot_surf_6,robot_surf_7, robot_surf_8]

robot_surf_1_ = pygame.image.load('img/robot/Run_1.png').convert_alpha()
robot_surf_1_ = pygame.transform.flip(robot_surf_1_, True, False)
robot_surf_1_ = pygame.transform.rotozoom(robot_surf_1_, 0, 0.4)
robot_surf_2_ = pygame.image.load('img/robot/Run_2.png').convert_alpha()
robot_surf_2_ = pygame.transform.flip(robot_surf_2_, True, False)
robot_surf_2_ = pygame.transform.rotozoom(robot_surf_2_, 0, 0.4)
robot_surf_3_ = pygame.image.load('img/robot/Run_3.png').convert_alpha()
robot_surf_3_ = pygame.transform.flip(robot_surf_3_, True, False)
robot_surf_3_ = pygame.transform.rotozoom(robot_surf_3_, 0, 0.4)
robot_surf_4_ = pygame.image.load('img/robot/Run_4.png').convert_alpha()
robot_surf_4_ = pygame.transform.flip(robot_surf_4_, True, False)
robot_surf_4_ = pygame.transform.rotozoom(robot_surf_4_, 0, 0.4)
robot_surf_5_ = pygame.image.load('img/robot/Run_5.png').convert_alpha()
robot_surf_5_ = pygame.transform.flip(robot_surf_5_, True, False)
robot_surf_5_ = pygame.transform.rotozoom(robot_surf_5_, 0, 0.4)
robot_surf_6_ = pygame.image.load('img/robot/Run_6.png').convert_alpha()
robot_surf_6_ = pygame.transform.flip(robot_surf_6_, True, False)
robot_surf_6_ = pygame.transform.rotozoom(robot_surf_6_, 0, 0.4)
robot_surf_7_ = pygame.image.load('img/robot/Run_7.png').convert_alpha()
robot_surf_7_ = pygame.transform.flip(robot_surf_7_, True, False)
robot_surf_7_ = pygame.transform.rotozoom(robot_surf_7_, 0, 0.4)
robot_surf_8_ = pygame.image.load('img/robot/Run_8.png').convert_alpha()
robot_surf_8_ = pygame.transform.flip(robot_surf_8_, True, False)
robot_surf_8_ = pygame.transform.rotozoom(robot_surf_8_, 0, 0.4)

robot_surf_forditott = [robot_surf_1_, robot_surf_2_, robot_surf_3_, robot_surf_4_, robot_surf_5_, robot_surf_6_,robot_surf_7_, robot_surf_8_]
bg = pygame.image.load("img/BG.png").convert_alpha()
robot_index = 0
robot_rect = robot_surf[robot_index].get_rect(midleft=(0, HEIGHT / 2))

pygame.display.set_caption("Megbolondult_robot.exe")
mehet_elore = True
mehet_hatra = False
counter = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    counter += 1
    if counter % 10 == 0:
        robot_index += 1
    if robot_index > len(robot_surf) - 1:
        robot_index = 0

    if robot_rect.right < WIDTH and mehet_elore:
        robot_rect.left += ROBOT_SPEED
        print(f"{robot_rect.left}")

    if robot_rect.right >= WIDTH:
        mehet_elore = False
        mehet_hatra = True

    if mehet_elore == False :
        robot_rect.left -= ROBOT_SPEED
        print(f"{robot_rect.left}")

    if robot_rect.left <= 0:
        mehet_elore = True

    screen.blit(bg, (0, 0))
    if mehet_elore:
        screen.blit(robot_surf[robot_index], robot_rect)
    elif mehet_hatra:
        screen.blit(robot_surf_forditott[robot_index], robot_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
