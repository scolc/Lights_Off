"""
The main sceen for the game.

The player clicks on light buttons to turn them on or off.
"""

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

        # Exit Button
        self.exit = Button(self.game,
                           text="Exit",
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
        win_y = int(screen_height * 25/100)

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
        self.grid[row][col].flip()

