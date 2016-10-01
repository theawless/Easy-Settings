import logging
from abc import ABC

from src.dictionaryhandler import DictionaryHandler

logger = logging.getLogger(__name__)


class Loader(ABC):
    def __init__(self, save_path, save_style, stencil):
        self.stencil = stencil
        self._dic_handler = DictionaryHandler(save_path, save_style)

    def _update_stencil(self, page, page_save_dict):
        for section in page.units:
            for item in section.units:
                item.value = page_save_dict[section.name][item.name]

    def load(self, page=None):
        if not page:
            for _page in self.stencil.units:
                self._update_stencil(_page, self._dic_handler.read_dict(_page.name))
        else:
            self._update_stencil(page, self._dic_handler.read_dict(page.name))
