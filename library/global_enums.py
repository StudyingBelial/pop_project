from enum import Enum, auto

# Global Ennumeration Class that is imported into class to define a size

class ItemSize(Enum):
    UNDEFINED = auto()
    MINI = auto()
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    INDUSTRIAL = auto()

class Warranty():

    class Duration(Enum):
        NONE = auto()
        SIX_MO = auto()
        TWELVE_MO = auto()
        EIGHTEEN_MO = auto()

    class Type(Enum):
        NONE = auto()
        FULL = auto()
        PARTIAL = auto()