from UDPComms import Publisher
from PS4Joystick import Joystick

import time

## you need to git clone the PS4Joystick repo and run `sudo bash install.sh`

## Configurable ##
MESSAGE_RATE = 20
PUPPER_COLOR = {"red":255, "blue":255, "green":0}

drive_pub = Publisher(8830)
j = Joystick()

while True:
    print("running")
    values = j.get_input()
    j.led_color(**PUPPER_COLOR)

    forward_left  = - values['left_analog_y']
    forward_right = - values['right_analog_y']
    twist_right   =   values['right_analog_x']
    twist_left    =   values['left_analog_x']

    L2 = values['l2_analog']
    R2 = values['r2_analog']

    on_right = values['button_r1']
    on_left  = values['button_l1']

    square   = values['button_square']
    x        = values['button_cross']
    circle   = values['button_circle'] 
    triangle = values['button_triangle']

    d_pad_x = values['dpad_right'] - values['dpad_left']
    d_pad_y = values['dpad_up']    - values['dpad_down']

    msg = { "ly" : forward_left,
            "lx" : twist_left,
            "rx" : twist_right,
            "ry" : forward_right,
            "L2" : L2,
            "R2" : R2,
            "R1" : on_right,
            "L1" : on_left,
            "dpady" : d_pad_y,
            "dpadx" : d_pad_x,
            "x": x,
            "square": square,
            "circle": circle,
            "triangle": triangle,
            "message_rate" : MESSAGE_RATE
         }
    drive_pub.send(msg)
    time.sleep(1/MESSAGE_RATE)
