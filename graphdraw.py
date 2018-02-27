""" Graphdraw: Drawing helpers for graphical things """

from graphics import *

from color import Color

def updateHive(hive, win):
    pass

def updatePlayer(player, win, settings = None):
    
    startat = None

    if settings == None:
        startat = (50, 450)

    location = startat
    delta = (50, 0)

    for pawn in list(player.pawns):

        print(location)
        draw_pawn(pawn, location, win)
        location = tuple(map(sum, zip(location, delta)))

def draw_pawn(pawn, location, win):

    x = location[0]
    y = location[1]

    (pawn_imgfile, color_imgfile) = pawn_image_lookup(pawn)
    
    color_graphic = Image(Point(x, y), color_imgfile)
    pawn_graphic  = Image(Point(x, y), pawn_imgfile)

    color_graphic.draw(win)
    pawn_graphic.draw(win)


def pawn_image_lookup(pawn):
    """ Lookup image, then return a sprite. """

    colorfile = 'images/';

    if pawn.color == Color.WHITE:
        colorfile += 'White.png'

    if pawn.color == Color.BLACK:
        colorfile += 'Black.png'

    typefile = 'images/' + str(pawn) + ".png"

    # T E M P O R A R Y TODO T E M P O R A R Y FIXME
    return (typefile, colorfile)
