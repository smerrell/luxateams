#!/usr/bin/env python3

import atexit
import json
import os
import sys
import threading
from typing import Any


import msal
import requests
from busylight.lights.luxafor import Flag
from busylight.lights.usblight import USBLight
from teams.teams import Activity


def set_light(flag: Flag, status):
    # Available, Away, BeRightBack, Busy, DoNotDisturb, InACall,
    # InAConferenceCall, Inactive,InAMeeting, Offline, OffWork,OutOfOffice,
    # PresenceUnknown,Presenting, UrgentInterruptionsOnly.
    if status == Activity.Available:
        flag.on([0, 255, 0])
    if status == Activity.Busy:
        flag.on([255, 0, 0])
    if status == Activity.Away:
        flag.on([255, 128, 0])


def get_presence(access_token) -> Activity:
    graph_data = requests.get('https://graph.microsoft.com/beta/me/presence',
                              headers={'Authorization': 'Bearer ' + access_token},).json()
    print(f"activity: {graph_data['activity']}")

    return Activity[graph_data['activity']]


def authenticate(config: Any):
    cache = msal.SerializableTokenCache()
    if os.path.exists('my_cache.bin'):
        cache.deserialize(open('my_cache.bin', 'r').read())
    atexit.register(lambda:
                    open('my_cache.bin', 'w').write(cache.serialize())
                    )
    app = msal.PublicClientApplication(
        config['application']['id'], None, token_cache=cache, authority=config['aad']['authority'])

    result = None
    accounts = app.get_accounts()
    if accounts:
        print("Account(s) exists in cache, probably with token too. Let's try.")
        # Assuming the end user chose this one
        chosen = accounts[0]
        # Now let's try to find a token in cache for this account
        result = app.acquire_token_silent(
            config['graph']["scopes"], account=chosen)

    if not result:
        print('Getting token from AAD')
        flow = app.initiate_device_flow(scopes=config['graph']['scopes'])
        if 'user_code' not in flow:
            raise ValueError(
                f"Fail to create device flow. Err; {json.dumps(flow, indent=2)}")

        print(flow['message'])
        sys.stdout.flush()

        # Blocks by default
        result = app.acquire_token_by_device_flow(flow)
        print(json.dumps(result, indent=2))

    if 'access_token' in result:
        pass
    else:
        print(json.dumps(result, indent=2))

    return result


def main() -> None:
    config = None
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    flag = Flag.first_light()

    result = authenticate(config)

    ticker = threading.Event()
    while not ticker.wait(1):
        if 'access_token' in result:
            print('getting presence.')
            presence = get_presence(result['access_token'])
            set_light(flag, presence)


if __name__ == '__main__':
    main()
