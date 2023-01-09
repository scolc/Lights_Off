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
        self.congrats["bg"] = self.config.col_win_bg

        pad_rows = 0.5
        pad = int(self.config.tile_size * pad_rows)
        win_cols = 6
        win_width = int(win_cols * self.config.tile_size)
        widget_width = win_width - (pad * 2)

        screen_width = self.congrats.winfo_screenwidth()
        screen_height = self.congrats.winfo_screenheight()

        win_x = int(screen_width / 2 - win_width / 2)
        win_y = int(screen_height * 25/100)

        # Widget Placement
        # Congrats Message
        message_frame = Frame(self.congrats,
                              highlightthickness=1,
                              highlightbackground=self.config.col_frame_border)

        message_label = Label(message_frame,
                             text="Congratulations!",
                             font=self.config.btn_font)

        current_y = pad
        win_rows = pad_rows

        message_frame_rows = 2
        message_frame.place(x=pad,
                            y=current_y,
                            width=widget_width,
                            height=message_frame_rows * self.config.tile_size)

        message_label.place(relx=0.5,
                            rely=0.5,
                            anchor="center")

        win_rows += message_frame_rows + pad_rows
        current_y = win_rows * self.config.tile_size

        # Button
        button_rows = 1
        self.back.place(x=pad,
                        y=current_y,
                        width=widget_width,
                        height=button_rows * self.config.tile_size)

        win_rows += button_rows + pad_rows
        current_y = win_rows * self.config.tile_size

        win_height = int(win_rows * self.config.tile_size)
        
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
