from bluedot import BlueDot
from signal import pause
import owi_maplin_robot_arm

arm = owi_maplin_robot_arm.Arm()


def led_pressed(pos):
    arm.tell(owi_maplin_robot_arm.LedOn)


def stop(*args):
    arm.tell(owi_maplin_robot_arm.Stop)


def grip_pressed(pos):
    if pos.top:
        arm.tell(owi_maplin_robot_arm.GripsClose)
    if pos.bottom:
        arm.tell(owi_maplin_robot_arm.GripsOpen)


def wrist_pressed(pos):
    if pos.top:
        arm.tell(owi_maplin_robot_arm.WristUp)
    if pos.bottom:
        arm.tell(owi_maplin_robot_arm.WristDown)


def elbow_pressed(pos):
    if pos.top:
        arm.tell(owi_maplin_robot_arm.ElbowUp)
    if pos.bottom:
        arm.tell(owi_maplin_robot_arm.ElbowDown)


def shoulder_pressed(pos):
    if pos.top:
        arm.tell(owi_maplin_robot_arm.ShoulderUp)
    if pos.bottom:
        arm.tell(owi_maplin_robot_arm.ShoulderDown)


def base_pressed(pos):
    if pos.left:
        arm.tell(owi_maplin_robot_arm.BaseCtrClockWise)
    if pos.right:
        arm.tell(owi_maplin_robot_arm.BaseClockWise)


bd = BlueDot(cols=3, rows=2)
led = bd[1, 0]

bd.when_released = stop
led.when_pressed = led_pressed
bd.when_client_disconnects = stop
pause()
