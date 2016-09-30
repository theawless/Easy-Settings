import logging

from gi.repository import GObject, Gtk

from src.loader import ConfigParserLoader, JsonLoader
from src.saver import ConfigParserSaver, JsonSaver
from src.types import SaveStyle

logger = logging.getLogger(__name__)


class EasySettings(GObject.GObject):
    __gsignals__ = {
        'settings_loaded': (GObject.SIGNAL_RUN_FIRST, None, (object,)),
        'settings_saved': (GObject.SIGNAL_RUN_FIRST, None, (object,)),
    }

    def __init__(self, save_path, stencil, save_style=SaveStyle.CONFIGPARSER):
        self._stencil = stencil
        self.is_stencil_dirty = True
        self.save_path = save_path
        self.save_style = save_style
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
        self._gui = Gtk.Dialog()
        self._gui.get_content_area().add(stencilbox)
        self._gui.connect('delete_event', self.save_settings)
        self.is_stencil_dirty = False

    def get_gui(self):
        if self.is_stencil_dirty:
            self._build_gui()
        return self._gui

    def save_settings(self, __, ___):
        self.stencil.update()
        if self.save_style == SaveStyle.CONFIGPARSER:
            encoder = ConfigParserSaver(self.save_path, self.stencil)
        else:
            encoder = JsonSaver(self.save_path, self.stencil)
        encoder.write()

    def load_settings(self):
        if self.save_style == SaveStyle.CONFIGPARSER:
            encoder = ConfigParserLoader(self.save_path, self.stencil)
        else:
            encoder = JsonLoader(self.save_path, self.stencil)
        self.stencil = encoder.read()
