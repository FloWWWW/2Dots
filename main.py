#!/usr/bin/env python

import pygame, sys, glob #twisted for networking 
from pygame.locals import *

from dot import *
from constants import *

pygame.init()

#screen canvas
x = 50
y = HEIGHT // 2 - RADIUS
dot1 = Dot(x, y)

clock = pygame.time.Clock() #fps


# Event loop
while True:

	#user key controls
	for event in pygame.event.get():
		#space key  is pressed down
		if event.type == QUIT:
			endProgram = True
			pygame.quit()
			sys.exit()

		#key down, jump
		elif event.type == KEYDOWN and event.key == K_SPACE:
			y -= (SPEED * 10)
			dot1.update(x, y)
		#natural fall
		
	y += SPEED
	dot1.update(x, y)

	#out of bound
	if y >= HEIGHT or y <= 0: #death
		y = HEIGHT//2

	clock.tick(30)