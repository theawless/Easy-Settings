from unittest import TestCase

from src.elements import Stencil, Page, Section
from src.items import Entry
from src.loader import ConfigParserLoader
from src.saver import ConfigParserSaver
from tests.helper import PATH, assert_unit_equal


class TestSaver(TestCase):
    def setUp(self):
        self.stencil = self._build_stencil()
        encoder = ConfigParserSaver(PATH, self.stencil)
        encoder.write()

    def _build_stencil(self, old=False):
        if not old:
            entry1 = Entry("name", "Name:", "newEasy")
            entry2 = Entry("age", "Age:", "new20")
        else:
            entry1 = Entry("name", "Name:", "Easy")
            entry2 = Entry("age", "Age:", "20")
        section = Section("section1.1", "Section 1.1")
        section.add_item(entry1)
        section.add_item(entry2)
        page = Page("page1", "Page 1")
        page.add_section(section)
        stencil = Stencil("test", "Test")
        stencil.add_page(page)
        return stencil

    def test_configparserloader(self):
        stencil_old = self._build_stencil(old=True)
        loader = ConfigParserLoader(PATH, stencil_old)
        loader.read()

        assert_unit_equal(self, self.stencil, stencil_old)

    def test_jsonloader(self):
        self.fail()
