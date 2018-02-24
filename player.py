"""
Player Object
"""

from pawn import default_pawns
from honeycomb import HCPoint as HCP

from interface import Default_Interface
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

    def __init__(self, color, interface = Default_Interface(), pawns = None):
        
        self.color = color;
        self.interface = interface;

        if pawns == None:
            self.pawns = default_pawns(color)
        else:
            self.pawns = pawns;

    def attempt_move(self, hive):
        """ Make a move with the self.inputs """

        attempt = self.interface.move_decision(self, hive);
        return attempt

    def place(self, pawntype, location, hive):
        """ Places a pawn on a hive board."""
        piece = self.find(pawntype);

        if piece != False:
            hive.add(piece, location)

    def find(self, pawntype):

        for pawn in self.pawns:

            if isinstance(pawn, pawntype):
                return pawn
        
        return False # No pawn of selectec type found.
