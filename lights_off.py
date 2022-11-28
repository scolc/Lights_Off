"""
Lights Off Game.

A game with the objective of turning off all lights by clicking on them.
Clicking on a light toggles it on or off and affects all adjacent lights as well.

Main executable for game.
"""


#from launch_screen import *
#from game_screen import *
from launch_screen import LaunchScreen as LS
from game_screen import GameScreen as GS


if __name__ == "__main__":
    playing = True
    #print("started")
    
    # GAME LOOP
    while playing:
        # Welcome Screen
        choice = LS().display()

        # Game Sceen
        if choice == "start":
            choice = GS().display()
        
        # Exit Game    
        if choice == "exit":
            playing = False
