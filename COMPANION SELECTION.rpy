#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       COMPANION SELECTION
#
#   CONTENT:
#        CONTAINS POSSIBLE COMPANIONS AND THEIR SELECTION
#
#   DESCRIPTION:
#       
#############################

init 7:
# NEED TO PUT AFTER THEY MAKE A SELECTION TO CALL SETNAME FUNCTION!


    screen CompanionSelection:
        $ tooltip = GetTooltip()
        if tooltip:
                text "[tooltip]":
                    xalign 0.48
                    yalign 0.1
        hbox:
            
            xalign 0.5
            yalign 0.5
            imagebutton:
                auto str(brother.base_image)
                tooltip "Brother"  
                action [SetVariable("player.companion", brother), Hide(screen= 'CompanionSelection'), Return()]
            imagebutton:
                auto str(henchman.base_image)
                tooltip "Henchman"
                action [SetVariable("player.companion", henchman), Hide(screen= 'CompanionSelection'), Return()]
        
        