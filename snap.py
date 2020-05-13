# h

import pygame
from pygame.locals import *


BLACK = (0,0,0)
WHITE = (255,255,255)
snap = 20

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (mouse_x // snap * snap, mouse_y // snap * snap, snap, snap)) ###
    pygame.display.flip()
    clock.tick()
