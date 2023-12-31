import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
class Parent:
    def __init__(self,x1,y1,x2,y2,color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.rect = pygame.Rect(self.x1,self.y1,self.x2,self.y2)
    def appear(self):
        pygame.draw.rect(screen,self.color,self.rect)

class Player(Parent):
    def __init__(self, x1,y1,x2,y2,color,level):
        super().__init__(x1,y1,x2,y2,color)
        self.level = level
class Enemy(Parent):
    def __init__(self, x1,y1,x2,y2,color):
        super().__init__(x1,y1,x2,y2,color)
class Objective(Parent):
    def __init__(self, x1,y1,x2,y2,color,level):
        super().__init__(x1,y1,x2,y2,color)
        self.level = level


player = Player(0,0,32,32,(255,0,0),1)
obj_list = []
enemy_list = []



running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while player.level == 0:
        pass
    while player.level == 1:
        player.appear()
        for obj in obj_list:
            if pygame.Rect.colliderect(player.rect,obj.rect):
                pass


    pygame.display.update()
