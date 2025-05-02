#############################
#   
#   PROJECT GRASP
#
#   FILE: PLAYER CLASS
#   
#   CONTENT: PLAYER CLASS/CHILD CLASSES/METHODS ONLY
#
#
#
#
#############################

init 6 python :

    class Player(Char):

        def __init__(self, name = "Player", base_image= "", current_health = 5, max_health = 5, strength= 0, perception= 0, confidence= 0, luck= 0, charisma= 0,
            inventory = [], equipped_weapon= fists, equipped_armor= no_armor, fightsp= [], dialoguesp= [], environsp= [], companion= brother):

            super().__init__(name, base_image, current_health, max_health, strength, perception, confidence, luck, charisma)

            self.inventory = inventory
            self.equipped_weapon = equipped_weapon
            self.equipped_armor = equipped_armor
            self.fightsp = fightsp
            self.dialoguesp = dialoguesp
            self.environsp = environsp
            self.companion = companion

        

            


        def setName(self):
            self.name = renpy.input(prompt= "What is your name? : ", allow= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length= 12)

        def equipItem(self, item):    # ITEM OBJECT TO BE EQUIPPED, CHECKS AND SETS IF EQUIPPABLE
            
            for i in self.inventory:   
                if item == i:
                    if i.type == "Weapon": 
                        
                        possible_weight= i.weight + self.equipped_armor.weight
                        if possible_weight > 5:
                            "Too Heavy! Cannot Equip!"
                            return
                        self.equipped_weapon = item
                        return
                    elif i.type == "Armor":
                        possible_weight= i.weight + self.equipped_weapon.weight
                        if possible_weight > 5: 
                            "Too Heavy! Cannot Equip!"
                            return
                        self.equipped_armor = item
                        return 
           
            renpy.say(who= None,what=(f"You cannot equip the {item.name}!")) 
            return
        
    player = Player(current_health= 5, max_health = 5, luck=0)
    
    


    