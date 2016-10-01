import os
from operator import attrgetter

from src.elements import CompositeElement
from src.items import Valued

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
