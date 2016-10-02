import json
from unittest import TestCase

from src import ES_FILE_NAME
from src.decoder import Decoder
from src.listconfigparser import ListConfigParser
from tests import *


class TestSaveFileDecoders(TestCase):
    def test_configparserdecoder(self):
        with open(PATH + '/' + ES_FILE_NAME + '.ini', 'w+') as es_file:
            ListConfigParser(get_es_dictionary()).write(es_file)

        decoder = Decoder(PATH)
        stencil = decoder.decode(False)

        assert_unit_equal(self, get_stencil(is_empty=True), stencil)

    def test_jsondecoder(self):
        with open(PATH + '/' + ES_FILE_NAME + '.json', 'w+') as es_file:
            json.dump(get_es_dictionary(), es_file)

        decoder = Decoder(PATH)
        stencil = decoder.decode(False)

        assert_unit_equal(self, get_stencil(is_empty=True), stencil)
