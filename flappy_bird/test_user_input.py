import pygame, sys

from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

box = pygame.Rect(200, 200, 200, 50)
passive_color = pygame.Color('blue')
active_color = pygame.Color('lightblue')
font = pygame.font.Font(None, 32)
text = 'hello world'

active = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if box.collidepoint(event.pos):
                active = True
            else:
                active = False
        
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode


    text_surface = font.render(text, True, (255, 255, 255))
    screen.fill((0, 0, 0))

    if active:
        pygame.draw.rect(screen, active_color, box, True)
    else:
        pygame.draw.rect(screen, passive_color, box, True)

    box.w = max(100, text_surface.get_width() + 20)
    screen.blit(text_surface, (box.x + 10, box.y + 10))

    pygame.display.flip()
    clock.tick(60)