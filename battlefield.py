from robot import Robot
from dinosaur import Dinosaur

class Battlefield: #the metaphor of two opponents, not an actual space
    def __init__(self):
        self.robot= Robot("freddy")
        self.dinosaur= Dinosaur("jason",12)
                
    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass