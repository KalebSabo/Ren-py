#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       ENVIRONMENT SPECIALS LIST
#
#   CONTENT:
#        ENVIRONMENT SPECIAL OBJECTS
#
#   DESCRIPTION:
#       CLICKING BUTTONS IN AN ENVIRONMENT WILL GIVE ACCESS TO THESE SPECIALS
#############################

init python:
    class EnviroSp:
        def __init__(self, name= "", description= ""):
            self.name = name
            self.description = description
            