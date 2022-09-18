from robot import Robot
from dinosaur import Dinosaur

class Battleground:
    def __init__(self):
        self.robot = Robot("Irresistible")
        self.dinosaur = Dinosaur("Immovable")

    def run_game(self): #executes all methods for game play
        self.display_welcome()  #runs method off of "self"
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nYou are live, cageside at Robot vs. Dinosaur! Scheduled for one fall: a fight for bragging rights!\n')

    def battle_phase(self):
        while self.robot.health > 0: #loops until one or the other reaches health = 0. 
            self.robot.attack(self.dinosaur) #calls the robot object and its "attack" method upon the object(dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot) #calls the dinosaur object and its "attack" method upon the object (robot)
            else:
                return

    def display_winner(self):
        if self.dinosaur.health == 0 :
            print(f'\nYour winner... and still irresistible: {self.robot.name}, the robot! Round of applause!')
        else:    
            print(f'\nYour winner... and still immovable: {self.dinosaur.name}, the dinosaur! Round of applause!')
        
        




