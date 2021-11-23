import pygame, sys

from pygame.constants import QUIT

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

base_font = pygame.font.Font(None, 32)
user_text = 'hi !!!!'

input_rect = pygame.Rect(200, 200, 140, 32)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')

active = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
        
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode




    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, color_active, input_rect, 2)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)