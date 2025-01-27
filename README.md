# Python Code to drive the Maplin/OWI "Edge" USB Robot arm

The main repository for this is https://github.com/orionrobots/python_usb_robot_arm.

[Video Demo](https://www.youtube.com/watch?v=dAvWBOTtGnU)

## Advice ahead of time

If you are considering buying this kit, I suggest looking at the more capable and simpler MeArm kit. The MeArm is simpler to build, has servo motors for better control (less gear slop, and positioning instead of dead reckoning), and also simpler to power (D-Cells are not that widely available). This arm does have an additional DOF with the wrist bending.

If you already have this kit, then I hope you find this library and it's information useful.

## Quick Raspberry Pi Installation

On a terminal at the Raspberry Pi enter these commands:

    curl https://raw.githubusercontent.com/orionrobots/python_usb_robot_arm/main/setup_arm.sh | sudo bash

I suggest review the setup_arm.sh script above to see what it does.

## Requirements for Other OS

This has previously been tested on Linux, OSX and Windows. OSX and Windows require signed drivers which may not easily be available.

* Python 3
* Libusb (on linux, mac or windows - <http://sourceforge.net/projects/libusb-win32/files/latest/download>) - the apt-get package will work.
* To work with Windows use this tool to install the **Libusb** driver for the arm: <https://github.com/pbatard/libwdi/releases/tag/v1.5.1>
* pyusb via pip - a virtual is recommended.

## Demos

- demos/simple.py - simple demonstration
- demos/pg_key_ctrl.py - Pygame keypress demo, including moving multiple motors simultaneously. Requires pygame installed in the same venv.
- demos/sh_key_ctrl.py - Console keypress demo
- demos/bluedot - Blue dot control demo, may be a bit stale
- demos/web_arm - Flask web control demo, may be a bit stale

## Usage

As a library:

    >>> import owi_maplin_usb_arm as usb_arm

To initialise libusb and the arm

    >>> arm = usb_arm.Arm()

This will tell you if all the dependencies work, and will throw an exception if it fails to find the arm and connect
 to it.

Now lets test it by turning on the LED

    >>> arm.move(usb_arm.LedOn)

It will turn on for 1 second, and automatically turn off. The moveArm function automatically turns off after each
move. You can optionally specify another time, but since the Maplin arm doesn't have any sensors, beware that if
it reaches limits before the time finishes, then it won't stop.

### Actual movement

    >>> arm.move(usb_arm.ElbowUp)

The elbow will move up.
The movements possible:

- `GripsOpen` (OpenGrips)
- `GripsClose` (CloseGrips)
- `WristUp`
- `WristDown`
- `ElbowUp`
- `ElbowDown`
- `ShoulderUp`
- `ShoulderDown`
- `BaseClockWise`
- `BaseCtrClockWise`

- `Stop`

- `LedOn`

## Combining Movements

Movements are based upon the BitPattern class, and you can feed arbitrary bitpatterns to it, but all those the
arm is currently capable of are represented above.

However, you may want to make more than one movement at the same time. You can do this by combining patterns with the
or operator:

    >>> arm.move(usb_arm.ElbowDown | usb_arm.BaseClockWise, 0.5)

The arm should turn clockwise and bring the elbow up simultaneously for half a second.

### Gear Lash

The unmodified arm has a few flaws - it has fairly loose gear chains in the "servos" it uses for the movements.
To see what I mean try the following:

    >>> arm.move(usb_arm.ShoulderUp, 0.5)
    >>> arm.move(usb_arm.ShoulderDown, 0.5)

You will note the arm moves, but when it returns, it does not quite return to the same position - there is an error,
which you will need to account for as you use the arm and in programmed sequences.

You should now know enough to move the arm to any location.

### Sequences of Actions

You can create programmed sequences of actions for the robot. However, before you issue one of these, ensure you
know the position of the arm, and wont move it past its limits - which could cause damage to it,

Sequences are created as arrays of commands. Each command is an array of the bitpattern, followed by the
optional time (defaulting to 1 second):

    >>> actions = [[usb_arm.ElbowDown, 0.5], [usb_arm.GripsClose, 0.5], [usb_arm.ElbowUp]]

To issue the action list:

    >>> arm.doActions(actions)

Note you can ctrl-c stop the movements.
There are a couple of canned actions already in the module:

    block_left
    block_right
    left_and_blink

## An Example Script

Using this in a python file couldn't be easier. For example you could put this in demo_arm.py:

    import usb_arm
    arm = usb_arm.Arm()
    actions = [[usb_arm.ElbowDown, 0.5], [usb_arm.GripsClose, 0.5], [usb_arm.ElbowUp]]
    arm.doActions(actions)

You can then run this with python3 demo_arm.py.

## Troubleshooting

### Linux - permissions

You will either need to run as root (not recommended) or modify your system to allow all users access to the device.

    sudo nano /etc/udev/rules.d/42-usb-arm-permissions.rules

and add:

    SUBSYSTEM=="usb", ATTR{idVendor}=="1267", ATTR{idProduct}=="0000", MODE:="0666"

Note: **idProduct** can vary (0000, 0001, etc.).
You can check these via the **lsusb** terminal command.


Plug in the device and you should be able to access it. Tested on Ubuntu and Mint Linux versions.

## License

CC BY SA 3.0 - http://creativecommons.org/licenses/by-sa/3.0/
Creative Commons By Attribution Share-Alike v3.0

## Related Work

* The original reverse engineering of the USB protocol was done by
[Vadim Zaliva](http://www.crocodile.org/lord/) and published on [his blog](http://notbrainsurgery.livejournal.com/38622.html)
* [Device assembly manual](https://www.robotpark.com/DT/PRO/91010-OWI-535%20ROBOTIC%20ARM%20EDGE%20KIT_PDF.pdf)
* [OWI (manufacturer) information](https://www.owirobots.com/store/index.php?l=product_detail&p=138)
* [PCB Scans](https://kyllikki.github.io/EdgeRobotArm/) - from Vincent Sanders aka Kyllikki

## Enabling Debug Logging

There's debug logging for the USB messages in the arm class using python standard logging.

If you want to see what USB messages are being sent, try this:

```python
>>> import usb_arm
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> arm = usb_arm.Arm()
>>> arm.move(usb_arm.ElbowUp)
```

You should see debug messages about the USB messages being sent.

```
DEBUG:usb_arm:Sending ctrl message (<BitPattern arm:16 base:0 led:0>)
DEBUG:usb_arm:Sending ctrl message (<BitPattern arm:0 base:0 led:0>)
```
