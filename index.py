import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
class Parent:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Player(Parent):
    def __init__(self, x1,y1,x2,y2,level):
        super().__init__(x1,y1,x2,y2)
        player.level = level
class Enemy(Parent):
    def __init__(self, x1,y1,x2,y2,level):
        super().__init__(x1,y1,x2,y2)

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if player.level == 0:
        
    if player.level == 1:



    pygame.display.update()
