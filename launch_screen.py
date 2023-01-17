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
        self.launch_canvas = Canvas(self.launch,
                                    highlightthickness=0)

        # Buttons
        self.start = Button(self.launch_canvas,
                            text="Start",
                            font=self.config.font_med,
                            command=lambda: self.button_choice("start"),
                            border=5,
                            background=self.config.col_light_on,
                            activebackground=self.config.col_btn_active)

        self.options = Button(self.launch_canvas,
                              text="Options",
                              font=self.config.font_med,
                              command=lambda: self.button_choice("options"),
                              border=5,
                              background=self.config.col_light_on,
                              activebackground=self.config.col_btn_active)

        self.exit = Button(self.launch_canvas,
                           text="Exit",
                           font=self.config.font_med,
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
        welcome_message = ("Welcome to Lights Off!\n\n" +
                           "Click 'Start' to play or\n'Exit' to quit.")
        
        current_y = pad

        welcome_frame_rows = 3
        welcome_frame_height = welcome_frame_rows * self.config.tile_size

        welcome_frame = MessageBox(toplevel=self.launch_canvas,
                                   width=widget_width,
                                   height=welcome_frame_height,
                                   text=welcome_message,
                                   config=self.config)

        welcome_frame.place(x=pad, y=current_y)

        current_y += welcome_frame_height + pad
        
        # Buttons
        button_height = self.config.tile_size
        
        self.start.place(x=pad,
                         y=current_y,
                         width=widget_width,
                         height=button_height)

        current_y += button_height + pad

        self.options.place(x=pad,
                           y=current_y,
                           width=widget_width,
                           height=button_height)

        current_y += button_height + pad

        self.exit.place(x=pad,
                        y=current_y,
                        width=widget_width,
                        height=button_height)
        
        current_y += button_height + pad

        # Update Window Size
        win_height = int(current_y)

        self.launch.geometry(str(win_width) +
                            "x" +
                            str(win_height) +
                            "+" +
                            str(win_x) +
                            "+" +
                            str(win_y))
        
        try:
            win_canvas_bg_img = ImageTk.PhotoImage(Image.open(self.config.bg_01).resize((int(win_width), int(win_height))))
            self.launch_canvas.create_image(0, 0, image=win_canvas_bg_img, anchor="nw")
        except:
            self.launch_canvas["bg"] = self.config.col_win_bg
        
        self.launch_canvas.place(x=0,
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
