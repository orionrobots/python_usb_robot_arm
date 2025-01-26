import owi_maplin_usb_arm as usb_arm
import logging

logging.basicConfig(level=logging.DEBUG)

arm = usb_arm.Arm()

arm.move(usb_arm.LedOn)
print("Wrist up")
arm.move(usb_arm.WristUp)
print("Wrist down")
arm.move(usb_arm.WristDown)

