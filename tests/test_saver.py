import json
from unittest import TestCase

from src import ES_FILE_NAME
from src.elements import Stencil, Page, Section
from src.items import Entry
from src.listconfigparser import ListConfigParser
from src.saver import Saver
from src.types import SaveStyle
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

        self.save_dict_correct = dict()
        self.save_dict_correct["section1.1"] = {"name": "Easy", "age": '20'}

        self.es_dict_correct = dict()
        self.es_dict_correct["main"] = {"test": "Test"}
        self.es_dict_correct["pages"] = {"page1": "Page 1"}
        self.es_dict_correct["sections"] = {"section1.1": "Section 1.1"}
        self.es_dict_correct["items"] = {"name": "Name:", "age": "Age:"}
        self.es_dict_correct["itemtypes"] = {"name": "Entry", "age": "Entry"}

    def test_cofigparsersaver(self):
        encoder = Saver(PATH, SaveStyle.CONFIGPARSER, self.stencil, True)
        encoder.save()

        save_dict = ListConfigParser()
        save_dict.read(PATH + '/' + 'page1.ini')

        es_dict = ListConfigParser()
        es_dict.read(PATH + '/' + ES_FILE_NAME + '.ini')

        self.assertEqual(self.save_dict_correct, save_dict.config_to_dict())
        self.assertEqual(self.es_dict_correct, es_dict.config_to_dict())

    def test_jsonsaver(self):
        encoder = Saver(PATH, SaveStyle.JSON, self.stencil, True)
        encoder.save()

        with open(PATH + '/' + 'page1.json') as save_file:
            save_dict = json.load(save_file)

        with open(PATH + '/' + ES_FILE_NAME + '.json') as es_file:
            es_dict = json.load(es_file)

        self.assertEqual(save_dict, self.save_dict_correct)
        self.assertEqual(es_dict, self.es_dict_correct)
