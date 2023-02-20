"""
Lights Off Game.

A game with the objective of turning off all lights
by clicking on them. Clicking on a light toggles it
on or off and affects all adjacent lights as well.

Main executable for game.

Author: Steven Colclough
Current Version: v1.0.0
"""

from config import Config
from game_screen import GameScreen as GS
from launch_screen import LaunchScreen as LS
from options_screen import OptionsScreen as OS


if __name__ == "__main__":
    playing = True
    config = Config()

    # GAME LOOP
    while playing:
        # Welcome Screen
        choice = LS(config).display()

        # Game Sceen
        if choice == "start":
            choice = GS(config).display()

        if choice == "options":
            OS(config).display()

        # Exit Game
        if choice == "exit":
            playing = False
            config.save_config()
