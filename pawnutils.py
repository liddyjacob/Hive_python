"""
    Pawnutils.py:

    Pawns will follow rules of movement and 
    thus we will need some utilities to combine
    rules of movement.
"""
from hive import make_border
from hive import make_zones

from honeycomb import create_line
from honeycomb import hcp_within_one
# movement_rules takes a set of boolean
# functions that must be satisfied and 
# returns a aggregate function which 
# uses all of those rules.
#
# By rules, we mean rules of movement
def movement_rules(rules):

    # Need the hive, intial position, and final location
    # to determine if a move is legal?
    def legalmove(init, final, hive):
        print("Checking for move legallity...")
        print "\tNumber of rules to check: ", len(rules)

        for rule in rules:
            if rule(init, final, hive):
                return True

        print("Move was illegal")
        return False

    return legalmove


""" 
## The slide rule ##

A piece that follows the slide rule must be able to physically
slide into its new position. Here is an example:
x,y - unoccupied locations
B - Black Player pawn
W - White player pawn
A - an ant pawn.

. W B . .
 B x . .
. W W . .
 B y . .
. B(A). .

The ant A can't move to x, as x does not have a nearby pair
of empty spaces, two dots. This is an easy way to check for thae
e slide rule. Note that here is another x that violates the slide
rule yet has two empty spaces next to it:

. . . . . . 
 . . p p . .
. p p . p . 
 p x . >!< .
. p . . p .
 . p p p . .
. A . . . .

The only possible path brings us through the hole denoted by an
explination point.

"""

def slide_rule(init, final, hive):
    return NotImplemented

def slides(source, dest, length, hive):

    print ("In slides")

    #Movements can only be on boarder.
    if len(hive.locdict[source]) >= 2: return False
    if dest not in hive.border(): return False

    # Need to fix this: We can't generate the border if the source
    # is still a part of the hive!
    mod_interior = hive.interior()
    mod_interior.remove(source)

    border = make_border(mod_interior)

    zones = make_zones(border, mod_interior)

    i = 0
    for zone in zones:
        print "Zone ", i
        i+=1
        for hcp in zone:
            print str(hcp)

    for zone in zones:
        if source in zone and dest in zone:
            return True #return pathfind(source, dest, length, zone)

    print("Illegal Slide")
    return False

"""
    The hop rule means the piece can be on top of the hive.
"""
def hop_rule(init, final, hive):
    line = create_line(init, final)
    if len(line) == 0 : return False

    for hcp in line:
        print "Checking if hcp is not empty: ", hcp
        if len(hive.locdict[hcp]) == 0: return False

    if hive.locdict.get(final) == None: return True
    if len(hive.locdict.get(final)) != 0: return False
 
    return True



def jump_rule(init, final, hive):

    mod_interior = hive.interior()
    mod_interior.remove(init)

    border = make_border(mod_interior)

    if final not in hcp_within_one(init):
        return False

    #Pieces on top can go anywhere.
    if len(hive.locdict[init]) >= 2: return True

    return (final in hive.interior())

def slide_rule_maker(length):
    #print("Slide rule construction")
    def length_rule(init, final, hive):
        print ("In length rule\n")

        if slides(init, final, length, hive):
            return True
        print ("Length rule failed")

        return False

    return length_rule
