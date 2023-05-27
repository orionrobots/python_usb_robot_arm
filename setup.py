from distutils.core import setup

setup(
    name='usb_arm',
    version='0.1.1',
    packages=['usb_arm',],
    author="Danny Staple - Orionrobots",
    license='Creative Commons By Attribution Share-Alike v3.0',
    long_description=open('README.md').read(),
    install_requires=[
        "pyusb"
    ]
)
