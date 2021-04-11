from enum import Enum

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


def get_presence(access_token) -> Activity:
    graph_data = requests.get('https://graph.microsoft.com/beta/me/presence',
                              headers={'Authorization': 'Bearer ' + access_token},).json()
    print(f"availability: {graph_data['availability']}")
    print(f"activity: {graph_data['activity']}")

    return Activity[graph_data['activity']]
