#!/usr/bin/env python
#dot class

import pygame, sys, tkinter, glob #twisted for networking 
from pygame.locals import *
from tkinter import *
from constants import *

screen = pygame.display.set_mode((WIDTH, LENGTH))

class Dot: 
	def __init__(self, x, y):
		print ("check pt 4")
		pygame.display.set_caption('2Dots')
		screen.fill(BACKGD)

		print ("check pt 5")

		self.speed = SPEED

		self.x = x
		self.y = y

		self.dot1 = pygame.draw.circle(screen, DOT_1, (self.x, self.y), 20, 0)
		self.dot2 = pygame.draw.circle(screen, DOT_2, (self.x, self.y + 100), 20, 0)
		self.animation(False)
	 	#image animation update

	def animation(self, jump):
		if jump == False:
			#vertical fall
			self.x += SPEED
			self.y += SPEED
			#pygame.draw.circle(screen, DOT_1, (self.x, self.y), 20, 0)
		elif jump == True:
			self.x += SPEED
			self.y -= (SPEED * 2)

		self.dot1.move(self.x, self.y)