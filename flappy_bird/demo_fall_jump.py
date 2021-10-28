import  pygame
import sys
from pygame.locals import *

def jump(): # method 2
    global jump_height, is_pressed, velocity

    if pygame.mouse.get_pressed() == (1,0,0) and not is_pressed:
        #rect1.y -= jump_height
        velocity = jump_height
        is_pressed = True
    
    if pygame.mouse.get_pressed()[0] == 0:
        is_pressed = False


def fall_down():
    global velocity
    velocity += 1
    if velocity > 8: velocity = 8
    rect1.y += velocity
    pygame.draw.rect(screen, (45, 204, 87), rect1)

    
pygame.init()

clock = pygame.time.Clock()

WIDTH = 500
HEIGHT = 900
velocity = 1
jump_height = -10
is_pressed = False

rect1 = pygame.Rect(200, 100, 50, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((252, 88, 242), rect=None, special_flags=0)
    
    fall_down()
    jump()

    pygame.display.update()
    clock.tick(60)

