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

        self.assertEqual(set(board.edge()),set(open_locations))

    def test_two_piece(self):
        board = Hive()
        piece1 = Spider(Color.WHITE)
        piece2 = Spider(Color.WHITE)
        board.add(piece1, HCP(0,0))
        board.add(piece2, HCP(1,0))

        open_locations = [HCP(1,1), HCP(0,1), HCP(-1,0),
                          HCP(0,-1), HCP(1,-1), HCP(-1,1),
                          HCP(2,0), HCP(2,-1)]

        self.assertEqual(set(board.edge()), set(open_locations))
       
    def test_hivebreak(self):
        board = Hive()

        piece1 = Spider(Color.WHITE)
        board.add(piece1, HCP(0,0))

        piece2 = Spider(Color.BLACK)
        board.add(piece2, HCP(1,0))

        piece3 = Spider(Color.BLACK)
        board.add(piece3, HCP(1,1))

        # These locations will break the hive
        breaker = [piece2, (1,0)]

        self.assertEqual(board.breaker(), breaker)
        
        

if __name__ == '__main__':
    unittest.main()
