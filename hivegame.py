"""
This module is what the controlls the hive game:
It enforces thee rules, moderates the game, and
determines the outcome.
"""
from hive import Hive

from rules import HiveRef
from rules import Movetype
from rules import HiveRulebook

from color import Color

from gamestate import Gamestate

from enum import Enum

class HiveGame:
    """ Represents a Hive Game (More details coming soon). """

    def __init__(self, playerlist, referee = None):
        # The list of players in our game of hive
        self.players = playerlist
        self.hive = Hive()

        # Make a standard referee
        if referee is None:
            self.ref = HiveRef(HiveRulebook())

    def start(self):
        self.fullcycles = 0 
        self.whosemove = 0 # It is player number zero's move
        self.gamestate = Gamestate.INGAME
        self.winner = None

    def step(self):
        
        player = self.players[self.whosemove]
        
        initial_player = self.whosemove
        referee = self.ref # For ease of reading code

        while referee.cant_move(player, self.hive):
            self.__next_player__()
            player = self.players[self.whosemove]
            
            if self.whosemove == initial_player:
                #Referee has determined that nobody can move
                self.gamestate = Gamestate.STALEMATE ##
                return

        attempt = player.attempt_move(self.hive)

        while referee.illegal_move(attempt, self):
            attempt = player.attempt_move(self.hive)
        # Unpackage attempt:
        
        movetype    = attempt.movetype
        parameters  = attempt.parameters + (self.hive,)

        if movetype == Movetype.PLACE:
            player.place(parameters)

        if movetype == Movetype.MOVE:
            player.move(parameters)
            
        if referee.game_ends(self):
            if self.winner is not None:
                if self.winner == Color.WHITE:
                    print "White Wins"
                else:
                    print "Black Wins"
            else: print "Tie Game!"
            #interface_endgame(self)
            
        self.__next_player__()

    def __next_player__(self):

        self.whosemove += 1 
        self.whosemove = self.whosemove % len(self.players)

        if self.whosemove is 0: # Back to the starting player
            self.fullcycles += 1
    def current_player(self):

        return self.players[self.whosemove]

