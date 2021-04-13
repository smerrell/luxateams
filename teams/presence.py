from enum import Enum
from typing import Optional

import requests


class Availability(Enum):
    Available = 'Available'
    AvailableIdle = 'AvailableIdle'
    Away = 'Away'
    BeRightBack = 'BeRightBack'
    Busy = 'Busy'
    BusyIdle = 'BusyIdle'
    DoNotDisturb = 'DoNotDisturb'
    Offline = 'Offline'
    PresenceUnknown = 'PresenceUnknown'


class Activity(Enum):
    Available = 'Available'
    Away = 'Away'
    BeRightBack = 'BeRightBack'
    Busy = 'Busy'
    DoNotDisturb = 'DoNotDisturb'
    InACall = 'InACall'
    InAConferenceCall = 'InAConferenceCall'
    Inactive = 'Inactive'
    InAMeeting = 'InAMeeting'
    Offline = 'Offline'
    OffWork = 'OffWork'
    OutOfOffice = 'OutOfOffice',
    PresenceUnknown = 'PresenceUnknown'
    Presenting = 'Presenting'
    UrgentInterruptionsOnly = 'UrgentInterruptionsOnly'


def get_presence(access_token) -> Optional[Activity]:
    graph_data = requests.get('https://graph.microsoft.com/beta/me/presence',
                              headers={'Authorization': 'Bearer ' + access_token},).json()

    if 'error' in graph_data and graph_data['error']['code'] == 'InvalidAuthenticationToken':
        return None

    try:
        print(f"availability: {graph_data['availability']}")
        print(f"activity: {graph_data['activity']}")
    except Exception as e:
        print("Uh oh")
        print(e)
        print(graph_data)

    return Activity[graph_data['activity']]
