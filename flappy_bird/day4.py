import pygame as pg
from pygame.locals import *
from sys import exit

HEIGHT = 768
WIDTH = 864

pg.init()
clock = pg.time.Clock()
fps = 60

screen = pg.display.set_mode((HEIGHT, WIDTH), pg.RESIZABLE)

bg = pg.image.load("img/bg.png").convert()
message = pg.image.load("assets/message.png").convert_alpha()
ground = pg.image.load("img/ground.png").convert_alpha()
bird_1 = pg.image.load("img/bluebird-1.png").convert_alpha()
bird_2 = pg.image.load("img/bluebird-2.png").convert_alpha()
bird_3 = pg.image.load("img/bluebird-3.png").convert_alpha()


x = 0
gravity = 1
is_pressed = False
game_over = False
is_started = False

class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bird_1
        self.counter = 0
        self.images = [bird_1, bird_2, bird_3]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        
    def update(self):
        global gravity, is_pressed, game_over
        
        if not game_over:
            self.rect.y += gravity
            if self.rect.y > 750:
                game_over = True

            gravity += 0.5
            if gravity > 8:
                gravity = 8

            if pg.mouse.get_pressed()[0] and not is_pressed:
                gravity = -8
                is_pressed = True

            if not pg.mouse.get_pressed()[0]:
                is_pressed = False
            self.counter += 1

            if self.counter > 16:
                self.image_index = self.image_index + 1
                self.counter = 0

            if self.image_index > 2:
                self.image_index = 0

            self.image = self.images[self.image_index]

            screen.blit(pg.transform.rotate(self.image, gravity * 2), (self.rect.x, self.rect.y))
        
        else:
            screen.blit(pg.transform.rotate(self.image, -90), (self.rect.x, self.rect.y))





bird = Bird(WIDTH / 2, HEIGHT / 2)

while True:
    clock.tick(fps)
    screen.blit(bg, (0, 0))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            is_started = True

    if is_started:
        bird.update()

        if not game_over:
            x -= 1
            if x == -100:
              x = 0

    else:
        screen.blit(message, (WIDTH / 2 - message.get_width() / 2,
                              HEIGHT / 2 - message.get_height() / 2))
    
    screen.blit(ground, (x, 768))
    

    pg.display.update()