import logging
from abc import ABC, abstractmethod

from src.listconfigparser import ListConfigParser

logger = logging.getLogger(__name__)


class Loader(ABC):
    def __init__(self, save_path, stencil):
        self.save_path = save_path
        self.stencil = stencil

    def read(self, page=None):
        if not page:
            for page_ in self.stencil.units:
                self._load_page(page_)
        else:
            self._load_page(page)

    @abstractmethod
    def _load_page(self, page):
        pass


class ConfigParserLoader(Loader):
    def _load_page(self, page):
        for page in self.stencil.units:
            save_dict = ListConfigParser()
            save_dict.read(self.save_path + '/' + page.name + '.ini')
            for section in page.units:
                for item in section.units:
                    item.value = save_dict[section.name][item.name]


class JsonLoader(Loader):
    def _load_page(self, page):
        pass
