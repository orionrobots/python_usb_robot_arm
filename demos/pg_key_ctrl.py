"""Pygame key_ctrl - key based arm controller"""
from functools import partial
import logging
import sys

import pygame
from pygame.locals import *

import owi_maplin_usb_arm as usb_arm

def handle_keys_held(arm):
    pressed_keys = pygame.key.get_pressed()
    pattern = usb_arm.Stop
    if pressed_keys[K_z]:
        pattern = pattern | usb_arm.BaseClockWise
    elif pressed_keys[K_x]:
        pattern = pattern | usb_arm.BaseCtrClockWise
    if pressed_keys[K_a]:
        pattern = pattern | usb_arm.ShoulderDown
    elif pressed_keys[K_q]:
        pattern = pattern | usb_arm.ShoulderUp
    if pressed_keys[K_s]:
        pattern = pattern | usb_arm.ElbowDown
    elif pressed_keys[K_w]:
        pattern = pattern | usb_arm.ElbowUp
    if pressed_keys[K_d]:
        pattern = pattern | usb_arm.WristDown
    elif pressed_keys[K_e]:
        pattern = pattern | usb_arm.WristUp
    if pressed_keys[K_r]:
        pattern = pattern | usb_arm.CloseGrips
    elif pressed_keys[K_f]:
        pattern = pattern | usb_arm.OpenGrips
    if pressed_keys[K_l]:
        pattern = pattern | usb_arm.LedOn
    arm.tell(pattern)


def key_loop():
    try:
        arm = usb_arm.Arm()
    except AttributeError:
        print("Please make sure the arm is connected and turned on")
        sys.exit(1)

    pygame.clock = pygame.time.Clock()
    FPS = 50

    try:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return
            handle_keys_held(arm)
            pygame.clock.tick(FPS)
    finally:
        arm.tell(usb_arm.Stop)


def main():
    logging.basicConfig()
    usb_arm.logger.setLevel(logging.DEBUG)
    pygame.init()
    pygame.display.set_mode([200, 200])
    print("Press z/x to turn the base motor")
    print("Press a/q to move the shoulder up/down")
    print("Press w/s to move the elbow up/down")
    print("Press e/d to move the wrist up/down")
    print("Press r/f to close/open the grips")
    print("Press l to toggle the LED")
    print("Press ESC to exit")
    key_loop()


main()
