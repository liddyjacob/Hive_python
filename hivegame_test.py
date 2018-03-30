import unittest

from hivegame import HiveGame

from player import Player

from color import Color

from interface import Preload
from interface import CommandLine
from interface import PlayerInterface
from interface import ExternalWindow

from time import sleep

class TestHiveGame(unittest.TestCase):

    """
    def test_move(self):
 
        test_input = Preload("tests/hivegame_moveinput")
        automated_interface = PlayerInterface(test_input, ExternalWindow())

        p1 = Player(Color.WHITE, automated_interface)
        p2 = Player(Color.BLACK, automated_interface)
        game = HiveGame([p1, p2])

        game.start() # Initialize the game.

        self.assertEqual(game.fullcycles, 0)

        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)

        self.assertEqual(game.fullcycles, 3)
    """


    def test_valid_twoplayer(self):

        white_input = Preload("tests/white_valid.txt")
        black_input = Preload("tests/black_valid.txt")

        output = ExternalWindow()

        white_inter = PlayerInterface(white_input, output)
        black_inter = PlayerInterface(black_input, output)

        p1 = Player(Color.WHITE, white_inter)
        p2 = Player(Color.BLACK, black_inter)
        game = HiveGame([p1, p2])

        game.start() # Initialize the game.

        self.assertEqual(game.fullcycles, 0)

        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        """        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        game.step()
        sleep(.2)
        """
        self.assertEqual(game.fullcycles, 4)







if __name__ == '__main__':
    unittest.main()
