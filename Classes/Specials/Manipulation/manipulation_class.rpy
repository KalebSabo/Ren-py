#from game.Classes.Specials.special_class import Special

init 2 python:
    class Manipulation(Special):
        def __init__(self, special_name, special_description):
            super().__init__(special_name, special_description)
            self.special_name = "Manipulation"
            self.special_description = "Use your manipulation to control others."
            self.manipulation = 1

    

