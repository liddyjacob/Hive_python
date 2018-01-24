import unittest

from hive import Hive
from honeycomb import HCPoint as HCP

from pawn import Spider
from pawn import Color

class TestHiveSetup(unittest.TestCase):

    def test_blankboard(self):
        board = Hive()
        self.assertTrue(board.empty())

    def test_starting_pawn(self):
        board = Hive()
        piece = Spider(Color.BLACK)
        board.add(piece, HCP(0,0))

        self.assertFalse(board.empty())
        #Need another test case here th check if 
        #the spider was added
         
    def test_boundries(self):
        board = Hive()
        piece = Spider(Color.WHITE)
        board.add(piece, HCP(0,0))

        # Note that these are in the hive coordinate system.
        open_locations = [HCP(1,0), HCP(0,1), HCP(-1,0),
                          HCP(0,-1), HCP(1,-1), HCP(-1,1)]

        self.assertTrue(set(board.edge()) == set(open_locations))


if __name__ == '__main__':
    unittest.main()
