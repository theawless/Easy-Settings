import logging

from gi.repository import Gtk

from src.elements import Guied
from src.loader import ConfigParserLoader, JsonLoader
from src.saver import ConfigParserSaver, JsonSaver
from src.types import SaveStyle

logger = logging.getLogger(__name__)


class EasySettings(Guied):
    def __init__(self, save_path, stencil, save_style=SaveStyle.CONFIGPARSER):
        super().__init__()
        self._stencil = stencil
        self._gui = None
        self.save_path = save_path
        self.save_style = save_style

    @property
    def stencil(self):
        return self._stencil

    @stencil.setter
    def stencil(self, new_stencil):
        self._is_dirty = True
        self._stencil = new_stencil

    def _build_gui(self):
        self._gui = Gtk.Dialog()
        self._gui.get_content_area().pack_start(self.stencil.get_gui(), False, False, 0)
        self._gui.connect('delete_event', self.save_settings)

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
        encoder.read()
