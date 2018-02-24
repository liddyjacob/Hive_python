from enum import Enum

from textdraw import draw as draw_as_text
from textdraw import draw_string
from textdraw import draw_list

from rules import Movetype

class Controller:

    def __init__(self):
        pass

    def select(self, decisions):
        """ Select from a list of decisions """

        return NotImplemented 

class Keyboard(Controller):

    def __init__(self):
        pass

    def select(self, decisions):

        choicenumber = input()
        choice = decisions[choicenumber]

        return choice

class Preload(Controller):
    
    def __init__(self):
        pass


class Display:
    
    def __init__(self):
        pass

class NoDisplay(Display):

    def __init__(self):
        pass
    
    def update(self, controller, player, hive):
        pass

class CommandLine(Display):
    
    def __init__(self):
        self.decision = None
        

    def update(self, controller, player, hive):
        """ Update for command line
            
        When using the command line, the controller must make
        a decision immedienty. There are no update cycles or 
        checking if the mouse is hovering, just a hive and
        some basic input and output

        """ 

        draw_as_text(hive)
        draw_string("Move(0) or Place(1): ")
        move = controller.select([Movetype.MOVE, Movetype.PLACE])
        draw_string("\n")

        unique_pawn = None

        if move == Movetype.MOVE:
            draw_string("What Piece?\n")
            
            pieces = hive.get_pieces()
            draw_list(pieces)
            piece = controller.select(pieces)
            
            unique_pawn = pieces[0] # From the tuplet get unique pawn

        if move == Movetype.PLACE:
            draw_string("What Piece?\n")
            
            pieces = player.pawns
            draw_list(pieces)
            piece = controller.select(pieces)
            
            unique_pawn = piece # From the tuplet get unique pawn

        draw_string("To where?")
        
        location = controller.enter_location()

        self.decision = (move, unique_pawn, location)

class Interface(object):
    """ An Interface is an input and output combined """

    def __init__(self, controller, display):
        self.controller = controller
        self.display = display

    def move_decision(self, player, hive):
        return NotImplemented

class PlayerInterface(Interface):
    """ An Interface is an input and output combined """

    def __init__(self, controller, display):
        super(PlayerInterface, self).__init__(controller, display)
        
    def move_decision(self, player, hive):
        """ Makes a decision on what move should be made 
        
        Returns parameters for desired move. These parameters are:
            * Movetype: What kind of move? Placement? Movement?
            * Piece: What piece on board or in hand?
            * Location: Desired location of piece? 
        """
        
        while self.display.update(self.controller, player, hive):
            if self.display.decision != None:
                return self.display.decision

def Default_Interface():
    return PlayerInterface(Keyboard(), CommandLine())
