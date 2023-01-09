"""
The main sceen for the game.

The player clicks on light buttons to turn them on or off.
"""

import random
from tkinter import *
from config import Config
from light_btn import LightBtn
from win_screen import WinScreen


class GameScreen():
    """
    The game screen class.
    
    Handles the main functionality of the game.
    """

    def __init__(self) -> None:
        # Initialise config
        self.config = Config()

        # Grid
        self.grid_size = 5
        self.grid = []

        # Window settings
        self.game = Tk()

        # Exit Button
        self.exit = Button(self.game,
                           text="Exit",
                           font=self.config.btn_font,
                           command=lambda: self.button_choice("exit"))
        
        # Player choice to continue or exit
        self.choice = ""

    # Display Function
    def display(self) -> str:
        """
        This function handles displaying the game window.

        @return The player choice string.
        """
        # Window Properties
        self.game.title("Lights Off!")
        self.game.resizable(width=False, height=False)
        self.game["bg"] = self.config.col_win_bg

        pad_rows = 0.5
        pad = int(self.config.tile_size * pad_rows)
        
        # Widget Placement
        # Game Message
        message_frame = Frame(self.game,
                              highlightthickness=1,
                              highlightbackground=self.config.col_frame_border)
        
        message = ("Click a light to turn it on or off.\n" +
                   "Each adjacent light will also switch.\n\n" +
                   "Turn off all the lights to win!")
        
        message_label = Label(message_frame,
                              text=message,
                              font=self.config.msg_font)
        
        widget_width = self.grid_size * self.config.tile_size + 2 * pad
        current_y = pad
        win_rows = pad_rows

        message_frame_rows = 2.5
        message_frame.place(x=pad,
                            y=current_y,
                            width=widget_width,
                            height=message_frame_rows * self.config.tile_size)
        
        message_label.place(relx=0.5,
                            rely=0.5,
                            anchor="center")

        win_rows += message_frame_rows + pad_rows
        current_y = win_rows * self.config.tile_size

        # Create grid
        grid_frame = Frame(self.game,
                           highlightthickness=1,
                           highlightbackground=self.config.col_frame_border,
                           bg=self.config.col_win_bg)

        grid_frame.place(x=pad,
                         y=current_y,
                         width=widget_width,
                         height=widget_width)

        grid_y = pad
        for row_num in range(self.grid_size):
            grid_x = pad
            row = []
                    
            for col_num in range(self.grid_size):
                light = LightBtn(win=grid_frame,
                                 row=row_num,
                                 col=col_num,
                                 action=self.light_press)
                
                light.light_btn.place(x=grid_x,
                                      y=grid_y,
                                      width=self.config.tile_size,
                                      height=self.config.tile_size)
                
                row.append(light)                
                grid_x += self.config.tile_size
            
            self.grid.append(row)
            grid_y += self.config.tile_size

        win_rows += self.grid_size + pad_rows * 3
        current_y = win_rows * self.config.tile_size
        

        # Button
        button_rows = 1
        self.exit.place(x=pad,
                        y=current_y,
                        width=widget_width,
                        height=button_rows * self.config.tile_size)

        win_rows += button_rows + pad_rows

        # Generate a puzzle
        self.random_grid()
        
        # Display the window

        screen_width = self.game.winfo_screenwidth()
        screen_height = self.game.winfo_screenheight()

        win_width = int(widget_width + pad * 2)
        win_height = int(win_rows * self.config.tile_size)

        win_x = int(screen_width / 2 - win_width / 2)
        win_y = int((screen_height - win_height) / 4)

        self.game.geometry(str(win_width) +
                           "x" +
                           str(win_height) +
                           "+" +
                           str(win_x) +
                           "+" +
                           str(win_y))

        self.game.protocol("WM_DELETE_WINDOW", func=lambda: self.button_choice("exit"))
        self.game.mainloop()

        return self.choice

    # Button Functions
    def button_choice(self, choice) -> None:
        """
        This function handles the button press and closes the window.

        @param choice The button choice text.
        """
        self.choice = choice
        self.game.destroy()
                
    def light_press(self, row, col) -> None:
        """
        This function handles the action when a light is pressed.
        
        @param row The row the light is in.
        @param col The column the light is in.
        """
        # Flip current button
        self.grid[row][col].flip()

        # Flip surrounding buttons
        # Left
        if col != 0: # Not the left edge
            self.grid[row][col - 1].flip()
        
        # Right
        if col != self.grid_size - 1: # Not the right edge
            self.grid[row][col + 1].flip()

        # Up
        if row != 0: # Not the top edge
            self.grid[row - 1][col].flip()
        
        # Down
        if row != self.grid_size - 1: # Not the bottom edge
            self.grid[row + 1][col].flip()
        
        if self.check_win():
            # Winning condition met, display congrats
            WinScreen(game_win=self.game).display()
            
            # Close window and return to the launch screen
            self.button_choice(choice="")
    
    # Game Functionality
    def random_grid(self) -> None:
        """
        This function randomly sets the lights of the grid to form the starting puzzle.
        """
        # Create list of indices to represent grid columns and rows
        col_indices = list(range(self.grid_size))
        row_indices = list(range(self.grid_size))

        # Shuffle the row indices to affect rows in random order
        random.shuffle(row_indices)

        for row_num in row_indices:
            # Shuffle the col indices and select a random number of them to flip
            random.shuffle(col_indices)
            num_indices = random.randint(0, int(self.grid_size))
            
            for i in range(num_indices):
                self.light_press(row=row_num, col=col_indices[i])

    def check_win(self) -> bool:
        """
        This function checks the grid to see if the win condition has been met.
        
        @return True if game has been won, False otherwise.
        """
        # Lights on counter
        lights_on = 0

        # Check each button state in the grid 
        for row in self.grid:
            for btn in row:
                if btn.state == "on":
                    # Add 1 to the counter
                    lights_on += 1
        
        if lights_on == 0:
            # Winning condition met
            return True
        else:
            return False


