"""
The main sceen for the game.

The player clicks on light buttons to turn them on or off.
"""

import random
from tkinter import *
from config import Config
from light_btn import *


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
        self.game.title("Lights Off!")
        self.game.resizable(width=False, height=False)
        self.game["bg"] = self.config.bg_window

        # Exit Button
        self.exit = Button(self.game,
                           text="Exit",
                           font=self.config.btn_font,
                           command=lambda: self.button_choice("exit"))
        
        # Player choice to continue or exit
        self.choice = ""


    def display(self) -> str:
        """
        This method handles displaying the game window.

        @return The player choice string.
        """
        # Sizes
        pad = int(self.config.tile_size / 2)
        win_width = int(self.grid_size * self.config.tile_size + pad * 2)
        win_height = int(self.grid_size * self.config.tile_size + self.config.tile_size + pad * 3)

        screen_width = self.game.winfo_screenwidth()
        screen_height = self.game.winfo_screenheight()

        win_x = int(screen_width / 2 - win_width / 2)
        win_y = int((screen_height - win_height) / 4)

        self.game.geometry(str(win_width) +
                            "x" +
                            str(win_height) +
                            "+" +
                            str(win_x) +
                            "+" +
                            str(win_y))

        # Create grid
        current_y = pad
        for row_num in range(self.grid_size):
            current_x = pad
            row = []
                    
            for col_num in range(self.grid_size):
                light = LightBtn(win=self.game,
                                 row=row_num,
                                 col=col_num,
                                 action=self.light_press)
                
                light.light_btn.place(x=current_x,
                                      y=current_y,
                                      width=self.config.tile_size,
                                      height=self.config.tile_size)
                
                row.append(light)                
                current_x += self.config.tile_size
            
            self.grid.append(row)
            current_y += self.config.tile_size

        self.exit.place(x=pad,
                        y=win_height - pad - self.config.tile_size,
                        width=win_width - (pad * 2),
                        height=self.config.tile_size)

        self.random_grid()
        
        self.game.mainloop()

        return self.choice

    # Button Methods
    def button_choice(self, choice):
        """
        This method handles the button press and closes the window.

        @param choice The button choice text.
        """
        self.choice = choice
        self.game.destroy()
                
    def light_press(self, row, col) -> None:
        """
        This method handles the action when a light is pressed.
        
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
            # Winning condition met, close window
            self.button_choice(choice="")
    
    # Functionality

    def random_grid(self) -> None:
        """
        This method randomly sets the lights of the grid.
        """
        # Create list of indices to represent grid columns
        indices = list(range(self.grid_size))
        
        for row_num in range(len(self.grid)):
            # Shuffle the indices and select a random number of them to flip
            random.shuffle(indices)
            n_indices = random.randint(0, int(self.grid_size * 75 / 100))

            for i in range(n_indices):
                self.light_press(row=row_num, col=i)


    
    def check_win(self) -> bool:
        """
        This method checks the grid to see if the win condition has been met.
        
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


