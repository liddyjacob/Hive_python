""" tactile: Contains TactileHex class, a hexagon you can interact with """
from enum import Enum

from honeycomb import HCPoint as HCP
from honeycomb import hcp_to_eucl
from honeycomb import dist_eucl

from graphdraw import pawn_image_lookup
from graphdraw import center

from graphics import *

class Settings(Enum):
    PLAYER = 0
    HIVE = 1


class TactileHex(object):

    def __init__(self, pawn):
        self.pawn = pawn
        self.hitbox = None
        self.color_img = None
        self.pawn_img = None
        self.eucl = None
    def create_images(self):
        x = self.eucl[0]
        y = self.eucl[1]

        (pawnfile, colorfile) = pawn_image_lookup(self.pawn)
        
        self.color_img = Image(Point(x, y), colorfile)
        self.pawn_img  = Image(Point(x, y), pawnfile)
        self.radius = self.color_img.getWidth() / 2.5
        
    """def create_hitbox(self):
        width = self.color_img.getWidth()

        x = self.eucl[0]
        y = self.eucl[1]
        self.radius = width / 2.5

        self.hitbox = Circle(Point(x,y), width / 2.5)
    """
    def draw(self, win):
        self.color_img.draw(win)
        self.pawn_img.draw(win)
        #self.hitbox.draw(win)

    def undraw(self):
        #self.hitbox.undraw()
        self.color_img.undraw()
        self.pawn_img.undraw()

    def move(self, dest):
        init_eucl = self.eucl
        dest_eucl = center(dest)
        diff = (dest_eucl[0] - init_eucl[0], dest_eucl[1] - init_eucl[1])

        dx = diff[0]
        dy = diff[1]
                        
        self.color_img.move(dx, dy)
        self.pawn_img.move(dx, dy) 

        self.eucl = dest_eucl
        self.hcp = dest

    def in_hitbox(self, point):

        if dist_eucl(self.eucl, point) < self.radius:
            return True
        return False

class HiveHex(TactileHex):

    def __init__(self, pawn, hcp, settings = None):
        super(HiveHex, self).__init__(pawn)
        self.hcp = hcp

        if settings == None:
            self.distance = 38#pixels
            self.center = (300, 225)#pixel

        eucl = hcp_to_eucl(hcp)
        eucl = (self.distance * eucl[0], self.distance * eucl[1])
        self.eucl = tuple(map(sum, zip(eucl, self.center)))

        self.create_images()
        #self.create_hitbox()

class PlayerHex(TactileHex):

    def __init__(self, pawn, i, settings = None):
        super(PlayerHex, self).__init__(pawn)

        if settings == None:
            self.delta = (50, 0)#pixels
            self.center = (50, 450)#pixel
        
        offset = (self.delta[0] * i, self.delta[1] * i)
        self.eucl = tuple(map(sum, zip(self.center, offset)))

        self.create_images()
        #self.create_hitbox()

class SheetHex(TactileHex):

    def __init__(self, hcp, settings = None):
        self.hcp = hcp

        if settings == None:
            self.distance = 38#pixels
            self.center = (300, 225)#pixel

        eucl = hcp_to_eucl(hcp)
        eucl = (self.distance * eucl[0], self.distance * eucl[1])
        self.eucl = tuple(map(sum, zip(eucl, self.center)))

        self.create_images()
        #self.create_hitbox()

    def create_images(self):
        x = self.eucl[0]
        y = self.eucl[1]

        transparent = "images/transparent.png"
        
        self.img = Image(Point(x, y), transparent)
        self.radius = self.img.getWidth() / 2.5
    """def create_hitbox(self):
        width = self.img.getWidth()

        x = self.eucl[0]
        y = self.eucl[1]
        self.radius = width / 2.5

        self.hitbox = Circle(Point(x,y), width / 2.5)
    """
    def draw(self, win): 
        self.img.draw(win)
        #self.hitbox.draw(win)

    def undraw(self):
        #self.hitbox.undraw()
        self.img.undraw()
        

def make_sheet(hive):
    sheet = []
    for hcp in hive.locations():
        sheet.append(SheetHex(hcp))

    if sheet == []: sheet.append(SheetHex(HCP(0,0)))

    return sheet
