from enum import Enum, auto

class Event(Enum):
    CTRL_C_PRESSED = auto()
    SHOW_OVERLAY   = auto()
