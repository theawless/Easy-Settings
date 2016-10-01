import logging
from abc import ABC

from src import ES_FILE_NAME
from src.dictionaryhandler import DictionaryHandler

logger = logging.getLogger(__name__)


class Saver(ABC):
    def __init__(self, save_path, save_style, stencil, decodable):
        self._stencil = stencil
        self.decodable = decodable
        self._dic_handler = DictionaryHandler(save_path, save_style)

    def save(self, page=None):
        if self.decodable:
            self._dic_handler.write_dict(self._make_es_dict(), ES_FILE_NAME)
        if not page:
            for _page in self._stencil.units:
                self._dic_handler.write_dict(self._make_page_save_dict(_page), _page.name)
        else:
            self._dic_handler.write_dict(self._make_es_dict(), page.name)

    def _make_es_dict(self):
        es_dict = {"main": {self._stencil.name: self._stencil.display_name}, "pages": {}, "sections": {}, "items": {},
                   "itemtypes": {}}
        for page in self._stencil.units:
            es_dict["pages"].update({page.name: page.display_name})
            for section in page.units:
                es_dict["sections"].update({section.name: section.display_name})
                for item in section.units:
                    es_dict["items"].update({item.name: item.display_name})
                    es_dict["itemtypes"].update({item.name: type(item).__name__})
        return es_dict

    def _make_page_save_dict(self, page):
        page_save_dict = {}
        for section in page.units:
            page_save_dict[section.name] = {}
            for item in section.units:
                page_save_dict[section.name].update({item.name: item.value})
        return page_save_dict
