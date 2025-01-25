#!/bin/env bash
# Raspbian/Debian setup
# Usage
#  source ./install.sh [-v <venv folder>]
# Will activate/create a venv for the installation
#
#  -v <venv folder>  : Optional, specify a virtual environment folder to install into
#                      If not specified, uses .venv in the current folder
set -e

# Doesn't run with sudo, uses sudo for specific commands
sudo apt-get update -y
sudo apt-get install -y python3-libusb1 python3-pip git

venv_folder=".venv"
# check for the -v flag
while getopts "v:" opt; do
  case ${opt} in
    v )
      venv_folder=$OPTARG
      ;;
    \? )
      echo "Usage: source ./install.sh [-v <venv folder>]"
      return 1
      ;;
  esac
done

if [ ! -d "$venv_folder" ]; then
  python3 -m venv "$venv_folder"
fi
source "$venv_folder/bin/activate"

pip3 install git+https://github.com/orionrobots/python_usb_robot_arm

# cat <<END >/etc/udev/rules.d/42-usb-arm-permissions.rules
# SUBSYSTEM=="usb", ATTR{idVendor}=="1267", ATTR{idProduct}=="0000", MODE:="0666"
# END

# echo "Please reboot for the udev rules to take effect"
echo "To use the library, source the virtual environment with:"
echo "  source $venv_folder/bin/activate"
