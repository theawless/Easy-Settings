from unittest import TestCase

from src.listconfigparser import ListConfigParser


class TestListConfigParser(TestCase):
    def setUp(self):
        self.lis = ["what", "is", "this", "?"]
        self.dic = {"sec1": {"opt1.1": "val1.1", "opt1.2": "val1.2"}, "sec2": {"opt2.1": "val2.1", "opt2.2": "val2.2"}}

    def _build_config(self):
        config = ListConfigParser()
        config["sec1"] = {"opt1.1": "val1.1", "opt1.2": "val1.2"}
        config["sec2"] = {"opt2.1": "val2.1", "opt2.2": "val2.2"}
        return config

    def test_save_list(self):
        config = self._build_config()
        config.save_list("sec2", "opt2.3", self.lis)
        self.assertEqual(config["sec2"]["opt2.3"], "what , is , this , ?")

    def test_get_list(self):
        config = self._build_config()
        config["sec2"]["opt2.3"] = "what , is , this , ?"
        lis = config.get_list("sec2", "opt2.3")
        self.assertEqual(self.lis, lis)

    def test_config_to_dict(self):
        config = self._build_config()
        self.assertEqual(self.dic, config.config_to_dict())

    def test_dict_to_config(self):
        config = ListConfigParser(self.dic)
        self.assertEqual(self.dic, config.config_to_dict())
