import pygame
from pygame.locals import *
from sys import exit, flags


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 288


background_image_filename = r'assets\background-day.png'
message_filename = r'assets\message.png'

pygame.init()
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=RESIZABLE, depth=32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
message = pygame.image.load(message_filename).convert_alpha()

x = SCREEN_WIDTH / 2 - message.get_width() / 2
y = SCREEN_HEIGHT / 2 - message.get_height() / 2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        print(event)

    screen.blit(background, (0,0))
    screen.blit(message, (x, y))

    pygame.display.update()