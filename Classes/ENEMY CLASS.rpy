#############################
#   
#   PROJECT GRASP
#
#   FILE: 
#       ENEMY CLASS
#
#   CONTENT: 
#       ENEMY CLASS
#
#   DESCRIPTION:
#       CONTAINS ENEMY CLASS AND ENEMY CHARACTERS
#
#############################

init 7 python:
    class Enemy(Player):
        def __init__(self, name, base_image, current_health, max_health, strength, perception, confidence, luck, charisma,
                        equipped_weapon, equipped_armor, targeted= False):
            super().__init__(name, base_image, current_health, max_health, strength, perception, confidence, luck, charisma, equipped_weapon, equipped_armor)
            self.targeted = targeted

    strong_minion = Enemy(name= "Minion 1", base_image= "images/test characters/Minion1PNG_%s.png", current_health= 3, max_health= 3, strength= 2, perception= 0, confidence= 0, luck = 1, charisma= 0, equipped_weapon= rusty_sword, equipped_armor= medium_armor, targeted= False)
    smart_minion = Enemy(name= "Minion 2", base_image= "images/test characters/Minion2PNG_%s.png", current_health= 2, max_health= 2, strength= 0,perception= 0, confidence= 0, luck= 2, charisma= 0, equipped_weapon= fists, equipped_armor= light_armor, targeted= False)
    evil_robot = Enemy(name= "GRASP Robot", base_image= "images/temp_grasp_bot.png", current_health= 3, max_health= 3, strength= 1, perception= 1,confidence= 0, luck= 0, charisma= 0, equipped_weapon = fists, equipped_armor= light_armor, targeted= False)


    class Boss(Enemy):
        def __init__(self, name, base_image, current_health, max_health, strength, perception, confidence, luck, charisma,
                        equipped_weapon, equipped_armor, targeted, stage = 0, boss_sp = []):
            super().__init__(name, base_image, current_health, max_health, strength, perception, confidence, luck, charisma, equipped_weapon, equipped_armor, targeted)
            self.stage = stage
            self.boss_sp = boss_sp

    