from enum import Enum

from honeycomb import hcp_within_one
from honeycomb import dist

from hive import breaks_hive

from pawn import Queen

from color import Color

from gamestate import Gamestate

class Movetype(Enum):
    """ Tupes of moves allowed """

    MOVE  = 0
    PLACE = 1

class Move:

    def __init__(self, movetype, parameters):
        self.movetype = movetype
        self.parameters = parameters

class Referee:
    """ The rule enforcer of the game.
        
        This is to allow flexibility of other developers to make
        their own modification of the game, or make a different
        game entirely based off of this referee.
    """

    def __init__(self, rulebook):
        """ Take in a set of rules to be enforced """
        self.rulebook = rulebook

    def cant_move(self, player, hive):
        return NotImplemented

    def illegal_move(self, move, game):
        """ Checks if a move attempt is illegal"""
        raise Exception("NotImplemented")

    def game_ends(self, game):
        raise Exception("NotImplemented")

class HiveRef(Referee):
    """ The standard rule-enforcer of the game """

    def cant_move(self, player, hive):
        return False
    
    def illegal_move(self, move, game):
        """ Checks if a move attempt is illegal
        
        Is the move with these parameters legal in this
        partuclar game?  """

        if move.movetype == Movetype.PLACE:
            if self.rulebook.badplace(move.parameters, game):
                return True

        if move.movetype == Movetype.MOVE:
            if self.rulebook.badmove(move.parameters, game):
                return True

        return False

    def game_ends(self, game):
        hive = game.hive
        blk = Color.BLACK
        wht = Color.WHITE
        colorloss = {}
        colorloss[blk] = False
        colorloss[wht] = False

        for hcp in hive.interior():

            if isinstance(hive[hcp], Queen):
        
                loser = True
                for touch in hcp_within_one(hcp):
                    
                    if touch not in hive.interior(): 
                        loser = False

                colorloss[hive[hcp].color] = loser

        if not colorloss[blk] and not colorloss[wht]: return False

        if colorloss[blk] and colorloss[wht]: 
            game.gamestate = Gamestate.STALEMATE
            return True

        if colorloss[blk]:
            game.winner = wht
            game.gamestate = Gamestate.VICTORY
            
        if colorloss[wht]:
            game.winner = blk
            game.gamestate = Gamestate.VICTORY

        return True

class Rulebook:
    def __init__(self):
        pass

class HiveRulebook(Rulebook):

    def badplace(self, (pawn, location), game):
        """ Check if placement of the piece is bad 
        
        First check if this location is on the boarder,
        then check if this piece will touch only pieces
        that share its color."""
        if location is None: return True 
        # No pieces on the hive 
        if len(game.hive.interior()) == 0:
            return False

        # Player did not place on boarder:
        if location not in game.hive.border():
            return True
 
        # Second move:
        if game.fullcycles == 0:
            return False
   
        # Check if boarding pieces share color
        for touching in hcp_within_one(location):

            touchingpawn = game.hive.pawn_at(touching)

            if touchingpawn == None:
                continue

            print(pawn)
            if touchingpawn.color != pawn.color:
                return True

    def badmove(self, (source, dest), game):
        
        if dest is None: return True 
        if dist(source, dest) == 0: return True

        player = game.current_player()
        pawn = game.hive[source]

        if player.color != pawn.color:
            return True

        if breaks_hive(source, game.hive): #See if the move breaks the hive
            return True

        return not pawn.rules(source, dest, game.hive)
