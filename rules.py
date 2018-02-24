from enum import Enum

class Referee:
    """ The rule enforcer of the game.
        
        This is to allow flexibility of other developers to make
        their own modification of the game, or make a different
        game entirely based off of this referee.
    """

    def __init__(self):
        pass

    def cant_move(self, player, hive):
        return NotImplemented

    def illegal_move(self, attempt):
        """ Checks if a move attempt is illegal"""
        return NotImplemented


class HiveRef(Referee):
    """ The standard rule-enforcer of the game """

    def cant_move(self, player, hive):
        return False

    def illegal_move(self, attempt):
        """ Checks if a move attempt is illegal"""
        return False


class Movetype(Enum):
    """ Tupes of moves allowed """

    MOVE  = 0
    PLACE = 1


