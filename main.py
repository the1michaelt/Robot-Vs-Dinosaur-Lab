from robot import Robot
from battlefield import Battlefield
from dinosaur import Dinosaur
# from weapon import Weapon

# (10 points): battle conclude once either the Robot or the Dinosaur has its health points reduced to zero.



 run_game()
 display_welcome()
 
 introduce_fighters()
 introduce_fighters.robot.name()
 
 introduce_fighters()
 introduce_fighters.dinosaur.name()
 
 battle_phase() #announce rules of the match
 take your wager on either fighter() #as a gameplay trigger event for how the battle will go
 
 announce_action() #narration of what are we witnessing, fight sequence; gameplay scenarios
  
 display_winner() #announce winner
 
 
## Possible Gameplay
# player may choose either robot or dino
# Player names either robot or dino
#  Random name assigned to the opponent
#  Player names the weapon of the robot (if chose robot)
#  the health points are recalculated after each round. (Random outcome and health point deductions)
#  health_points displayed at the end of each round

# # Optional
# # player gets to wager a bet on one of the fighters
# # take player bet $50 to $500; that number is compared to a random number
# # perhaps allow user to bet on each round.
##  All scenarios are predicated upon the comparison of the wager of the player and the random number


# A. BATTLE DETAILS
    #   "Robot {robot.name} wailed on Dino {dino.name} with {weapon}. Dino staggered."
    #   "Dino {dino.name} blocked {robot.name} Robot's {weapon} and cornered him. {robot.name} looked trapped and weak."
    #    "Robot {robot.name} flipped and stunned Dino {dino.name} with the {weapon} across his skull. Can {dino.name} recover from such a blow?"
    #    "Dino {dino.name} pounded {robot.name} Robot's {weapon} into the ground. {robot.name} Robot was pummeled without his weapon."



# B. FINAL OUTCOMES-- WINNER ANNOUNCED
#  if player wager is slightly higher (within 20) than Random, player pick wins close battle (scenario is given); ## player wins double the wager (2x)
# #  if player wager is slightly lower (within 20 points) than Random, player pick loses close battle (scenario is given); ## player loses the whole wager
    #     "Robot {dino.name} landed one last sneaky blow with {weapon}. Dino toppled in a close battle."
    #     "Dino {dino.name} used his reach advantage to knock away the Robot's weapon and then knock him out."

#  if player wager is equal to Random, then double KO (scenario is given); player gets wager returned
 # "Robot {robot.name} started strong. Dino {dino.name} relatiated. Knocked away  {robot.name} Robot's {weapon}. We have a stalemate."
 # "Dino {dino.name} led the charge. Robot  {robot.name} resisted with the {weapon}. There is no clear winner."
 # "The battle was too intense and the injuries were too much for  {robot.name} and  {dino.name} ."

#  if player wager is otherwise lower than Random, player pick gets slaughtered; player loses all but $1
#  if player wager is otherwise higher than Random, player pick slaughters opponent; player wins triple (3x) 
    # "Dino {dino.name} swats Robot into oblivion with his tail. A brutal finish."
    # "Robot {robot.name}  dominates {dino.name} Dino with the {weapon}. Dino {dino.name} never saw it coming."

 
## possible narration scenarios:
# "Robot hits dino without Weapon and loses strength. Dino crushes him."

""
 
 
 
 
 