Python Code to drive the Maplin/OWI "Edge" USB Robot arm. The main repository for this is https://github.com/orionrobots/python_usb_robot_arm.

[Video Demo](https://www.youtube.com/watch?v=dAvWBOTtGnU)

Quick Raspberry Pi Installation
===============================

On a terminal at the Raspberry Pi enter these commands:

    curl https://raw.githubusercontent.com/orionrobots/python_usb_robot_arm/master/setup_arm.sh | sudo bash

I suggest review the setup_arm.sh script above to see what it does.

Requirements for Other OS
==========================

This has previously been tested on Linux, OSX and Windows. OSX and Windows require signed drivers which may not easily be avialable.

* Python 2.7 or 3
* Libusb (on linux, mac or windows - http://sourceforge.net/projects/libusb-win32/files/latest/download) - the apt-get package will work.
* pyusb via pip

Usage
=====
As a library:

    >>> import usb_arm

To initialise libusb and the arm

    >>> arm = usb_arm.Arm()

This will tell you if all the dependencies work, and will throw an exception if it fails to find the arm and connect
 to it.

Now lets test it by turning on the LED

    >>> arm.move(usb_arm.LedOn)

It will turn on for 1 second, and automatically turn off. The move() function automatically turns off after each
move. You can optionally specify another time, but since the Maplin arm doesn't have any sensors, beware that if
it reaches limits before the time finishes, then it won't stop.

Actual movement
---------------

    >>> arm.move(usb_arm.ElbowUp)

The elbow will move up.
The movements possible:

GripsOpen
GripsClose
WristUp
WristDown
ElbowUp
ElbowDown
ShoulderUp
ShoulderDown
BaseClockWise
BaseCtrClockWise

Stop

LedOn

Combining Movements
-------------------
Movements are based upon the BitPattern class, and you can feed arbitrary bitpatterns to it, but all those the
arm is currently capable of are represented above.

However, you may want to make more than one movement at the same time. You can do this by combining patterns with the
or operator:

    >>> arm.move(usb_arm.ElbowDown | usb_arm.BaseClockWise, 0.5)

The arm should turn clockwise and bring the elbow up simultaneously for half a second.

Gear Lash
---------

The unmodified arm has a few flaws - it has fairly loose gear chains in the "servos" it uses for the movements.
To see what I mean try the following:

    >>> arm.move(usb_arm.ShoulderUp, 0.5)
    >>> arm.move(usb_arm.ShoulderDown, 0.5)

You will note the arm moves, but when it returns, it does not quite return to the same position - there is an error,
which you will need to account for as you use the arm and in programmed sequences.

You should now know enough to move the arm to any location.

Sequences of Actions
--------------------
You can create programmed sequences of actions for the robot. However, before you issue one of these, ensure you
know the position of the arm, and wont move it past its limits - which could cause damage to it,

Sequences are created as arrays of commands. Each command is an array of the bitpattern, followed by the
optional time (defaulting to 1 second):

    >>> actions = [[usb_arm.ElbowDown, 0.5], [usb_arm.CloseGrips, 0.5], [usb_arm.ElbowUp]]

To issue the action list:

    >>> arm.doActions(actions)

Note you can ctrl-c stop the movements.
There are a couple of canned actions already in the module:

    block_left
    block_right
    left_and_blink

An Example Script
=================

Using this in a python file couldn't be easier. For example you could put this in demo_arm.py:

    import usb_arm
    arm = usb_arm.Arm()
    actions = [[usb_arm.ElbowDown, 0.5], [usb_arm.CloseGrips, 0.5], [usb_arm.ElbowUp]]
    arm.doActions(actions)
    
You can then run this with python3 demo_arm.py.

Troubleshooting
===============

Linux - permissions
-------------------

You will either need to run as root (not recommended) or modify your system to allow all users access to the device.

    sudo nano /etc/udev/rules.d/42-usb-arm-permissions.rules

and add:

    SUBSYSTEM=="usb", ATTR{idVendor}=="1267", ATTR{idProduct}=="0000", MODE:="0666"

Plug in the device and you should be able to access it. Tested on Ubuntu and Mint Linux versions.

License
=======
CC BY SA 3.0 - http://creativecommons.org/licenses/by-sa/3.0/
Creative Commons By Attribution Share-Alike v3.0

Related Work
============

* The original reverse engineering of the UBS protocol was done by 
[Vadim Zaliva](http://www.crocodile.org/lord/) and published on [his blog] (http://notbrainsurgery.livejournal.com/38622.html)
* [An alternative Objective-C control program](https://armctrl.codeplex.com)
* Device assembly manual https://www.robotshop.com/media/files/pdf/owi-535_manual.pdf
* [OWI (manufacturer) information](http://www.owirobots.com/cart/catalog/OWI-535USB-ROBOTIC-ARM-KIT-with-USB-PC-INTERFACE-Assembled-103.html)

