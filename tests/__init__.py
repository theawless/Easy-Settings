import os
from operator import attrgetter

from src.elements import CompositeElement, Stencil, Page, Section
from src.items import Valued, Entry

PATH = os.path.dirname(os.path.abspath(__file__)) + "/ini"

if not os.path.exists(PATH):
    os.makedirs(PATH)


def assert_unit_equal(test, s1, s2):
    test.assertEqual(s1.name, s2.name)
    test.assertEqual(s1.display_name, s2.display_name)
    if isinstance(s2, Valued):
        test.assertEqual(s1.value, s2.value)
    if isinstance(s2, CompositeElement):
        test.assertEqual(len(s1.units), len(s2.units))
        for unit1, unit2 in zip(sorted(s1.units, key=attrgetter('name')), sorted(s2.units, key=attrgetter('name'))):
            assert_unit_equal(test, unit1, unit2)


def get_stencil(is_new=False, is_empty=False):
    stencil = Stencil("stencil", "Stencil")
    page1 = Page("page1", "Page 1")
    page2 = Page("page2", "Page 2")
    section11 = Section("section1.1", "Section 1.1")
    section12 = Section("section1.2", "Section 1.2")
    section21 = Section("section2.1", "Section 2.1")
    section22 = Section("section2.2", "Section 2.2")
    if is_empty:
        entry111 = Entry("entry1.1.1", "Entry 1.1.1")
        entry112 = Entry("entry1.1.2", "Entry 1.1.2")
        entry121 = Entry("entry1.2.1", "Entry 1.2.1")
        entry122 = Entry("entry1.2.2", "Entry 1.2.2")
        entry211 = Entry("entry2.1.1", "Entry 2.1.1")
        entry212 = Entry("entry2.1.2", "Entry 2.1.2")
        entry221 = Entry("entry2.2.1", "Entry 2.2.1")
        entry222 = Entry("entry2.2.2", "Entry 2.2.2")
    else:
        if not is_new:
            entry111 = Entry("entry1.1.1", "Entry 1.1.1", "1.1.1")
            entry112 = Entry("entry1.1.2", "Entry 1.1.2", "1.1.2")
            entry121 = Entry("entry1.2.1", "Entry 1.2.1", "1.2.1")
            entry122 = Entry("entry1.2.2", "Entry 1.2.2", "1.2.2")
            entry211 = Entry("entry2.1.1", "Entry 2.1.1", "2.1.1")
            entry212 = Entry("entry2.1.2", "Entry 2.1.2", "2.1.2")
            entry221 = Entry("entry2.2.1", "Entry 2.2.1", "2.2.1")
            entry222 = Entry("entry2.2.2", "Entry 2.2.2", "2.2.2")
        else:
            entry111 = Entry("entry1.1.1", "Entry 1.1.1", "new1.1.1")
            entry112 = Entry("entry1.1.2", "Entry 1.1.2", "new1.1.2")
            entry121 = Entry("entry1.2.1", "Entry 1.2.1", "new1.2.1")
            entry122 = Entry("entry1.2.2", "Entry 1.2.2", "new1.2.2")
            entry211 = Entry("entry2.1.1", "Entry 2.1.1", "new2.1.1")
            entry212 = Entry("entry2.1.2", "Entry 2.1.2", "new2.1.2")
            entry221 = Entry("entry2.2.1", "Entry 2.2.1", "new2.2.1")
            entry222 = Entry("entry2.2.2", "Entry 2.2.2", "new2.2.2")
    section11.add_items(entry111, entry112)
    section12.add_items(entry121, entry122)
    section21.add_items(entry211, entry212)
    section22.add_items(entry221, entry222)
    page1.add_sections(section11, section12)
    page2.add_sections(section21, section22)
    stencil.add_pages(page1, page2)
    return stencil


def get_page_dictionaries(is_new=False):
    if not is_new:
        dic1 = {"section1.1": {"entry1.1.1": "1.1.1", "entry1.1.2": "1.1.2"},
                "section1.2": {"entry1.2.1": "1.2.1", "entry1.2.2": "1.2.2"}}
        dic2 = {"section2.1": {"entry2.1.1": "2.1.1", "entry2.1.2": "2.1.2"},
                "section2.2": {"entry2.2.1": "2.2.1", "entry2.2.2": "2.2.2"}}
    else:
        dic1 = {"section1.1": {"entry1.1.1": "new1.1.1", "entry1.1.2": "new1.1.2"},
                "section1.2": {"entry1.2.1": "new1.2.1", "entry1.2.2": "new1.2.2"}}
        dic2 = {"section2.1": {"entry2.1.1": "new2.1.1", "entry2.1.2": "new2.1.2"},
                "section2.2": {"entry2.2.1": "new2.2.1", "entry2.2.2": "new2.2.2"}}
    return dic1, dic2


def get_es_dictionary():
    return {
        "###main###": {"stencil": "Stencil"},
        "###pages###": {"page1": "Page 1", "page2": "Page 2"},
        "page1": {"section1.1": "Section 1.1", "section1.2": "Section 1.2"},
        "page2": {"section2.2": "Section 2.2", "section2.1": "Section 2.1"},
        "section1.1": {"entry1.1.2": "Entry 1.1.2", "entry1.1.1": "Entry 1.1.1"},
        "section1.2": {"entry1.2.2": "Entry 1.2.2", "entry1.2.1": "Entry 1.2.1"},
        "section2.1": {"entry2.1.2": "Entry 2.1.2", "entry2.1.1": "Entry 2.1.1"},
        "section2.2": {"entry2.2.1": "Entry 2.2.1", "entry2.2.2": "Entry 2.2.2"},
        "###itemtypes###": {
            "entry2.2.1": "Entry", "entry2.1.2": "Entry", "entry1.2.1": "Entry", "entry1.1.2": "Entry",
            "entry1.2.2": "Entry", "entry2.2.2": "Entry", "entry2.1.1": "Entry", "entry1.1.1": "Entry"
        }
    }
