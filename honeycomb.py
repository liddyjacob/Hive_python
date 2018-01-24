
""" Honeycomb.py
This is the geometric space in which
a game of hive takes place. Each point
can describe the center of a hexagon

Specifically a paralellogram lattice with
angle 120 degrees
aralellogram lattice point
"""

"""
#k

^
|
. . . . 
|. . .
. . . X
|. . . 
.-1-2-3-----> h 

 X = (4,2)
"""

class HCPoint:

    def __init__(self, h, k):
        self.h = h
        self.k = k

    def __add__(self, other):
        h = self.h + other.h
        k = self.k + other.k
        return HCPoint(h,k)

    def __eq__(self, other):
        return (self.h == other.h) and (self.k == other.k)

    def __str__(self):
        return "HCP(" + str(self.h) + ", " + str(self.k) + ")"

    def __hash__(self):
        return 3*self.h + 13*self.k

#Converts a honeycomb point to euclidian
def hpc_to_eucl(hcp):

    # Describes (0,1) from HoneyComb to euclidian,
    # "k" vector.
    v_k = (0.0,1.0)

    # Describes (1,0) from HoneyComb to euclidian
    # "h" vector.
    v_k = (sqrt(3)/2.0,1.0/2.0)

    xy_point = v_h * hpc.h + v_k * hpc.k

    return xy_point

# Find the points within one euclidian unit of distance.
# Returns the set of points
def hpc_within_one(hpc):
    
    directions = [HCPoint(1,0), HCPoint(0,1),
                  HCPoint(-1,1), HCPoint(-1,0),
                  HCPoint(0,-1), HCPoint(1, -1)]
    
    nearby_points = []

    for direction in directions:
        nearby_points.append(hpc + direction)

    return nearby_points
