import pygame
import time
import sys
from __future__ import print_function

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
#hat_number = j.get_numhats() - 1
print 'Initialized Joystick : %s' % j.get_name()
#print (hat_number)


while True:
	try:
		pygame.event.wait()
		myEvents = pygame.event.get()
		for x in range(0, j.get_numbuttons()-1):
			print(str(j.get_button(x)) + ",", end="", flush=True)
			print ("")
	except KeyboardInterrupt:
		j.quit()
