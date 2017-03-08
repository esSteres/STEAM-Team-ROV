import pygame
import time
#I know there will be other imports for data transmission, but those will be added when this is merged with roy's code

pygame.init()
pygame.event.setAllowed(pygame.JOYBUTTONDOWN)
stick = pygame.joysick.Joystick(0)
stick.init()
lights = False
try:
  while true:
    events = pygame.event.get()
    for event in events:
      if event.button == 3:
        lights = not lights
    fb = stick.get_axis(1)
    lr = stick.get_axis(0)
    motorL = int((-fb+lr)*250)
    motorR = int((-fb-lr)*250)
    motorV = int(stick.get_axis(4)*-250)
    print ({motorL, motorR, motorV, lights})
    time.sleep(0.09)
except KeyboardInterrupt:
  stick.quit()
  pygame.quit()
