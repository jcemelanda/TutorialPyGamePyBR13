#! /usr/bin/env python
from random import randrange
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((956, 560), 0, 32)
background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()
pygame.display.set_caption('Hello World')
ship_filename = 'ship.png'
ship = pygame.image.load(ship_filename).convert_alpha()
position = [0, 0]
running = True
clock = pygame.time.Clock()
asteroids = []
ticks_to_asteroid = 90
speed = {'x': 0, 'y': 0}

def create_asteroid():
    return {
        'surface': pygame.image.load('asteroid.png').convert_alpha(),
        'position': [randrange(892), -64],
        'speed': randrange(1, 11)
    }

def move_asteroids():
    for asteroid in asteroids:
        asteroid['position'][1] += asteroid['speed']

def remove_used_asteroids():
    for asteroid in asteroids:
        if asteroid['position'][1] > 560:
            asteroids.remove(asteroid)
ticks = 0

while running:
    if ticks < ticks_to_asteroid:
        ticks += 1
    else:
        ticks = 0
        asteroids.append(create_asteroid())
    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    screen.blit(background, (0, 0))
    position[0] += speed['x']
    position[1] += speed['y']
    screen.blit(ship, position)
    remove_used_asteroids()
    move_asteroids()
    for asteroid in asteroids:
        screen.blit(asteroid['surface'], asteroid['position'])
    pygame.display.update()
    
    speed = {'x': 0, 'y': 0}
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        speed['y'] = -5
    elif pressed_keys[K_DOWN]:
        speed['y'] = 5
    if pressed_keys[K_LEFT]:
        speed['x'] = -5
    elif pressed_keys[K_RIGHT]:
        speed['x'] = 5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            pygame.display.quit()
            running = False
    clock.tick(30)
