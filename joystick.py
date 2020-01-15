import os
import pygame
from UDPComms import Publisher
import signal

drive_pub = Publisher(8830)

# prevents quiting on pi when run through systemd
def handler(signum, frame):
    print("GOT singal", signum)
signal.signal(signal.SIGHUP, handler)

# those two lines allow for running headless (hopefully)
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.putenv('DISPLAY', ':0.0')

pygame.display.init()
pygame.joystick.init()

# wait until joystick is connected
while 1:
    try:
        pygame.joystick.Joystick(0).init()
        break
    except pygame.error:
        pygame.time.wait(500)

# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print("Name of the joystick:")
print(JoyName)
# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print("Number of axis:")
print(JoyAx)

## Configurable ##
MESSAGE_RATE = 50
while True:
    print("running")

    pygame.event.pump()

    forward_left  = -(pygame.joystick.Joystick(0).get_axis(1))
    forward_right = -(pygame.joystick.Joystick(0).get_axis(5))
    twist_right = (pygame.joystick.Joystick(0).get_axis(2))
    twist_left = (pygame.joystick.Joystick(0).get_axis(0))

    on_right = (pygame.joystick.Joystick(0).get_button(5))
    on_left = (pygame.joystick.Joystick(0).get_button(4))
    l_trigger = (pygame.joystick.Joystick(0).get_axis(3))

    (d_pad_x, d_pad_y) = (pygame.joystick.Joystick(0).get_hat(0))

    msg = { "y" : forward_left,
            "x" : twist_left,
            "twist" : twist_right,
            "pitch" : forward_right,
            "gait_toggle" : on_right,
            "stance_movement" : d_pad_y,
            "roll_movement" : d_pad_x,
            "message_rate" : MESSAGE_RATE
         }
    drive_pub.send(msg)

    dt = int(1000 / MESSAGE_RATE)
    pygame.time.wait(dt)
