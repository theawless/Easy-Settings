from unittest import TestCase

from src.elements import Stencil, Page, Section
from src.items import Entry
from src.listconfigparser import ListConfigParser
from src.saver import ConfigParserSaver
from tests import PATH


class TestSaver(TestCase):
    def setUp(self):
        entry1 = Entry("name", "Name:", "Easy")
        entry2 = Entry("age", "Age:", "20")
        section = Section("section1.1", "Section 1.1")
        section.add_item(entry1)
        section.add_item(entry2)
        page = Page("page1", "Page 1")
        page.add_section(section)
        self.stencil = Stencil("test", "Test")
        self.stencil.add_page(page)

    def test_cofigparsersaver(self):
        encoder = ConfigParserSaver(PATH, self.stencil)
        encoder.write()

        save_dict = ListConfigParser()
        save_dict.read(PATH + '/' + 'page1.ini')
        save_dict_correct = ListConfigParser()
        save_dict_correct["section1.1"] = {"name": "Easy", "age": 20}

        save__dict = ListConfigParser()
        save__dict.read(PATH + '/' + '.__es__.ini')
        save__dict_correct = ListConfigParser()
        save__dict_correct["main"] = {"test": "Test"}
        save__dict_correct["pages"] = {"page1": "Page 1"}
        save__dict_correct["sections"] = {"section1.1": "Section 1.1"}
        save__dict_correct["items"] = {"name": "Name:", "age": "Age:"}
        save__dict_correct["itemtypes"] = {"name": "Entry", "age": "Entry"}

        self.assertEqual(save_dict.config_to_dict(), save_dict_correct.config_to_dict(), "")
        self.assertEqual(save__dict_correct.config_to_dict(), save__dict.config_to_dict(), "")

    def test_jsonsaver(self):
        self.fail()
