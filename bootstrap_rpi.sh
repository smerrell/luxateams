#!/usr/bin/env bash

# Get our dependencies for busylight to work with the Luxafor flag
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install cython libudev-dev libusb-1.0.0 libusb-dev libusb-1.0.0-dev libhidapi-dev

# Install the python dependencies
pipenv install

# Configure the USB rules so the script can control the Luxafor Flag
pipenv run ./busylight.sh

