import os
from unittest import TestCase

from gi.repository import Gtk

from src.easysettings import EasySettings
from src.elements import Page, Stencil
from src.elements import Section
from src.items import Entry
from src.types import SaveStyle

PATH = os.path.dirname(os.path.abspath(__file__)) + "/ini"

if not os.path.exists(PATH):
    os.makedirs(PATH)


class TestEasySettings(TestCase):
    def test_get_gui(self):
        entry1 = Entry("name", "Name:", "Easy")
        entry2 = Entry("age", "Age:", "20")
        section = Section("section1.1", "Section 1.1")
        section.add_item(entry1)
        section.add_item(entry2)
        page = Page("page1", "Page 1")
        page.add_section(section)
        stencil = Stencil("test", "Test")
        stencil.add_page(page)
        easysettings = EasySettings(PATH, stencil, SaveStyle.CONFIGPARSER)
        gui = easysettings.get_gui()
        gui.show_all()
        gui.connect("delete-event", Gtk.main_quit)
        Gtk.main()
