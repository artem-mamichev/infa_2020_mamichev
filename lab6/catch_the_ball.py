import pygame
import math
from pygame.draw import *
from random import randint

pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 30
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))


def new_ball():
    '''
    Draws a ball with a random center (x, y), radius r and a random color
    '''
    global x, y, r, Vx, Vy, color
    Vx = randint(-300,300)
    Vy = randint(-300,300)
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def redraw_map():
    screen.fill(BLACK)
    circle(screen, color, (x, y), r)


def ball_is_clicked(event):
    '''
    Returns True if the player clicked on the ball, False else
    '''
    distance = math.sqrt((event.pos[0] - x)**2 + (event.pos[1] - y)**2)    # distance from a center of the ball to a click place
    if distance <= r:
        return True
    else: 
        return False


def borders_check():
    '''
    Changes parameters of aims that hit a border
    '''
    if x - r < 0:
        x = r
        Vx = -Vx
    if x + r > screen_width:
        x = screen_width - r 
        Vx = -Vx
    if y - r < 0:
        y = r
        Vy = -Vy
    if y + r > screen_height:
        y = screen_height - r
        Vy = -Vy


time_to_catch = 3    # player has time_to_catch seconds to click on the ball
timer = time_to_catch
delta_time = 1 / FPS    # time between two frames    


need_aim = True

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ball_is_clicked(event):
                    need_aim = True

    # next aim
    if need_aim:
        screen.fill(BLACK)    
        new_ball()
        need_aim = False
        timer = time_to_catch

    # countdown
    if timer > 0:    
        timer -= delta_time
    else:
        print('you lose')
        screen.fill(BLACK)
        timer = time_to_catch
        need_aim = True

    # motion
    x += Vx * delta_time
    y += Vy * delta_time
    if x - r < 0:
        x = r
        Vx = -Vx
    if x + r > screen_width:
        x = screen_width - r 
        Vx = -Vx
    if y - r < 0:
        y = r
        Vy = -Vy
    if y + r > screen_height:
        y = screen_height - r
        Vy = -Vy

    pygame.display.update()
    redraw_map()
    

pygame.quit()