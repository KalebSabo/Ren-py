#from game.Classes.Specials.special_class import Special

init 2 python:
    class Authority(Special):
        def __init__(self, special_name, special_description):
            super().__init__(special_name, special_description)
            self.special_name = "Authority"
            self.special_description = "Use your authority to command others."
            self.authority = 1