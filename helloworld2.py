#! /usr/bin/env python
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Hello World')
running = True

count = 0
while running:
    
    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    pygame.display.update()
    
    count += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            print(count)
            pygame.quit()
            pygame.display.quit()
            running = False
