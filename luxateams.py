#!/usr/bin/env python3

import json
import sys
from typing import Any

import msal
import requests


def foo(config: Any):
    app = msal.PublicClientApplication(
        config['application']['id'], None, authority=config['aad']['authority'])

    result = None
    accounts = app.get_accounts()
    if accounts:
        print('wow, we have an account!')

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
        print("WE HAVE AN ACCESS TOKEN")
        print(result['access_token'])
        graph_data = requests.get('https://graph.microsoft.com/beta/me/presence',
                                  headers={'Authorization': 'Bearer ' + result['access_token']},).json()
        print(json.dumps(graph_data, indent=2))
    else:
        print(json.dumps(result, indent=2))


def main() -> None:
    config = None
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    foo(config)


if __name__ == '__main__':
    main()
