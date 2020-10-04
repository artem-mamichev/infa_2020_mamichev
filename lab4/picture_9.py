import pygame
from pygame.draw import *
import random

pygame.init()

size = width, height = (700, 800)
FPS = 30
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
GREEN = (19, 64, 52)
LIGHT_BLUE = (33, 225, 225)
GREY = (224, 224, 224)
PURPLE = (101, 95, 238)
LIGHT_RED = (212, 148, 149)
YELLOW = (255, 245, 203)


# sky
screen.fill(LIGHT_BLUE)


# land
rect(screen, GREY, (0, 0.55 * height, width, 0.45 * height))
line(screen, BLACK, (0, 0.55 * height), (700, 0.55 * height))


# sun
sun_surface_width = 0.61 * width
sun_surface_height = 0.39 * height
sun_surface = pygame.Surface((sun_surface_width, sun_surface_height))

rect(sun_surface, YELLOW, (0.02 * sun_surface_width, 0.15 * height, 0.55 * width, 0.04 * height))    # horizontal ray
rect(sun_surface, YELLOW, (0.27 * width, 0, 0.04 * height, 0.45 * width))    # vertical ray

ellipse(screen, YELLOW, (0.575 * width, 0.155 * height, 0.06 * width, 0.05 * height))    # center
ellipse(screen, YELLOW, (0.31 * width, 0.156 * height, 0.04 * width, 0.03 * height))    # left
ellipse(screen, YELLOW, (0.87 * width, 0.174 * height, 0.04 * width, 0.03 * height))    # right
ellipse(screen, YELLOW, (0.585 * width, 0.01 * height, 0.04 * width, 0.03 * height))    # top
ellipse(screen, YELLOW, (0.575 * width, 0.37 * height, 0.04 * width, 0.03 * height))   # down

ellipse(sun_surface, YELLOW, (0, 0, 0.61 * width, 0.45 * width), 65)    # big 

sun_surface.set_alpha(100)
sun_surface = pygame.transform.rotate(sun_surface, -2)
screen.blit(sun_surface, (0.30 * width, 0))


# stick
for i in range(5):    #using cycle to increase stick's width
    aalines(screen, BLACK, False, [(0.3 * width + i, 0.62 * height), 
                                   (0.35 * width + i, 0.53 * height), 
                                   (0.5 * width + i, 0.40 * height),
                                   (0.7 * width + i, 0.25 * height)], 5)
                            





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()