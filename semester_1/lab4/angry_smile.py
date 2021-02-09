import pygame
from pygame.draw import *
import random

pygame.init()

size = width, height = (700, 700)
FPS = 30
screen = pygame.display.set_mode(size)
left_brow = pygame.Surface((180, 20))
right_brow = pygame.Surface((150, 20))

YELLOW = pygame.Color('yellow')
BLACK = pygame.Color('black')
RED = pygame.Color('red')
GREY = pygame.Color('grey')


screen.fill(GREY)
#head
circle(screen, BLACK, (350, 350), 201, 1)
circle(screen, YELLOW, (350, 350), 200, 0)
#left eye
circle(screen, BLACK, (250, 300), 41, 1)
circle(screen, RED, (250, 300), 40, 0)
circle(screen, BLACK, (250, 300), 18, 0)
#right eye
circle(screen, BLACK, (450, 300), 31, 1)
circle(screen, RED, (450, 300), 30, 0)
circle(screen, BLACK, (450, 300), 14, 0)
#mouth
rect(screen, BLACK, (250, 450, 200, 35), 0)
#eyebrows
left_brow.fill(BLACK)
left_brow = pygame.transform.rotate(left_brow, -30)
screen.blit(left_brow, (160, 185))
right_brow.fill(BLACK)
right_brow = pygame.transform.rotate(right_brow, 20)
screen.blit(right_brow, (390, 217))
    


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()