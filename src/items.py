import logging
from abc import ABCMeta
from gi.repository import Gtk
from src.elements import CompositeElement, Element

logger = logging.getLogger(__name__)


class Valued:
    def __init__(self, value=""):
        self.value = value


class Item(Element, Valued, metaclass=ABCMeta):
    def __init__(self, name, display_name, value=None):
        Element.__init__(self, name, display_name)
        Valued.__init__(self, value)


class CompositeItem(CompositeElement, Valued, metaclass=ABCMeta):
    def __init__(self, name, display_name, value=None):
        CompositeElement.__init__(self, name, display_name)
        Valued.__init__(self, value)


class Entry(Item):
    def get_gui(self):
        entrybox = Gtk.HBox()
        entry = Gtk.Entry()
        entry.set_text(self.value)
        label = Gtk.Label(self.display_name)
        entrybox.pack_start(label, False, False, 0)
        entrybox.pack_start(entry, False, False, 0)
        return entrybox


class RadioGroup(CompositeItem):
    def get_gui(self):
        pass


class CheckBox(CompositeItem):
    def get_gui(self):
        pass


class ComboBox(CompositeItem):
    def get_gui(self):
        pass
