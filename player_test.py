import unittest

from color import Color
from player import Player

#from hive import Hive
#from honeycomb import HCPoint as HCP

class TestPlayer(unittest.TestCase):

    def test_init(self):
        player1 = Player(Color.WHITE, pawns = {});
        self.assertTrue(player1.pawns == {})
        

if __name__ == '__main__':
    unittest.main()
