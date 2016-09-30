import logging
import os
from abc import ABC, abstractmethod

from src.betterconfigparser import BetterConfigParser

logger = logging.getLogger(__name__)


class Saver(ABC):
    def __init__(self, save_path, stencil):
        self.save_path = save_path
        self.stencil = stencil

    def write(self, page=None):
        self._save_es_file()
        if not page:
            for page_ in self.stencil.units:
                self._save_page(page_)
        else:
            self._save_page(page)

    # not used
    def _check_for_esfile(self):
        return os.path.isfile(self.save_path + '/' + '.__es__.ini')

    @abstractmethod
    def _save_es_file(self):
        pass

    @abstractmethod
    def _save_page(self, page):
        pass


class ConfigParserSaver(Saver):
    def _save_es_file(self):
        es_dict = BetterConfigParser()
        es_dict["main"] = {self.stencil.name: self.stencil.display_name}
        es_dict["pages"] = {}
        es_dict["sections"] = {}
        es_dict["items"] = {}
        es_dict["itemtypes"] = {}
        for page in self.stencil.units:
            es_dict["pages"].update({page.name: page.display_name})
            for section in page.units:
                es_dict["sections"].update({section.name: section.display_name})
                for item in section.units:
                    es_dict["items"].update({item.name: item.display_name})
                    es_dict["itemtypes"].update({item.name: type(item).__name__})
        with open(self.save_path + '/' + '.__es__.ini', 'w+') as es_file:
            es_dict.write(es_file)

    def _save_page(self, page):
        save_dict = BetterConfigParser()
        for section in page.units:
            for item in section.units:
                if section.name in save_dict:
                    save_dict[section.name].update({item.name: item.value})
                else:
                    save_dict[section.name] = {item.name: item.value}
        with open(self.save_path + '/' + page.name + '.ini', 'w+') as save_file:
            save_dict.write(save_file)


class JsonSaver(Saver):
    def _save_page(self, page):
        pass

    def _save_es_file(self):
        pass
