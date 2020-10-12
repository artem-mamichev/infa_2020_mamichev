import pygame
from math import sqrt, pi
from pygame.draw import *
from random import randint

pygame.init()

YELLOW = (255, 255,   0)
WHITE = (255, 255, 255)
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
    creates new element in the balls list
    '''
    global balls, time_to_catch
    Vx = randint(-300,300)
    Vy = randint(-300,300)
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    timer = time_to_catch
    is_clicked = False

    balls.append([x, y, r, Vx, Vy, color, is_clicked, timer])


def redraw_map():
    '''
    Draws map with updated parameters
    '''
    screen.fill(BLACK)
    for ball in balls:
        circle(screen, ball[5], (int(ball[0]), int(ball[1])), ball[2])

        # timer visualization
        end_angle = 2 * pi * ball[7] / time_to_catch
        arc(screen, WHITE, (int(ball[0] - ball[2]), int(ball[1] - ball[2]), ball[2] * 2, ball[2] * 2), 0, end_angle, 5)


def click_check(event):
    '''
    Checks which balls was clicked and updaiting is_clicked parameter for every ball
    '''
    global balls
    for ball in balls:
        distance = sqrt((event.pos[0] - ball[0])**2 + (event.pos[1] - ball[1])**2)    # distance from a center of the ball to a click place
        if distance <= ball[2]:
            ball[6] = True
        else: 
            ball[6] = False
            

def motion():
    '''
    Recalculates positions of the balls on the next frame
    '''
    global balls
    for ball in balls:
        # borders check
        if ball[0] - ball[2] < 0:
            ball[0] = ball[2]
            ball[3] = -ball[3]
        if ball[0] + ball[2] > screen_width:
            ball[0] = screen_width - ball[2] 
            ball[3] = -ball[3]
        if ball[1] - ball[2] < 0:
            ball[1] = ball[2]
            ball[4] = -ball[4]
        if ball[1] + ball[2] > screen_height:
            ball[1] = screen_height - ball[2]
            ball[4] = -ball[4]
        
        # moving
        ball[0] += ball[3] * delta_time
        ball[1] += ball[4] * delta_time


def balls_refresh():
    '''
    removing clicked balls, adding new ones
    '''
    # spawn
    global spawn_timer, spawn_time
    if spawn_timer <= 0:
        new_ball()
        spawn_timer = spawn_time
        
    # removing clicked balls 
    for ball in balls:
        if ball[6]:
            balls.remove(ball)
        

def time_flow():
    '''
    recalculates all timers
    '''
    global spawn_timer, delta_time
    spawn_timer -= delta_time
    for ball in balls:
        ball[7] -= delta_time


def recalculate_score():
    '''
    adds score for clicked balls
    '''
    global score, spawn_time
    for ball in balls:
        if ball[6]:
            score += 1


def check_loose():
    '''
    Checking if the player loose
    '''
    global finished
    for ball in balls:
        if ball[7] < 0:
            loose_animation()


def loose_animation():
    font = pygame.font.Font('freesansbold.ttf', 150)
    textSurface = font.render('YOU LOOSE', True, RED, BLACK)
    textRect = textSurface.get_rect()
    textRect.center = (int(screen_width / 2), int(screen_height * 0.45))

    font2 = pygame.font.Font('freesansbold.ttf', 100)
    textSurface2 = font2.render('Score: ' + str(score), True, GREEN, BLACK)
    textRect2 = textSurface2.get_rect()
    textRect2.center = (int(screen_width / 2), int(screen_height * 0.65))

    screen.fill(BLACK)
    screen.blit(textSurface, textRect)
    screen.blit(textSurface2, textRect2) 

    pygame.display.update()


time_to_catch = 3    # seconds to click on the ball 
spawn_time0 = 1   # time before spawns in the beginning
spawn_time = spawn_time0    # current spawn time
spawn_timer = 0    
delta_time = 1 / FPS    # time between two frames    

balls = []    # balls[i] = [x, y, r, Vx, Vy, color, is_clicked, timer]
              #             0  1  2  3   4     5         6        7

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_check(event)

    recalculate_score()
    balls_refresh()
    motion()
    redraw_map()    
    check_loose()
    time_flow()

    spawn_time = spawn_time0 * (0.8 + 0.3/(score + 1))

    pygame.display.update()
    

pygame.quit()