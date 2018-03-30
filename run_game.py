""" Run the game: For Developing purpose """

from interface import PlayerInterface
from interface import Keyboard
from interface import ExternalWindow

from color import Color

from player import Player

from hivegame import HiveGame

from game import run_game

def main():
    
    interface = PlayerInterface(Keyboard(), ExternalWindow())
    p1 = Player(Color.WHITE, interface)
    p2 = Player(Color.BLACK, interface)

    game = HiveGame([p1, p2])
    run_game(game)

    return

if __name__ == "__main__":
    main()
