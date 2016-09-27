from abc import ABC, abstractmethod
import logging

from src.betterconfigparser import BetterConfigParser
from src.elements import Stencil, Section, Entry, Page

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
        save__file = BetterConfigParser()
        save__file.read(self.save_path + '/.__es__.ini')
        print(save__file["main"])
        name, display_name = save__file["main"][0]
        stencil = Stencil(name, display_name)
        for _page in save__file["pages"]:
            page = Page(_page.key, _page.value)
            stencil.add_page(page)
        return stencil


class JsonDecoder(SaveFileDecoder):
    def read(self):
        self.save__dict = []
        self.decode_savefile()

    def decode_savefile(self):
        pass
