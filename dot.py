#!/usr/bin/env python
# dot class

import pygame
import sys
import glob  # twisted for networking

from pygame import *
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import random

from constants import *


class Dot(ConnectionListener):  # class dot extend connectionListener

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2Dots')
    screen.fill(BACKGD)

    def __init__(self, x, y):
        # screen
        self.speed = SPEED
        self.x = x
        self.y = y

        pygame.draw.circle(Dot.screen, DOT_1, (self.x, self.y), RADIUS, 0)

        self.gameid = 0
        self.num = 0

        #self.Connect()
        #manually select server
        address = raw_input("Address of Server: ")
        try:
            if not address:
                host, port = "localhost", 8000
            else:
                #split input
                host, port = address.split(":") 
            self.Connect((host, int(port)))
        except:
            print "Error Connecting to Server"
            print "Usage:", "host:port"
            print "e.g.", "localhost:31425"
            exit()
        print "Dots client started"

        #wait until it receives the message to start the game
        # self.running = False
        # while not self.running:
        #     self.Pump()
        #     connection.Pump()
        #     sleep(0.01)

        #determine attributes from player 
        # if self.num == 0:
        #     self.turn=True
        #     self.marker = self.greenplayer
        #     self.othermarker = self.blueplayer
        # else:
        #     self.turn=False
        #     self.marker = self.blueplayer
        #     self.othermarker = self.greenplayer

    def update(self, x, y):

        # look for new events/messages
        connection.Pump()
        self.Pump()

        # clear screen
        self.x = x
        self.y = y

        # self.gameid += 1
        # self.num += 1

        data['x'] = self.x
        data['y'] = self.y
        data['gameid'] = self.gameid
        data['num'] = self.num
        # pygame.display.update(self.dot)
        pygame.draw.circle(Dot.screen, DOT_1, (self.x, self.y), RADIUS, 0)
        print "local update"

        #server communication n send coordinates: data
        self.Send({'action': "place",'x': self.x,'y': self.y, 'gameid': self.gameid, 'num': self.num})

    # get data from server
    def Network_place(self, data):
        # get attributes from server
        try:
            x = int(data['x'])
            y = int(data['y'])
            
            self.gameid = int(data['gameid'])
            self.num = int(data['num'])

            # updates dot accordingly
            Dot.screen.fill(BACKGD)
            pygame.draw.circle(Dot.screen, DOT_2, (x, y), RADIUS, 0)
            print "server update"

        except TypeError:
            print "data x", data['x']


    def Network_startgame(self, data):
        self.running = True
        self.num = data["player"]
        self.gameid = data["gameid"]

    def Network_close(self, data):
        data["gameid"] = 0
        exit()
