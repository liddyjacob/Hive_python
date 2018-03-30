"""
    Pawnutils.py:

    Pawns will follow rules of movement and 
    thus we will need some utilities to combine
    rules of movement.
"""
from hive import make_border

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
    #if trapped(source, hive): return False
    #Movements can only be on boarder.
    if len(hive.locdict[source]) >= 2: return False
    if dest not in hive.border(): return False

    # Need to fix this: We can't generate the border if the source
    # is still a part of the hive!
    mod_locs = hive.interior()
    mod_locs.remove(source)

    border = make_border(mod_locs)
    
    print("Passed test!")
    #if zone(source, boarder) != zone(dest, boarder): return False
    #return pathfind(source, dest, length, boarder)

    return True

"""
    The hop rule means the piece can be on top of the hive.
"""
def hop_rule(init, final, hive):
    pass



def jump_rule(init, final, hive):
    pass


def slide_rule_maker(length):
    print("Slide rule construction")
    def length_rule(init, final, hive):
        print ("In length rule\n")

        if slides(init, final, length, hive):
            return True
        print ("Length rule failed")

        return False

    return length_rule
