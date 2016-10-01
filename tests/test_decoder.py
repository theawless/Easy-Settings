import json
from unittest import TestCase

from src import ES_FILE_NAME
from src.decoder import Decoder
from src.elements import Section, Page, Stencil
from src.items import Entry
from src.listconfigparser import ListConfigParser
from tests import assert_unit_equal, PATH


class TestSaveFileDecoders(TestCase):
    def setUp(self):
        entry1 = Entry("name", "Name:", "Easy")
        entry2 = Entry("age", "Age:", "20")
        section = Section("section1.1", "Section 1.1")
        section.add_item(entry1)
        section.add_item(entry2)
        page = Page("page1", "Page 1")
        page.add_section(section)
        self.stencil_correct = Stencil("test", "Test")
        self.stencil_correct.add_page(page)

    def test_configparserdecoder(self):
        es_dict = ListConfigParser()
        es_dict["main"] = {"test": "Test"}
        es_dict["pages"] = {"page1": "Page 1"}
        es_dict["sections"] = {"section1.1": "Section 1.1"}
        es_dict["items"] = {"name": "Name:", "age": "Age:"}
        es_dict["itemtypes"] = {"name": "Entry", "age": "Entry"}

        with open(PATH + '/' + ES_FILE_NAME + '.ini', 'w+') as save__file:
            es_dict.write(save__file)

        save_dict = ListConfigParser()
        save_dict["section1.1"] = {"name": "Easy", "age": "20"}
        with open(PATH + '/' + 'page1.ini', 'w+') as save_file:
            save_dict.write(save_file)

        decoder = Decoder(PATH)
        stencil = decoder.decode()

        assert_unit_equal(self, self.stencil_correct, stencil)

    def test_jsondecoder(self):
        es_dict = {"main": {"test": "Test"}, "pages": {"page1": "Page 1"}, "sections": {"section1.1": "Section 1.1"},
                   "items": {"name": "Name:", "age": "Age:"}, "itemtypes": {"name": "Entry", "age": "Entry"}}

        with open(PATH + '/' + ES_FILE_NAME + '.json', 'w+') as es_file:
            json.dump(es_dict, es_file)

        save_dict = {"section1.1": {"name": "Easy", "age": "20"}}
        with open(PATH + '/' + 'page1.json', 'w+') as save_file:
            json.dump(save_dict, save_file)

        decoder = Decoder(PATH)
        stencil = decoder.decode()

        assert_unit_equal(self, self.stencil_correct, stencil)
