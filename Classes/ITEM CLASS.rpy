#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       ITEM CLASS
#
#   CONTENT: 
#       ITEM CLASS
#
#   DESCRIPTION:
#
#############################


init 1 python:


    class Item: # THIS CLASS IS FOR ANYTHING THAT CAN GO INTO AN INVENTORY
        def __init__(self, name = "", base_image= "", type= ""):
            self.name = name
            self.base_image = base_image
            self.type = type

    
    ###############################################

    class Equipment(Item):  # THIS CLASS IS FOR EQUIPPABLE ITEMS
        def __init__(self, name, base_image, type= "Equipment", durability= 0, style= 0):
            super().__init__(name, base_image, type)
            self.durability = durability
            self.style = style
