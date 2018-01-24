 
from honeycomb import hpc_within_one


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

    def __pawn_loc__(self):
        locations = []
        for pawn, location in self.pawns.iteritems():
            print location
            locations.append(location)

        return locations

    def edge(self):
        locations = self.__pawn_loc__()
        edges = []
        for loc in locations:
            for edge in hpc_within_one(loc):
                edges.append(edge)
                print edge

        return edges
            
