"""
A config file to hold all the application settings.
"""

import json


class Config():
    """
    The config class.

    Used to store all the settings.
    """

    def __init__(self) -> None:
        # Load config settings from file
        self.main = self.load_config()
        self.colours = self.load_colours()

        # Tile size
        self.tile_size = self.main["tile_size"]
        self.font_med = self.main["font"] + " " + str(int(self.tile_size / 3))
        self.font_small = (self.main["font"] + " "
                           + str(int(self.tile_size / 4)))
        self.font_large = (self.main["font"] + " "
                           + str(int(self.tile_size / 2.5)))

        self.update()

    def load_config(self) -> dict:
        """
        Retrieves config data from file and returns it.
        """
        try:
            # Open file
            input_file = open("config.json", "r", encoding="utf-8")

            # Load data
            config = json.load(input_file)
            input_file.close()
        except FileNotFoundError:
            # Default config
            config = {"tile_size": 60,
                      "font": "Calibri",
                      "icon": "images/lights_off.ico",
                      "current": "blue"}

        return config

    def load_colours(self) -> dict:
        """
        Retrieves colour data from file and returns it.
        """
        try:
            # Open file
            input_file = open("colours.json", "r", encoding="utf-8")

            # Load data
            colours = json.load(input_file)
            input_file.close()
        except FileNotFoundError:
            # Default colour options with no files
            colours = {"blue": {"id": "blue",
                                "col_01": "#24e1f2",
                                "col_02": "#192526",
                                "col_03": "#8cf5ff",
                                "col_04": "#000000",
                                "file_01": "images/bg_blue_01.png",
                                "file_02": "images/bg_blue_02.png"}}

            self.main["current"] = "blue"

        return colours

    def save_config(self):
        """
        Saves the config data to file.
        """
        # Create empty file
        output_file = open("config.json", "w", encoding="utf-8")

        # Save to file
        json.dump(self.main, output_file, indent=4)
        output_file.close()

    def update(self):
        """
        Updates the colour settings.
        """
        # Button colours
        # col_01 = main colour for light on, primary bg etc
        # col_02 = colour for light off, secondary bg etc
        # col_03 = colour for button press, default window bg etc
        # col_04 = colour for frame borders
        self.col_light_on = self.colours[self.main["current"]]["col_01"]
        self.col_light_off = self.colours[self.main["current"]]["col_02"]
        self.col_btn_active = self.colours[self.main["current"]]["col_03"]

        # Window General
        self.col_win_bg = self.colours[self.main["current"]]["col_03"]
        self.col_frame_border = self.colours[self.main["current"]]["col_04"]

        # Image files
        self.icon = self.main["icon"]
        self.bg_01 = self.colours[self.main["current"]]["file_01"]
        self.bg_02 = self.colours[self.main["current"]]["file_02"]
