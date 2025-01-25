from bluedot import BlueDot
from signal import pause
import owi_maplin_robot_arm

arm = owi_maplin_robot_arm.Arm()


def led_pressed(pos):
    arm.tell(owi_maplin_robot_arm.LedOn)


def stop(*args):
    arm.tell(owi_maplin_robot_arm.Stop)


bd = BlueDot(cols=3, rows=2)
led = bd[1, 0]

bd.when_released = stop
led.when_pressed = led_pressed
bd.when_client_disconnects = stop
pause()
