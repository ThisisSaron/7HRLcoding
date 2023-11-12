import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
class Parent:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.rect = pygame.rect(x1,y1,x2,y2)

class Player(Parent):
    def __init__(self, x1,y1,x2,y2,level):
        super().__init__(x1,y1,x2,y2)
        self.level = level
class Enemy(Parent):
    def __init__(self, x1,y1,x2,y2):
        super().__init__(x1,y1,x2,y2)
class Objective(Parent):
    def __init__(self, x1,y1,x2,y2,level):
        super().__init__(x1,y1,x2,y2)
        self.level = level



obj_list = []
enemy_list = []



running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while player.level == 0:

    while player.level == 1:
        for obj in obj_list:
            if pygame.Rect.colliderect(player.rect,obj.rect)



    pygame.display.update()
