import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 30

screen_width = 288
screen_height = 550

screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4
fall_velocity = 1
is_alive = True
is_start = False
is_pressed = False

#load images
bg = pygame.image.load('assets/background-day.png')
ground_img = pygame.image.load('assets/base.png')
message = pygame.image.load('assets/message.png')

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        

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
        global fall_velocity, is_alive, is_pressed

        #handle the animation
        self.counter += 1
        flap_cooldown = 10

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0
                
        #self.image = self.images[self.index]
        if fall_velocity < 0 :
            self.image = pygame.transform.rotate(self.images[self.index], fall_velocity * -1 * 5)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], fall_velocity * -1 * 3)

        # handle gravity
        self.rect.y += fall_velocity
        
        fall_velocity += 0.8
        if fall_velocity > 6 : fall_velocity = 6
        
        if self.rect.y > 485: 
            is_alive = False
        
        if pygame.mouse.get_pressed() == (1, 0, 0) and not is_pressed :
            fall_velocity = -5
            is_pressed = True
        
        if pygame.mouse.get_pressed()[0] == 0 : is_pressed = False



bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 5))
bird_group.add(flappy)



run = True
while run:

    #draw and scroll the ground
    if is_alive:
        screen.blit(bg, (0,0))
       
        if not is_start :
            message_x = screen_width / 2 - message.get_width() / 2
            message_y = screen_height / 2 - message.get_height() / 2
            screen.blit(message, (message_x, message_y))

        

        if is_start:
            bird_group.draw(screen)
            bird_group.update()

            ground_scroll -= scroll_speed

            if abs(ground_scroll) > 35:
                ground_scroll = 0

        screen.blit(ground_img, (ground_scroll, 500))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_start = True

    pygame.display.update()
    clock.tick(fps)
pygame.quit()