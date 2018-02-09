import unittest

from pawn import default_pawns
from pawn import Ant



from honeycomb import HCPoint as HCP
from hive import Hive
from color import Color
from player import Player


#from hive import Hive
#from honeycomb import HCPoint as HCP

class TestPlayer(unittest.TestCase):

    def test_init(self):
        player1 = Player(Color.WHITE, pawns = {});
        self.assertTrue(player1.pawns == {})

        player2 = Player(Color.BLACK);
        """ Note that the pawns are not suppose to be the same,
            same pieces but each piece is unique."""
        self.assertNotEqual(player2.pawns, default_pawns(Color.BLACK))
        


    def test_place(self):
        """ test placement of moves
            
        Test to see if the a player can place a piece
        """
        p1 = Player(Color.WHITE);
        hive = Hive();

        p1.place(Ant, HCP(1,1), hive)

        self.assertFalse(hive.empty())

if __name__ == '__main__':
    unittest.main()
