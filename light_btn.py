"""
The buttons that represent the lights for the game.
"""

from tkinter import *
from typing import Callable

from config import Config


class LightBtn():
    """
    The light button class.
    
    Used to store the light's variables.

    Manages the light state and position in the grid.
    """

    def __init__(self,
                 win: Toplevel,
                 row,
                 col,
                 action: Callable) -> None:
        """
        @param win The game window
        @param row The row the light is in
        @param col The column the light is in
        @param action The button command method
        """
        # Initialise config
        self.config = Config()

        # Position
        self.row = row
        self.col = col

        # Button properties
        self.state = "off"
        
        self.light_btn = Button(win, command=lambda: action(row=self.row, col=self.col))
        self.light_btn["bg"] = self.config.col_light_off

    def flip(self) -> None:
        """
        This method flips the state and colour of the button.
        """
        if self.state == "on":
            # Switch the light off
            self.state = "off"
            self.light_btn["bg"] = self.config.col_light_off
        else:
            # Switch the light on
            self.state = "on"
            self.light_btn["bg"] = self.config.col_light_on