#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       ARMOR CLASS
#
#   CONTENT:
#        ARMOR CLASS/CHILD CLASSES/METHODS ONLY
#
#   DESCRIPTION:
#
#############################

init 2 python:
    class Armor(Equipment): #THIS CLASS IS FOR ALL EQUIPPABLE ARMOR
        def __init__(self, name, base_image, type= "Armor", durability= 0, style= 0, weight= 0, damage_reduction=0, presence= 0, dodge=0):
            super().__init__(name, base_image, type, durability, style)
            self.weight = weight
            self.damage_reduction = damage_reduction
            self.presence = presence
            self.dodge = dodge


