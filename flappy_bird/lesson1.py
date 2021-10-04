import pygame
from pygame.locals import *
from sys import exit

SCREEN_HEIGHT = 550
SCREEN_WEIGHT = 288


background_image_filename = r'assets\background-day.png'
mouse_image_filename = r'assets\yellowbird-midflap.png'

pygame.init()
screen = pygame.display.set_mode((SCREEN_WEIGHT, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    screen.blit(mouse_cursor, (SCREEN_WEIGHT/2, SCREEN_HEIGHT/2))

    pygame.display.update()