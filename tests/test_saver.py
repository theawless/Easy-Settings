import json
from unittest import TestCase

from src import ES_FILE_NAME
from src.listconfigparser import ListConfigParser
from src.saver import Saver
from src.types import SaveStyle
from tests import *


class TestSaver(TestCase):
    def test_configparsersaver(self):
        encoder = Saver(PATH, SaveStyle.CONFIGPARSER, get_stencil(), True)
        encoder.save()

        save_dict1 = ListConfigParser()
        save_dict1.read(PATH + '/' + 'page1.ini')
        save_dict2 = ListConfigParser()
        save_dict2.read(PATH + '/' + 'page2.ini')

        es_dict = ListConfigParser()
        es_dict.read(PATH + '/' + ES_FILE_NAME + '.ini')

        save_dict1_correct, save_dict2_correct = get_page_dictionaries()
        es_dict_correct = get_es_dictionary()
        self.assertEqual(save_dict1_correct, save_dict1.config_to_dict())
        self.assertEqual(save_dict2_correct, save_dict2.config_to_dict())
        self.assertEqual(es_dict_correct, es_dict.config_to_dict())

    def test_jsonsaver(self):
        encoder = Saver(PATH, SaveStyle.JSON, get_stencil(), True)
        encoder.save()

        with open(PATH + '/' + 'page1.json') as save_file:
            save_dict1 = json.load(save_file)
        with open(PATH + '/' + 'page2.json') as save_file:
            save_dict2 = json.load(save_file)

        with open(PATH + '/' + ES_FILE_NAME + '.json') as es_file:
            es_dict = json.load(es_file)

        save_dict1_correct, save_dict2_correct = get_page_dictionaries()
        es_dict_correct = get_es_dictionary()
        self.assertEqual(save_dict1_correct, save_dict1)
        self.assertEqual(save_dict2_correct, save_dict2)
        self.assertEqual(es_dict_correct, es_dict)
