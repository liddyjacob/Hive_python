


"""
The hive is the structure which is formed
when playing the game of hive. It is a set
of pieces, on a honeycomb lattice.
"""
class Hive:
    
    def __init__(self):
        self.pawns = {}

    def empty(self):
        return len(self.pawns) == 0

    def add(self, pawn, location):
        self.pawns[pawn] = location
