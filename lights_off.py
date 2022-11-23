"""
Lights Off Game.

A game with the objective of turning off all lights by clicking on them.
Clicking on a light toggles it on or off and affects all adjacent lights as well.

Main executable for game.
"""


from launch_screen import *
from game_screen import *


if __name__ == "__main__":
    playing = True
    print("started")
    
    # GAME LOOP
    while playing:
        # Welcome Screen
        launch_sc = LaunchScreen()
        #launch_sc.display()
        choice = launch_sc.display()
        

        # Game Sceen
        
        if choice == "start":
            print("launching game screen")
            game_sc = GameScreen()
            choice = game_sc.display()
            
        if choice == "exit":
            print("stopping")
            playing = False

    # Exit Game
print ("stopped")