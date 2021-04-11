#!/usr/bin/env python3

import json
import signal
import sys
import threading

from busylight.lights.luxafor import Flag

from aad.authentication import authenticate
from teams.presence import Activity, get_presence


def set_light(flag: Flag, status):
    if status == Activity.Available:
        flag.on([0, 255, 0])
    if status == Activity.Busy:
        flag.on([255, 0, 0])
    if status == Activity.Away:
        flag.on([255, 128, 0])
    if status == Activity.OffWork:
        flag.off()


def graceful_exit(signal, frame):
    sys.exit(0)


def main() -> None:
    # Handle Ctrl+C
    signal.signal(signal.SIGINT, graceful_exit)

    config = None
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    flag = Flag.first_light()

    result = authenticate(config)

    ticker = threading.Event()
    while not ticker.wait(config['check_interval']):
        if 'access_token' in result:
            print('getting presence.')
            presence = get_presence(result['access_token'])
            set_light(flag, presence)


if __name__ == '__main__':
    main()
