import pygame
from pygame.locals import *

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 956
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

klingons = {"speed": {"x":0, "y":8},
            "ship": pygame.image.load('glider-75px.png').convert_alpha(),
            "position": {"x":230,"y":SCREEN_HEIGHT}}

mouser = {"speed": {"x":0, "y":12},
            "ship": pygame.image.load('mouser-75px.png').convert_alpha(),
            "position": {"x":630,"y":SCREEN_HEIGHT}}

julio = {"speed": {"x":0, "y":10},
            "ship": pygame.image.load('ship.png').convert_alpha(),
            "position": {"x":430,"y":SCREEN_HEIGHT}}

ships = [klingons, mouser, julio]

pygame.display.set_caption('Multiplayer!')
running = True

def move(thing):
    thing['position']['x'] += thing['speed']["x"]
    thing['position']['y'] -= thing['speed']["y"]
    if thing['position']['y'] < -20:
        thing['position']['y'] = SCREEN_HEIGHT
    if thing['position']['y'] > SCREEN_HEIGHT:
        thing['position']['y'] = 0
    if thing['position']['x'] < -50:
        thing['position']['x'] = SCREEN_WIDTH
    if thing['position']['x'] > SCREEN_WIDTH:
        thing['position']['x'] = 0

        
def show(thing):
    screen.blit(thing["ship"], (thing["position"]["x"],thing["position"]["y"]))

def quit():
    pygame.quit()
    pygame.display.quit()
    running = False

def get_rect(ship):
    return Rect(ship['position']["x"],
                ship['position']["y"],
                75,
                75)

def is_collided():
    ship_rect = get_rect(julio)
    if ship_rect.colliderect(get_rect(klingons)):
            return True
    return False


y = SCREEN_HEIGHT

clock = pygame.time.Clock()
while running:
    
    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    screen.blit(background, (0, 0))
    for s in ships:
        show(s)
    pygame.display.update()
    
    pressed_keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    if pressed_keys[K_LEFT]:
        julio['speed']['x'] = -5
    elif pressed_keys[K_RIGHT]:
        julio['speed']['x'] = 5
    elif pressed_keys[K_UP]:
        julio['speed']['y'] += 1 
    elif pressed_keys[K_DOWN]:
        julio['speed']['y'] -= 1
    elif pressed_keys[pygame.K_a]:
        klingons['speed']['x'] = -5
    elif pressed_keys[pygame.K_d]:
        klingons['speed']['x'] = 5
    elif pressed_keys[pygame.K_w]:
        klingons['speed']['y'] += 1 
    elif pressed_keys[pygame.K_s]:
        klingons['speed']['y'] -= 1
    
    elif pressed_keys[K_ESCAPE]:
        quit()
    
    clock.tick(30)
    for s in ships:
        move(s)
        
    if is_collided():
        quit()
