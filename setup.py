from distutils.core import setup

setup(
    name='owi_maplin_usb_arm',
    version='0.4.0',
    packages=['owi_maplin_usb_arm',],
    author="Danny Staple - Orionrobots",
    license='Creative Commons By Attribution Share-Alike v3.0',
    long_description=open('README.md').read(),
    install_requires=[
        "pyusb"
    ]
)
