from src import *
from src.dictionaryhandler import DictionaryHandler
from src.items import CompositeItem

logger = logging.getLogger(__name__)


class Saver:
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
        es_dict = {ES_FILE_MAIN: {self._stencil.name: self._stencil.display_name}, ES_FILE_PAGES: {},
                   ES_FILE_ITEM_TYPES: {}}
        for page in self._stencil.units:
            es_dict[ES_FILE_PAGES].update({page.name: page.display_name})
            es_dict[page.name] = {}
            for section in page.units:
                es_dict[page.name].update({section.name: section.display_name})
                es_dict[section.name] = {}
                for item in section.units:
                    es_dict[section.name].update({item.name: item.display_name})
                    es_dict[ES_FILE_ITEM_TYPES].update({item.name: type(item).__name__})
                    if isinstance(item, CompositeItem):
                        es_dict[item.name] = {}
                        for subitem in item.units:
                            es_dict[item.name].update({subitem.name: subitem.display_name})

        return es_dict

    def _make_page_save_dict(self, page):
        page_save_dict = {}
        for section in page.units:
            page_save_dict[section.name] = {}
            for item in section.units:
                page_save_dict[section.name].update({item.name: item.value})
        return page_save_dict
