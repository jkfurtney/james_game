import sys
import pygame
from math import sqrt

pygame.init()
clock = pygame.time.Clock()
size = width, height = 640, 480
speed_magnitude = 20
speed = [speed_magnitude, speed_magnitude]
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
        sx = mx - bx
        sy = my - by
        magnitude = sqrt(sx**2 + sy**2)
        sx = speed_magnitude * sx / magnitude
        sy = speed_magnitude * sy / magnitude
        speed = [sx, sy]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(30)
