

## Honeycomb.py
## This is the geometric space in which
## a game of hive takes place. Each point
## can describe the center of a hexagon

## Specifically a paralellogram lattice with
## angle 120 degrees
##Paralellogram lattice point

#k
#^
#|
#4 . . . 
#|. . .
#2 . . X
#|. . . 
#.-1-2-3-----> h 
#
# X = (4,2)


class HCombPoint:

    def __init__(self,h, k):
        self.h = h
        self.k = k


#Converts a honeycomb point to euclidian
def hpc_to_eucl(hcp):

    # Describes (1,0) from HoneyComb to euclidian,
    # "h" vector.
    v_h = (1.0,0.0)

    # Describes (0,1) from HoneyComb to euclidian
    # "k" vector.
    v_k = (sqrt(3)/2.0,1.0/2.0)

    xy_point = v_h * hpc.h + v_k * hpc.k

    return xy_point


