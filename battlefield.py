from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.contains_robot=Robot()
        self.contains_dino=Dinosaur()
                
    def run_game(self):
        pass
    
    def display_welcome(self):
        # print("Robot vs. Dinosaur inside the Rocktagon")
        pass
    
    # def announce_action(self):
    #     pass #randomly selects 2-3 actions
    # #narrates the action 
    # # determines a winner
    
    def display_winner(self):
        if winner == Robot:
            print (name, ', the Robot wins')
        else: 
            print (name, ', the Dinosaur wins')
    
    def battle_phase(self):
        pass       
    
    # def elements_can_be_destroyed(self):
    #     pass

    # def can_hurt_Robot(self):
    #     pass
    
    # def can_hurt_Dino(self):
    #     pass
        
# has_welcome_display
# run_game
# display_welcome
# display_winner
# battle_phase
## EXTRAS below ##
# rugged environment with concrete and brick
# urban, city setting
# gravity
# sunny
# terrified, animated bystanders in the background
# elements surrounding can be destroyed
# can hurt either Robot or Dino
