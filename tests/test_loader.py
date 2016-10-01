import json
from unittest import TestCase

from src.elements import Stencil, Page, Section
from src.items import Entry
from src.listconfigparser import ListConfigParser
from src.loader import Loader
from src.types import SaveStyle
from tests import PATH, assert_unit_equal


class TestLoader(TestCase):
    def setUp(self):
        self.stencil_correct = self._build_stencil(old=False)

    def _build_stencil(self, old):
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
        save_dict = ListConfigParser()
        save_dict["section1.1"] = {"name": "newEasy", "age": "new20"}
        with open(PATH + '/' + 'page1.ini', 'w+') as save_file:
            save_dict.write(save_file)

        stencil = self._build_stencil(old=True)
        loader = Loader(PATH, SaveStyle.CONFIGPARSER, stencil)
        loader.load()

        assert_unit_equal(self, self.stencil_correct, stencil)

    def test_jsonloader(self):
        save_dict = {"section1.1": {"name": "newEasy", "age": "new20"}}
        with open(PATH + '/' + 'page1.json', 'w+') as save_file:
            json.dump(save_dict, save_file)

        stencil = self._build_stencil(old=True)
        loader = Loader(PATH, SaveStyle.JSON, stencil)
        loader.load()

        assert_unit_equal(self, self.stencil_correct, stencil)
