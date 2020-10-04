import pygame
from pygame.draw import *
import random
import math

pygame.init()

size = width, height = (700, 800)
FPS = 30
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
FOREST_GREEN = (19, 64, 52)
LIGHT_BLUE = (33, 225, 225)
GREY = (224, 224, 224)
DARK_GREY = (60, 60, 60)
PURPLE = (101, 95, 238)
LIGHT_RED = (212, 148, 149)
YELLOW = (255, 245, 203)
MIDDLE_GREY = (178, 191, 188)
WHITE = (255, 255, 255)


def my_ellipse(screen, color, x, y, width, height):
    '''
    draws an ellipse with a black border
    '''
    ellipse(screen, color, (x, y, width, height))
    ellipse(screen, BLACK, (x - 1, y - 1, width + 2, height + 2), 1)


# SKY
screen.fill(LIGHT_BLUE)


# LAND
rect(screen, GREY, (0, 0.55 * height, width, 0.45 * height))
line(screen, BLACK, (0, 0.55 * height), (700, 0.55 * height))


# SUN
sun_surface_width = 0.61 * width
sun_surface_height = 0.39 * height
sun_surface = pygame.Surface((sun_surface_width, sun_surface_height))

rect(sun_surface, YELLOW, (0.02 * sun_surface_width, 0.15 * height, 0.55 * width, 0.04 * height))    # horizontal ray
rect(sun_surface, YELLOW, (0.27 * width, 0, 0.04 * height, 0.45 * width))    # vertical ray

ellipse(screen, YELLOW, (0.57 * width, 0.155 * height, 0.07 * width, 0.05 * height))    # center
ellipse(screen, YELLOW, (0.31 * width, 0.156 * height, 0.04 * width, 0.03 * height))    # left
ellipse(screen, YELLOW, (0.87 * width, 0.174 * height, 0.04 * width, 0.03 * height))    # right
ellipse(screen, YELLOW, (0.585 * width, 0.01 * height, 0.04 * width, 0.03 * height))    # top
ellipse(screen, YELLOW, (0.575 * width, 0.37 * height, 0.04 * width, 0.03 * height))   # down

ellipse(sun_surface, YELLOW, (0, 0, 0.61 * width, 0.45 * width), 65)    # big 

sun_surface.set_alpha(100)
sun_surface = pygame.transform.rotate(sun_surface, -2)
screen.blit(sun_surface, (0.30 * width, 0))


# HOLE
my_ellipse(screen, DARK_GREY, 0.55 * width, 0.7 * height, 0.35 * width, 0.12 * height)
my_ellipse(screen, FOREST_GREEN, 0.575 * width, 0.74 * height, 0.3 * width, 0.08 * height)


# FISHING ROD
for i in range(5):    #using cycle to increase stick's width
    aalines(screen, BLACK, False, [(0.3 * width + i, 0.62 * height), 
                                   (0.35 * width + i, 0.53 * height), 
                                   (0.5 * width + i, 0.40 * height),
                                   (0.7 * width + i, 0.25 * height)], 5)
aalines(screen, BLACK, False, [(0.7 * width, 0.25 * height), 
                               (0.72 * width, 0.78 * height)])      


# POLAR BEAR
my_ellipse(screen, GREY, 0.15 * width, 0.335 * height, 0.19 * width, 0.09 * height)    # head
my_ellipse(screen, GREY, 0.01 * width, 0.4 * height, 0.28 * width, 0.45 * height)    # body
my_ellipse(screen, GREY, 0.24 * width, 0.53 * height, 0.13 * width, 0.05 * height)    # hand
my_ellipse(screen, GREY, 0.16 * width, 0.72 * height, 0.22 * width, 0.13 * height)    # leg
my_ellipse(screen, GREY, 0.29 * width, 0.82 * height, 0.14 * width, 0.045 * height)    # foot
ellipse(screen, BLACK, (0.226 * width, 0.362 * height, 0.016 * width, 0.011 * height))    # eye
circle(screen, BLACK, (0.34 * width, 0.37 * height), 4)    # nose

# smile
aalines(screen, BLACK, False, [(0.226 * width, 0.399 * height), 
                               (0.255 * width, 0.4 * height),
                               (0.31 * width, 0.398 * height), 
                               (0.335 * width, 0.394* height)])     

# ear                              
arc(screen, BLACK, (0.17 * width, 0.335 * height,  0.027 * width, 0.024 * height), math.pi / 6, 3/2 * math.pi) 
ellipse(screen, GREY, (0.17 * width, 0.335 * height,  0.027 * width, 0.024 * height)) 


# FISH
# tale (start drawing from th intersection point counterclock-wise)
polygon(screen, MIDDLE_GREY, [(0.7 * width, 0.9 * height), 
                              (0.65 * width, 0.95 * height),
                              (0.63 * width, 0.92 * height),
                              (0.67 * width, 0.915 * height)])
aalines(screen, BLACK, True, [(0.7 * width, 0.9 * height), 
                              (0.65 * width, 0.95 * height),
                              (0.63 * width, 0.92 * height),
                              (0.67 * width, 0.915 * height)])    

# body (start drawing from th intersection point clock-wise)
polygon(screen, MIDDLE_GREY, [(0.7 * width, 0.9 * height), 
                              (0.74 * width, 0.858 * height),
                              (0.82 * width, 0.835 * height),
                              (0.87 * width, 0.84 * height),
                              (0.85 * width, 0.875 * height),
                              (0.8 * width, 0.901 * height)])
aalines(screen, BLACK, True, [(0.7 * width, 0.9 * height), 
                              (0.74 * width, 0.858 * height),
                              (0.82 * width, 0.835 * height),
                              (0.87 * width, 0.84 * height),
                              (0.85 * width, 0.875 * height),
                              (0.8 * width, 0.901 * height)])   

# eye 
circle(screen, PURPLE, (0.835 * width, 0.855 * height), 8) 
line(screen, WHITE, (0.83 * width, 0.85 * height), (0.835 * width, 0.855 * height), 2)  

# top fin
polygon(screen, LIGHT_RED, [(0.74 * width, 0.858 * height),
                            (0.725 * width, 0.844 * height),
                            (0.68 * width, 0.83 * height),
                            (0.8 * width, 0.82 * height),
                            (0.82 * width, 0.835 * height)])
aalines(screen, BLACK, True, [(0.74 * width, 0.858 * height),
                              (0.725 * width, 0.844 * height),
                              (0.68 * width, 0.83 * height),
                              (0.8 * width, 0.82 * height),
                              (0.82 * width, 0.835 * height)])

# down left fin
polygon(screen, LIGHT_RED, [(0.74 * width, 0.9 * height),
                            (0.725 * width, 0.93 * height),
                            (0.765 * width, 0.928 * height),
                            (0.764 * width, 0.9 * height)])
aalines(screen, BLACK, True, [(0.74 * width, 0.9 * height),
                            (0.725 * width, 0.93 * height),
                            (0.765 * width, 0.928 * height),
                            (0.764 * width, 0.9 * height)])  

# down right fin
polygon(screen, LIGHT_RED, [(0.814 * width, 0.892 * height),
                            (0.83 * width, 0.92 * height),
                            (0.87 * width, 0.9 * height),
                            (0.84 * width, 0.891 * height),
                            (0.83 * width, 0.884 * height)])                                   
aalines(screen, BLACK, True, [(0.814 * width, 0.892 * height),
                              (0.83 * width, 0.92 * height),
                              (0.87 * width, 0.9 * height),
                              (0.84 * width, 0.891 * height),
                              (0.83 * width, 0.884 * height)])                            





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()