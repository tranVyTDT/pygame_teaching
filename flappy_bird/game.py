import pygame as pg
import sys
import random

PIPE_GAP = 100

pg.init()
#path
background_path = r"assets\background-day.png "
floor_path = r"assets\base.png"
start_game_message = r'assets\message.png'

#screen
scroll_speed = 1
screen_height = 512 
screen_width = 288
screen = pg.display.set_mode((screen_width, screen_height), pg.RESIZABLE)
clock = pg.time.Clock()
velocity = 0 
jump_height = -8
is_pressed = False
is_start = False
#background
background = pg.image.load(background_path).convert_alpha()
#floor
floor = pg.image.load(floor_path).convert_alpha()
message = pg.image.load(start_game_message).convert_alpha()
floor_x = 0

class Pipe(pg.sprite.Sprite):

    def __init__(self, x, y, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"assets\pipe-green.png").convert_alpha()
        self.rect = self.image.get_rect()

        if pos == 'top':
            self.image = pg.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - PIPE_GAP / 2 )
        
        if pos == 'bottom':
            self.rect.topleft = (x, y + PIPE_GAP / 2 )
    

    def update(self):
        self.rect.x -= scroll_speed

        if self.rect.x < -100:
            self.kill()


class Bird(pg.sprite.Sprite):
    
    COOLDOWN = 10
    
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.images =[]
        self.image_index = 0
        self.load_data()
        self.count_cooldown =0
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (x, y)
        
    
    def load_data(self):
        self.image_paths = [ r"assets\bluebird-midflap.png",
                             r"assets\bluebird-downflap.png",
                             r"assets\bluebird-upflap.png"]
        for path in self.image_paths:
            img = pg.image.load(path).convert_alpha()
            self.images.append(img)
    
    def fall_down(self):
        global velocity
        velocity += 0.5
        if velocity > 8 : velocity = 8
        self.rect.y += velocity

    def update(self):
        global velocity, jump_height, is_pressed, is_start

        self.count_cooldown += 1
        if self.count_cooldown == Bird.COOLDOWN:
            self.image_index += 1
            if self.image_index > 2:
                self.image_index =0
        
            self.image  = self.images[self.image_index]
            self.count_cooldown =0
        
        if pg.mouse.get_pressed()[0] == 1 and not is_pressed:
            velocity = jump_height
            is_pressed = True
        
        if pg.mouse.get_pressed()[0] == 0 :
            is_pressed = False

            
        self.fall_down()


        if velocity > 0:
            self.image = pg.transform.rotate(self.images[self.image_index], velocity * 3)
        else:
            self.image = pg.transform.rotate(self.images[self.image_index], velocity * 2)



bird_group = pg.sprite.Group()
pipe_group = pg.sprite.Group()

bird = Bird(80,screen_height/2)
bird_group.add(bird)

spawn_pipe = 3000
time = pg.time.get_ticks()

while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            is_start = True
    
    screen.blit(background,(0,0))
    screen.blit(floor,(floor_x,450))

    if not is_start:
        x = screen_width / 2 - message.get_width() / 2
        y = screen_height / 2 - message.get_height() / 2
        screen.blit(message, (x, y))

    else:
        floor_x -= scroll_speed
        if floor_x < -40:
            floor_x = 0
            
        if pg.time.get_ticks() - time > spawn_pipe:
            y = random.randint(screen_height/ 2 - 75, screen_height/ 2 + 75)
            pipe1 = Pipe(screen_width, y, 'top')
            pipe2 = Pipe(screen_width, y, 'bottom')
            pipe_group.add(pipe1)
            pipe_group.add(pipe2)
            time = pg.time.get_ticks()
    
        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)
        pipe_group.update()
    
    
    pg.display.update()
    clock.tick(60)
    
    
pg.quit()