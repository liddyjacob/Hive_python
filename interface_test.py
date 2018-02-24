""" Tests some types of interfaces """
import unittest

from interface import Preload
from interface import CommandLine
from interface import PlayerInterface

class TestHiveSetup(unittest.TestCase):

    def test_preload(self):
        inputs = Preload("tests/001.txt")
        chars = ['a', 'b', 'c']

        char = inputs.select(chars)
        self.assertEqual(char, 'a');

        char = inputs.select(chars)
        self.assertEqual(char, 'a');

        char = inputs.select(chars)
        self.assertEqual(char, 'b');

if __name__ == '__main__':
    unittest.main()
