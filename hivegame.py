"""
This module is what the controlls the hive game:
It enforces thee rules, moderates the game, and
determines the outcome.
"""


class HiveGame:
    """ Represents a Hive Game (More details coming soon). """

    def __init__(self, playerlist, referee = None):
        # The list of players in our game of hive
        self.plist = playerlist

        # Make a standard referee
        if referee is None:
            self.ref = HiveRef()

    def start(self):
        self.fullcycles = 0 
        self.whosemove = 0 # It is player number zero's move
        

    def step(self):
        
        # TODO: Rethink this design stratagy. May not be great?
        # I may have rushed this section.
        self.whosemove += 1 
        self.whosemove = self.whosemove % len(self.plist)

        if self.whosemove is 0: # Back to the starting player
            self.fullcycles += 1
        
        

class Referee:
    """ The rule enforcer of the game.
        
        This is to allow flexibility of other developers to make
        their own modification of the game, or make a different
        game entirely based off of this referee.
    """

    def __init__(self):
        pass

class HiveRef(Referee):
    """ The standard rule-enforcer of the game """


