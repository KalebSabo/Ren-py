#from game.Classes.Characters.character_class import Character

init 2 python:
    class Enemy(Character):
        def __init__(self, character_name, current_health, max_health, inventory,  
                        force, analysis, faith, manipulation, authority,
                        is_alive, special_list, unique_special):
            super().__init__(character_name, current_health, max_health, inventory,  
                        force, analysis, faith, manipulation, authority,
                        is_alive, special_list)
            self.unique_special = unique_special
            