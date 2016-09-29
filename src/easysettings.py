import logging

from gi.repository import GObject, Gtk

from src.savefiledecoder import ConfigParserDecoder, JsonDecoder
from src.savefileencoder import ConfigParserEncoder, JsonEncoder
from src.types import SaveStyle

logger = logging.getLogger(__name__)


class EasySettings(GObject.GObject):
    __gsignals__ = {
        'settings_loaded': (GObject.SIGNAL_RUN_FIRST, None, (object,)),
        'settings_saved': (GObject.SIGNAL_RUN_FIRST, None, (object,)),
        # 'page_dirtied': (GObject.SIGNAL_RUN_FIRST, None, (object,))
    }

    def __init__(self, save_path, stencil, save_style=None):
        self._stencil = stencil
        self.is_stencil_dirty = True
        self.save_path = save_path
        self.save_style = save_style or SaveStyle.CONFIGPARSER
        self._gui = None
        self._page_gui = []

    @property
    def stencil(self):
        return self._stencil

    @stencil.setter
    def stencil(self, new_stencil):
        self.is_stencil_dirty = True
        self._stencil = new_stencil

    def _build_gui(self):
        stencilbox = self.stencil.get_gui()
        dialog = Gtk.Dialog()
        dialog.get_content_area().add(stencilbox)
        self._gui = dialog
        self.is_stencil_dirty = False

    def get_gui(self):
        if self.is_stencil_dirty:
            self._build_gui()
        return self._gui

    def get_page_gui(self, page):
        if self.is_stencil_dirty:
            self._build_gui()
            # fix this
        return self._page_gui[page]

    def save_settings(self):
        if self.save_style == SaveStyle.CONFIGPARSER:
            encoder = ConfigParserEncoder(self.save_path, self.stencil)
        else:
            encoder = JsonEncoder(self.save_path, self.stencil)
        encoder.write()

    def load_settings(self):
        if self.save_style == SaveStyle.CONFIGPARSER:
            encoder = ConfigParserDecoder(self.save_path)
        else:
            encoder = JsonDecoder(self.save_path)
        self.stencil = encoder.read()
