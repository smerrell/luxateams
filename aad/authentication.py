
import atexit
import json
import os
import sys

import msal
from luxateams.config import Config


def authenticate(config: Config):
    cache = msal.SerializableTokenCache()
    if os.path.exists('my_cache.bin'):
        cache.deserialize(open('my_cache.bin', 'r').read())
    atexit.register(lambda:
                    open('my_cache.bin', 'w').write(cache.serialize())
                    )
    app = msal.PublicClientApplication(
        config.application.id, None, token_cache=cache, authority=config.aad.authority)

    result = None
    accounts = app.get_accounts()
    if accounts:
        print("Account(s) exists in cache, probably with token too. Let's try.")
        # Assuming the end user chose this one
        chosen = accounts[0]
        # Now let's try to find a token in cache for this account
        result = app.acquire_token_silent(
            config.graph.scopes, account=chosen)

    if not result:
        print('Getting token from AAD')
        flow = app.initiate_device_flow(scopes=config.graph.scopes)
        if 'user_code' not in flow:
            raise ValueError(
                f"Fail to create device flow. Err; {json.dumps(flow, indent=2)}")

        print(flow['message'])
        sys.stdout.flush()

        # Blocks by default
        result = app.acquire_token_by_device_flow(flow)
        # print(json.dumps(result, indent=2))

    if 'access_token' in result:
        pass
    else:
        print(json.dumps(result, indent=2))

    return result
