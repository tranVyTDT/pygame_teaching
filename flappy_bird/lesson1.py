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
bird = pygame.image.load(bird_filename).convert_alpha()


x_base = 0
y_base = 500


class Bird(pygame.sprite.Sprite):

    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.animation_index =  0
        self.change_image = 0
        bird1 = pygame.image.load(r"assets\redbird-downflap.png").convert_alpha()
        bird2 = pygame.image.load(r"assets\redbird-midflap.png").convert_alpha()
        bird3 = pygame.image.load(r"assets\redbird-upflap.png").convert_alpha()
        self.animation = [bird1, bird2, bird3]

        # assign the first bird image for the bird 
        self.image = self.animation[self.animation_index]

    def blit_bird(self):
        self.change_image += 1

        if self.change_image % 10 == 0:
            self.animation_index += 1
            
            if self.animation_index > 2 :
                self.animation_index = 0 # reset index to 0 if index greater than 2
            
            # change bird image
            self.image = self.animation[self.animation_index] 
        
        if pygame.mouse.get_pressed() == (1, 0, 0) :
            self.rect.y -= 10
        
        # show the bird on the screen
        screen.blit(self.image, (self.x, self.y))

x = SCREEN_WIDTH / 2 - 50
y = SCREEN_HEIGHT / 2 

bird = Bird(x, y)


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
    bird.blit_bird()
    
    pygame.display.update()
    clock.tick(60) # fps frame per second