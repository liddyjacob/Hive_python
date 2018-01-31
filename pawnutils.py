"""
    Pawnutils.py:

    Pawns will follow rules of movement and 
    thus we will need some utilities to combine
    rules of movement.
"""


# movement_rules takes a set of boolean
# functions that must be satisfied and 
# returns a aggregate function which 
# uses all of those rules.
#
# By rules, we mean rules of movement
def movement_rules(rules):

    # Need the hive, intial position, and final location
    # to determine if a move is legal?
    def legalmove(hive, init, final):
        
        for rule in rules:
            
            if not rule(hive, init, final):
                return False

        return True

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

def slide_rule(hive, init, final):
    return NotImplemented


"""
    The hop rule means the piece can be on top of the hive.
"""
def hop_rule(hive, init, final):




def jump_rule(hive, init, final):



def length_rule
