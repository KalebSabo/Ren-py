#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       WEAPON CLASS
#
#   CONTENT: 
#       WEAPON CLASS
#       DEAL DAMAGE METHOD
#
#   DESCRIPTION:
#       
#
#############################

init 1 python:
    class Weapon(Equipment):    #THIS CLASS IS FOR ALL EQUIPPABLE WEAPONS
        def __init__(self, name, base_image, type= "Weapon", durability= 0, style= 0, weight= 0, damage = 0, power = 0, armor_pen = 0):   #type must remain unchanged
            super().__init__(name, base_image, type, durability, style)
            self.weight = weight
            self.damage = damage
            self.power = power
            self.armor_pen = armor_pen

            
            
        






