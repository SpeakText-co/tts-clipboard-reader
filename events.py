from enum import Enum, auto

class Event(Enum):
    CLIPBOARD_TRIGGER = auto()
    STOP = auto()
    TOGGLE_PAUSE = auto()
