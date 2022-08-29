from robot import Robot
from dinosaur import Dinosaur

# This is one-page scratchwork to try to get some of the functions to work

class Battlefield: #the metaphor of two opponents, not an actual space
    def __init__(self):
        self.robot = Robot("Irresistible")  # passes through the name
        self.dinosaur = Dinosaur("Immovable", 40)
                
    def run_game(self):
        display_welcome(self)
        battle_phase(self)        
        display_winner(self)
    run_game(self)
    
    def display_welcome(self):
        print("Ringside at Robot vs. Dinosaur")

    def battle_phase(self):
        while dinosaur.health > 0:
            dino_attack(self)
            robot.health -= amount_of_damage

        while robot.health > 0:
            robot_attack(self)
            dinosaur.health -= 50

                    
    def display_winner(self):
        if dinosaur.health <= 0:
            print(f'{dinosaur.name}, at {dinosaur.health}% health, dies from injuries.', robot.name, 'survives as the winner.')
        elif robot.health <= 0:
            print(f'{robot.name}, at {robot.health}% health, dies from injuries.', dinosaur.name, 'survives as the winner.')
