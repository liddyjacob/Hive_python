import unittest

from hivegame import HiveGame

from player import Player

from color import Color

from interface import Preload
from interface import CommandLine
from interface import PlayerInterface
from interface import ExternalWindow

class TestHiveGame(unittest.TestCase):

    def test_step(self):

        test_input = Preload("tests/hivegame_input")
        automated_interface = PlayerInterface(test_input, CommandLine())

        p1 = Player(Color.WHITE, automated_interface)
        p2 = Player(Color.BLACK, automated_interface)
        game = HiveGame([p1])

        game.start() # Initialize the game.

        self.assertEqual(game.fullcycles, 0)

        game.step()
        game.step()
        game.step()
        game.step()
        game.step()
        game.step()

        self.assertEqual(game.fullcycles, 6)


    def test_place(self):
 
        test_input = Preload("tests/hivegame_input")
        automated_interface = PlayerInterface(test_input, ExternalWindow())

        p1 = Player(Color.WHITE, automated_interface)
        p2 = Player(Color.BLACK, automated_interface)
        game = HiveGame([p1, p2])

        game.start() # Initialize the game.

        self.assertEqual(game.fullcycles, 0)

        game.step()
        game.step()
        game.step()
        game.step()
        game.step()
        game.step()

        self.assertEqual(game.fullcycles, 3)




if __name__ == '__main__':
    unittest.main()
