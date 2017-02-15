import pygame
import time
#I know there will be other imports for data transmission, but those will be added when this is merged with roy's code

pygame.init()
stick = pygame.joysick.Joystick(0)
stick.init()
try:
  while true:
    pygame.event.pump()
    fb = stick.get_axis(1)
    lr = stick.get_axis(0)
    motorL = int((-fb+lr)*250)
    motorR = int((-fb-lr)*250)
    motorV = stick.get_axis(4)*-250
    print ({motorL, motorR, motorV})
    time.sleep(0.1)
except KeyboardInterrupt:
  stick.quit()
  pygame.quit()
