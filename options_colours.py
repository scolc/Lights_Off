"""
The frame to handle the colour picker for the options screen.

Automatically sizes the frame to match the number of colours
available in the config file.
"""

from tkinter import *
from typing import Callable

from config import Config
from selection_btn import SelectionBtn


class OptionsColours():
    """
    The options colour frame class.

    Handles creation of a custom sized frame.
    Stores the player's colour selection.
    """

    def __init__(self,
                 toplevel: Toplevel,
                 width,
                 updater: Callable,
                 config: Config) -> None:
        """
        @param toplevel The TopLevel container.
        @param width The width of the frame.
        @param config The config.
        """
        self.width = width
        self.height = 0
        self.config = config
        self.canvas_bg_img = ""
        self.selection = ""
        self.buttons = []
        self.updater = updater
        self.frame = Frame(toplevel,
                           width=self.width,
                           height=self.height,
                           background=self.config.col_win_bg,
                           highlightthickness=1,
                           highlightbackground=self.config.col_frame_border)
        self.canvas = Canvas(self.frame,
                             highlightthickness=0)
        self.create_frame()

    def create_frame(self) -> None:
        """
        Constructs the colour selection frame and returns it.
        """
        # Initial Frame Settings
        pad_rows = 0.25
        pad = self.config.tile_size * pad_rows
        current_y = pad

        # Canvas Text Space

        self.canvas.create_text((self.width / 2),
                                current_y,
                                anchor="n",
                                text="Select A Colour Scheme",
                                font=self.config.font_med)

        current_y += self.config.tile_size

        # Create Buttons
        # Iterate through the available colours and create a button for each.
        btn_width = self.config.tile_size
        btn_height = self.config.tile_size
        for entry in self.config.colours:
            btn = SelectionBtn(self.canvas,
                               width=btn_width,
                               height=btn_height,
                               id=entry,
                               action=self.update_selection,
                               config=self.config)
            self.buttons.append(btn)

        # Place each button
        btn_space_width = self.width - (pad * 2)
        btn_x = pad + (btn_space_width % btn_width / 2)
        for btn in self.buttons:
            # Check if another button will fit
            if btn_x + btn_width > btn_space_width:
                btn_x = pad + (btn_space_width % btn_width / 2)
                current_y += btn_height

            btn.place(x=btn_x, y=current_y)
            # Check if button matches current selection
            if btn.id == self.config.main["current"]:
                btn.flip()
                self.selection = btn.id

            # Update coords
            btn_x += btn_width

        current_y += btn_height + pad

        self.height = current_y

        self.canvas["bg"] = self.config.col_win_bg

        self.canvas.place(x=0,
                          y=0,
                          relwidth=1,
                          relheight=1)

        return self.frame

    def place(self, x, y) -> None:
        """
        Places the frame at (x, y).
        """
        self.frame.place(x=x,
                         y=y,
                         width=self.width,
                         height=self.height)

    def update_selection(self, id) -> None:
        """
        Updates the selected button and alters the current
        colour scheme to match.
        """
        # Button State
        for btn in self.buttons:
            if btn.id == id and not btn.selected:
                # Button matches id and not in selected state
                btn.flip()
            elif btn.selected and not (btn.id == id):
                # Button is previous selection
                btn.flip()
                self.selection = id
                self.config.main["current"] = id

        self.config.update()
        self.frame["bg"] = self.config.col_win_bg
        self.canvas["bg"] = self.config.col_win_bg
        for btn in self.buttons:
            btn.frame["bg"] = self.config.col_win_bg
        self.updater()
