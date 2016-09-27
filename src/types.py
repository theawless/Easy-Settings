from enum import Enum


class SaveStyle(Enum):
    CONFIGPARSER = 1
    JSON = 2


class ItemType(Enum):
    ENTRY = 0
    RADIOGROUP = 1
    CHECKBOX = 2
    COMBOBOX = 3


class StencilType(Enum):
    EMPTY = -1
    SINGLE = 0
    NOTEBOOK = 1
    STACKSWITCHER = 2
