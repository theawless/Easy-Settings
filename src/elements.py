import logging

from src.types import StencilType

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


class Stencil(CompositeElement):
    def __init__(self, name, display_name, stencil_type=None):
        super().__init__(name, display_name)
        self.stencil_type = stencil_type or StencilType.EMPTY

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


class Valued:
    def __init__(self, value=None):
        self.value = value


class CompositeItem(CompositeElement, Valued):
    def __init__(self, name, display_name, value=None):
        CompositeElement.__init__(self, name, display_name)
        Valued.__init__(self, value)


class Item(Element, Valued):
    def __init__(self, name, display_name, value=None):
        Element.__init__(self, name, display_name)
        Valued.__init__(self, value)


class Entry(Item):
    pass


class RadioGroup(CompositeItem):
    pass


class CheckBox(CompositeItem):
    pass


class ComboBox(CompositeItem):
    pass
