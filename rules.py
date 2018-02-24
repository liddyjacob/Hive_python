from enum import Enum

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
    

class Movetype(Enum):
    """ Tupes of moves allowed """

    MOVE  = 0
    PLACE = 1


