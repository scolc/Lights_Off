"""
The welcome screen for the game.

The player chooses to either play a grid or exit the game.
"""

from tkinter import *

from config import *


class LaunchScreen():
    """
    The Welcome screen class.
    
    Handles the creation of the launch window, display of the buttons
    and the player interaction.
    """

    def __init__(self):
        # Initialise config
        self.config = Config()
        
        # Window Settings
        self.launch = Tk()
        self.win_cols = 6
        self.win_rows = 4

        self.start = Button(self.launch,
                            text="Start",
                            command=lambda: self.button_choice("start"))

        self.exit = Button(self.launch,
                           text="Exit",
                           command=lambda: self.button_choice("exit"))

        # Button Choice
        self.choice = ""

    # Display Method
    def display(self) -> None:

        pad = int(self.config.tile_size / 2)
        win_width = int(self.win_cols * self.config.tile_size)
        win_height = int(self.win_rows * self.config.tile_size)

        screen_width = self.launch.winfo_screenwidth()
        screen_height = self.launch.winfo_screenheight()

        win_x = int(screen_width / 2 - win_width / 2)
        win_y = int(screen_height * 25/100)

        self.start.place(x=pad,
                         y=pad,
                         width=win_width - (pad * 2),
                         height=self.config.tile_size)

        self.exit.place(x=pad,
                        y=self.config.tile_size + (pad * 2),
                        width=win_width - (pad * 2),
                        height=self.config.tile_size)

        self.launch.geometry(str(win_width) +
                            "x" +
                            str(win_height) +
                            "+" +
                            str(win_x) +
                            "+" +
                            str(win_y))

        self.launch.mainloop()

    # Button Method
    def button_choice(self, choice):
        self.choice = choice
        self.launch.destroy()
