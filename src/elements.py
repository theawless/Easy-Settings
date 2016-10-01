import logging
from abc import abstractmethod, ABCMeta, ABC

from gi.repository import Gtk

from src.types import StencilType

logger = logging.getLogger(__name__)


class Guied(ABC):
    def __init__(self):
        self._is_dirty = True
        self._gui = None

    def get_gui(self):
        if self._is_dirty:
            self._build_gui()
            self._is_dirty = False
        return self._gui

    @abstractmethod
    def _build_gui(self):
        pass


class Element(Guied, metaclass=ABCMeta):
    def __init__(self, name, display_name):
        super().__init__()
        self.name = name
        self.display_name = display_name


class CompositeElement(Element, metaclass=ABCMeta):
    def __init__(self, name, display_name):
        super().__init__(name, display_name)
        self.units = []

    def _add_unit(self, unit):
        self._is_dirty = True
        self.units.append(unit)

    def _remove_unit(self, unit):
        self._is_dirty = True
        self.units.remove(unit)


class Stencil(CompositeElement):
    def __init__(self, name, display_name, stencil_type=StencilType.EMPTY):
        super().__init__(name, display_name)
        self.stencil_type = stencil_type
        self.expected_stencil_type = stencil_type

    def get_gui(self):
        if self.stencil_type == StencilType.SINGLE:
            return self.get_page_gui(self.units[0])
        else:
            super().get_gui()

    def get_page_gui(self, page):
        return page.get_gui()

    def _build_gui(self):
        self._gui = Gtk.VBox()
        if self.stencil_type == StencilType.STACKSWITCHER:
            stack = Gtk.Stack()
            for page in self.units:
                stack.add_titled(page.get_gui(), page.name, page.display_name)
            stack_switcher = Gtk.StackSwitcher()
            stack_switcher.set_stack(stack)
            self._gui.pack_start(stack_switcher, False, False, 0)
            self._gui.pack_start(stack, False, False, 0)
        elif self.stencil_type == StencilType.NOTEBOOK:
            notebook = Gtk.Notebook()
            for page in self.units:
                notebook.append_page(page.get_gui(), Gtk.Label(page.display_name))
            self._gui.pack_start(notebook, False, False, 0)

    def add_page(self, page):
        self._add_unit(page)
        self._fix_stencil_type()

    def remove_page(self, page):
        self._remove_unit(page)
        self._fix_stencil_type()

    def _fix_stencil_type(self):
        if len(self.units) == 1:
            self.stencil_type = StencilType.SINGLE
        elif len(self.units) == 0:
            self.stencil_type = StencilType.EMPTY
        elif len(self.units) > 1 and (
                        self.stencil_type is StencilType.EMPTY or self.stencil_type == StencilType.SINGLE):
            if self.expected_stencil_type == StencilType.EMPTY or self.expected_stencil_type == StencilType.SINGLE:
                self.stencil_type = StencilType.STACKSWITCHER
            else:
                self.stencil_type = self.expected_stencil_type

    def update(self):
        for page in self.units:
            for section in page.units:
                for item in section.units:
                    item.update()


class Page(CompositeElement):
    def _build_gui(self):
        self._gui = Gtk.VBox()
        for section in self.units:
            self._gui.pack_start(section.get_gui(), False, False, 0)

    def add_section(self, section):
        self._add_unit(section)

    def remove_section(self, section):
        self._remove_unit(section)


class Section(CompositeElement):
    def _build_gui(self):
        self._gui = Gtk.VBox()
        for item in self.units:
            self._gui.pack_start(item.get_gui(), False, False, 0)

    def add_item(self, item):
        self._add_unit(item)

    def remove_item(self, item):
        self._remove_unit(item)
