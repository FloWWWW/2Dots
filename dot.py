#!/usr/bin/env python
# dot class

import pygame
import sys
import glob  # twisted for networking

from pygame import *
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

from constants import *


class Dot(ConnectionListener):  # class dot extend connectionListener

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2Dots')
    screen.fill(BACKGD)

    def __init__(self, x, y):
        # screen
        print ("check pt 5")

        self.speed = SPEED
        self.x = x
        self.y = y
        pygame.draw.circle(Dot.screen, DOT_1, (self.x, self.y), RADIUS, 0)
        self.Connect()

    def update(self, x, y):
        # server pump
        connection.Pump()
        self.Pump()

        # clear screen
        Dot.screen.fill(BACKGD)

        self.x = x
        self.y = y

        # pygame.display.update(self.dot)
        pygame.draw.circle(Dot.screen, DOT_1, (self.x, self.y), RADIUS, 0)

        screen = pygame.display.flip()
