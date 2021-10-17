import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 288
screen_height = 550

screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('assets/background-day.png')
ground_img = pygame.image.load('assets/base.png')


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        
        img1 = pygame.image.load('assets\yellowbird-downflap.png')
        img2 = pygame.image.load('assets\yellowbird-midflap.png')
        img3 = pygame.image.load('assets\yellowbird-upflap.png')
        self.images.extend([img1, img2, img3])

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):

        #handle the animation
        self.counter += 1
        flap_cooldown = 10

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)



run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()

    #draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()