#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       COMBAT SCRIPT
#
#   CONTENT: 
#       COMBAT SEQUENCE
#
#   DESCRIPTION:
#       BASIC COMBAT SCRIPT THAT TAKES X NUMBER OF COMBATANTS AND FIGHTS IN TURN ORDER
#
#############################


screen statsUI:
    style_prefix "statsUI"
    
    frame:
        add Solid("#ffff")
        add "UI/bg_frame.png":
            xsize 300
            ysize 200    
        xsize 300
        ysize 200
        xpos 1920
        xalign 1.0
        xoffset -20     # x side borders
        yoffset 200     # y side borders
        xanchor 1.0  # anchor position of the item, inside the item
        text "hello"

    frame:      # will wrap around the hbox
        xpadding 20
        ypadding 10 # space around the boxes
        xalign 0.5
        yalign 0.5
        hbox:           # horizontal box
            spacing 20
            text "Charm"
            text "Kindness"
            text "Guts"

        hbox:
            spacing 20
            vbox:
                text "C3harm"
            vbox:
                text "1"

            text "kind"
            text "2"

            text "Guts"
            text "3"

style statsUI_text:     # Changes every text in that particular screen 
    size 40             
    color "#ce2121ff"

style statsUI_vbox:
    spacing 20


screen MainmenuUI:
    