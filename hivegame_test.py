import unittest

from hivegame import HiveGame
from player import Player
from color import Color

class TestHiveSetup(unittest.TestCase):

    def test_step(self):

        p1 = Player(Color.WHITE)
        p2 = Player(Color.BLACK)
        game = HiveGame([p1, p2])

        game.start() # Initialize the game.

        self.assertEqual(game.fullcycles, 0)

        game.step()
        game.step()

        self.assertEqual(game.fullcycles, 1)


    def test_place(self):

        p1 = Player(Color.WHITE)
        p2 = Player(Color.BLACK)

        game = HiveGame([p1, p2])

        game.start() # Initialize the game.

        self.assertEqual(game.fullcycles, 0)

        game.step() #Calls step but with predefined inputs
        game.step() #

        self.assertEqual(game.fullcycles, 1)




if __name__ == '__main__':
    unittest.main()
