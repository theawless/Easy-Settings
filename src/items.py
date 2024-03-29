import logging
from abc import ABCMeta, abstractmethod

from gi.repository import Gtk

from src.elements import CompositeElement, Element

logger = logging.getLogger(__name__)


class Valued(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def update(self, gui, data):
        pass


class Item(Element, Valued, metaclass=ABCMeta):
    def __init__(self, name, display_name, value=""):
        Element.__init__(self, name, display_name)
        Valued.__init__(self, value)


class CompositeItem(CompositeElement, Valued, metaclass=ABCMeta):
    def __init__(self, name, display_name, subitem_class, value=""):
        CompositeElement.__init__(self, name, display_name)
        Valued.__init__(self, value)
        self.subitem_class = subitem_class

    def add_subitems(self, *args):
        self._add_units(args)

    def remove_subitems(self, *args):
        self._remove_units(args)


class Entry(Item):
    def _build_gui(self):
        self._gui = Gtk.HBox()
        entry = Gtk.Entry()
        entry.set_text(self.value)
        entry.connect('changed', self.update)
        self._gui.pack_start(Gtk.Label(self.display_name), False, False, 0)
        self._gui.pack_start(entry, False, False, 0)

    def update(self, entry, _=None):
        self.value = entry.get_text()


class Radio(Element):
    def _build_gui(self):
        self._gui = Gtk.RadioButton(None, self.display_name)


class RadioGroup(CompositeItem):
    def __init__(self, name, display_name, value):
        super().__init__(name, display_name, Radio, value)

    def _build_gui(self):
        self._gui = Gtk.VBox()
        hbox = Gtk.HBox()
        group = None
        for _radio in self.units:
            radio = _radio.get_gui()
            radio.set_group(group)
            group = radio
            if _radio.name == self.value:
                radio.set_active(True)
            radio.connect('toggled', self.update, _radio.name)
            hbox.pack_start(radio, False, False, 0)
        self._gui.pack_start(hbox, False, False, 0)

    def update(self, radio, radio_name):
        if radio.get_active():
            self.value = radio_name


class CheckBox(CompositeItem):
    def _build_gui(self):
        pass

    def update(self, _, __):
        pass


class ComboBox(CompositeItem):
    def _build_gui(self):
        pass

    def update(self, _, __):
        pass
