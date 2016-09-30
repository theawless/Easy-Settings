import logging
from abc import ABC, abstractmethod

import sys

from src.betterconfigparser import BetterConfigParser
from src.elements import Stencil, Page, Section

logger = logging.getLogger(__name__)


class SaveFileDecoder(ABC):
    def __init__(self, save_path):
        self.save__dict = None
        self.save_path = save_path

    @abstractmethod
    def decode_savefile(self):
        pass

    @abstractmethod
    def read(self):
        pass


class ConfigParserDecoder(SaveFileDecoder):
    def read(self):
        self.save__dict = BetterConfigParser()
        return self.decode_savefile()

    def decode_savefile(self):
        save__dict = BetterConfigParser()
        save__dict.read(self.save_path + '/.__es__.ini')
        name, display_name = next(iter(save__dict["main"].items()))
        stencil = Stencil(name, display_name)
        for name, display_name in save__dict["pages"].items():
            page = Page(name, display_name)
            save_dict = BetterConfigParser()
            save_dict.read(self.save_path + '/' + name + '.ini')
            for section_name in save_dict.sections():
                section = Section(section_name, save__dict["sections"][section_name])
                for item_name, item_val in save_dict[section_name].items():
                    item_type = save__dict["itemtypes"][item_name]
                    item_class = getattr(sys.modules[__name__], item_type)
                    item = item_class(item_name, save__dict["items"][item_name], item_val)
                    section.add_item(item)
                page.add_section(section)
            stencil.add_page(page)
        return stencil


class JsonDecoder(SaveFileDecoder):
    def read(self):
        self.save__dict = []
        self.decode_savefile()

    def decode_savefile(self):
        pass
