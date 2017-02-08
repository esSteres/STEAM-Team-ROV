import pygame
#I know there will be other imports for data transmission, but those will be added when this is merged with roy's code

pygame.init()
stick = pygame.joystick.Joystick(0)
stick.init()
try:
  while True:
    event = pygame.event.wait()
	if (event.type == JOYBUTTONDOWN):
		for i in (0, stick.get_numbuttons()):
			print ("buttion " + `i` + ": " `stick.get_button(i)`)
except KeyboardInterrupt:
  stick.quit()
  pygame.quit()
