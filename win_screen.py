"""
The win screen for the game.

The player is informed that they have won the game.
"""

from tkinter import *

from config import Config


class WinScreen():
    """
    The win screen class.
    
    Handles the creation of the win screen window, display of the button
    and the player interaction.
    """

    def __init__(self, game_win: Tk) -> None:
        # Initialise config
        self.config = Config()
        
        # Window Settings
        self.game_win = game_win
        self.congrats = Toplevel(game_win)
        self.win_cols = 6
        self.win_rows = 4

        # Message
        self.message = Label(self.congrats,
                             text="Congratulations",
                             font=self.config.btn_font)
        
        # Button
        self.back = Button(self.congrats,
                           text="Back",
                           font=self.config.btn_font,
                           command=lambda: self.button_press())

    # Display Function
    def display(self) -> None:
        """
        This function handles displaying the window.
        """
        # Prevent user interacting with main game window
        self.congrats.grab_set()

        # Window properties
        self.congrats.title("Lights Off!")
        self.congrats.resizable(width=False, height=False)
        self.congrats["bg"] = self.config.bg_window

        pad = int(self.config.tile_size / 2)
        win_width = int(self.win_cols * self.config.tile_size)
        win_height = int(self.win_rows * self.config.tile_size)

        screen_width = self.congrats.winfo_screenwidth()
        screen_height = self.congrats.winfo_screenheight()

        win_x = int(screen_width / 2 - win_width / 2)
        win_y = int(screen_height * 25/100)

        #win_x = int(self.game_win.winfo_x() +
        #            (self.game_win.winfo_width() / 2 - win_width / 2))
        #win_y = int(self.game_win.winfo_y() +
        #            (self.game_win.winfo_height() / 2 - win_height / 2))        

        self.message.place(x=pad,
                           y=pad,
                           width=win_width - (pad * 2),
                           height=self.config.tile_size)

        self.back.place(x=pad,
                        y=self.config.tile_size + (pad * 2),
                        width=win_width - (pad * 2),
                        height=self.config.tile_size)

        self.congrats.geometry(str(win_width) +
                            "x" +
                            str(win_height) +
                            "+" +
                            str(win_x) +
                            "+" +
                            str(win_y))

        # Display the congrats window and resume the game window once closed
        self.game_win.wait_window(self.congrats)

    # Button Function
    def button_press(self) -> None:
        """
        This function handles the button press and closes the window.
        """
        self.congrats.destroy()
