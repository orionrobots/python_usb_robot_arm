"""Console keyboard based arm controller.
Requires readchar
"""
from functools import partial
import logging
import sys
import time

from readchar import readkey, key

import owi_maplin_usb_arm as usb_arm


KEYMAP =  {
    'z': usb_arm.BaseClockWise,
    'x': usb_arm.BaseCtrClockWise,
    'r': usb_arm.CloseGrips,
    'f': usb_arm.OpenGrips,
    'a': usb_arm.ShoulderDown,
    'q': usb_arm.ShoulderUp,
    's': usb_arm.ElbowDown,
    'w': usb_arm.ElbowUp,
    'd': usb_arm.WristDown,
    'e': usb_arm.WristUp,
    'l': usb_arm.LedOn
}

def handle_key(arm, pressed_key):
    if pressed_key in KEYMAP:
        message = KEYMAP[pressed_key]
        print("Key ", pressed_key, "Movement message", message)

        arm.move(message, 0.5)

def key_loop():
    try:
        arm = usb_arm.Arm()
    except AttributeError:
        print("Please make sure the arm is connected and turned on")
        sys.exit(1)
    handle = partial(handle_key, arm)
    exit_key = key.ESC

    while True:
        pressed_key = readkey()
        if pressed_key == exit_key:
            return
        else:
            handle(pressed_key)
        time.sleep(0.1)

def main():
    logging.basicConfig()
    usb_arm.logger.setLevel(logging.DEBUG)
    print("Press z/x to turn the base motor")
    print("Press a/q to move the shoulder up/down")
    print("Press w/s to move the elbow up/down")
    print("Press e/d to move the wrist up/down")
    print("Press r/f to close/open the grips")
    print("Press l to toggle the LED")
    print("Press ESC to exit")
    key_loop()

main()
