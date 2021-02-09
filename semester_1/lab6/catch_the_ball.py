import pygame
from math import sqrt, pi
from pygame.draw import *
from random import randint

pygame.init()

YELLOW = (255, 255, 0)
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


class Brick:
    global time_factor    # how to make global var among the separate class?
    time_factor = 1.5
    def __init__(self):
        '''
        x, y - rectangle centre coordinates  
        width - length of horizontal side
        height - length of vertical side
        timer - time left to click this brick, otherwise player looses
        '''
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.width = randint(40, 100)
        self.height = randint(40, 100)
        self.Vx = randint(-400, 400)
        self.Vy = randint(-400, 400)
        self.color = COLORS[randint(0, 5)]
        self.is_clicked = False
        self.timer = time_factor * time_to_catch


    def draw(self):
        rect(screen, self.color, (int(self.x - self.width/2), int(self.y - self.height/2), self.width, self.height))

        # timer visualization (white strip)
        time_passed = time_factor * time_to_catch - self.timer
        strip_length = 2 * (self.height + self.width) * time_passed / (time_factor * time_to_catch)
        for sign in [1, -1]:
            if strip_length > 0:
                if strip_length // self.height == 0:
                    line(screen, WHITE, (self.x + self.width/2 * sign, self.y - self.height/2 * sign),
                                        (self.x + self.width/2 * sign, self.y - self.height/2 * sign + strip_length * sign), 5)
                    strip_length = 0
                else: 
                    line(screen, WHITE, (self.x + self.width/2 * sign, self.y - self.height/2 * sign),
                                        (self.x + self.width/2 * sign, self.y + self.height/2 * sign), 5)
                    strip_length -= self.height
            if strip_length > 0:
                if strip_length // self.width == 0:
                    line(screen, WHITE, (self.x + self.width/2 * sign, self.y + self.height/2 * sign),
                                        (self.x + self.width/2 * sign - strip_length * sign, self.y + self.height/2 * sign), 5)
                    strip_length = 0
                else:
                    line(screen, WHITE, (self.x + self.width/2 * sign, self.y + self.height/2 * sign),
                                        (self.x - self.width/2 * sign, self.y + self.height/2 * sign), 5)
                    strip_length -= self.width


    def clicked_check(self, event):
        if (abs(event.pos[0] - self.x) <= self.width/2) and (abs(event.pos[1] - self.y) <= self.height/2):
            self.is_clicked = True
        else: 
            self.is_clicked = False
    

    def moove(self):
        x = self.x
        y = self.y
        Vx = self.Vx
        Vy = self.Vy
        # borders check
        if (x < 0) or (x > screen_width) or (y < 0) or (y > screen_height):
            x = randint(100, 700)
            y = randint(100, 500)

        V = sqrt(Vx**2 + Vy**2)
        Vx = randint(int(-abs(V)), int(abs(V)))
        Vy = sqrt(V**2 - Vx**2)
        x += Vx * delta_time
        y += Vy * delta_time

        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy



class Ball:
    def __init__(self):
        '''
        x, y - ball centre coordinates 
        r - ball radius
        timer - time left to click this ball, otherwise player looses
        '''
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.Vx = randint(-300, 300)
        self.Vy = randint(-300, 300)
        self.color = COLORS[randint(0, 5)]
        self.is_clicked = False
        self.timer = time_to_catch


    def draw(self):
        circle(screen, self.color, (int(self.x), int(self.y)), self.r)

        # timer visualization (white strip)
        end_angle = 2 * pi * self.timer / (time_factor * time_to_catch)
        arc(screen, WHITE, (int(self.x - self.r - 3), int(self.y - self.r - 3), self.r * 2 + 6, self.r * 2 + 6), 0, end_angle, 5)
    

    def clicked_check(self, event):
        distance = sqrt((event.pos[0] - self.x)**2 + (event.pos[1] - self.y)**2)    # distance from a center of the ball to a click place
        if distance <= self.r:
            self.is_clicked = True
        else: 
            self.is_clicked = False


    def moove(self):
        # borders check
        if self.x - self.r < 0:
            self.x = self.r
            self.Vx = -self.Vx
        if self.x + self.r > screen_width:
            self.x = screen_width - self.r 
            self.Vx = -self.Vx
        if self.y - self.r < 0:
            self.y = self.r
            self.Vy = -self.Vy
        if self.y + self.r > screen_height:
            self.y = screen_height - self.r
            self.Vy = -self.Vy
        
        self.x += self.Vx * delta_time
        self.y += self.Vy * delta_time



def new_aim():
    '''
    creates new element in the aims list
    '''
    global aims, spawns_number
    if (spawns_number + 1) % 5 == 0:
        aim = Brick()
    else:
        aim = Ball()
    aims.append(aim)
    spawns_number += 1


def redraw_map():
    '''
    Draws map with updated parameters
    '''
    screen.fill(BLACK)
    for aim in aims:
        aim.draw()
    
    font = pygame.font.Font('freesansbold.ttf', 30)
    textSurface = font.render(str(score), True, WHITE, BLACK)
    textRect = textSurface.get_rect()
    textRect.center = (25,30)
    screen.blit(textSurface, textRect)


def click_check(event):
    '''
    Checks which aims was clicked and updaiting is_clicked parameter for every aim
    '''
    for aim in aims:
        aim.clicked_check(event)
            

def motion():
    '''
    Recalculates positions of the aims on the next frame
    '''
    for aim in aims:
        aim.moove()


def aims_refresh():
    '''
    removing clicked aims, adding new ones
    '''
    # spawn
    global spawn_timer
    if spawn_timer <= 0:
        new_aim()
        spawn_timer = spawn_time
        
    # removing clicked aims 
    for aim in aims:
        if aim.is_clicked:
            aims.remove(aim)
        

def time_flow():
    '''
    recalculates all timers
    '''
    global spawn_timer
    spawn_timer -= delta_time
    for aim in aims:
        aim.timer -= delta_time


def recalculate_score():
    '''
    adds score for clicked aims
    '''
    global score
    for aim in aims:
        if aim.is_clicked:
            if isinstance(aim, Ball):
                score += 1
            if isinstance(aim, Brick):
                score += 2


def check_loose():
    '''
    Checking if the player loose
    '''
    global loosed, aims
    for aim in aims:
        if aim.timer < 0:
            loose_window()
            loosed = True
            aims = []


def loose_window():
    '''
    Draws "you loose" screen after you lost
    '''
    global textRect3
    font = pygame.font.Font('freesansbold.ttf', 150)
    textSurface = font.render('YOU LOOSE', True, RED, BLACK)
    textRect = textSurface.get_rect()
    textRect.center = (int(screen_width / 2), int(screen_height * 0.4))

    font2 = pygame.font.Font('freesansbold.ttf', 100)
    textSurface2 = font2.render('Score: ' + str(score), True, GREEN, BLACK)
    textRect2 = textSurface2.get_rect()
    textRect2.center = (int(screen_width / 2), int(screen_height * 0.6))

    font3 = pygame.font.Font('freesansbold.ttf', 60)
    textSurface3 = font3.render('TRY AGAIN', True, YELLOW, BLACK)
    textRect3 = textSurface3.get_rect()
    textRect3.center = (int(screen_width / 2), int(screen_height * 0.75))

    screen.fill(BLACK)
    screen.blit(textSurface2, textRect2) 
    screen.blit(textSurface3, textRect3) 
    screen.blit(textSurface, textRect)

    pygame.display.update()


def try_again(event):
    '''
    Restarts if "try again" button pressed
    '''
    if (textRect3.left < event.pos[0] < textRect3.right) and (textRect3.top < event.pos[1] < textRect3.top + textRect3.height): 
        return True
    else:
        return False


def main():   
    global loosed, spawn_time, spawn_timer, delta_time, time_to_catch, score, aims, spawns_number
    time_to_catch = 3    # seconds player has to click the aim 
    spawn_time0 = 1.2   # time before spawns in the beginning
    spawn_time = spawn_time0    # current spawn time
    spawn_timer = 0    
    spawns_number = 0    # number of spawned aims
    delta_time = 1 / FPS    # time between two frames in seconds  
    aims = []  
    clock = pygame.time.Clock()
    loosed = False
    score = 0
    while not loosed:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_check(event)

        recalculate_score()
        aims_refresh()
        motion()
        redraw_map()    
        check_loose()
        time_flow()

        spawn_time = spawn_time0 * (0.4 + 0.6/(score * 0.05 + 1))

        pygame.display.update()

    while loosed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if try_again(event):
                        loosed = False
                        score = 0
                        main()





main()


                    
    
pygame.quit()