#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)
background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

ship_filename = 'ship.png'
ship = pygame.image.load(ship_filename).convert_alpha()

pygame.display.set_caption('Hello World')

ship_position = [0, 0]
speed = (3, 2)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    screen.blit(background, (0, 0))
    ship_position[0] += speed[0]
    ship_position[1] += speed[1]
    screen.blit(ship, ship_position)
    pygame.display.update() 
    time_passed = clock.tick(30)
