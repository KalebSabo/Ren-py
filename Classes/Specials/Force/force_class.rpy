#from game.Classes.Specials.special_class import Special

init 2 python:
    class Force(Special):
        def __init__(self, special_name, special_description):
            super().__init__(special_name, special_description)
            self.special_name = "Force"
            self.special_description = "Use your force to push others back."
            self.force = 1