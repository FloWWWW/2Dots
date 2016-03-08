#!/usr/bin/env python
#dot class

import pygame, sys, glob #twisted for networking 
from pygame.locals import *

from constants import *

class Dot: 

	pygame.init()

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('2Dots')
	screen.fill(BACKGD)

	def __init__(self, x, y):
		#screen

		print ("check pt 5")

		self.speed = SPEED

		self.x = x
		self.y = y

		pygame.draw.circle(Dot.screen, DOT_1, (self.x, self.y), RADIUS, 0)
	 	#image animation update

	def update(self, x, y):
		
		#clear screen
		Dot.screen.fill(BACKGD)		

		self.x = x
		self.y = y

		#pygame.display.update(self.dot)
		pygame.draw.circle(Dot.screen, DOT_1, (self.x, self.y), RADIUS, 0)

		screen = pygame.display.flip()