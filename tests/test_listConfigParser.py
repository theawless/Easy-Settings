from unittest import TestCase

from src.listconfigparser import ListConfigParser


class TestListConfigParser(TestCase):
    def setUp(self):
        self.lis = ["what", "is", "this", "?"]

    def _build_config(self):
        self.config = ListConfigParser()
        self.config["sec1"] = {"opt1.1": "val1.1", "opt1.2": "val1.2"}
        self.config["sec2"] = {"opt2.1": "val2.1", "opt2.2": "val2.2"}

    def test_save_list(self):
        self._build_config()
        self.config.save_list("sec2", "opt2.3", self.lis)
        self.assertEqual(self.config["sec2"]["opt2.3"], "what , is , this , ?")

    def test_get_list(self):
        self._build_config()
        self.config["sec2"]["opt2.3"] = "what , is , this , ?"
        lis = self.config.get_list("sec2", "opt2.3")
        self.assertEqual(self.lis, lis)
