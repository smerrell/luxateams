#!/usr/bin/env python3

import json
import signal
import sys
import threading
from typing import Dict, List

from busylight.lights.luxafor import Flag

from aad.authentication import authenticate
from luxateams import config
from teams.presence import Activity, get_presence


def set_light(flag: Flag, status_map: Dict[str, str], status: Activity):
    status_color = config.to_rgb(status_map[status.value])
    flag.on(status_color)


def graceful_exit(signal, frame):
    sys.exit(0)


def main() -> None:
    # Handle Ctrl+C
    signal.signal(signal.SIGINT, graceful_exit)

    configuration = config.load_config()

    flag = Flag.first_light()

    result = authenticate(configuration)

    ticker = threading.Event()
    while not ticker.wait(configuration.check_interval):
        if 'access_token' in result:
            presence = get_presence(result['access_token'])
            set_light(flag, configuration.activity_map, presence)
        else:
            print('No access token found!')
            flag.on([255, 128, 0])
            sys.exit(1)


if __name__ == '__main__':
    main()
