import logging
from abc import ABCMeta, abstractmethod

from gi.repository import Gtk

from src.elements import CompositeElement, Element

logger = logging.getLogger(__name__)


class Valued(metaclass=ABCMeta):
    def __init__(self, value=""):
        self.value = value

    @abstractmethod
    def update(self):
        pass


class Item(Element, Valued, metaclass=ABCMeta):
    def __init__(self, name, display_name, value=None):
        Element.__init__(self, name, display_name)
        Valued.__init__(self, value)


class CompositeItem(CompositeElement, Valued, metaclass=ABCMeta):
    def __init__(self, name, display_name, value=None):
        CompositeElement.__init__(self, name, display_name)
        Valued.__init__(self, value)


class Entry(Item):
    def _build_gui(self):
        self._gui = Gtk.HBox()
        self.entry = Gtk.Entry()
        self.entry.set_text(self.value)
        label = Gtk.Label(self.display_name)
        self._gui.pack_start(label, False, False, 0)
        self._gui.pack_start(self.entry, False, False, 0)

    def update(self):
        self.value = self.entry.get_text()


class RadioGroup(CompositeItem):
    def _build_gui(self):
        pass

    def update(self):
        pass


class CheckBox(CompositeItem):
    def _build_gui(self):
        pass

    def update(self):
        pass


class ComboBox(CompositeItem):
    def _build_gui(self):
        pass

    def update(self):
        pass
