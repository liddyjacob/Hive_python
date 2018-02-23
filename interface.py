class Controller:

    def __init__(self):
        pass



class Keyboard(Controller):

    def __init__(self):
        pass


class Preload(Controller):
    
    def __init__(self):
        pass


class Display:
    
    def __init__(self):
        pass

class NoDisplay(Display):

    def __init__(self):
        pass

class CommandLine(Display):
    
    def __init__(self):
        pass


class Interface:
    """ An Interface is an input and output form """

    def __init__(self, controller, display):
        self.controller = controller
        self.display = display

    def move(self, player, hive):
        return NotImplemented


def Default_Interface():
    return Interface(Keyboard(), CommandLine())
