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
        settings = self.load_config()
        self.main = settings["main"]
        self.colours = settings["colours"]

        # Tile size
        #self.tile_size = 60
        #self.font_med = "Calibri " + str(int(self.tile_size / 3))
        #self.font_small = "Calibri " + str(int(self.tile_size / 4))
        #self.font_large = "Calibri " + str(int(self.tile_size / 2.5))
        self.tile_size = self.main["tile_size"]
        self.font_med = self.main["font"] + " " + str(int(self.tile_size / 3))
        self.font_small = self.main["font"] + " " + str(int(self.tile_size / 4))
        self.font_large = self.main["font"] + " " + str(int(self.tile_size / 2.5))

        ## Button colours
        ## col_01 = main colour for light on, primary bg etc
        ## col_02 = colour for light off, secondary bg etc
        ## col_03 = colour for button press, default window bg etc
        ## col_04 = colour for frame borders
#
        ##self.col_light_on = "#ffec00" # Yellow
        ##self.col_light_off = "#525252" # Grey
        ##self.col_btn_active = "#f8feb5" # Light Yellow
        #self.col_light_on = self.colours[self.main["current"]]["col_01"]
        #self.col_light_off = self.colours[self.main["current"]]["col_02"]
        #self.col_btn_active = self.colours[self.main["current"]]["col_03"]
#
        ## Window General
        ##self.col_win_bg = "#26c6da" # Light Blue
        ##self.col_frame_border = "#000000" # Black
        #self.col_win_bg = self.colours[self.main["current"]]["col_03"]
        #self.col_frame_border = self.colours[self.main["current"]]["col_04"]
#
        ## Image files
        ##self.icon = "images/lights_off.ico"
        ##self.bg_01 = "images/bg_yellow_01.png"
        ##self.bg_02 = "images/bg_yellow_02.png"
        #self.icon = self.main["icon"]
        #self.bg_01 = self.colours[self.main["current"]]["file_01"]
        #self.bg_02 = self.colours[self.main["current"]]["file_02"]
        self.update()
        
    def load_config(self) -> dict:
        """
        Retrieves config data from file and returns it.
        """
        # Open file
        input_file = open("config.json", "r", encoding="utf-8")

        # Load data
        config = json.load(input_file)
        input_file.close()

        return config

    def save_config(self):
        """
        Saves the config data to file.
        """
        # Create Dictionary
        config = {}
        config["main"] = self.main
        config["colours"] = self.colours

        # Create empty file
        output_file = open("config.json", "w", encoding="utf-8")

        # Save to file
        json.dump(config, output_file, indent=4)
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
