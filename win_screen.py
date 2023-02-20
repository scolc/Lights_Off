"""
The win screen for the game.

The player is informed that they have won the game.
"""

from tkinter import *

from PIL import Image, ImageTk

from config import Config
from message_box import MessageBox


class WinScreen():
    """
    The win screen class.

    Handles the creation of the win screen window, display of the button
    and the player interaction.
    """

    def __init__(self, game_win: Tk, config: Config) -> None:
        """
        @param config The config
        """
        # Initialise config
        self.config = config

        # Window Settings
        self.game_win = game_win
        self.congrats = Toplevel(game_win)
        self.congrats_canvas = Canvas(self.congrats,
                                      highlightthickness=0)

        # Button
        self.back = Button(self.congrats,
                           text="Back",
                           font=self.config.font_med,
                           command=lambda: self.button_press(),
                           border=5,
                           background=self.config.col_light_on,
                           activebackground=self.config.col_btn_active)

    # Display Function
    def display(self) -> None:
        """
        This function handles displaying the window.
        """
        # Prevent user interacting with main game window
        self.congrats.grab_set()

        # Initial Window settings
        self.congrats.title("Lights Off! - Congratulations")
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
        current_y = pad
        win_rows = pad_rows

        message_frame_rows = 2
        message_frame_height = message_frame_rows * self.config.tile_size

        message_frame = MessageBox(toplevel=self.congrats_canvas,
                                   width=widget_width,
                                   height=message_frame_height,
                                   text="Congratulations!",
                                   config=self.config,
                                   font_size="large")

        message_frame.frame.place(x=pad, y=current_y)

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

        # Update Window Size
        win_height = int(win_rows * self.config.tile_size)

        self.congrats.geometry(str(win_width) +
                               "x" +
                               str(win_height) +
                               "+" +
                               str(win_x) +
                               "+" +
                               str(win_y))

        try:
            congrats_canvas_bg_img = (ImageTk
                                      .PhotoImage(Image.open(self.config.bg_01)
                                                  .resize((int(win_width),
                                                           int(win_height)))))
            self.congrats_canvas.create_image(0, 0,
                                              image=congrats_canvas_bg_img,
                                              anchor="nw")
        except FileNotFoundError:
            self.congrats_canvas["bg"] = self.config.col_win_bg

        self.congrats_canvas.place(x=0,
                                   y=0,
                                   relwidth=1,
                                   relheight=1)

        # Set Icon
        try:
            img = self.config.icon
            Image.open(self.config.icon)
        except FileNotFoundError:
            img = ""

        # Display the congrats window and resume the game window once closed
        self.congrats.iconbitmap(img)
        self.congrats.protocol("WM_DELETE_WINDOW", func=self.button_press)
        self.game_win.wait_window(self.congrats)

    # Button Function
    def button_press(self) -> None:
        """
        This function handles the button press and closes the window.
        """
        self.congrats.destroy()
