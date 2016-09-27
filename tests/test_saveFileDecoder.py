import os
from unittest import TestCase

from src.betterconfigparser import BetterConfigParser
from src.elements import Entry, Section, Page, Stencil, CompositeElement, Valued
from src.savefiledecoder import ConfigParserDecoder

PATH = os.path.dirname(os.path.abspath(__file__))


class TestSaveFileDecoders(TestCase):
    def setUp(self):
        save__dict = BetterConfigParser()
        save__dict["main"] = {"test": "Test"}
        save__dict["pages"] = {"page1": "Page 1"}
        save__dict["sections"] = {"section1.1": "Section 1.1"}
        save__dict["items"] = {"name": "Name:", "age": "Age:"}
        with open(PATH + '/' + '.__es__.ini', 'w+') as save__file:
            save__dict.write(save__file)

        save_dict = BetterConfigParser()
        save_dict["section1.1"] = {"name": "Easy", "age": "20"}
        with open(PATH + '/' + 'page1.ini', 'w+') as save_file:
            save_dict.write(save_file)

    def assertUnitEqual(self, s1, s2):
        self.assertEqual(s1.name, s2.name)
        self.assertEqual(s1.display_name, s2.display_name)
        if isinstance(s2, Valued):
            self.assertEqual(s1.value, s2.value)
        if isinstance(s2, CompositeElement):
            self.assertEqual(len(s1.units), len(s2.units))
            for (unit1, unit2) in zip(s1.units, s2.units):
                self.assertUnitEqual(unit1, unit2)

    def test_configparserdecoder(self):
        decoder = ConfigParserDecoder(PATH)
        stencil = decoder.read()

        entry1 = Entry("name", "Name:", "Easy")
        entry2 = Entry("age", "Age:", "20")
        section = Section("section1.1", "Section 1.1")
        section.add_item(entry1)
        section.add_item(entry2)
        page = Page("page1", "Page 1")
        page.add_section(section)
        stencil_correct = Stencil("test", "Test")
        stencil_correct.add_page(page)

        self.assertUnitEqual(stencil, stencil_correct)

    def test_jsondecoder(self):
        self.fail()
