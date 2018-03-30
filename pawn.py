from color import Color

from pawnutils import movement_rules
from pawnutils import slide_rule_maker

class Pawn(object):
    """ Base class for pawns.
    
    Warning: This class should not be used directly. 
    Use derived classes instead.

    A pawn is a piece used in hive.
    Every piece is a pawn, and each
    pawn has its own move.

    The goal of hive is to surround the
    opponents queen bee pawn.

    We should probably precompile the rules
    for each piece so that they are not compiled
    on the spot.
    """

    def __init__(self, color = None):
        self.color = color
        self._setrules_()

class Queen(Pawn):

#    rules = movement_rules([(slide_rule_maker(1))])
    def __str__(self):
        return "Queen"

    def _setrules_(self):
        self.rules = movement_rules([slide_rule_maker(1)])

class Ant(Pawn):

    def __str__(self):
        return "Ant"

    def _setrules_(self):
        self.rules = movement_rules([slide_rule_maker(1)])



class Spider(Pawn):

    def __str__(self):
        return "Spider"

    def _setrules_(self):
        self.rules = movement_rules([slide_rule_maker(1)])



class Beetle(Pawn):
    
    def __str__(self):
        return "Beetle"

    def _setrules_(self):
        self.rules = movement_rules([slide_rule_maker(1)])


class Grasshopper(Pawn):

    def __str__(self):
        return "Grasshopper"

    def _setrules_(self):
        self.rules = movement_rules([slide_rule_maker(1)])


def default_pawns(color):
    """ Generate a set of default pawns for a player to use
        
        This will include:
            * 1x Queen,
            * 3x Ants,
            * 2x Spiders,
            * 2x Beetles,
            * 3x Grasshoppers """
        
    c = color # For shorthand

    default_set = {Queen(c), Ant(c), Ant(c), Ant(c),
                   Spider(c), Spider(c), Beetle(c),
                   Beetle(c), Grasshopper(c), Grasshopper(c),
                   Grasshopper(c)}

    return default_set;
