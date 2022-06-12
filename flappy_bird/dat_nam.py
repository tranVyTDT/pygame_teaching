import pygame
import random
from pygame.locals import *

pygame.init()
#setup
screen_WIDTH = 288
screen_HEIGHT = 512
scroll_speed = 4
game_over = False
velocity = 8
is_pressed = False
is_started = False
PIPE_GAP = 100

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size =(screen_WIDTH , screen_HEIGHT), depth=32)

#tạo biến chauws file hình ảnh
background_image_filename = r"assets\background-day.png"
base_image = r"assets\base.png"

#đọc file hình ảnh để hiển thị ra màn hình game
background = pygame.image.load(background_image_filename)
message = pygame.image.load('assets/message.png').convert_alpha()
base = pygame.image.load(base_image)


pygame.display.set_caption("Flappy Bird 2022")

pipe_group = pygame.sprite.Group()      
bird_group = pygame.sprite.Group()   

class Bird(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
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
        
    def update(self):
        global velocity , is_pressed, game_over
        
        self.change_image += 1
        image = self.animation[self.animation_index]
        self.rect.y += velocity
        
        if self.rect.y > 400:
            game_over = True
        
        velocity += 0.5
        if velocity > 8:
            velocity = 8

        if not game_over:
                
            if self.change_image % 10 == 0:
                self.animation_index += 1

                if self.animation_index > 2:
                    self.animation_index = 0

            if pygame.mouse.get_pressed() == ( 1, 0 ,0) and not is_pressed:
                velocity = -8
                is_pressed = True
            if pygame.mouse.get_pressed()[0] == 0:
                is_pressed = False

        #show the bird on the screen
        if velocity < 0:
            self.image = pygame.transform.rotate(image, -velocity*4)
        else:
            self.image = pygame.transform.rotate(image, velocity*-2)
                

class Pipe(pygame.sprite.Sprite):
    def __init__ (self , x , y , pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'assets\pipe-green.png').convert_alpha()
        self.rect = self.image.get_rect()

        if pos == 'top':
            self.image = pygame.transform.flip(self.image , False , True)
            self.rect.bottomleft = (x , y - PIPE_GAP / 2)

        if pos == 'bottom':
            self.rect.topleft = ( x, y + PIPE_GAP / 2)

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x < - 100:
            self.kill()

bird = Bird(screen_WIDTH/ 2 - 50 ,screen_HEIGHT / 2 )
bird_group.add(bird)

x = 0
timeline = pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            is_started = True

    screen.blit(background , (0,0))

    if is_started:
        pipe_group.draw(screen)
        bird_group.draw(screen)
        bird_group.update()
        
        if not game_over:
            if pygame.time.get_ticks() > timeline + 1000:
                pipe1 = Pipe(screen_WIDTH, screen_HEIGHT/2 + random.randint(0, 50), 'top')
                pipe2 = Pipe(screen_WIDTH, screen_HEIGHT/2 + random.randint(0, 50), 'bottom')
                pipe_group.add(pipe1)
                pipe_group.add(pipe2)
                timeline = pygame.time.get_ticks()
                
            x -= 1
            if x < -50:
                x = 0
            pipe_group.update()
            

            if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
                game_over = True

        screen.blit(base ,(x, 400))
        
    else:
        screen.blit(message, (screen_WIDTH/2 - message.get_width()/2,
                            screen_HEIGHT/2 - message.get_height()/2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
