
from robot import Robot
from dinosaur import Dinosaur

class Battlefield: #the metaphor of two opponents, not an actual space
    def __init__(self):
        self.robot = Robot("Fredee")  # passes through the name
        self.dinosaur = Dinosaur("Jayzen", 40)
                
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
            robot.health -= 20
            print(f'{dinosaur.health} % remains.')
            
        while robot.health >0:
            robot_attack(self)
            dinosaur.health -= amount_of_damage
            print(f'{dinosaur.health} % remains.')


        
    def display_winner(self):
        if dinosaur.health <= 0:
            print(robot.name, ',the robot wins!')
        else:
            dino_attack(self, robot)
        
        if robot.health <= 0:
            print(dinosaur.name, ",the dinosaur wins!")
        else:
            robo_attack(self, dinosaur)
        
