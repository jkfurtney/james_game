import sys
import pygame
from math import sqrt

pygame.init()
clock = pygame.time.Clock()
size = width, height = 640, 480
size = width, height = 1920, 1080 #640, 480

diagional = sqrt(width**2 + height**2)
max_speed = 20 # int(10 * width/640)
mass = 1
acceleration_time = 1 # second
acceleration_distance = diagional/2.
max_acceleration = acceleration_distance/2/acceleration_time**2
kn = max_acceleration/diagional
kd = kn*diagional/max_speed
fps = 30
tic = 1/fps

speed = [0,0]
black = 0, 0, 0
white = (255, 255, 255)
red = (255, 50, 50)
green = (50, 255, 50)

screen = pygame.display.set_mode(size)

class ring_buffer(list):
    def __init__(self,N):
        self.N = N
    def push(self, value):
        self.insert(0, value)
        if len(self) > self.N:
            self.pop()

tail = ring_buffer(100)

ball_diameter = 10
ballrect = pygame.Rect(0, 0, ball_diameter, ball_diameter)
tail.push(ballrect.center)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        bx, by = ballrect.center
        sx, sy = speed
        fx = kn * (mx - bx) - kd * sx / max_speed
        fy = kn * (my - by) - kd * sy / max_speed
        d_sx = fx * mass * tic
        d_sy = fy * mass * tic
        sx = sx + d_sx
        sy = sy + d_sy
        magnitude = sqrt(sx**2 + sy**2)

        # sx =  sx / magnitude
        # sy =  sy / magnitude
        speed = [sx, sy]
        # if ballrect.left < 0:
        #     speed[0] = 1
        # elif ballrect.right > width:
        #     speed[0] = -1
        # if ballrect.top < 0:
        #     speed[1] = -1
        #     or ballrect.bottom > height:
        #     speed = [0,0]
        #     #speed[1] = -0.8 * speed[1]

        ballrect = ballrect.move(speed)
        tail.push(ballrect.center)



    screen.fill(black)
    #screen.blit(ball, ballrect)
    pygame.draw.circle(screen, red, ballrect.center, int(ball_diameter/2.0))
    for i in range(len(tail)-1):
        pygame.draw.line(screen, red, tail[i], tail[i+1], 1)
    pygame.display.flip()
    clock.tick(fps)
