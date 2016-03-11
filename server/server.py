#!/usr/bin/env python

# server init checkup
# run a PodSixNet custom server on a specific port 
# then run the client to communicate with the server through that port.

import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

from constants import *

#connection that listens for connections on a default port
class ClinetChannel (PodSixNet.Channel.Channel): 

	channelClass = ClinetChannel

	def Connected(self, channel, addr):
		print ("new connection:", channel) #prints init message when someone is connected

print ("STARTING SERVER ON LOCALHOST")

boxesServe = boxesServer()
while True:
	boxesServe.Pump()
	sleep(0.01)