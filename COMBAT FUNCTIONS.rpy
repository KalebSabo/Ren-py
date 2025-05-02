#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       COMBAT FUNCTIONS
#
#   CONTENT: 
#       COMBAT INITIALIZATION MEASURES
#
#   DESCRIPTION:
#       CORE STAT INTERACTION FUNCTIONS
#
#############################


init python:


    List_of_Combatants = []
    currentEnemy = ""
    current_debilitation_level = 0





    tooltip = GetTooltip()

    def getTurnOrder(args): # INSERT ALL COMBATANT OBJECTS, RETURNS A SORTED LIST BASED ON LUCK
        y = []
        for x in args:
            y.append(x)

        y.sort(key= lambda s: s.luck, reverse= False)

        return y 

    def plusDebilitation(current_debilitation_level): # INSERT CURRENT DEBILITATION LEVEL, RETURNS +1 DEBILITATION
        current_debilitation_level += 1
        if current_debilitation_level >= 5:
            current_debilitation_level = 5

        return current_debilitation_level
        
    def getCompanion_specials(player_confidence): # PLAYER CONFIDENCE AS ARGUMENT, RETURNS COMPANION LEVEL
        if player_confidence == 0:
            companion_level = 0
        elif player_confidence ==  1:
            companion_level = 1
        elif player_confidence ==  2:    
            companion_level = 2
        elif player_confidence ==  3:    
            companion_level = 3 
        elif player_confidence ==  4:
            companion_level = 4
        elif player_confidence == 5:
            companion_level = 5
        
        return companion_level

    def getPerceptionView(player_perception): # PLAYER PERCEPTION AS ARGUMENT, RETURNS INTEL LEVEL
        intel_level = player_perception
        if player_perception > 5:           # CHECKS IF PLAYER PERCEPTION MIGHT BE OUT OF RANGE AND RESETS IT
            player_perception = 5
            intel_level = player_perception
        return intel_level

    def getItemAccessLevel(player_strength): # INSERT PLAYER STRENGTH, RETURNS WEIGHT LEVEL
        if player_strength == 0:
            weight_level = 0
        elif player_strength ==  1:
            weight_level = 1
        elif player_strength ==  2:    
            weight_level = 2
        elif player_strength ==  3:    
            weight_level = 3 
        elif player_strength ==  4:
            weight_level = 4
        elif player_strength == 5:
            weight_level = 5
        
        return weight_level

    

        