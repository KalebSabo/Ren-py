#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       MAIN SCRIPT
#
#   CONTENT:
#        STARTING POINT OF THE GAME
#
#   DESCRIPTION:
#       THIS SCRIPT IS THE BEGINNING OF THE GAME
#############################





# The game starts here.

label start:

    ##############################   CHARACTER CREATION  ##########################################
    #$ player.setName()
    
    #call screen CompanionSelection
    
    


    ##############################      INTRODUCTION/BEGIN GAME  ####################################
    #scene IntroductionEviron at reset      # BEGINS THE GAME WITH INTRODUCTION SCENE

    #call IntroEnvironment                  # CALLS PREFIGHT INTRODUCTION ENVIRONMENT
    #call screen EnvironmentSelection       # SETS BUTTONS ON SCREEN TO GET ENVIRONMENT SPECIALS
    


            # WILL NEED TO GET WHAT CHARACTERS/COMPANIONS ARE MET

    $ combatants = [player, strong_minion, smart_minion]
    call Combat

    #############################    END CREDITS  ####################################################
    #call EndCredits
    
    
    return








label IntroEnvironment:
    show screen TreeButton
    show screen CornButton
    show screen SunlightButton
    return


label HideIntroEnviron:
    hide screen TreeButton
    hide screen CornButton
    hide screen SunlightButton
    return

    
