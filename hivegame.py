"""
This module is what the controlls the hive game:
It enforces thee rules, moderates the game, and
determines the outcome.
"""
from hive import Hive

from rules import HiveRef
from rules import Movetype

from enum import Enum

class HiveGame:
    """ Represents a Hive Game (More details coming soon). """

    def __init__(self, playerlist, referee = None):
        # The list of players in our game of hive
        self.players = playerlist
        self.hive = Hive()

        # Make a standard referee
        if referee is None:
            self.ref = HiveRef()

    def start(self):
        self.fullcycles = 0 
        self.whosemove = 0 # It is player number zero's move
        self.gamestate = Gamestate.INGAME

    def step(self):
        
        player = self.players[self.whosemove]
        initial_player = self.whosemove
        referee = self.ref # For ease of reading code

        while referee.cant_move(player, self.hive):
            self.__next_player__()
            
            if self.whosemove == initial_player:
                #Referee has determined that nobody can move
                self.gamestate = Gamestate.STALEMATE ##
                return

        attempt = player.attempt_move(self.hive)

        while referee.illegal_move(attempt):
            attempt = player.attempt_move(self.hive)

        # Unpackage attempt:
        
        movetype    = attempt[0] 
        unique_pawn = attempt[1] 
        location    = attempt[2] 

        if movetype == Movetype.PLACE:
            player.place(type(unique_pawn), location, self.hive)

        if movetype == Movetype.MOVE:
            return NotImplemented

        self.__next_player__()

    def __next_player__(self):

        self.whosemove += 1 
        self.whosemove = self.whosemove % len(self.players)

        if self.whosemove is 0: # Back to the starting player
            self.fullcycles += 1

class Gamestate(Enum):
    INGAME = 0
    STALEMATE = 1 # No player can move
    VICTORY = 2
    DRAW = 3 # Both players have queen surrounded
        

