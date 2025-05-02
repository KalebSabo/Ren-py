#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       PLAYER UI
#
#   CONTENT: 
#       CONTAINS MULTIPLE UI INTERFACES
#
#   DESCRIPTION:
#       UI INTERFACES
#
#############################

init: 
    screen playerUI:
        if combat:
            $ player.base_image= "firstperson_hold_sword.png"         ## IF COMBAT IS TRUE, SETS PLAYER IMAGE TO HAVE SWORD IN HAND
        else:
            $ player.base_image= "FPVReach.png"

        add "[player.base_image]" at center
            