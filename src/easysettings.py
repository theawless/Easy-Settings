import logging

from gi.repository import GObject

from src.savefiledecoder import ConfigParserDecoder, JsonDecoder
from src.savefileencoder import ConfigParserEncoder, JsonEncoder
from src.types import SaveStyle

logger = logging.getLogger(__name__)


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
        self.save_style = save_style or SaveStyle.CONFIGPARSER

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
        if self.save_style == SaveStyle.CONFIGPARSER:
            encoder = ConfigParserEncoder(self.stencil)
        else:
            encoder = JsonEncoder(self.stencil)
        encoder.write()

    def load_settings(self):
        if self.save_style == SaveStyle.CONFIGPARSER:
            encoder = ConfigParserDecoder(self.save_path)
        else:
            encoder = JsonDecoder(self.save_path)
        self.stencil = encoder.read()
