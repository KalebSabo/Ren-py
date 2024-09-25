#COMBAT FILE : 
# 
# FOCUS ON COMBAT AND STATS

init python: 
    
    class Player():
        def __init__(self, name = "", portrait = "", current_health = 100, max_health = 100, current_stamina = 100, max_stamina = 100, intelligence = 0, strength = 0, luck = 0, endurance = 0, charisma = 0, abilities = [], equipped_weapon = '', equipped_armor = ''):
            self.name = name                                                                
            self.portrait = portrait
            self.current_health = current_health                    #CREATING THE PLAYER 
            self.max_health = max_health
            self.abilities = abilities
            self.equipped_weapon = equipped_weapon
            self.intelligence = intelligence
            self.strength = strength
            self.luck = luck
            self.endurance = endurance
            self.charisma = charisma
            self.current_stamina = current_stamina
            self.max_stamina = max_stamina
            self.equipped_armor = equipped_armor

    class Companion():
        def __init__(self, name = "", portrait = "", current_health = 100, max_health = 100, abilities = [], attack = 0, defend = 0):
            self.name = name 
            self.portrait = portrait
            self.current_health = current_health
            self.max_health = max_health
            self.abilities = abilities
            self.attack = attack
            self.defend = defend
    
    class Weapon():
        def __init__(self, name = "", description = "", base_damage = 0, ranged = False, melee = False, throw = False, parry = False, has_ammo = False, ammo_count = 0, makeshift = False, assisting = False, personal = False, w_type = "", stamina_drain = 0):
            self.name = name
            self.description = description                      # CREATES WEAPONS
            self.base_damage = base_damage
            self.ranged = ranged
            self.melee = melee
            self.throw = throw
            self.parry = parry
            self.has_ammo = has_ammo
            self.makeshift = makeshift
            self.assisting = assisting
            self.personal = personal
            self.ammo_count = ammo_count
            self.w_type = w_type
            self.stamina_drain = stamina_drain

        def getCritEffect(self, actor, target, damage):                     # CALL THIS AND PASS IN THE DAMAGE PARAMETER TO RETURN A SWORD CRIT
            if actor.equipped_weapon.w_type == 'Sword':
                renpy.say(who = None, what = "The Sword strikes with critical effect! reducing lost stamina!")
                actor.current_stamina = actor.current_stamina / (actor.equipped_weapon.stamina_drain / 2) 
                target.current_health -= actor.equipped_weapon.base_damage
                


            elif actor.equipped_weapon.w_type == 'Gun':
                
                target.current_health -= actor.equipped_weapon.base_damage          #might not need the equipped_weapon
                renpy.say(who = None, what = "The Gun strikes with critical effect! ignoring armor!")
            
            elif actor.equipped_weapon.w_type == 'Bow':
                
                target.current_health -= (actor.equipped_weapon.base_damage - actor.equipped_armor.damage_reduction) + 10 
                renpy.say(who = None, what = "The Bow strikes with critical effect! dealing 10 extra damage!")

            elif actor.equipped_weapon.w_type == 'Dagger':
                renpy.say(who = None, what = "The Dagger strikes with critical effect!")
                "TBD"                                         ########## needs turns   ##############
            
            elif actor.equipped_weapon.w_type == 'Club':
                
                target.current_health -= actor.equipped_weapon.base_damage
                renpy.say(who = None, what = "The Club strikes with critical effect! ignoring armor!")

            elif actor.equipped_weapon.w_type == 'Nail':
                actor.current_health += 10
                renpy.say(who = None, what = "The Butcher's Nail strikes with critical effect! regaining 10 health!", who_color = '#fc0000ff')    
            
            return 

        def dealDamage(self, actor, target, damage):                    # CHECKS IF THE DAMAGE IS ABOVE 20, IF IT IS RETURNS TRUE OR FALSE BASED ON IT, THOUGHT IT WOULD BE COOL AT 20 DAMAGE YOU CRIT
            if damage > 20:
                if actor == butchertest:
                    renpy.show("playercriticalblink", layer = "transient")
                    renpy.pause()

                    renpy.say(what = "The Butcher Crit!")
                    p.equipped_weapon.getCritEffect(actor = butchertest, target = p, damage = butchertest.equipped_weapon.base_damage)
                    return
                elif actor == p:
                    
                    renpy.show("butchercriticalblink", layer = "transient", behind = "[p.portrait]")
                    
                    renpy.say(Boss1, "GAHHHH!")
                    butchertest.equipped_weapon.getCritEffect(actor = p, target = butchertest, damage = p.equipped_weapon.base_damage)
                    return
            else: 
                
                target.current_health = target.current_health - (actor.equipped_weapon.base_damage - target.equipped_armor.damage_reduction) 
                renpy.say(who = None, what = f"{actor.name} dealt damage with their {actor.equipped_weapon.name}!")
            return



    class Armor():
        def __init__(self, name, damage_reduction):
            self.damage_reduction = damage_reduction
            self.name = name


    class Butcher():
        def __init__(self, portrait, current_health, max_health, abilities, equipped_weapon, equipped_armor):
            self.current_health = current_health
            self.max_health = max_health                            # CREATES THE BUTCHER
            self.abilities = abilities
            self.equipped_weapon = equipped_weapon
            self.portrait = portrait
            self.equipped_armor = equipped_armor

        def isDead(self):
            deathanswer = self.current_health < 0                   # CHECKS IF THE CHARACTER YOU PASS IN IS DEAD
            return deathanswer  

        def getAngry(self):
            if self.current_health <= 50:                           # CALL THIS TO CHECK PASSED IN CHARACTER HP IF IT IS READY FOR THE NEXT PHASE AND DISPLAY THEIR NEW FORM
                if self == butchertest:
                    self.portrait = "butcher_angry.png"
            return

        
    
    class Ability():                                    # SIMPLE ABILITY CREATION FOR NOW, ONLY NAME AND DESCRIPTION
        def __init__(self, name, description):
            self.name = name
            self.description = description


##################################   MISC   ##################################       
screen PlayerHUD():
    vbox:
        xalign 0.2 yalign 0.8
        text "PC HP: [p.current_health]"
        text "PC Weapon Damage: [p.equipped_weapon.base_damage]"
        text "PC armor: [p.equipped_armor.damage_reduction]"

screen criticaltextblink():
    vbox:
        xalign 0.8 yalign 0.4
        text "A CRITICAL HIT!!!" 
    

image playercriticalblink:
    animation
    "firstperson_hold_sword.png" 
    pause 0.2
    "firstperson_hold_sword_bw.png"
    pause 0.2
    repeat 3
    

image butchercriticalblink: 
    animation
    "butcher_angry.png"
    pause 0.2
    "butcher_normal.png"
    pause 0.2
    repeat 3
    
screen ButcherHealthDisplay():
    vbox:
        xalign 0.7 yalign 0.5 
        text "HP: [butchertest.current_health]" 
        text "Armor: [butchertest.equipped_armor.damage_reduction]"


default damage = 0

##########################  ARMOR   ####################################
define noarmor = Armor("No Armor", 5)

################################ WEAPONS    #################################
define rusty_sword = Weapon("Rusty Sword", "Not much of a sword really", 5, False, True, 1, True, False, 0, False, False, False, 'Sword', 10)
define nail = Weapon("The Nail", "A grotesque weapon the Butcher uses with deadly precision that restores his HP on crits.", 15, False, True, False, True, False, 0, False, False, False, 'Nail', 10)
define club = Weapon("Club", "A club that does massive damage at high stamina drain, critcals ignore armor", 15, False, True, 1, False, False, 0, False, False, True, 'Club', 25)
define dagger = Weapon("Dagger", "A small blade that allows the bearer to observe and strike with accuracy and precision", 5, False, True, 1, True, False, 0, False, True, True, 'Dagger', 5)
define gun = Weapon("Gun", "A small blackpowder gun that carries one shot, but one shot is all you need", 50, True, False, 1, False, True, 1, False, True, False, 'Gun', 5)


######################    ABILITIES  ########################################
define phase_jump = Ability("Phase Jump", "The Butcher has sped up! He has become a blurs!")
define quick_slash = Ability("Quick Slash", "If phase jump is active, The Butcher strikes twice!")
define ravage = Ability("RAVAGE", "Double attack, Triple if phase jump is active. The Butcher is stunned for a turn!")
define protect = Ability("PROTECT!", "Your brother has stepped in and taken the blow!")
define syncattk = Ability("Synchronized Attack!", "Both your brother and you attack together as one!")


###################  THE BUTCHER   ########################################
define Boss1 = Character("The Butcher", who_color = "#e22121")
default butchertest = Butcher(portrait = "butcher_normal.png",current_health = 100, max_health = 100, abilities = [phase_jump, quick_slash, ravage], equipped_weapon = nail, equipped_armor = noarmor)


##################  PLAYER  #############################################
#define p = Character("[playername]",who_color = "#424ef5")

###################  COMPANIONS   ########################################

define brother = Companion(Character(name = "Brother", who_color = "#59eef3ff"), "old_man_w_watermark.png", 100, 100, [], 10, 10)



label test():
    define config.window_auto_hide = [ 'pause' ]
    python:
        #playername = renpy.input("What is your Name ", length = 32)                 
        #playername = playername.strip()
        #player = Player(playername, "firstperson_hold_sword.png", 100, 100, [], rusty_sword)
        p = Player(Character(renpy.input("What is your name : ", allow = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', length = 12, copypaste = False), who_color = "#4126b9"),"firstperson_hold_sword.png", 100, 100, 100, 100, 0, 0, 0, 0, 0, [], rusty_sword, noarmor)   # ASKS THE PLAYER FOR NAME AND SETS IT
        
        #c = Player(Character("The Companion", who_color = "#39e7d0ff"), "old_man_w_watermark.png",100, 100, 100, 100, 0, 0, 0, 0, 0, [], rusty_sword, noarmor)
    pause
    scene notebook
    #$ p.equipped_weapon.dealDamage(p, butchertest, 21)

    menu:
        "Rusty Sword, 10 attack damage, sword critical effect of halving stamina drain, 10 stam drain":
            $ p.equipped_weapon = rusty_sword
            "You have choosen the rusty sword!"
        "The Gun, 50 attack damage, one shot, crits ignore armor, 5 stam drain":
            $ p.equipped_weapon = gun
            "You have choosen the gun!"
        "The Club, 25 attack, crits ignore armor, 25 stam drain":
            $ p.equipped_weapon = club
            "You have choosen the Club!"
        

    #$ p.equipped_weapon.dealDamage(p, butchertest, p.equipped_weapon.base_damage)

    #"The battle begins!""Combat Loop Beginning""What are the reasons for the battle?""To beat the Butcher"
    #"What Characters could possibly participate?""The Player, The Butcher, The Companion, The Twins"
    #"What Outside Forces could possibly participate?""None""What stat should change before the fight?""None"
    #"What Companions could possibly participate?""The Companion""What endings could possibly happen?""Player Defeat, Player Success"

    pause



    #python:
    #    stats = []
    #    for i in dir(p):
    #        if i == 'strength' or i == 'endurance' or i == 'luck' or i == 'intelligence' or i == 'charisma':   
    #            p.i = int(renpy.input(f"Please set your {i} : ", allow = "1234567890", length = 2))
    #            while p.i >= 11:
    #                p.i = int(renpy.input("Invalid! Please choose a number 10 or less! : ", allow = "1234567890", length = 2)) 
    #            
    #            stats.append(i)
    #        else:
    #            pass


    #screen StatSet():
    #    hbox:
    #        xalign 0.1 yalign 0.5
    #        text "Please select stats to increase : "
    #        textbutton "Strength"
    #        textbutton "Charisma"
    #        textbutton "Endurance"
    #        textbutton "Luck"
    #        textbutton "Intelligence"

            

    #show screen StatSet
    "Beginning Steps..."
    
    #play music "PW New Combat Loop.mp3" volume 0.5 loop

    show image "[butchertest.portrait]" with moveintop

    #show text "Butcher HP: [butchertest.current_health]" at xalign 0.7 yalign 0.5

    show screen ButcherHealthDisplay
    show screen PlayerHUD

    show image "[p.portrait]" with moveinbottom 

    show image "[brother.portrait]" at right

    jump OptionsStep

    pause
    
    return

label OptionsStep:

    pause .2
    call screen Option_Choice  # THIS CALLS THE OPTIONS SCREEN ABOVE THE CURRENT SCREEN SO YOU STILL SEE COMBAT
    
    

    



    



screen Option_Choice():

    vbox:
        xalign 0.5 yalign 0.5 spacing 20 
        textbutton "Dialogue" action Jump("Dialogue_Option")
        textbutton "Fight" action Jump("Fight_Option")
        textbutton "Defend" action Jump("Defend_Option")                ## PUTS FOUR BUTTONS ON SCREEEN TO JUMP TO THEIR RESPECTIVE OPTIONS
        textbutton "Run" action Jump("Run_Option") 


label Dialogue_Option:
    "TBD"
    return

label Fight_Option:
    pause .2
    menu: 
        "Attack with [p.equipped_weapon.name]!":
            $ p.equipped_weapon.dealDamage(p, butchertest, p.equipped_weapon.base_damage)
        "Special: Heavy Attack!" if p.strength >= 5:
            $ p.equipped_weapon.dealDamage(p,butchertest, p.equipped_weapon.base_damage + 10) 
        
    jump OptionsStep

    
    return

label Defend_Option:

    return

label Run_Option:

    return