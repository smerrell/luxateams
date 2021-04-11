from enum import Enum


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
