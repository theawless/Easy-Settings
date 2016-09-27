from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class SaveFileDecoder(ABC):
    def __init__(self, save_path):
        self.conf_dict = None
        self.save_path = save_path

    @abstractmethod
    def decode__savefile(self):
        pass

    @abstractmethod
    def decode_savefile(self):
        pass


class JsonDecoder(SaveFileDecoder):
    def decode__savefile(self):
        pass

    def decode_savefile(self):
        pass


class ConfigParserDecoder(SaveFileDecoder):
    def decode__savefile(self):
        pass

    def decode_savefile(self):
        pass
