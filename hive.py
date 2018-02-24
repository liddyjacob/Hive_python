from honeycomb import hcp_within_one


class Hive:
    """
    The hive is the structure which is formed
    when playing the game of hive. It is a set
    of pieces, on a honeycomb lattice.
    """
    def __init__(self):
        self.pawns = {}

        self.hmin = 0
        self.hmax = 0
        self.kmin = 0
        self.kmax = 0

    def empty(self):
        return len(self.pawns) == 0

    def add(self, pawn, location):
        self.pawns[pawn] = location
        
        self.__adjrange__(location)

    def boarder(self):

        locations = self.__pawn_loc__()
        edges = []
        for loc in locations:

            for edge in hpc_within_one(loc):

                if edge in locations:
                    continue

                if edge in edges:
                    continue

                edges.append(edge)

        return edges

    def h_range(self):
        """ Return x range of hive pieces """
        return range(self.hmin, self.hmax + 1)
    

    def k_range(self):
        """ Return y range of hive pieces """ 
        return range(self.hmin, self.hmax + 1)
    
    def get_pieces(self):

        pieces = []

        for pawn, location in self.pawns.iteritems():
            pieces.append((pawn, location))

        return pieces

    def __adjrange__(self, location):
        self.hmin = min(location.h, self.hmin)
        self.hmax = max(location.h, self.hmax)

        self.kmin = min(location.k, self.kmin)
        self.kmax = max(location.k, self.kmax)

    def __pawn_loc__(self):

        locations = []

        for pawn, location in self.pawns.iteritems():
            locations.append(location)

        return locations


