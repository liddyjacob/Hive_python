#pawn.py

"""
    A pawn is a piece used in hive.
    Every piece is a pawn, and each
    pawn has its own move.

    The goal of hive is to surround the
    opponents queen bee pawn.
"""

class Pawn:

    def __init__(self, color):
        self.color = color



class Queen(Pawn):

    def move(self):
        return NotImplemented


class Ant(Pawn):

    def move(self):
        return NotImplemented

class Spider(Pawn):

    def move(self):
        return NotImplemented

class Beetle(Pawn):
    
    def move(self):
        return NotImplemented

class Grasshopper(Pawn):

    def move(self):
        return NotImplemented

