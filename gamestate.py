from enum import Enum

class Gamestate(Enum):
    INGAME = 0
    STALEMATE = 1 # No player can move
    VICTORY = 2
    DRAW = 3 # Both players have queen surrounded
    END = 4

 
