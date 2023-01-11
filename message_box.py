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
        self.canvas_bg_img = ""
        self.frame = self.create_frame(toplevel=toplevel, font_size=font_size)

    def create_frame(self, toplevel: Toplevel, font_size) -> Frame:
        """
        Constructs the message frame and returns it.

        @return the message frame.
        """
        frame = Frame(toplevel,
                      width=self.width,
                      height=self.height,
                      highlightthickness=1,
                      highlightbackground=self.config.col_frame_border)

        canvas = Canvas(frame,
                        highlightthickness=0)

        try:
            #print("started frame")
            #print(f"width={self.width}")
            #print(f"height={self.height}")
            self.canvas_bg_img = ImageTk.PhotoImage(Image.open(self.config.bg_02).resize((int(self.width), int(self.height))))
            canvas.create_image(0, 0, image=self.canvas_bg_img, anchor="nw")
            #print("worked")
        except:
            canvas["bg"] = self.config.col_win_bg

        canvas.place(x=0,
                     y=0,
                     relwidth=1,
                     relheight=1)
        
        if font_size == "large":
            font = self.config.msg_font_large
        else:
            font = self.config.msg_font
        

        canvas.create_text((self.width / 2),
                           (self.height / 2),
                           anchor="center",
                           text=self.text,
                           font=font,
                           justify="center")
        
        return frame
