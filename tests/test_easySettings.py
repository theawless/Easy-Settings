from unittest import TestCase

from gi.repository import Gtk

from src.easysettings import EasySettings
from tests import *


class TestEasySettings(TestCase):
    def test_get_gui(self):
        easysettings = EasySettings(PATH, get_stencil())
        easysettings.load_settings()
        gui = easysettings.get_gui()
        gui.connect("delete-event", Gtk.main_quit)
        gui.show_all()
        Gtk.main()
