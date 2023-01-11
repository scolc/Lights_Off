"""
The welcome screen for the game.

The player chooses to either play a grid or exit the game.
"""

from tkinter import *
from PIL import ImageTk, Image

from config import Config
from message_box import MessageBox


class LaunchScreen():
    """
    The Welcome screen class.
    
    Handles the creation of the launch window, display of the buttons
    and the player interaction.
    """

    def __init__(self, config: Config) -> None:
        """
        @param config The config
        """
        # Initialise config
        self.config = config
        
        # Window Settings
        self.launch = Tk()
        self.win_canvas = Canvas(self.launch,
                                 highlightthickness=0)

        # Buttons
        self.start = Button(self.win_canvas, #self.launch,
                            text="Start",
                            font=self.config.btn_font,
                            command=lambda: self.button_choice("start"),
                            border=5,
                            background=self.config.col_light_on,
                            activebackground=self.config.col_btn_active)

        self.exit = Button(self.win_canvas, #self.launch,
                           text="Exit",
                           font=self.config.btn_font,
                           command=lambda: self.button_choice("exit"),
                           border=5,
                           background=self.config.col_light_on,
                           activebackground=self.config.col_btn_active)

        # Button Choice
        self.choice = ""

    # Display Function
    def display(self) -> str:
        """
        This function handles displaying the launch window.

        @return The player choice string.
        """
        # Initial Window Settings
        self.launch.title("Lights Off!")
        self.launch.resizable(width=False, height=False)
        self.launch["bg"] = self.config.col_win_bg

        win_cols = 6
        pad_rows = 0.5
        pad = int(self.config.tile_size * pad_rows)
        win_width = int(win_cols * self.config.tile_size)
        widget_width = win_width - (pad * 2)

        screen_width = self.launch.winfo_screenwidth()
        screen_height = self.launch.winfo_screenheight()

        win_x = int(screen_width / 2 - win_width / 2)
        win_y = int(screen_height * 25/100)

        # Widget Placement
        # Welcome Message
#        welcome_frame = Frame(self.win_canvas, #self.launch,
#                              highlightthickness=1,
#                              highlightbackground=self.config.col_frame_border)
        
        welcome_message = ("Welcome to Lights Off!\n\n" +
                           "Click 'Start' to play or\n'Exit' to quit.")
        
#        welcome_canvas = Canvas(welcome_frame,
#                                highlightthickness=0)
        
        current_y = pad
        win_rows = pad_rows

        welcome_frame_rows = 3
        welcome_frame_height = welcome_frame_rows * self.config.tile_size
#        welcome_frame.place(x=pad,
#                            y=current_y,
#                            width=widget_width,
#                            height=welcome_frame_height)

#        try:
#            welcome_canvas_bg_img = ImageTk.PhotoImage(Image.open(self.config.bg_02).resize((widget_width, welcome_frame_height)))
#            welcome_canvas.create_image(0, 0, image=welcome_canvas_bg_img, anchor="nw")
#        except:
#            welcome_canvas["bg"] = self.config.col_win_bg
#
#        welcome_canvas.place(x=0,
#                             y=0,
#                             relwidth=1,
#                             relheight=1)
#
#        welcome_canvas.create_text((widget_width / 2),
#                                   (welcome_frame_height / 2),
#                                   anchor="center",
#                                   text=welcome_message,
#                                   font=self.config.msg_font,
#                                   justify="center")

        welcome_frame = MessageBox(toplevel=self.win_canvas,
                                   width=widget_width,
                                   height=welcome_frame_height,
                                   text=welcome_message,
                                   config=self.config)

        welcome_frame.frame.place(x=pad, y=current_y)

        win_rows += welcome_frame_rows + pad_rows
        current_y = win_rows * self.config.tile_size
        
        # Buttons
        button_rows = 1
        
        self.start.place(x=pad,
                         y=current_y,
                         width=widget_width,
                         height=button_rows * self.config.tile_size)

        win_rows += button_rows + pad_rows
        current_y = win_rows * self.config.tile_size

        self.exit.place(x=pad,
                        y=current_y,
                        width=widget_width,
                        height=self.config.tile_size)
        
        win_rows += button_rows + pad_rows

        # Update Window Size
        win_height = int(win_rows * self.config.tile_size)

        self.launch.geometry(str(win_width) +
                            "x" +
                            str(win_height) +
                            "+" +
                            str(win_x) +
                            "+" +
                            str(win_y))
        
        try:
            win_canvas_bg_img = ImageTk.PhotoImage(Image.open(self.config.bg_01).resize((int(win_width), int(win_height))))
            self.win_canvas.create_image(0, 0, image=win_canvas_bg_img, anchor="nw")
        except:
            self.win_canvas["bg"] = self.config.col_win_bg
        
        self.win_canvas.place(x=0,
                              y=0,
                              relwidth=1,
                              relheight=1)

        # Set Icon
        try:
            img = self.config.icon
            Image.open(self.config.icon)
        except:
            img = ""

        self.launch.iconbitmap(img)
        self.launch.protocol("WM_DELETE_WINDOW", func=lambda: self.button_choice("exit"))
        self.launch.mainloop()
        return self.choice

    # Button Function
    def button_choice(self, choice) -> None:
        """
        This function handles the button press and closes the window.

        @param choice The button choice text.
        """
        self.choice = choice
        self.launch.destroy()
