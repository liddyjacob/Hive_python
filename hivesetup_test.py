import unittest
from hive import Hive

class TestHiveSetup(unittest.TestCase):

    def test_blankboard(self):
        board = Hive()
        self.assertTrue(board.empty())

    def test_starting_pawn(self):
        return NotImplemented

if __name__ == '__main__':
    unittest.main()
