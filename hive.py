from honeycomb import hcp_within_one
from honeycomb import HCPoint

class Stack(list):
    def put(self, item):
        self.append(item)

    def get(self):
        item = self[-1]
        self.pop()
        return item

    def top(self):
        return self[-1]    


class Hive:
    """
    The hive is the structure which is formed
    when playing the game of hive. It is a set
    of pieces, on a honeycomb lattice.
    """
    def __init__(self):
        self.locdict = {}

        self.hmin = 0
        self.hmax = 0
        self.kmin = 0
        self.kmax = 0

    def empty(self):
        return len(self.pawns) == 0


    def add(self, pawn, loc):
        self.locdict.setdefault(loc, Stack()).put(pawn);    
        self.__adjrange__(loc)

    def remove(self, loc):

        ld = self.locdict
        item = ld[loc].get()
        print(item);

        if len(ld[loc]) == 0: # Empty stack
            del ld[loc];

        return item

    def border(self):

        locations = self.interior()
        edges = []

        for loc in locations:
            for edge in hcp_within_one(loc):

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

        for location, stack in self.locdict.iteritems():
            pawn = stack.top()
            if pawn != None: # Weird bug 
                pieces.append((pawn, location))

        return pieces

    def locations(self):
        """ Return locations and boarders """

        interior = self.interior()
        exterior = self.border()

        return interior + exterior

    def top(self, loc): 
        """ Get top pawn on a location """
        return self.locdict[loc].top()

    def __getitem__(self, loc):
        return self.locdict[loc].top()


    def __adjrange__(self, location):
        self.hmin = min(location.h, self.hmin)
        self.hmax = max(location.h, self.hmax)

        self.kmin = min(location.k, self.kmin)
        self.kmax = max(location.k, self.kmax)

    def interior(self):

        locations = []

        for location, stack in self.locdict.iteritems():
            locations.append(location)

        return locations

    def pawn_at(self, loc):
        if loc in self.locdict:
            return self.locdict[loc].top()
        return None

def breaks_hive(source, hive):

    print(hive.locdict[source])
    if len(hive.locdict[source]) >= 2: return False

    modified = hive.interior()
    modified.remove(source)
    if len(modified) == 1: return False
    print(modified)

    for loc in hive.interior():
        hole_in_hive = True

        for nearby in hcp_within_one(loc):
            print "Nearby ",nearby, "| Loc ", str(loc) 
            if nearby in modified: hole_in_hive = False

        if hole_in_hive:
            print("Hole in hive")
            return True

    return False

def make_border(locations):

    edges = []

    for loc in locations:
        for edge in hcp_within_one(loc):

            if edge in locations:
                continue

            if edge in edges:
                continue

            edges.append(edge)

    return edges


