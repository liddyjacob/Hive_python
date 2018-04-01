
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

from math import sqrt


class HCPoint:

    def __init__(self, h, k):
        self.h = h
        self.k = k

    def __add__(self, other):
        h = self.h + other.h
        k = self.k + other.k
        return HCPoint(h, k)

    def __sub__(self, other):
        h = self.h - other.h
        k = self.k - other.k
        return HCPoint(h, k)




    def __eq__(self, other):
        return (self.h == other.h) and (self.k == other.k)

    def __str__(self):
        return "HCP(" + str(self.h) + ", " + str(self.k) + ")"

    def __hash__(self):
        return 3*self.h + 13*self.k

def dist(source, dest):
    hdiff = source.h - dest.h
    kdiff = source.k - dest.k

    return sqrt(hdiff*hdiff + kdiff*kdiff)

def dist_eucl(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]

    return sqrt(dx * dx + dy * dy)

def hcp_to_eucl(hcp):
    """ Converts a honeycomb point to euclidian"""

    # Describes (0,1) from HoneyComb to euclidian,
    # "k" vector.
    v_k = (sqrt(3)/2.0, -1.0/2.0)

    # Describes (1,0) from HoneyComb to euclidian
    # "h" vector.
    v_h = (sqrt(3)/2.0, 1.0/2.0)

    # Adjust vectors according to point
    v_h = (v_h[0] * hcp.h, v_h[1] * hcp.h)
    v_k = (v_k[0] * hcp.k, v_k[1] * hcp.k)

    xy_point = tuple(map(sum, zip(v_h, v_k)))

    print(xy_point)

    return xy_point


def hcp_within_one(hcp):
    """ Find the points within one euclidian unit of distance.
        Returns the sequence of points, in a cyclic order
        5
      4   0
        .
      3   1
        2
    """

    directions = [HCPoint(1, 0), HCPoint(0, 1),
                  HCPoint(-1, 1), HCPoint(-1, 0),
                  HCPoint(0, -1), HCPoint(1, -1)]
    nearby_points = []

    for direction in directions:
        nearby_points.append(hcp + direction)

    return nearby_points

#Integral line where points are continuous
def create_line(source, dest):

    if source == dest: return []

    directions = [HCPoint(1, 0), HCPoint(0, 1),
                  HCPoint(-1, 1), HCPoint(-1, 0),
                  HCPoint(0, -1), HCPoint(1, -1)]   
    diff = dest - source
    unit_vector = HCPoint(diff.h / dist(source, dest), 
                          diff.k / dist(source, dest))

    print "Unit vector: ", str(unit_vector)
    point = source
    if unit_vector in directions:
        unit_vector.h = int(unit_vector.h)
        unit_vector.k = int(unit_vector.k)

        point = point + unit_vector
        line = []
        while dist(point, dest) != 0.0:
            print "Point on line: ", point
            line.append(point)
            point = point + unit_vector
        return line

    return []

