from enum import Enum
from typing import Optional
from datetime import datetime

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
        print(f"{datetime.now()}: Error: {graph_data}")
        return None

    if 'activity' in graph_data:
        print(f"{datetime.now()}: activity: {graph_data['activity']}")
    else:
        print("Unable to find 'activity' in graph data")
        print(graph_data)

    return Activity[graph_data['activity']]
