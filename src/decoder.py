import importlib
import logging
from abc import ABC, abstractmethod

from src.elements import Stencil, Page, Section
from src.listconfigparser import ListConfigParser

logger = logging.getLogger(__name__)


class Decoder(ABC):
    def __init__(self, save_path):
        self.save_path = save_path

    @abstractmethod
    def decode_savefile(self):
        pass


class ConfigParserDecoder(Decoder):
    def decode_savefile(self):
        save__dict = ListConfigParser()
        save__dict.read(self.save_path + '/.__es__.ini')
        name, display_name = next(iter(save__dict["main"].items()))
        stencil = Stencil(name, display_name)
        for name, display_name in save__dict["pages"].items():
            page = Page(name, display_name)
            save_dict = ListConfigParser()
            save_dict.read(self.save_path + '/' + name + '.ini')
            for section_name in save_dict.sections():
                section = Section(section_name, save__dict["sections"][section_name])
                for item_name, item_val in save_dict[section_name].items():
                    item_type = save__dict["itemtypes"][item_name]
                    item_class = getattr(importlib.import_module("src.items"), item_type)

                    item = item_class(item_name, save__dict["items"][item_name], item_val)
                    section.add_item(item)
                page.add_section(section)
            stencil.add_page(page)
        return stencil


class JsonDecoder(Decoder):
    def decode_savefile(self):
        pass
