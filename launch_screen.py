"""
The welcome screen for the game.

The player chooses to either play a grid or exit the game.
"""

from tkinter import *


class LaunchScreen():
    """
    The Wwelcome screen class.
    
    Handles the creation of the window, display of the buttons
    and the player interaction.
    """

    def __init__(self):
        self.launch = Tk()
        self.launch.geometry = ("500x500")
        self.start = Button(self.launch, text="Start")
        self.start.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.exit = Button(self.launch, text="Exit")
        self.exit.place(relx=0.5, rely=0.6, anchor=CENTER)


    def display(self):
        self.launch.mainloop()