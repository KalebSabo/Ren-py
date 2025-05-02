#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       ARMOR LIST
#
#   CONTENT: 
#       ARMOR LIST
#       
#
#   DESCRIPTION:
#       EACH ARMOR HAS A SET OF ATTRIBUTES
#       
#       DURABILTY, STYLE, WEIGHT, DAMAGE_REDUCTION, PRESCENCE, DODGE
#############################


init 5 python:

    no_armor = Armor(name= "No Armor", base_image= "", durability= 1000, style= 0, weight= 0, damage_reduction= 0, presence= 1, dodge= 5)
    light_armor = Armor(name= "Light Armor", base_image="", durability= 1, style= 0, weight=1, damage_reduction= 1, presence= 2, dodge= 4)
    medium_armor = Armor(name= "Medium Armor", base_image= "", durability= 3, style= 0, weight= 2, damage_reduction= 2, presence= 3, dodge= 2)
    heavy_armor = Armor(name= "Heavy Armor", base_image= "", durability= 3, style= 0, weight= 3, damage_reduction= 3, presence= 4, dodge= 1)
    legendary_armor = Armor(name= "Legendary Armor", base_image= "", durability= 5, style= 0, weight= 5, damage_reduction= 3, presence= 4, dodge= 1)
