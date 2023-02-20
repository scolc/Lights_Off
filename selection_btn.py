"""
The buttons that the player can use to select an option.
"""

from tkinter import *
from typing import Callable

from config import Config


class SelectionBtn():
    """
    The selection button class.

    Used to store the selection variables.

    Manages the selection state.
    """

    def __init__(self,
                 win: Toplevel,
                 width,
                 height,
                 id: str,
                 action: Callable,
                 config: Config) -> None:
        """
        @param win The game window.
        @param width The width of the button
        @param height The height of the button
        @param id The button colour id.
        @param action The button command method.
        @param config The config.
        """
        # Initialise config
        self.config = config

        # Position
        self.id = id

        # Button properties
        self.selected = False

        self.frame = Frame(win,
                           width=width,
                           height=height,
                           background=self.config.col_win_bg,
                           highlightbackground=self.config.col_frame_border,
                           highlightthickness=0)

        self.btn = Button(self.frame,
                          command=lambda: action(id=self.id),
                          background=self.config.colours[self.id]["col_01"],
                          activebackground=(self.config
                                            .colours[self.id]["col_03"]))

        self.btn.place(relx=0.5,
                       rely=0.5,
                       width=width * 0.8,
                       height=height * 0.8,
                       anchor="center")

    def place(self, x, y) -> None:
        """
        Places the frame at (x, y).
        """
        self.frame.place(x=x, y=y)

    def flip(self) -> None:
        """
        This method flips the state of the button.
        """
        if self.selected:
            # Deselection
            self.selected = False
            self.frame["highlightthickness"] = 0
        else:
            # Selection
            self.selected = True
            self.frame["highlightthickness"] = 1
