from enum import Enum

from textdraw import draw as draw_as_text
from textdraw import draw_string
from textdraw import draw_list
from textdraw import stringToObject

from graphdraw import center
from graphdraw import updatePlayer
from graphdraw import drawPawn

from honeycomb import HCPoint as HCP

from rules import Movetype
from rules import Move

from graphics import *

# The tnkinter GUI: from Tkinter import

import Queue



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
    
    def __init__(self, inputs_file = None):
    
        self.queue = Queue.Queue()

        if inputs_file is not None:
            self.load(inputs_file)


    def select(self, decisions):
        
        if self.queue.empty():
            raise Exception("No decisions left in the Preload!")

        choice = self.queue.get()
        print("Preload Choice")
        print(choice);
        return choice

    def load(self, inputs_file):
        """ Load a file of inputs, convert strings to inputs """

        with open(inputs_file) as infile:
            for string in infile:
                obj = stringToObject(string.rstrip())
                self.queue.put(obj)

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
        draw_string("=====HIVE=====\n\n")
        draw_as_text(hive)
        draw_string("\n")
        draw_string("==============\n")
        draw_string("Move(0) or Place(1): ")
        move = controller.select([Movetype.MOVE, Movetype.PLACE])
        draw_string("\n")

        parameter1 = None

        if move == Movetype.MOVE:
            draw_string("What Piece?\n")
            
            pieces = hive.get_pieces()
            draw_list(pieces)
            piece = controller.select(pieces)
            
            parameter1 = pieces[1] # From the tuplet get unique pawn

        if move == Movetype.PLACE:
            draw_string("What Piece?\n")
            
            pieces = list(player.pawns)
            draw_list(pieces)
            piece = controller.select(pieces)
            
            parameter1 = type(piece) # From the tuplet get unique pawn

        draw_string("\n")

        locations = hive.locations()

        if len(locations) == 0:
            locations = [HCP(0,0)]    
        
        draw_string("To where\n")
        draw_list(locations)
        parameter2 = controller.select(locations)

        self.decision = (move, parameter1, parameter2)

        draw_string("\n")
        return self.decision != None 

class ExternalWindow(Display):

    def __init__(self):
        self.decision = None
        self.init();

    def init(self):
        self.win = GraphWin('Hive!', 600, 600)
        self.imgdict = {}
    

    def update(self, controller, player, hive):

        updatePlayer(player, self.win)

        draw_string("=====HIVE=====\n\n")
        draw_as_text(hive)
        draw_string("\n")
        draw_string("==============\n")
        draw_string("Move(0) or Place(1): ")

        movetype = controller.select([Movetype.MOVE, Movetype.PLACE])
        draw_string("\n")

        draw_string("What Piece?\n")

        if movetype == None:
            return True

        parameter1 = None

        if movetype == Movetype.MOVE:
            
            interior = hive.interior()
            draw_list(interior)
            location = controller.select(interior)
            
            parameter1 = location # From the tuplet get unique pawn

        if movetype == Movetype.PLACE:
            
            pieces = list(player.pawns)
            draw_list(pieces)
            piece = controller.select(pieces)
            
            parameter1 = piece #type(piece) # From the tuplet get unique pawn

        locations = hive.locations()

        if len(locations) == 0:
            locations = [HCP(0,0)]
    
        draw_string("To where\n")
        draw_list(locations)
        parameter2 = controller.select(locations)

        self.decision = Move(movetype, (parameter1, parameter2))

        draw_string("\n") 

        return self.decision != None


    """ Place a piece on the board """
    def place(self, pawn, loc):
        pawnimg, colorimg = drawPawn(pawn, loc, self.win);

        self.imgdict.setdefault(loc, (pawnimg, colorimg))

        print self.win.items
#        for item in self.win.items:
#            item.undraw() 

        self.win.redraw()
 
        #updateHive(hive, self.win)
        #updatePlayer(player, self.win)

    """ Move a piece from it's initial location to its final location """
    def move(self, init, dest):

        print self.win.items

        init_eucl = center(init)
        dest_eucl = center(dest)
        diff = (dest_eucl[0] - init_eucl[0], dest_eucl[1] - init_eucl[1])

        dx = diff[0]
        dy = diff[1]

        pawnimg = self.imgdict[init][0]
        colorimg = self.imgdict[init][1]

        del self.imgdict[init]

        pawnimg.move(dx, dy) 
        colorimg.move(dx, dy)       

        self.imgdict.setdefault(dest, (pawnimg, colorimg))
        self.win.redraw()
       


class Interface(object):
    """ An Interface is an input and output combined """

    def __init__(self, controller, display):
        self.controller = controller
        self.display = display

    def move_decision(self, player, hive):
        return NotImplemented

class PlayerInterface(Interface):
    """ A player interface makes decisions based off a controller 
    where the real life player has a direct input to the computer"""

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

        raise Exception("No decision made in interface.move_decision")

    def place(self, pawn, loc):
        self.display.place(pawn, loc)


    def move(self, init, dest):
        self.display.move(init, dest)

class NPCInterface(Interface):
    pass


def Default_Interface():
    return PlayerInterface(Keyboard(), CommandLine())
