import logging
from enum import Enum

from gi.repository import GObject

logger = logging.getLogger(__name__)


class SaveStyle(Enum):
    CONFIGPARSER = 1
    JSON = 2


class EasySettings(GObject.GObject):
    __gsignals__ = {
        'settings_loaded': (GObject.SIGNAL_RUN_FIRST, None, (object,)),
        'settings_saved': (GObject.SIGNAL_RUN_FIRST, None, (object,))
    }

    def __init__(self, save_path, stencil, save_style=None):
        self._stencil = None
        self.save_path = save_path
        self.stencil_dirty = None
        self._gui = None
        self.stencil(stencil)
        if save_style == SaveStyle.CONFIGPARSER.name:
            self.save_style = SaveStyle.CONFIGPARSER
        else:
            self.save_style = SaveStyle.JSON

    @property
    def stencil(self):
        return self._stencil

    @stencil.setter
    def stencil(self, new_val):
        self.stencil_dirty = True
        self._stencil = new_val

    @property
    def gui(self):
        if self.stencil_dirty:
            self._build_gui()
        return self._gui

    def _build_gui(self):
        self.stencil_dirty = False

    def save_settings(self):
        pass

    def load_settings(self):
        pass
