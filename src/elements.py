import logging
from enum import Enum

logger = logging.getLogger(__name__)


class Element:
    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name


class CompositeElement(Element):
    def __init__(self, name, display_name):
        super().__init__(name, display_name)
        self.units = []

    def _add_unit(self, unit):
        self.units.append(unit)

    def _remove_unit(self, unit):
        self.units.remove(unit)


class StencilType(Enum):
    EMPTY = -1
    SINGLE = 0
    NOTEBOOK = 1
    STACKSWITCHER = 2


class Stencil(CompositeElement):
    def __init__(self, name, display_name, stencil_type=None):
        super().__init__(name, display_name)

        if stencil_type == StencilType.SINGLE.name:
            self.stencil_type = StencilType.SINGLE
        elif stencil_type == StencilType.NOTEBOOK.name:
            self.stencil_type = StencilType.NOTEBOOK
        elif stencil_type == StencilType.STACKSWITCHER.name:
            self.stencil_type = StencilType.STACKSWITCHER
        else:
            self.stencil_type = StencilType.EMPTY

    def add_page(self, page):
        self._add_unit(page)

    def remove_page(self, page):
        self._remove_unit(page)


class Page(CompositeElement):
    def add_section(self, section):
        self._add_unit(section)

    def remove_section(self, section):
        self._remove_unit(section)


class Section(CompositeElement):
    def add_item(self, item):
        self._add_unit(item)

    def remove_item(self, item):
        self._remove_unit(item)


class ItemType(Enum):
    ENTRY = 0
    RADIOGROUP = 1
    CHECKBOX = 2
    COMBOBOX = 3


class Entry(Element):
    pass


class RadioGroup(CompositeElement):
    pass


class CheckBox(CompositeElement):
    pass


class ComboBox(CompositeElement):
    pass
