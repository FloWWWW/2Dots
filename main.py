#!/usr/bin/env python

import pygame, sys, tkinter, glob #twisted for networking 
from pygame.locals import *
from tkinter import *

from dot import *
from constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, LENGTH))

def main():

	#screen canvas

	clock = pygame.time.Clock()

	dot1 = Dot(300, 200)
	jump = False
	print ("check pt 0")

	# Event loop
	while True:

		clock.tick(60) #60 frames each cycle

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#event as uswer input
			#right key  is pressed down
			elif event.type == KEYDOWN and event.key == K_SPACE:
				jump = True
				print ("check pt 1")

			#right key is lifted
			elif event.type == KEYUP and event.key == K_SPACE:
				jump = False 
				print ("check pt 2")


		dot1.animation(jump)
		pygame.display.update()		

if __name__ == '__main__': main()




