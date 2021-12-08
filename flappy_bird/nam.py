import pygame
import random
from pygame.locals import *
from sys import exit, flags

pygame.init()

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 238
PIPE_GAP = 100
NEW_PIPE = 1000


background_image_filename = r'assets\background-day.png'
bluefilename = r'assets\bluebird-downflap.png'
base =  r'assets\base.png'
message = r'assets\message.png'

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=RESIZABLE, depth=32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
blue = pygame.image.load(bluefilename).convert_alpha()
base1 = pygame.image.load(base).convert_alpha()
message = pygame.image.load(message).convert_alpha()

font = pygame.font.SysFont('Segoe UI', 35)

x = SCREEN_WIDTH / 2 - blue.get_width() / 2
y = SCREEN_HEIGHT / 2 - blue.get_height() / 2

x_base = 0
y_base = 500
fall_velocity = 1
is_alive = True
is_start = False
ground_scroll = 0
scroll_speed = 4
is_pressed = True
pass_pipe = False
score = 0

def draw_text(font, text, x, y):
   text_surface = font.render(text, '-1' , 'orange')
   screen.blit(text_surface, (x, y))


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'assets\pipe-green.png').convert_alpha()
        self.rect = self.image.get_rect()

        if position == 'top':
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y]
        else:
            self.rect.topleft = [x,y]
    
    def update(self):
        PIPE_VEL = 2

        if is_alive:    
            self.rect.x -= PIPE_VEL

        if self.rect.x < -50:
            self.kill()
        

class Bird(pygame.sprite.Sprite):


    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.animation_index = 0
        self.change_image = 0
        blue1 = pygame.image.load(r'assets\bluebird-downflap.png').convert_alpha()
        blue2 = pygame.image.load(r'assets\bluebird-midflap.png').convert_alpha()
        blue3 = pygame.image.load(r'assets\bluebird-upflap.png').convert_alpha()
        self.animation = [blue1, blue2, blue3]
        self.image = self.animation[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.score_sound = pygame.mixer.Sound('sound\sfx_point.wav')

        
    def update(self):
        global fall_velocity, is_alive, is_pressed

        if is_alive:
            #làm con chim đập cánh
            self.change_image += 1
            if self.change_image % 5 == 0:
                self.animation_index +=1
            
            if self.animation_index > 2:
                self.animation_index = 0

            if fall_velocity < 0:
                #screen.blit(pygame.transform.rotate(self.image[self.index], fall_velocity*-1*3))
                self.image = pygame.transform.rotate(self.animation[self.animation_index], fall_velocity*-1*5)
            else:
                self.image = pygame.transform.rotate(self.animation[self.animation_index], fall_velocity*-1*4)            

        #làm con chim rớt
        if self.rect.y < 480:
            self.rect.y += fall_velocity
            fall_velocity += 0.3
            if fall_velocity > 6: fall_velocity = 6

        
        #screen.blit(self.image, (self.x, self.y))

        if self.rect.y >= 480:
            is_alive = False

            
        if pygame.mouse.get_pressed() == (1, 0, 0) and is_alive:
            fall_velocity = -5
            is_pressed = True
        if pygame.mouse.get_pressed()[0] == 0: is_pressed = False

bird_Group = pygame.sprite.Group()
pipe_Group = pygame.sprite.Group()            
        
x = SCREEN_WIDTH / 2 - 15
y = SCREEN_HEIGHT / 2 - 15
bird = Bird(x,y)
bird_Group.add(bird)

last_pipe = clock.get_time()

backgruond1 = 0
backgruond2 = 0
    
while True:
    
    screen.blit(background, (backgruond1,backgruond2))

    draw_text(font, 'score: ' + str(score), SCREEN_WIDTH / 2, 100)

    if is_start:
        bird_Group.draw(screen)
        bird.update()
        pipe_Group.draw(screen)
        pipe_Group.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_start = True


    if len(pipe_Group) > 0:
        if bird_Group.sprites()[0].rect.left > pipe_Group.sprites()[0].rect.left and \
           bird_Group.sprites()[0].rect.right < pipe_Group.sprites()[0].rect.right and \
           pass_pipe == False:
           pass_pipe = True

        if pass_pipe:
            if bird_Group.sprites()[0].rect.left > pipe_Group.sprites()[0].rect.right:
                score += 1
                bird.score_sound.play()
                pass_pipe = False

    if is_alive:
        if not is_start:
            message_x = SCREEN_WIDTH/2 - message.get_width() /2
            message_y = SCREEN_HEIGHT/2 - message.get_height() /2
            screen.blit(message, (message_x, message_y))

        if is_start:

            # create pipe
            now = pygame.time.get_ticks()
            if now - last_pipe > NEW_PIPE:

                x = SCREEN_WIDTH + 20
                y = random.randint(int(SCREEN_HEIGHT*1/4), int(SCREEN_HEIGHT*2/4))
                pipe1 = Pipe(x, y - PIPE_GAP, 'top')
                pipe2 = Pipe(x, y + PIPE_GAP, 'bottom')
                pipe_Group.add(pipe1)
                pipe_Group.add(pipe2)

                last_pipe = pygame.time.get_ticks()

            if pygame.sprite.groupcollide(bird_Group, pipe_Group, False, False):
                is_alive = False


            # scroll background
            ground_scroll -= scroll_speed

            if abs(ground_scroll) > 35:
                ground_scroll = 0

            ground_scroll -= scroll_speed

        
        x_base -= 1
        if x_base < -50:
            x_base = 0
        backgruond1 -= 0.5
        if backgruond1 < -50:
            backgruond1 = 0
    
    screen.blit(base1, (x_base,y_base))

    pygame.display.update()
    clock.tick(90)
