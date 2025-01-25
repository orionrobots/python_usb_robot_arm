"""key_ctrl - key based arm controller"""
from functools import partial
import owi_maplin_robot_arm
import pygame
from pygame.locals import *
import sys


def handle_key(arm, delay, key_map, key):
    def do_it():
        if key in key_map:
            print("Doing key ", key)
            arm.move(key_map[key], delay)
    arm.safe_tell(do_it)


def make_keymap():
    """Bp - an initialised arm bitpattern.
    returns the keymap"""
    return {
        K_z: owi_maplin_robot_arm.BaseClockWise,
        K_x: owi_maplin_robot_arm.BaseCtrClockWise,
        K_r: owi_maplin_robot_arm.CloseGrips,
        K_f: owi_maplin_robot_arm.OpenGrips,
        K_a: owi_maplin_robot_arm.ShoulderDown,
        K_q: owi_maplin_robot_arm.ShoulderUp,
        K_s: owi_maplin_robot_arm.ElbowDown,
        K_w: owi_maplin_robot_arm.ElbowUp,
        K_d: owi_maplin_robot_arm.WristDown,
        K_e: owi_maplin_robot_arm.WristUp}


def key_loop():
    km = make_keymap()
    try:
        arm = owi_maplin_robot_arm.Arm()
    except AttributeError:
        print("Please make sure the arm is connected and turned on")
        sys.exit(1)
    handle = partial(handle_key, arm, 0.5, km)
    exit_key = K_ESCAPE

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.key == exit_key:
                    return
                else:
                    handle(event.key)


def main():
    pygame.init()
    key_loop()


main()
