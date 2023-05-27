Help Setting Up On Windows
==========================

Tested with Python 2.7, Windows 8 64 bit.

First ensure you have a version of python installed.

[Windows Installation Video](https://www.youtube.com/watch?v=sNp8Z_MH7iQ)

LibUSB - The Backend
====================
To get libusb running, the backend, go to http://sourceforge.net/projects/libusb-win32/files/ and pick up the latest release.

Extract this zipfile, then go into the extracted folder and find bin/inf-wizard.exe. Run this _as administrator_.
When you are asked to find the device - it has Vendor ID 0x1267, Product ID 0000.

This should install a driver on your computer giving you access to the arm. 
If it complains about installing the driver, remember that this tool shoudl be run as administrator.

PyUSB
=====
Warning - confusingly there are two completely different python libraries of this name. 

This is the correct one: http://walac.github.io/pyusb/
This is the wrong one: http://bleyer.org/pyusb/

On the walac site, there is a zip. Download this, and extract it into a folder.
Start a terminal, and CD into the folder.
Then run :
python setup.py 

Now you should be able to run the usb_arm code. Import it and try some simple movements.


