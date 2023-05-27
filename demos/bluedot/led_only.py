from bluedot import BlueDot
from signal import pause
import usb_arm

arm = usb_arm.Arm()


def led_pressed(pos):
    arm.tell(usb_arm.LedOn)


def stop(*args):
    arm.tell(usb_arm.Stop)


bd = BlueDot(cols=3, rows=2)
led = bd[1, 0]

bd.when_released = stop
led.when_pressed = led_pressed
bd.when_client_disconnects = stop
pause()
