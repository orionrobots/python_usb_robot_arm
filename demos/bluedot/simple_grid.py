from bluedot import BlueDot
from signal import pause
import usb_arm

arm = usb_arm.Arm()


def led_pressed(pos):
    arm.tell(usb_arm.LedOn)


def stop(*args):
    arm.tell(usb_arm.Stop)


def grip_pressed(pos):
    if pos.top:
        arm.tell(usb_arm.GripsClose)
    if pos.bottom:
        arm.tell(usb_arm.GripsOpen)


def wrist_pressed(pos):
    if pos.top:
        arm.tell(usb_arm.WristUp)
    if pos.bottom:
        arm.tell(usb_arm.WristDown)


def elbow_pressed(pos):
    if pos.top:
        arm.tell(usb_arm.ElbowUp)
    if pos.bottom:
        arm.tell(usb_arm.ElbowDown)


def shoulder_pressed(pos):
    if pos.top:
        arm.tell(usb_arm.ShoulderUp)
    if pos.bottom:
        arm.tell(usb_arm.ShoulderDown)


def base_pressed(pos):
    if pos.left:
        arm.tell(usb_arm.BaseCtrClockWise)
    if pos.right:
        arm.tell(usb_arm.BaseClockWise)


bd = BlueDot(cols=3, rows=2)
led = bd[1, 0]

bd.when_released = stop
led.when_pressed = led_pressed
bd.when_client_disconnects = stop
pause()
