"""
A config file to hold all the application settings.
"""

class Config():
    """
    The config class.
    
    Used to store all the settings.
    """

    def __init__(self) -> None:
        # Tile size
        self.tile_size = 50
        self.btn_font = "Calibri " + str(int(self.tile_size / 3))
        self.msg_font = "Calibri " + str(int(self.tile_size / 4))

        # Light button colours
        self.col_light_on = "#ffec00" # Yellow
        self.col_light_off = "#525252" # Grey
        self.col_frame_border = "#000000" # Black

        # Window
        self.col_win_bg = "#26c6da"