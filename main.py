#!/usr/bin/env python
#RUN THIS WITH python2.7-32 BECAUSE PYGAME ONLY WORKS FOR 32 BITS

import pygame, sys, glob 
from pygame import *

from dot import Dot
from constants import *

pygame.init()

#screen canvas
infoObject = pygame.display.Info()

WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h

x = 50
y = HEIGHT // 2 - RADIUS


print "RUNNING PYGAME"
dot1 = Dot(x, y)
print "DOT CLASS INITALIZED"
dot1.Network_startgame(data)

clock = pygame.time.Clock() #fps

# Event loop
while True:

	# if data['gameid'] == 0:
	#user key controls
	for event in pygame.event.get():
		#space key  is pressed down
		if event.type == QUIT:
			endProgram = True

			dot1.Network_close(data)
			pygame.quit()
			sys.exit()
			print "QUIT"

		#key down, jump
		elif event.type == KEYDOWN and event.key == K_SPACE:
			y -= (SPEED * 10)
			Dot.screen.fill(BACKGD)
			dot1.update(x, y)
	# else:
	# 	x = data['x']
	# 	y = data['y']
	# 	dot1.update(x, y)
		
	# fall	
	y += SPEED
	Dot.screen.fill(BACKGD)
	dot1.update(x, y)
	dot1.Network_place(data)


	#out of bound
	if y >= HEIGHT or y <= 0: #death
		y = HEIGHT//2

	clock.tick(3)