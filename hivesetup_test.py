import unittest

from hive import Hive

from pawn import Spider
from pawn import Color

class TestHiveSetup(unittest.TestCase):

    def test_blankboard(self):
        board = Hive()
        self.assertTrue(board.empty())

    def test_starting_pawn(self):
        board = Hive()
        piece = Spider(Color.BLACK)
        board.add(piece, (0,0))

        self.assertFalse(board.empty())
        #Need another test case here th check if 
        #the spider was added
         
    def test_boundries(self):
        board = Hive()
        piece = Spider(Color.WHITE)
        board.add(piece, (0,0))

        # Note that these are in the hive coordinate system.
        open_locations = {(1,0),(0,1),(-1,0),(0,-1),(1,-1)(-1,1)}

        self.assertTrue(board.opened() = open_locations)

if __name__ == '__main__':
    unittest.main()
