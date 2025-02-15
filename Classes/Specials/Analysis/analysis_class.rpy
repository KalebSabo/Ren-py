#from game.Classes.Specials.special_class import Special

init 2 python:

    class Analysis(Special):
        def __init__(self, special_name, special_description):
            super().__init__(special_name, special_description)
            self.special_name = "Analysis"
            self.special_description = "Analyze the situation and make the best decision."
            self.analysis = 1

