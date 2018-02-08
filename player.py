"""
Player Object
"""

from pawn import default_pawns

# Author: Jacob Liddy<jpl61@zips.uakron.edu>

class Player:
    """ Represents a Player of Hive 
    
    Parameters:

    Color: Required
        There are two colors in hive, what color will Player be 
        using?

    pawns: Set, optional (default: see comment) 
        The players starting pieces, by default this is three 
        ants, two spiders, three grasshoppers, two beetles, and 
        the queen bee.

    Attrubutes
    ----------
    """

    def __init__(self, color, pawns = None):
        
        self.color = color;
        if pawns == None:
            self.pawns = default_pawns(color)
        else:
            self.pawns = pawns

