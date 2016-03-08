#!/usr/bin/env python

import pygame, sys, glob #twisted for networking 
from pygame.locals import *

pygame.init()

infoObject = pygame.display.Info()

WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h

#dot
RADIUS = 20
SPEED = 10

#color: http://www.colorcombos.com/color-schemes/125/ColorCombo125.html
BACKGD = (217, 226, 225)
DOT_1 = (223, 148, 150)
DOT_2 = (114, 123, 132)