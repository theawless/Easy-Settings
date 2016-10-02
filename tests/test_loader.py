import json
from unittest import TestCase

from src.listconfigparser import ListConfigParser
from src.loader import Loader
from src.types import SaveStyle
from tests import *


class TestLoader(TestCase):
    def test_configparserloader(self):
        save_dict1, save_dict2 = get_page_dictionaries(True)
        with open(PATH + '/' + 'page1.ini', 'w+') as save_file:
            ListConfigParser(save_dict1).write(save_file)
        with open(PATH + '/' + 'page2.ini', 'w+') as save_file:
            ListConfigParser(save_dict2).write(save_file)

        stencil = get_stencil(False)
        loader = Loader(PATH, SaveStyle.CONFIGPARSER, stencil)
        loader.load()

        assert_unit_equal(self, get_stencil(True), stencil)

    def test_jsonloader(self):
        save_dict1, save_dict2 = get_page_dictionaries(True)
        with open(PATH + '/' + 'page1.json', 'w+') as save_file:
            json.dump(save_dict1, save_file)
        with open(PATH + '/' + 'page2.json', 'w+') as save_file:
            json.dump(save_dict2, save_file)

        stencil = get_stencil(False)
        loader = Loader(PATH, SaveStyle.JSON, stencil)
        loader.load()

        assert_unit_equal(self, get_stencil(True), stencil)
