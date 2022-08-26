
from robot import Robot
from dinosaur import Dinosaur

class Battlefield: #the metaphor of two opponents, not an actual space
    def __init__(self):
        self.robot= Robot("freddy")
        self.dinosaur= Dinosaur("jason",12)
                
    def run_game(self):
        pass
    
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur")

    # def battle_phase(self):
    #     while robot.health > 0 or dino.health > 0:
    #         dino.health = dino.health -= 30
    #         print(f'''
    #               {robot.name} hits with {robot.active_weapon} for 30 damage.
    #               {dinosaur.name} , has ,{dinosaur.health} remaining.''')

    #         robot.health = robot.health = -20
    #         print(f'''
    #               {dinosaur.name} hits {robot.name} for 20 damage.
    #               {robot.name} , has ,{robot.health} remaining.''')

    # def display_winner(self):
    #         print(outcomes)