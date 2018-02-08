from color import Color


class Pawn:
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

    def __init__(self, color):
        self.color = color

class Queen(Pawn):

    def move(self):
        return NotImplemented

class Ant(Pawn):

    def move(self):
        return NotImplemented

class Spider(Pawn):

    def move(self):
        return NotImplemented

class Beetle(Pawn):
    
    def move(self):
        return NotImplemented

class Grasshopper(Pawn):

    def move(self):
        return NotImplemented

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
