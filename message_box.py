"""
The messages displayed in the game windows, placed
within a frame.
"""

from tkinter import *
from PIL import ImageTk, Image

from config import Config

class MessageBox():
    """
    The Message class.
    
    Creates a message of custom text within a frame.
    """

    def __init__(self,
                 toplevel: Toplevel,
                 width,
                 height,
                 text,
                 config: Config,
                 font_size = "normal") -> None:
        """
        @param toplevel The TopLevel container.
        @param width The width of the message frame.
        @param height The height of the message frame.
        @param text The message text.
        @param config The config.
        @param font_size Text font size to use, "normal" (default) or "large"
        """
        self.width = width
        self.height = height
        self.text = text
        self.config = config
        self.frame = Frame(toplevel,
                           width=self.width,
                           height=self.height,
                           highlightthickness=1,
                           highlightbackground=self.config.col_frame_border)
        self.canvas = Canvas(self.frame,
                             highlightthickness=0)
        self.create_canvas(font_size=font_size)

    def create_canvas(self, font_size) -> Frame:
        """
        Constructs the message canvas.
        """
        try:
            self.canvas_bg_img = ImageTk.PhotoImage(Image.open(self.config.bg_02).resize((int(self.width), int(self.height))))
            self.canvas_image = self.canvas.create_image(0, 0, image=self.canvas_bg_img, anchor="nw")
        except:
            self.canvas["bg"] = self.config.col_win_bg

        self.canvas.place(x=0,
                     y=0,
                     relwidth=1,
                     relheight=1)

        if font_size == "large":
            font = self.config.font_large
        elif font_size == "normal":
            font = self.config.font_med
        else:
            font = self.config.font_small

        self.canvas.create_text((self.width / 2),
                           (self.height / 2),
                           anchor="center",
                           text=self.text,
                           font=font,
                           justify="center")

    def place(self, x, y) -> None:
        """
        Places the frame at (x, y).
        """
        self.frame.place(x=x, y=y)
    
    def update(self) -> None:
        """
        Updates the colour scheme when a new button is selected.
        """
        try:
            self.canvas_bg_img = ImageTk.PhotoImage(Image.open(self.config.bg_02).resize((int(self.width), int(self.height))))
            self.canvas.itemconfig(self.canvas_image, image=self.canvas_bg_img)
        except:
            self.canvas["bg"] = self.config.col_win_bg
