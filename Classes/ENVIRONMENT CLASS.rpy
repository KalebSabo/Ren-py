#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       ENVIRONMENT CLASS
#
#   CONTENT:
#        ENVIRONMENT CLASS
#
#   DESCRIPTION:
#       BEFORE FIGHTING AN ENVIRONMENT MOMENT CAN UNLOCK SPECIALS
#############################

init python:
    tooltip = GetTooltip()          # ALL THESE ARE TEMPORARY VARIABLES!!!
    time = 10
    timer_range = 10
    timer_jump = "menu2"
    count = 0
    environSpecial = set()
    treeSpecial = "tree"
    cornSpecial = "corn"
    sunlightSpecial = "sunlight"
    tree_found = False
    corn_found = False
    sunlight_found = False


init: 

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Call(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
    
    




screen EnvironmentSelection():
    on "show" action Show("countdown")


    vbox: 
         
        text "{color=#Ffff}{size=+10}You have 10 seconds to find the Specials!!{/size}{/color}"
        text "{color=#FF0000}{size=+10}Specials Found: [count]{/size}{/color}"
    

    

            
        #imagebutton:
        #    auto "images/environment test/window_%s.png"
            

label menu2:
    call HideIntroEnviron
    if tree_found:
        $ environSpecial.add(treeSpecial)
        "You found the tree!"
    
    if corn_found:
        $ environSpecial.add(cornSpecial)
        "You found the corn!"
    
    if sunlight_found:
        $ environSpecial.add(sunlightSpecial)
        "You found the sun!"

    "You made it" 
    return
            


screen TreeButton():
    imagebutton:
        auto "images/environment test/tree_%s.png"
        xpos 202
        ypos 437
        action [SetVariable("tree_found", True), SetVariable("count", count + 1), Hide()]

screen CornButton():
    imagebutton:
        auto "images/environment test/corn_%s.png"
        xpos 180
        ypos 708
        action [SetVariable("corn_found", True),SetVariable("count", count + 1), Hide()]

screen SunlightButton():
    imagebutton:
        auto "images/environment test/sunlight_%s.png"
        action [SetVariable("sunlight_found", True), SetVariable("count", count + 1), Hide()]