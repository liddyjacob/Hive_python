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
