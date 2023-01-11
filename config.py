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
        self.tile_size = 60
        self.btn_font = "Calibri " + str(int(self.tile_size / 3))
        self.msg_font = "Calibri " + str(int(self.tile_size / 4))
        self.msg_font_large = "Calibri " + str(int(self.tile_size / 2.5))

        # Button colours
        self.col_light_on = "#ffec00" # Yellow
        self.col_light_off = "#525252" # Grey
        self.col_btn_active = "#f8feb5" # Light Yellow

        # Window General
        self.col_win_bg = "#26c6da" # Light Blue
        self.col_frame_border = "#000000" # Black

        # Image files
        self.icon = "images/lights_off.ico"
        self.bg_01 = "images/bg_01.png"
        self.bg_02 = "images/bg_02b.png"
        


#    def load_image(self, filename: str, colour: str):
#        """
#        Handles loading the images used in the program.
#        If an image can't be found, it returns the colour code
#        as a string instead.
#
#        @param filename The filepath for the image to use
#        @param colour The colour code to use if the file cannot be found
#        @return The image or colour that will be used
#        """
#        #try:
#        #    Image.open(filename)
#            
#        # Favicon
#
#        # Window BG
#
#        # Frame BG
#
#        pass

