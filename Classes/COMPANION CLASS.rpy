#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       COMPANION CLASS
#
#   CONTENT: 
#       COMPANION CLASS
#
#   DESCRIPTION:
#       SUPPORTING CHARACTERS FOR THE PLAYER
#############################


init python:
    class Companion(Char):
        def __init__(self, name= "", base_image = "", current_health= 5, max_health= 5, comp_specials= [], comp_level = 0):
            super().__init__(name, base_image, current_health, max_health)
            self.comp_specials = comp_specials 
            self.comp_level = comp_level

    
    brother = Companion(name= "Brother", base_image= "images/test characters/BrotherPNG_%s.png", current_health= 5, max_health= 5)
    henchman = Companion(name= "Henchman", base_image= "images/test characters/Minion1PNG_%s.png", current_health= 5, max_health= 5)
    