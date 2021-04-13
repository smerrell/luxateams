#!/usr/bin/env python3

import atexit
import signal
import sys
import threading
from typing import Dict

from busylight.lights.luxafor import Flag

from aad.authentication import authenticate
from luxateams import config
from teams.presence import Activity, get_presence


def set_light(flag: Flag, status_map: Dict[str, str], status: Activity):
    status_color = config.to_rgb(status_map[status.value])
    flag.on(status_color)


def graceful_exit(signal, frame) -> None:
    sys.exit(0)


def shutdown_light(flag: Flag) -> None:
    flag.off()


def main() -> None:
    flag = Flag.first_light()
    # Handle Ctrl+C
    atexit.register(shutdown_light, flag)
    signal.signal(signal.SIGINT, graceful_exit)

    configuration = config.load_config()

    result = authenticate(configuration)

    ticker = threading.Event()
    attempts = 0
    while not ticker.wait(configuration.check_interval):
        if 'access_token' in result:
            presence = get_presence(result['access_token'])
            if presence is None and attempts < 5:
                # We had an auth error, try authenticating again
                flag.on([255, 128, 0])
                result = authenticate(configuration)
                attempts += 1
            else:
                set_light(flag, configuration.activity_map, presence)
                attempts = 0
        else:
            print('No access token found!')
            flag.on([255, 128, 0])
            sys.exit(1)


if __name__ == '__main__':
    main()
