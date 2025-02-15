#from Classes.character_class import Character

init 2 python:

    class Player(Character):
        def __init__(self, character_name, current_health, max_health, inventory,  
                        force, analysis, faith, manipulation, authority, is_alive,
                        special_list, companion,):
            super().__init__(character_name, current_health, max_health, inventory,  
                        force, analysis, faith, manipulation, authority, is_alive,
                        companion, special_list)
            self.companion = companion
        
        def initialize_player(self):
            self.character_name = "Player"
            self.current_health = 100
            self.max_health = 100
            self.force = 1
            self.analysis = 1
            self.faith = 1
            self.manipulation = 1
            self.authority = 1
            self.inventory = []
            self.is_alive = True
            self.special_list = []
            self.companion = None