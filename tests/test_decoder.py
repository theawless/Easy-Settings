from unittest import TestCase

from src.decoder import ConfigParserDecoder
from src.elements import Section, Page, Stencil
from src.items import Entry
from src.listconfigparser import ListConfigParser
from tests import assert_unit_equal, PATH


class TestSaveFileDecoders(TestCase):
    def setUp(self):
        save__dict = ListConfigParser()
        save__dict["main"] = {"test": "Test"}
        save__dict["pages"] = {"page1": "Page 1"}
        save__dict["sections"] = {"section1.1": "Section 1.1"}
        save__dict["items"] = {"name": "Name:", "age": "Age:"}
        save__dict["itemtypes"] = {"name": "Entry", "age": "Entry"}

        with open(PATH + '/' + '.__es__.ini', 'w+') as save__file:
            save__dict.write(save__file)

        save_dict = ListConfigParser()
        save_dict["section1.1"] = {"name": "Easy", "age": "20"}
        with open(PATH + '/' + 'page1.ini', 'w+') as save_file:
            save_dict.write(save_file)

    def test_configparserdecoder(self):
        decoder = ConfigParserDecoder(PATH)
        stencil = decoder.decode_savefile()

        entry1 = Entry("name", "Name:", "Easy")
        entry2 = Entry("age", "Age:", "20")
        section = Section("section1.1", "Section 1.1")
        section.add_item(entry1)
        section.add_item(entry2)
        page = Page("page1", "Page 1")
        page.add_section(section)
        stencil_correct = Stencil("test", "Test")
        stencil_correct.add_page(page)

        assert_unit_equal(self, stencil_correct, stencil)

    def test_jsondecoder(self):
        self.fail()
