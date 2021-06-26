#!/usr/bin/env bash

busylight udev-rules -o 99-busylight.rules
sudo cp 99-busylight.rules /etc/udev/rules.d
sudo udevadm control -R
rm 99-busylight.rules

