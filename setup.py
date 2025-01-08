from distutils.core import setup

setup(
    name='usb_robot_arm',
    version='0.2.0',
    packages=['usb_robot_arm',],
    author="Danny Staple - Orionrobots",
    license='Creative Commons By Attribution Share-Alike v3.0',
    long_description=open('README.md').read(),
    install_requires=[
        "pyusb"
    ]
)
