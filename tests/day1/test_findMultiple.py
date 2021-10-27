import unittest

from classes.day1.day1 import Multiple

class TestMultiple(unittest.TestCase):

    def test_findMultiple(self):
        input = [1, 0, 2019]
        cut = Multiple()
        self.assertEqual (2019, cut.findMultiple(input))