import pygame
from pygame.locals import *
from sys import exit


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 288


background_image_filename = r'assets\background-day.png'
bird_filename = r'assets\bluebird-midflap.png'
base_filename = r'assets\base.png'

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=RESIZABLE, depth=32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
base = pygame.image.load(base_filename).convert()

x_base = 0
y_base = 500




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    

    x_base -= 1
    if x_base < -50 :
        x_base = 0

    screen.blit(background, (0,0))
    screen.blit(base, (x_base, y_base))
    
    pygame.display.update()
    clock.tick(60) # fps frame per second

