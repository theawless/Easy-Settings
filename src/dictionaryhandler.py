import json
import os

from src.listconfigparser import ListConfigParser
from src.types import SaveStyle


class DictionaryHandler:
    def __init__(self, save_path, save_style):
        self.save_style = save_style
        self.save_path = save_path

    @staticmethod
    def check_for_file(save_path, name, ext):
        if not os.path.isfile(save_path + '/' + name + ext):
            raise FileNotFoundError("Not decodable! es-file not found.")

    def write_dict(self, dic, name):
        if self.save_style == SaveStyle.CONFIGPARSER:
            with open(self.save_path + '/' + name + '.ini', 'w+') as save_file:
                ListConfigParser(dic).write(save_file)
        elif self.save_style == SaveStyle.JSON:
            with open(self.save_path + '/' + name + '.json', 'w+') as save_file:
                json.dump(dic, save_file, indent=4)

    def read_dict(self, name):
        if self.save_style == SaveStyle.CONFIGPARSER:
            self.check_for_file(self.save_path, name, ".ini")
            dic = ListConfigParser()
            dic.read(self.save_path + '/' + name + '.ini')
            return dic.config_to_dict()
        elif self.save_style == SaveStyle.JSON:
            self.check_for_file(self.save_path, name, ".json")
            with open(self.save_path + '/' + name + '.json') as save_file:
                dic = json.load(save_file)
            return dic
