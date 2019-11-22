import sys
import pygame
from math import sqrt

pygame.init()
clock = pygame.time.Clock()
size = width, height = 640, 480

diagional = sqrt(width**2 + height**2)
max_speed = 10
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

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

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
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(fps)