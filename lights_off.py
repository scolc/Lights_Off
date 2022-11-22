"""
Lights Off Game.

A game with the objective of turning off all lights by clicking on them.
Clicking on a light toggles it on or off and affects all adjacent lights as well.

Main executable for game.
"""


from launch_screen import *


if __name__ == "__main__":
    playing = True
    # GAME LOOP
    while playing:
        print("started")
    
        # Welcome Screen
        launch_sc = LaunchScreen()
        launch_sc.display()

        # Game Sceen

        playing = False

    # Exit Game
print ("stopped")