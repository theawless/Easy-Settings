import logging
from abc import ABC, abstractmethod

from src.betterconfigparser import BetterConfigParser

logger = logging.getLogger(__name__)


class SaveFileEncoder(ABC):
    def __init__(self, save_path, stencil):
        self.save__dict = None
        self.save_path = save_path
        self.stencil = stencil

    @abstractmethod
    def encode_savefile(self):
        pass

    @abstractmethod
    def write(self):
        pass


class ConfigParserEncoder(SaveFileEncoder):
    def write(self):
        self.save__dict = BetterConfigParser()
        self.encode_savefile()

    def encode_savefile(self):
        save__dict = BetterConfigParser()
        save__dict["main"] = {self.stencil.name: self.stencil.display_name}
        save__dict["pages"] = {}
        save__dict["sections"] = {}
        save__dict["items"] = {}
        for page in self.stencil.units:
            save_dict = BetterConfigParser()
            save__dict["pages"].update({page.name: page.display_name})
            for section in page.units:
                save__dict["sections"].update({section.name: section.display_name})
                for item in section.units:
                    save__dict["items"].update({item.name: item.display_name})
                    if section.name in save_dict:
                        save_dict[section.name].update({item.name: item.value})
                    else:
                        save_dict[section.name] = {item.name: item.value}
            with open(self.save_path + '/' + page.name + '.ini', 'w+') as save_file:
                save_dict.write(save_file)
        with open(self.save_path + '/' + '.__es__.ini', 'w+') as save__file:
            save__dict.write(save__file)


class JsonEncoder(SaveFileEncoder):
    def write(self):
        self.save__dict = []
        self.encode_savefile()

    def encode_savefile(self):
        pass
