"""
The options screen for the game.

Allows the player to set options that update the config.
"""

from tkinter import *

from PIL import Image, ImageTk

from config import Config
from message_box import MessageBox
from options_colours import OptionsColours


class OptionsScreen():
    """
    The options screen class.

    Handles creation of the options and updates config based
    on user selection.
    """

    def __init__(self, config: Config) -> None:
        """
        @param config The config.
        """
        # Initialise config
        self.config = config

        # Window Settings
        self.options = Tk()
        self.options_canvas = Canvas(self.options,
                                     highlightthickness=0)

        self.message_frame = ""

        # Button
        self.save = Button(self.options_canvas,
                           text="Save & Exit",
                           font=self.config.font_med,
                           command=lambda: self.button_press(),
                           border=5,
                           background=self.config.col_light_on,
                           activebackground=self.config.col_btn_active)

        self.choice = ""

    def display(self) -> None:
        """
        This function handles displaying the window.
        """
        # Initial Window Settings
        self.options.title("Lights Off! - Options")
        self.options.resizable(width=False, height=False)
        self.options["bg"] = self.config.col_win_bg

        pad_rows = 0.5
        pad = int(self.config.tile_size * pad_rows)
        win_cols = 6
        self.win_width = int(win_cols * self.config.tile_size)
        widget_width = self.win_width - (pad * 2)

        screen_width = self.options.winfo_screenwidth()
        screen_height = self.options.winfo_screenheight()

        win_x = int(screen_width / 2 - self.win_width / 2)
        win_y = int(screen_height * 25/100)

        # Widget Placement
        # Options Message
        current_y = pad

        message_frame_rows = 2
        message_frame_height = message_frame_rows * self.config.tile_size

        self.message_frame = MessageBox(toplevel=self.options_canvas,
                                        width=widget_width,
                                        height=message_frame_height,
                                        text="Options",
                                        config=self.config,
                                        font_size="large")

        self.message_frame.place(x=pad, y=current_y)
        self.options_canvas.itemref = self.message_frame

        current_y += message_frame_height + pad

        # Colour Setting Frame
        self.options_frame = OptionsColours(toplevel=self.options_canvas,
                                            width=widget_width,
                                            updater=self.update,
                                            config=self.config)
        self.options_frame.place(x=pad, y=current_y)

        current_y += self.options_frame.height + pad

        # Button
        btn_height = self.config.tile_size

        self.save.place(x=pad,
                        y=current_y,
                        width=widget_width,
                        height=btn_height)

        current_y += btn_height + pad

        # Update Window Size
        self.win_height = int(current_y)

        self.options.geometry(str(self.win_width) +
                              "x" +
                              str(self.win_height) +
                              "+" +
                              str(win_x) +
                              "+" +
                              str(win_y))

        try:
            optns_canv_bg_img = (ImageTk
                                 .PhotoImage(Image
                                             .open(self.config.bg_01)
                                             .resize((int(self.win_width),
                                                      int(self.win_height)))))
            self.canvas_image = (self.options_canvas
                                 .create_image(0, 0,
                                               image=optns_canv_bg_img,
                                               anchor="nw"))
        except FileNotFoundError:
            self.options_canvas["bg"] = self.config.col_win_bg

        self.options_canvas.place(x=0,
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
        self.options.iconbitmap(img)
        self.options.protocol("WM_DELETE_WINDOW", func=self.button_press)
        self.options.mainloop()

    # Button Function
    def button_press(self) -> None:
        """
        This function handles the button press and closes the window.
        """
        self.options.destroy()

    def update(self) -> None:
        """
        Updates the colour scheme when a new button is selected.
        """
        self.options["bg"] = self.config.col_win_bg
        try:
            optns_cnv_bg_img = (ImageTk
                                .PhotoImage(Image.open(self.config.bg_01)
                                            .resize((int(self.win_width),
                                                    int(self.win_height)))))
            self.options_canvas.itemconfig(self.canvas_image,
                                           image=optns_cnv_bg_img)
            self.options_canvas.imgref = optns_cnv_bg_img
        except FileNotFoundError:
            self.options_canvas["bg"] = self.config.col_win_bg

        # Message Frame
        self.message_frame.update()

        # Button
        self.save["bg"] = self.config.col_light_on
        self.save["activebackground"] = self.config.col_btn_active
