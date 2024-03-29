import configparser
import logging

logger = logging.getLogger(__name__)

LIST_DELIMITER = " , "


# implement using CSV
class ListConfigParser(configparser.ConfigParser):
    def __init__(self, dic=None):
        super().__init__()
        if dic:
            self._dict_to_config(dic)

    def save_list(self, section, option, seq):
        string = LIST_DELIMITER.join(map(str, seq))
        self[section][option] = string

    def get_list(self, section, option):
        seq = self[section][option].split(LIST_DELIMITER)
        return seq

    def config_to_dict(self):
        settings_dictionary = {}
        for sect in self.sections():
            settings_dictionary[sect] = {}
            for opt in self.options(sect):
                settings_dictionary[sect][opt] = self.get(sect, opt)
        return settings_dictionary

    def _dict_to_config(self, dic):
        for section in dic:
            self.add_section(section)
            for item in dic[section]:
                self[section].update({item: dic[section][item]})
