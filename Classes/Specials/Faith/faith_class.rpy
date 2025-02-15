#from game.Classes.Specials.special_class import Special

init 2 python:
    class Faith(Special):
        def __init__(self, special_name, special_description):
            super().__init__(special_name, special_description)
            self.special_name = "Faith"
            self.special_description = "Use your faith to heal yourself or others."
            self.faith = 1