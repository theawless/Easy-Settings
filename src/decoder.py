import importlib
import logging

from src import ES_FILE_NAME
from src.dictionaryhandler import DictionaryHandler
from src.elements import Stencil, Page, Section
from src.loader import Loader
from src.types import SaveStyle

logger = logging.getLogger(__name__)


class Decoder:
    def __init__(self, save_path):
        self.save_path = save_path
        self._dict_handler = None
        self.save_style = None

    def get_save_style(self):
        try:
            DictionaryHandler.check_for_file(self.save_path, ES_FILE_NAME, '.ini')
            self.save_style = SaveStyle.CONFIGPARSER
            self._dict_handler = DictionaryHandler(self.save_path, self.save_style)
        except FileNotFoundError:
            try:
                self._dict_handler.check_for_file(self.save_path, ES_FILE_NAME, '.json')
                self.save_style = SaveStyle.JSON
                self._dict_handler = DictionaryHandler(self.save_path, self.save_style)
            except FileNotFoundError:
                raise

    def _make_stencil(self, es_dict):
        stecil_name, stencil_display_name = next(iter(es_dict["main"].items()))
        stencil = Stencil(stecil_name, stencil_display_name)
        for page_name in es_dict["pages"]:
            page = Page(page_name, es_dict["pages"][page_name])
            for section_name in es_dict["sections"]:
                section = Section(section_name, es_dict["sections"][section_name])
                for item_name in es_dict["items"]:
                    item_type = es_dict["itemtypes"][item_name]
                    item_class = getattr(importlib.import_module("src.items"), item_type)
                    item = item_class(item_name, es_dict["items"][item_name])
                    section.add_item(item)
                page.add_section(section)
            stencil.add_page(page)
        return stencil

    def decode(self):
        if not self._dict_handler:
            self.get_save_style()
        stencil = self._make_stencil(self._dict_handler.read_dict(ES_FILE_NAME))
        loader = Loader(self.save_path, SaveStyle.CONFIGPARSER, stencil)
        loader.load()
        return stencil
