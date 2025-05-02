#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       CHAR CLASS (CHARACTER)
#
#   CONTENT: 
#       CHARACTER CLASS
#
#   DESCRIPTION:
#       EVERY CHARACTER OBJECT IN THE GAME WILL HAVE THESE ATTRIBUTES
#############################

init python:

    class Char: 
        def __init__(self, name= "", base_image= "", current_health = 5, max_health = 5, strength= 0, 
                        perception= 0, confidence= 0, luck= 0, charisma= 0):
            self.name = name
            self.base_image = base_image
            self.current_health = current_health
            self.max_health = max_health
            self.strength = strength
            self.perception = perception
            self.confidence = confidence
            self.luck = luck
            self.charisma = charisma

    test1 = Char(name= "test1",luck= 1)
    test2 = Char(name= "test2",luck= 2)           # TEST CHARACTERS
    test3 = Char(name= "test3",luck= 3)
    test4 = Char(name= "test4",luck= 3)
            
                

            