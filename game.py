""" game.py: Cycling a hive game """

from hivegame import Gamestate

def run_game(hivegame):
    
    hivegame.start()

    while (hivegame.gamestate == Gamestate.INGAME):
        hivegame.step()

    hivegame.step()
    while True: pass

    if (hivegame.gamestate == Gamestate.END):
        return
