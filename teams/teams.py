from enum import Enum


class Availability(Enum):
    available = 'Available'
    available_idle = 'AvailableIdle'
    away = 'Away'
    be_right_back = 'BeRightBack'
    busy = 'Busy'
    busy_idle = 'BusyIdle'
    do_not_disturb = 'DoNotDisturb'
    offline = 'Offline'
    presence_unknown = 'PresenceUnknown'


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
