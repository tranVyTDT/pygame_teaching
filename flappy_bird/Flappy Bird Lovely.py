import pygame
from pygame.locals import *

#setup
screen_WIDTH = 288
screen_HEIGHT = 512

velocity = 8
is_pressed = False
PIPE_GAP = 100

clock = pygame.time.Clock()

#tạo biến chauws file hình ảnh
background_image_filename = r"assets\background-day.png"
base_image = r"assets\base.png"
#đọc file hình ảnh để hiển thị ra màn hình game
background = pygame.image.load(background_image_filename)
base = pygame.image.load(base_image)

pygame.init()
screen = pygame.display.set_mode(size =(screen_WIDTH , screen_HEIGHT), depth=32)
pygame.display.set_caption("Flappy Bird 2022")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x , y):
      
      
        self.animation_index = 0
        self.change_image = 0
        bird_down = pygame.image.load(r'assets\yellowbird-downflap.png')
        bird_mid = pygame.image.load(r'assets\yellowbird-midflap.png')
        bird_up = pygame.image.load(r'assets\yellowbird-upflap.png')

        self.animation = [bird_down , bird_mid , bird_up]

        self.image = self.animation[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def blit_bird(self):
        global velocity , is_pressed
        self.change_image += 1
        self.rect.y += velocity
         
        velocity += 0.5
        if velocity > 8:
            velocity = 8
        if self.change_image % 10 == 0:
            self.animation_index += 1

            if self.animation_index > 2:
                self.animation_index = 0

            self.image = self.animation[self.animation_index]

        if pygame.mouse.get_pressed() == ( 1, 0 ,0) and not is_pressed:
            velocity = -8
            is_pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            is_pressed = False

        #show the bird on the screen
        if velocity < 0:
            screen.blit(pygame.transform.rotate(self.image, -velocity*4) , (self.rect.x , self.rect.y))
        else:
            screen.blit(pygame.transform.rotate(self.image, velocity*-2) , (self.rect.x , self.rect.y))
                


bird = Bird(screen_WIDTH/ 2 - 50 ,screen_HEIGHT / 2 )

class Pipe(pg.sprite.Sprite):
    def __init__ (self , x , y , pos):
        pg.sprite.Sprite.__init__(self)
        base.image = pygame.image.load(r'assets\green_pipe.png').convert_alpha()
        self.rect = self.image.get_rect()

        if pos == 'top':
            self.image = pg.transform.flip(self.image , False , True)
            self.rect.bottomleft = (x , y - PIPE_GAP / 2)

        if pos == 'bottom':
            self.rect.topleft = ( x, y + PIPE_GAP / 2)

    def update(self):
        self.rect.x == scroll_speed
        if self.rect.x < - 100:
            self.kill()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    screen.blit(background , (0,0))
    screen.blit(base ,(0, 400))
    bird.blit_bird()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
