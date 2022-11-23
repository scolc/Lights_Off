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
        self.tile_size = 32

        # Light button colours
        self.light_btn_on = "#ffec00" # Yellow
        self.light_btn_off = "#525252" # Grey