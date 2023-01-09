"""
The welcome screen for the game.

The player chooses to either play a grid or exit the game.
"""

from tkinter import *

from config import Config


class LaunchScreen():
    """
    The Welcome screen class.
    
    Handles the creation of the launch window, display of the buttons
    and the player interaction.
    """

    def __init__(self) -> None:
        # Initialise config
        self.config = Config()
        
        # Window Settings
        self.launch = Tk()

        # Buttons
        self.start = Button(self.launch,
                            text="Start",
                            font=self.config.btn_font,
                            command=lambda: self.button_choice("start"))

        self.exit = Button(self.launch,
                           text="Exit",
                           font=self.config.btn_font,
                           command=lambda: self.button_choice("exit"))

        # Button Choice
        self.choice = ""

    # Display Function
    def display(self) -> str:
        """
        This function handles displaying the launch window.

        @return The player choice string.
        """
        # Window Settings
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
        welcome_frame = Frame(self.launch,
                              highlightthickness=1,
                              highlightbackground=self.config.col_frame_border)
        
        welcome_message = ("Welcome to Lights Off!\n\n" +
                           "Click 'Start' to play or\n'Exit' to quit.")
        
        welcome_label = Label(welcome_frame,
                              text=welcome_message,
                              font=self.config.msg_font)
        
        current_y = pad
        win_rows = pad_rows

        welcome_frame_rows = 3
        welcome_frame.place(x=pad,
                            y=current_y,
                            width=widget_width,
                            height=welcome_frame_rows * self.config.tile_size)
        
        welcome_label.place(relx=0.5,
                            rely=0.5,
                            anchor="center")
        
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

        win_height = int(win_rows * self.config.tile_size)

        self.launch.geometry(str(win_width) +
                            "x" +
                            str(win_height) +
                            "+" +
                            str(win_x) +
                            "+" +
                            str(win_y))
        
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
