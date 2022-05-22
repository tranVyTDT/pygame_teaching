import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 30

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption('homeword 4')







class Block(pygame.sprite.Sprite):
    def __init__(self,x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = color

        
    def update(self):
        pygame.draw.rect(screen,  self.color, self.rect)


block1 = Block(50, 50, 'red')
block2 = Block(100, 100, 'blue')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    block1.update()
    block2.update()

    pygame.display.update()
    clock.tick(fps)
pygame.quit()